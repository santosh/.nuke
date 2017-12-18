import os
import threading # is it feasible with multiprocessing
import getpass
import datetime
import json
import re
import nuke
import time

CURRENT_USER = getpass.getuser()
LOG_DIR = os.path.expanduser("~")
TIMER = 5
IDLE_TIME = 30

class TimeLog():
    def start_thread(self):
        self.thread = threading.Timer(5, self.validate_path)
        self.thread.start()

    def validate_path(self):
        self.script_path = nuke.root()['name'].value()
        if not os.path.exists(self.script_path):
            print("Invalid path! Abort")
            return

        print("Valid path!")
        self.start_thread()
