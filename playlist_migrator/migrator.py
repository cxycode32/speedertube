import time
import random
from googleapiclient.discovery import build
from PySide6.QtCore import Qt, QThread, Signal, QMutex, QWaitCondition
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui.ui_form import Ui_SpeederTubeGUI
from .spotify import get_spotify_token
from .youtube import get_youtube_token

class SpotifyMigrator(QThread):
    progress_update = Signal(str)
    playlist_fetched = Signal(list)

    def __init__(self, spotify_token):
        super().__init__()
        self.sp = spotify_token

    def run(self):
        try:
            self.progress_update.emit("Fetching Spotify playlists...")
            playlists = self.sp.current_user_playlists()
            playlist_items = playlists['items']
            self.playlist_fetched.emit(playlist_items)
            self.progress_update.emit(f"{len(playlist_items)} Spotify {"playlists" if len(playlist_items)>0 else "playlist"} playlists fetched!")
        except Exception as e:
            self.progress_update.emit(f"Error fetching playlists: {e}")

class YouTubeMigrator(QThread):
    progress_update = Signal(str)
    song_migrated_success = Signal(str)
    song_migrated_failed = Signal(str, str)

    def __init__(self, spotify_playlist_tracks, youtube_playlist_id, youtube_token):
        super().__init__()
        self.spotify_playlist_tracks = spotify_playlist_tracks
        self.youtube_playlist_id = youtube_playlist_id
        self.youtube_token = youtube_token

        self.paused = False
        self.stopped = False
        self.mutex = QMutex()
        self.pause_condition = QWaitCondition()

    def run(self):
        youtube_service = build('youtube', 'v3', credentials=self.youtube_token)

        for track in self.spotify_playlist_tracks:
            self.mutex.lock()
            if self.stopped:
                self.mutex.unlock()
                break

            while self.paused:
                self.pause_condition.wait(self.mutex)

            self.mutex.unlock()

            song_name = track['track']['name']
            artist_name = track['track']['artists'][0]['name']
            search_result = self.search_youtube(youtube_service, song_name, artist_name)

            if search_result:
                try:
                    self.add_to_youtube_playlist(youtube_service, self.youtube_playlist_id, search_result)
                    self.song_migrated_success.emit(f"'{song_name}' by {artist_name} added to YouTube.")
                except Exception as e:
                    self.song_migrated_failed.emit(f"'{song_name}' by {artist_name}", str(e))
            else:
                self.song_migrated_failed.emit(f"'{song_name}' by {artist_name}", "Song not found on YouTube.")

    def search_youtube(self, youtube_service, song_name, artist_name):
        query = f"{song_name} {artist_name}"
        search_response = youtube_service.search().list(
            q=query,
            part='snippet',
            maxResults=1
        ).execute()

        if search_response['items']:
            return search_response['items'][0]['id']['videoId']
        return None

    def add_to_youtube_playlist(self, youtube_service, playlist_id, video_id, retries=3):
        for attempt in range(retries):
            try:
                youtube_service.playlistItems().insert(
                    part='snippet',
                    body={
                        'snippet': {
                            'playlistId': playlist_id,
                            'resourceId': {
                                'kind': 'youtube#video',
                                'videoId': video_id
                            }
                        }
                    }
                ).execute()
                return
            except Exception as e:
                if 'SERVICE_UNAVAILABLE' in str(e):
                    # Wait for a random time before retrying
                    time.sleep(2 ** attempt + random.uniform(0, 1))
                    continue  # Retry the request
                else:
                    raise e

    def pause(self):
        self.mutex.lock()
        self.paused = True
        self.mutex.unlock()

    def resume(self):
        self.mutex.lock()
        self.paused = False
        self.pause_condition.wakeAll()
        self.mutex.unlock()

    def stop(self):
        self.mutex.lock()
        self.stopped = True
        self.paused = False
        self.pause_condition.wakeAll()
        self.mutex.unlock()

class SpeederTubeGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SpeederTubeGUI()
        self.ui.setupUi(self)

        self.move(0, 0)

        self.log_model_success = QStandardItemModel()
        self.ui.listView.setModel(self.log_model_success)

        self.log_model_failed = QStandardItemModel()
        self.ui.listView_2.setModel(self.log_model_failed)

        self.log_model_general = QStandardItemModel()
        self.ui.listView_3.setModel(self.log_model_general)

        self.ui.progressBar.setValue(0)

        self.total_songs = 0
        self.processed_songs = 0

        self.spotify_token = get_spotify_token()
        self.youtube_token = get_youtube_token()

        self.fetch_spotify_playlists()
        self.fetch_youtube_playlists()

        self.ui.pushButton.clicked.connect(self.start_migration)
        self.ui.pushButton_2.clicked.connect(self.stop_migration)

        self.migration_in_progress = False
        self.migration_paused = False

    def fetch_spotify_playlists(self):
        self.sp_crawler = SpotifyMigrator(self.spotify_token)
        self.sp_crawler.progress_update.connect(self.update_general_progress)
        self.sp_crawler.playlist_fetched.connect(self.populate_spotify_playlists)
        self.sp_crawler.start()

    def populate_spotify_playlists(self, playlists):
        for playlist in playlists:
            self.ui.comboBox.addItem(playlist['name'], playlist['id'])

    def fetch_youtube_playlists(self):
        self.update_general_progress("Fetching YouTube playlists...")
        yt_service = build('youtube', 'v3', credentials=self.youtube_token)
        playlists = []
        next_page_token = None

        while True:
            playlists_response = yt_service.playlists().list(
                part="snippet",
                mine=True,
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            playlists.extend(playlists_response['items'])

            next_page_token = playlists_response.get('nextPageToken')
            if not next_page_token:
                break

        self.update_general_progress(f"{len(playlists)} YouTube {"playlists" if len(playlists)>0 else "playlist"} fetched!")
        self.populate_youtube_playlists(playlists)

    def populate_youtube_playlists(self, playlists):
        for playlist in playlists:
            self.ui.comboBox_2.addItem(playlist['snippet']['title'], playlist['id'])

    def create_new_youtube_playlist(self, youtube_service, playlist_name):
        privacy_status = 'public'

        if self.ui.radioButton.isChecked():
            privacy_status = 'public'
        elif self.ui.radioButton_2.isChecked():
            privacy_status = 'private'

        playlist_response = youtube_service.playlists().insert(
            part='snippet,status',
            body={
                'snippet': {'title': playlist_name, 'description': 'by SpeederTube'},
                'status': {'privacyStatus': privacy_status}
            }
        ).execute()
        return playlist_response['id']

    def start_migration(self):
        if self.migration_in_progress and self.migration_paused:
            self.yt_crawler.resume()
            self.update_general_progress("Resuming migration...")
            self.migration_paused = False
        else:
            spotify_playlist_index = self.ui.comboBox.currentIndex()
            selected_spotify_playlist_id = self.ui.comboBox.itemData(spotify_playlist_index)
            youtube_playlist_name = self.ui.lineEdit.text()
            youtube_playlist_id = self.ui.comboBox_2.currentData()

            if not selected_spotify_playlist_id:
                self.update_general_progress("Please select a Spotify playlist.")
                return

            youtube_service = build('youtube', 'v3', credentials=self.youtube_token)

            if youtube_playlist_name:
                youtube_playlist_id = self.create_new_youtube_playlist(youtube_service, youtube_playlist_name)
                self.update_general_progress(f"Created a new YouTube playlist '{youtube_playlist_name}'")
            else:
                if not youtube_playlist_id:
                    self.update_general_progress("Please select or create a YouTube playlist.")
                    return

            self.update_general_progress(f"Starting migration to YouTube playlist '{youtube_playlist_name or self.ui.comboBox_2.currentText()}'")
            spotify_tracks = self.spotify_token.playlist_tracks(selected_spotify_playlist_id)['items']

            self.total_songs = len(spotify_tracks)
            self.processed_songs = 0
            self.ui.progressBar.setValue(0)

            if self.total_songs == 0:
                self.update_general_progress("No songs found in the selected Spotify playlist.")
                return

            self.yt_crawler = YouTubeMigrator(spotify_tracks, youtube_playlist_id, self.youtube_token)

            self.yt_crawler.song_migrated_success.connect(self.update_success_progress)
            self.yt_crawler.song_migrated_failed.connect(self.update_failed_progress)

            self.yt_crawler.start()

            self.migration_in_progress = True
            self.migration_paused = False

    def stop_migration(self):
        if not self.migration_in_progress:
            self.update_general_progress("Migration has not started yet.")
            return

        if self.migration_paused:
            self.update_general_progress("Migration is already paused.")
            return

        self.yt_crawler.pause()
        self.update_general_progress("Pausing migration...")
        self.migration_paused = True

    def add_non_editable_item(self, model, text):
        item = QStandardItem(text)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Make the item non-editable
        model.appendRow(item)

    def update_success_progress(self, message):
        self.add_non_editable_item(self.log_model_success, message)
        self.ui.listView.scrollToBottom()
        self.update_progress_bar()

    def update_failed_progress(self, song, reason):
        self.add_non_editable_item(self.log_model_failed, f"Failed to migrate {song}.\nReason: {reason}")
        self.ui.listView_2.scrollToBottom()
        self.update_progress_bar()

    def update_general_progress(self, message):
        self.add_non_editable_item(self.log_model_general, message)
        self.ui.listView_3.scrollToBottom()

    def update_progress_bar(self):
        if self.total_songs > 0:
            self.processed_songs += 1
            progress_percentage = int((self.processed_songs / self.total_songs) * 100)
            self.ui.progressBar.setValue(progress_percentage)

            if self.processed_songs == self.total_songs:
                self.update_general_progress("Playlist migration completed!")