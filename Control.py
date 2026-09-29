from Watcher import Watcher
from Classifier import Classifier
from config import keywords

class Control:

    def __init__(self):
        self.Running = True
        self.classifier = Classifier(keywords)

    def run(self):
        print("Here I am")
        watcher = Watcher(self)
        watcher.run()

    def file_created(self, filepath):
        if filepath.endswith(".txt"):
            category = self.classifier.classify(filepath)
            if category:
                #Organizers turn
                pass
            else:
                print("Category couldn't be matched")




