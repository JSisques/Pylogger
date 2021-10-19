from datetime import datetime
import os

class Constants:

    #System
    SYSTEM_SEPARATOR = os.path.sep
    SYSTEM_CURRENT_DIRECTORY = os.getcwd() + SYSTEM_SEPARATOR
    SYSTEM_CURRENT_DATETIME = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    #Paths
    PATH_LOG = "log" + SYSTEM_SEPARATOR
    PATH_OU = "output" + SYSTEM_SEPARATOR

    #Extensions
    EXTENSION_JSON = ".json"
    EXTENSION_TXT = ".txt"
    EXTENSION_LOG = ".log"

    #File names
    FILE_NAME_OUTPUT = "output" + EXTENSION_TXT
    FILE_NAME_LOG = "app" + EXTENSION_LOG

    #Log messages
    LOG_MESSAGE_PROGRAM_STARTED = "Program started"
    LOG_MESSAGE_FILE_WRITTEN = "File written"
    LOG_MESSAGE_EMAIL_SENDED = "Email sended"
    LOG_MESSAGE_KEY_PRESSED = "Key pressed: "

    #File options
    FILE_OPTIONS_APPEND = "a"
    FILE_OPTIONS_WRITE = "w"
    FILE_OPTIONS_READ = "r"

    #Special characters
    SPECIAL_CHAR_ENTER = "\n"
    SPECIAL_CHAR_TAB = "\t"