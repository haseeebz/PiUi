

from PySide6.QtWidgets import QFrame, QHBoxLayout
from PySide6.QtCore import Qt
from typing import Tuple

from .xstrut import Strut
from PiUi.components.widgets.widget import PiWidget
from PiUi.app.utils.helper import enforceType

class PiWindow():

    def __init__(
        self,
        *,
        name: str | None = None,
        position: Tuple[int, int],
        size: Tuple[int, int],
        rootWidget: PiWidget = None,
        strut: Strut = None
        ):

        self._qt___: QFrame = QFrame()

        self._qt___.setGeometry(*position, *size)
        self._qt___.setFixedSize(*size)
        
        self._qt___.setWindowFlags(
            Qt.WindowType.BypassWindowManagerHint |
            Qt.WindowType.Tool |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Desktop |
            Qt.WindowType.WindowStaysOnBottomHint |
            Qt.WindowType.Widget
        )

        if name:
            self._qt___.setObjectName(name)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        
        enforceType(rootWidget, (PiWidget, type(None)), "rootWidget")
        if rootWidget:
            layout.addWidget(rootWidget._qt___)

        self._qt___.setLayout(layout)
        self._qt___.setContentsMargins(0,0,0,0)

        enforceType(strut, (Strut, type(None)), "strut")
        self.strut = strut
        if strut:
            self.strut.setup()
            self.strut.hide()


    def showExplicit(self, t: bool):
        if t:
            self._qt___.show()
            if self.strut: self.strut.show()
        else:
            self._qt___.hide()
            if self.strut: self.strut.hide()
        
    def show(self):
        if self._qt___.isHidden():
            self.showExplicit(True)
        else:
            self.showExplicit(False)
            
    def close(self):
        if self.strut:
            self.strut.close()
        self._qt___.close()