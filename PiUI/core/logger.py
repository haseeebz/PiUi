
import logging
import os
from typing import Literal

def setupLogger(logfile: str, level: str):

    if not os.path.exists(os.path.expanduser("~/.cache/PiUI")):
        os.mkdir(os.path.expanduser("~/.cache/PiUI"))

    levels = {
        "debug" : logging.DEBUG,
        "info"  : logging.INFO,
        "warning" : logging.WARNING,
        "critical" : logging.CRITICAL
    }

    loggerCore = logging.getLogger("PiUI.core")
    loggerComp = logging.getLogger("PiUI.component")
    loggerUser = logging.getLogger("PiUI.user")

    loggers = [loggerCore, loggerComp, loggerUser]

    for logger in loggers:

        logger.setLevel(levels[level])
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
        
        full_file = os.path.expanduser(logfile)
        if not os.path.exists(full_file):
            with open(full_file, "w") as file:
                file.writable()

        file_handler = logging.FileHandler(full_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    
def getLogger(component: Literal["core", "component", "user"]):
    logger = logging.getLogger(f"PiUI.{component}")
    return logger