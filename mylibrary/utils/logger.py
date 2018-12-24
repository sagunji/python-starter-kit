import logging
import datetime

import settings
from enum import Enum
from folder_actions import make_directory


log_level = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warn": logging.WARN,
    "error": logging.ERROR,
    "fatal": logging.FATAL,
}


class Log(Enum):
    DEFAULT_LOG = {"name": "default_log", "path": settings.LOG_LOCATION}
    API = {"name": "api", "path": "{}/api".format(settings.LOG_LOCATION)}
    DATABASE = {"name": "database", "path": "{}/database".format(settings.LOG_LOCATION)}


class Logger:
    """
    Common Logger configuration class
    """

    @staticmethod
    def _setup_logging_folders():
        """ Create log folders
        """
        for log in Log:
            make_directory(log.value["path"])

    @staticmethod
    def _configure_logger(filename, folder_path="./logs"):
        """ Configure logger

        :param filename: string
        :param folder_path: string
        :return logger
        """
        name = filename.replace(".log", "")
        logger = logging.getLogger(name)
        logger.setLevel(log_level.get(settings.LOG_LEVEL, logging.INFO))

        if logger.handlers:
            return logger

        file_name = "{}/{}".format(folder_path, filename)
        handler = logging.FileHandler(file_name)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s - {%(pathname)s:%(lineno)d}"
        )
        handler.setFormatter(formatter)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.addHandler(consoleHandler)
        return logger

    @classmethod
    def get(cls, log_name=Log.DEFAULT_LOG):
        """Get logger

        :param log_name: Log 
        :return logger:
        """
        if not isinstance(log_name, Log):
            return

        file_name = datetime.datetime.now().strftime("%Y-%m-%d") + "_{}.log".format(
            log_name.value["name"]
        )
        cls._setup_logging_folders()
        return cls._configure_logger(file_name, log_name.value["path"])
