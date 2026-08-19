from logger import Logger

class FileLogger(Logger):

    def log_error(self, message: str, exception: Exception) -> None:
        with open("./logging.log", "a", encoding = "utf-8") as f:
            f.write(f"error: {message}, exception: {exception}\n")

    def log_info(self, message: str) -> None:
        with open("./logging.log", "a", encoding = "utf-8") as f:
            f.write(f"info: {message}\n")

    def log_warning(self, message: str) -> None:
        with open("./logging.log", "a", encoding = "utf-8") as f:
            f.write(f"warning: {message}\n")



'''
logger = FileLogger()

logger.log_info('this is an info message')
logger.log_warning('this is a warning') 
logger.log_error('this is an error', Exception('some weird exception'))
'''