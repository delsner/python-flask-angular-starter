import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent

class Watcher:
    DIRECTORY_TO_WATCH = "./"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("error")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.src_path == "./requirements.txt":
            subprocess.call(["./install.sh"])


if __name__ == '__main__':
    w = Watcher()
    w.run()
