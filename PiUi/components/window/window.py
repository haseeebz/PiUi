

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from typing import Tuple

from .xstrut import Strut

class PiWindow():

    def __init__(
        self,
        *,
        name: str | None,
        position: Tuple[int, int],
        size: Tuple[int, int],
        rootWidget,
        strut: Strut = None
        ):

        self.qt = QMainWindow()

        self.qt.setGeometry(*position, *size)
        self.qt.setFixedSize(*size)
        
        self.qt.setWindowFlags(
            Qt.WindowType.BypassWindowManagerHint |
            Qt.WindowType.Tool |
            Qt.WindowType.FramelessWindowHint
        )

        if name:
            self.qt.setObjectName(name)

        self.qt.setCentralWidget(rootWidget.qt)
        self.qt.setContentsMargins(0,0,0,0)
        
        if strut:
            self.strut = strut
            strut.setup()

        self.show(True)

    def show(self, t: bool):
        if t:
            self.qt.show()
        else:
            self.qt.hide()
        
