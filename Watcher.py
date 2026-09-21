from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time


class Watcher:
    #r means raw string and makes sure "\" don't mess with python strings
    DIRECTORY_TO_WATCH = r"C:\Users\Admin\Downloads"

    #Watcher classes constructor
    def __init__(self, script_to_run):
        self.observer = Observer()
        self.script_to_run = script_to_run

    def run(self):
        event_Handler = Handler(self.script_to_run)

        #tells watchdog to watch directory and let handler deal with it
        self.observer.schedule(event_Handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        finally:
            self.observer.stop()
            self.observer.join()


class Handler(FileSystemEventHandler):

    def __init__(self, script_to_run):
        self.script_to_run = script_to_run

    #event handler called when watchdog detects new file in download
    def on_created(self, event):
        print("New file detected")


if __name__ == '__main__':
    w = Watcher(r"C:\Users\Admin\PycharmProjects\PDFManager\Classifier")
    w.run()
