from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(, event.src_path)
        
    def on_modified(self, event):
        print(, event.src_path)
        grad = "aeiouаоуеиэюя"
        file = open(event.src_path)
        for k in file.read():
            if k in grad: file.write(str(k).lower())
            else: file.write(str(k).upper())



event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=r"D:\Practic\Python\Pract2\files", recursive=False)
observer.start()
while True:
    try:
        pass
    except KeyboardInterrupt:
        observer.stop()