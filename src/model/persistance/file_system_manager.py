from src.model.util.constants import Constants

import os
import shutil

class FileSystemManager:

    def __init__(self) -> None:
        pass
    
    def remove_directory(self, path) -> str:
        shutil.rmtree(path)
        return Constants.SYSTEM_CURRENT_DIRECTORY + path 

    def check_if_exists(self, path) -> bool:
        return True if os.path.exists(path) else False