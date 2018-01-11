#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time

import utils.globalvar as g
from utils.common import programEroor
from utils.common import makeDirectory
from utils.common import copyFile

try:
    from watchdog.observers import Observer  
    from watchdog.events import FileSystemEventHandler
except ImportError:
    programEroor("[!] Please pip install watchdog")
        

class ArcHandler(FileSystemEventHandler):
    def on_created(self, event):
        backup_path = g.getBackupPath()
        day_time = time.strftime("%Y%m%d")
        src_path = event.src_path
        dst_path = os.path.join(backup_path, day_time ,src_path[1:])

        try:
            if event.is_directory:
                makeDirectory(dst_path)
            else:
                copyFile(src_path, dst_path)
        except IOError:
            pass

class ArcWarden(object):
    def __init__(self, watch_path):
        self.watch_path = watch_path
        self.event_handler = ArcHandler()
        self.observer = Observer()

    def start(self):
        self.observer.schedule(self.event_handler, path=self.watch_path, recursive=True)  
        self.observer.start()

    def stop(self):
        self.observer.stop()

    def join(self):
        self.observer.join()
