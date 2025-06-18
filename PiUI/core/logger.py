
import logging
import os
from typing import Literal
from colorlog import ColoredFormatter

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

    logger = logging.getLogger("PiUI")


    logger.setLevel(levels[level])

    if logger.handlers:
        return

    color_formatter  = ColoredFormatter(

        "[%(asctime)s] %(log_color)s[%(levelname)s] %(name_log_color)s(%(name)s) %(message_log_color)s%(message)s",

        datefmt = "%H:%M:%S",

        log_colors={
            'DEBUG'   : 'cyan',
            'INFO'    : 'green',
            'WARNING' : 'yellow',
            'ERROR'   : 'red',
            'CRITICAL': 'red,bg_white',
        },

        secondary_log_colors={
            'message': {
            'DEBUG'   : 'white',
            'INFO'    : 'white',
            'WARNING' : 'white',
            'ERROR'   : 'white',
            'CRITICAL': 'white'
            },

            'name': {
            'DEBUG'   : 'purple',
            'INFO'    : 'purple',
            'WARNING' : 'purple',
            'ERROR'   : 'purple',
            'CRITICAL': 'purple'
            }
        }
    )

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] (%(name)s) %(message)s",
        datefmt = "%H:%M:%S",
    )

    stream = logging.StreamHandler()
    stream.setFormatter(color_formatter)
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