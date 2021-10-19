from datetime import datetime

from src.model.util.constants import Constants

class Logger:

    def __init__(self, path, file_name) -> None:
        self.path = path
        self.file_name = file_name

    def write_log(self, body) -> str:
        message = "[" + Constants.SYSTEM_CURRENT_DATETIME + "]"+ " " + body + Constants.SPECIAL_CHAR_ENTER

        return message