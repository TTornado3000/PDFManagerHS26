import watchdog.observers as Observer
import watchdog.events as FileSystesmEventHandler
import os
import time

class Watcher:

    def __init__(self, fileToRun):
        self.observer = Observer
        self.fileToRun = fileToRun

    def run(self):
        



class Handler: