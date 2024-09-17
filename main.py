import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from playlist_migrator import SpeederTubeGUI, SpotifyMigrator, YouTubeMigrator, get_spotify_token, get_youtube_token
from ui import Ui_SpeederTubeGUI

def main():
    app = QApplication(sys.argv)
    gui = SpeederTubeGUI()
    gui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()