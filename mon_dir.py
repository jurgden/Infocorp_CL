import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class DirectoryWatcher(FileSystemEventHandler):
    def __init__(self, script_path, python_executable):
        self.script_path = script_path
        self.python_executable = python_executable

    def on_modified(self, event):
        if event.src_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            print(f"Detected change in {event.src_path}. Running the script...")
            try:
                result = subprocess.run([self.python_executable, self.script_path], check=True, capture_output=True, text=True)
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error running script: {e}\n{e.stderr}")

def main():
    # Absolute paths to the directory and the script
    path_to_watch = os.path.abspath('assets/images/banner')
    script_path = os.path.abspath('image_finder.py')
    
    # Absolute path to the Python interpreter in the virtual environment
    python_executable = os.path.abspath('.venv/Scripts/python')

    event_handler = DirectoryWatcher(script_path, python_executable)
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
