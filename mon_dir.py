import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class DirectoryWatcher(FileSystemEventHandler):
    def __init__(self, script_path):
        self.script_path = script_path

    def on_modified(self, event):
        if event.src_path.endswith('.png') or event.src_path.endswith('.jpg') or event.src_path.endswith('.jpeg') or event.src_path.endswith('.gif'):
            print(f"Detected change in {event.src_path}. Running the script...")
            subprocess.run(['python', self.script_path], check=True)

def main():
    # Path to the directory you want to monitor
    path_to_watch = 'assets/images/banner'
    # Path to the script to run when changes are detected
    script_path = 'image_finder.py'
    
    event_handler = DirectoryWatcher(script_path)
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=False)
    
    print(f"Monitoring changes in {path_to_watch}...")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
