from constants import *

import os
import shutil

class DirectoryManager:

    def __init__(self) -> None:
        pass

    def check_if_exists(self, path) -> bool:
        return True if os.path.exists(path) else False

    def create_directory(self, path) -> str:
        if not self.check_if_exists(path):
            os.makedirs(path)
        
        return Constants.CURRENT_DIRECTORY + Constants.SYSTEM_SEPARATOR + path 

    def remove_directory(self, path) -> str:
        shutil.rmtree(path)
        return Constants.CURRENT_DIRECTORY + Constants.SYSTEM_SEPARATOR + path 