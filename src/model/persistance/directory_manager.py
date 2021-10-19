from src.model.persistance.file_system_manager import FileSystemManager
from src.model.util.constants import *

import os
import shutil

class DirectoryManager(FileSystemManager):

    def __init__(self) -> None:
        super().__init__()

    def create_directory(self, path) -> str:
        if not self.check_if_exists(path):
            os.makedirs(path)
        
        return Constants.SYSTEM_CURRENT_DIRECTORY + path 
