# SpeederTube - Spotify to YouTube Playlist Migration

SpeederTube is a Python-based application with a GUI developed using PySide6. This tool allows you to migrate your playlists from Spotify to YouTube Music.

## Features:
- Select Spotify playlists and migrate them to YouTube Music.
- Option to create a new playlist on YouTube Music or add to an existing one.
- Progress tracking for each song migrated.
- Handles errors such as unavailable songs on YouTube or API issues.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/cxycode32/speedertube.git
cd speedertube
```

### 2. Install dependencies

Optional. Run the following command to create virtual environment:

```bash
python3 -m venv venv
source ./venv/bin/activate
```

Run the following command to install all the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a .env file in the root directory with the following content:

SPOTIFY_CLIENT_ID=<your-spotify-client-id>
SPOTIFY_CLIENT_SECRET=<your-spotify-client-secret>
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback

YOUTUBE_CLIENT_SECRETS=client_secrets.json

### 4. Obtain Your Spotify Token

1. Go to the Spotify Developer Dashboard (https://developer.spotify.com/dashboard) and create an application.
2. Copy the Client ID and Client Secret.

### 5. Obtain Your YouTube Token

1. Go to the Google Developer Console (https://console.developers.google.com/project), create a project, and enable the YouTube Data API v3.
2. Create OAuth 2.0 credentials and download the client_secrets.json file.
3. Place client_secrets.json in the project root directory.

### 6. Run the Application

To monitor file changes and restart the application automatically:

```bash
python3 watcher.py
```


If you don't want to monitor changes:

```bash
python3 main.py
```
