from Watcher import Watcher
import Classifier


class Control:

    def __init__(self):
        self.Running = True

    def run(self):
        print("Here I am")
        watcher = Watcher(self)
        watcher.run()

    def file_created(self, path):
        print("File created: ", path)



