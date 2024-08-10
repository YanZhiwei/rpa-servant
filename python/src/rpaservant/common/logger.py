import logging
import os
from logging import handlers
from datetime import datetime


class Logger(object):

    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "crit": logging.CRITICAL,
    }

    def __init__(
        self,
        level="info",
        when="D",
        backCount=3,
        fmt="%(asctime)s -[line:%(lineno)d] - %(levelname)s: %(message)s",
    ):
        file_log_name = "{:%Y-%m-%d}.log".format(datetime.now())
        file_log_folder = os.path.join(os.getenv("LOCALAPPDATA"), "rpaservant", "logs")
        if os.path.exists(file_log_folder) == False:
            os.makedirs(file_log_folder)
        file_log_path = os.path.join(file_log_folder, file_log_name)
        self.logger = logging.getLogger(file_log_path)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        sh = logging.StreamHandler()
        sh.setFormatter(format_str)
        th = handlers.TimedRotatingFileHandler(
            filename=file_log_path, when=when, backupCount=backCount, encoding="utf-8"
        )
        th.setFormatter(format_str)
        self.logger.addHandler(sh)
        self.logger.addHandler(th)

    __static_logger: logging.Logger = None

    @staticmethod
    def get() -> logging.Logger:
        if Logger.__static_logger is None:
            Logger.__static_logger = Logger("debug").logger
        return Logger.__static_logger
