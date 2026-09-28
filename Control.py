import Watcher
import Classifier


class Control:

    def __init__(self):
        self.Running = True

    def run(self):
        print("Here I am")
        #print(self.Running)

        watcher = Watcher
