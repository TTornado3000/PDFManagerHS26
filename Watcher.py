import watchdog.observers as Observer
import watchdog.events as FileSystemEventHandler
import os
import time


class Watcher:
    DIRECTORY_TO_WATCH = r"C:\Users\Admin\Downloads"

    def __init__(self, script_to_run):
        self.observer = Observer()
        self.script_to_run = script_to_run

    def run(self):
        event_Handler = Handler(self.script_to_run)
        self.observer.schedule(event_Handler, ".", recursive=True)
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


if __name__ == '__main__':
    w = Watcher(r"C:\Users\Admin\PycharmProjects\PDFManager\Classifier")
    w.run()
