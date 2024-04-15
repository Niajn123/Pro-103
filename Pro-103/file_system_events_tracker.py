import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

from_dir="/Users/niajain/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

    def on_modified(self, event):
        print(f"Someone modified this {event.src_path}!")

    def on_moved(self, event):
        print(f"Someone moved this file {event.src_path}!") 
eventHandler=FileEventHandler()
observer=Observer()
observer.schedule(eventHandler,from_dir,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()