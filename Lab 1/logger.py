from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def log_error(message: str, exception: Exception) -> None:
        pass

    @abstractmethod
    def log_info(message: str) -> None:
        pass

    @abstractmethod
    def log_warning(message: str) -> None:
        pass

'''
logger = Logger()
'''
