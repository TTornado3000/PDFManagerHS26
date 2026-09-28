import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class Watcher:
    #r means raw string and makes sure "\" don't mess with python strings
    DIRECTORY_TO_WATCH = r"C:\Users\Admin\Downloads"

    #Watcher classes constructor
    def __init__(self, control):
        self.observer = Observer()
        self.control = control

    def run(self):
        print("hey")
        event_Handler = EventHandler(self.control)

        #tells watchdog to watch directory and let handler deal with it
        self.observer.schedule(event_Handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        finally:
            self.observer.stop()
            self.observer.join()


#Todo: The Logger should take care of printing or logging changes

def on_createddd(event):
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

    try:
        #buffer time for file to be written
        time.sleep(1)

        #Calls out change and executes the external script
        print(f"{BLUE}New file detected!{RESET}")
        return True
        #subprocess.run(["python", self.script_to_run], check=True)

    except FileNotFoundError:
        print(f"{RED}File not found!{RESET}")
    except PermissionError:
        print(f"{RED}Permission denied!{RESET}")
    except Exception as e:
        print(f"{RED}Error processing file {e}!{RESET}")


class EventHandler(FileSystemEventHandler):
    def __init__(self, control):
        self.control = control
        print("yo")
    def on_created(self, event):
        if not event.is_directory:
            print("Here we are")
            self.control.file_created(event.src_path)



