import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.process = None
        self.restart_script()

    def on_modified(self, event):
        files_to_watch = [
            "main.py",
            "playlist_migrator/__init__.py",
            "playlist_migrator/migrator.py",
            "playlist_migrator/spotify.py",
            "playlist_migrator/youtube.py",
            "ui/__init__.py",
            "ui/form.ui",
            "ui/ui_form.py",
            "requirements.txt"
        ]

        # Check if the modified file is in the list of files to watch
        if any(event.src_path.endswith(file) for file in files_to_watch):
            print(f'{event.src_path} has been modified!')
            self.restart_script()

    def restart_script(self):
        if self.process:
            print("Killing old main.py process...")
            self.process.terminate()
            self.process.wait()

        print("Running main.py...")
        self.process = subprocess.Popen(["python", "main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == "__main__":
    path = "."
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if event_handler.process:
            event_handler.process.terminate()
        observer.join()
