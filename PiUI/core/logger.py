
import logging
import os
from typing import Literal

def setupLogger(logfile: str, level):

    loggerCore = logging.getLogger("PiUI.core")
    loggerWindow = logging.getLogger("PiUI.window")
    loggerWidget = logging.getLogger("PiUI.widget")
    loggerUtils = logging.getLogger("PiUI.utils")

    loggers = [loggerCore, loggerWindow, loggerWidget, loggerUtils]

    for logger in loggers:

        logger.setLevel(level)
        logger.propagate = False
        if logger.handlers:
            continue

        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] (%(name)s) %(message)s",
            datefmt = "%H:%M:%S"
        )  

        stream = logging.StreamHandler()
        stream.setFormatter(formatter)
        logger.addHandler(stream)

        if not os.path.exists(logfile):
            open(logfile, "w").close()

        file_handler = logging.FileHandler(logfile)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    


def getLogger(component: Literal["core", "window", "widget", "utils"]):
    logger = logging.getLogger(f"PiUI.{component}")
    return logger