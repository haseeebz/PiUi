

from PySide6.QtWidgets import QMainWindow, QFrame, QHBoxLayout
from PySide6.QtCore import Qt
from typing import Tuple

from .xstrut import Strut


class PiWindow():

    def __init__(
        self,
        name: str | None,
        *,
        position: Tuple[int, int],
        size: Tuple[int, int],
        strut: Strut = None
        ):

        self.__qt__: QFrame = QFrame()

        self.__qt__.setGeometry(*position, *size)
        self.__qt__.setFixedSize(*size)
        
        self.__qt__.setWindowFlags(
            Qt.WindowType.BypassWindowManagerHint |
            Qt.WindowType.Tool |
            Qt.WindowType.FramelessWindowHint
        )

        if name:
            self.__qt__.setObjectName(name)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)

        self.__qt__.setLayout(layout)
        self.__qt__.setContentsMargins(0,0,0,0)

        if strut:
            self.strut = strut
            strut.setup()

    def root(self, rootWidget):
        self.__qt__.layout().addWidget(rootWidget)

    def show(self, t: bool):
        if t:
            self.__qt___.show()
        else:
            self.__qt___.hide()
        
