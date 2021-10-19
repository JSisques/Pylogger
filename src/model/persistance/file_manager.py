import os

from src.model.persistance.file_system_manager import FileSystemManager
from src.model.util.constants import Constants

class FileManager(FileSystemManager):

    def __init__(self) -> None:
        super().__init__()

    def create_file(self, path, name) -> str:
        path += name
        
        if not super().check_if_exists(path):
            file = open(path, Constants.FILE_OPTIONS_WRITE)
            file.write("")
            file.close()

        return Constants.SYSTEM_CURRENT_DIRECTORY + path 

    def read_file(self, path, file_name) -> str:
        path += file_name
        file = open(path, Constants.FILE_OPTIONS_READ)
        result = file.read()
        file.close()
        return result

    def write_file(self, path, file_name, body, append_on_end = True) -> str:
       
        path += file_name
        file = open(path, Constants.FILE_OPTIONS_APPEND) if append_on_end else open(path, Constants.FILE_OPTIONS_WRITE)
        file.write(body)
        file.close()
       
        return body