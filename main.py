from src.model.persistance.directory_manager import *
from src.model.persistance.file_manager import *
from src.model.util.logger import *

if __name__ == "__main__":
    directory_manager = DirectoryManager()
    file_manager = FileManager()
    logger = Logger(Constants.PATH_LOG, Constants.FILE_NAME_LOG)

    directory_manager.create_directory(Constants.PATH_LOG)
    file_manager.create_file(Constants.PATH_LOG, Constants.FILE_NAME_LOG)
    file_manager.write_file(Constants.PATH_LOG, Constants.FILE_NAME_LOG, logger.create_log_message(Constants.LOG_MESSAGE_PROGRAM_STARTED))