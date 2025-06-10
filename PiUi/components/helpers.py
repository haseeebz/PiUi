
from PySide6.QtWidgets import QWidget, QPushButton, QFrame
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from typing import Callable


class CustomEventWidget(QFrame):

    def __init__(self):
        super().__init__()
        self.rightClicked: Callable = None
        self.leftClicked: Callable = None
        self.middleClicked: Callable = None
        self.doubleClicked: Callable = None
        self.mouseReleased: Callable = None
        self.mouseEnter: Callable = None
        self.mouseLeave: Callable = None
        self.show()

    def mousePressEvent(self, event: QMouseEvent):

        if event.button() == Qt.MouseButton.RightButton:
            if self.rightClicked:
                self.rightClicked()

        elif event.button() == Qt.MouseButton.MiddleButton:
            if self.middleClicked:
                self.middleClicked()

        elif event.button() == Qt.MouseButton.LeftButton:
            if self.leftClicked:
                self.leftClicked()
        
    def mouseDoubleClickEvent(self, event):
        if self.doubleClicked:
            self.doubleClicked()

    def mouseReleaseEvent(self, event):
        if self.mouseReleased:
            self.mouseReleased()

    def enterEvent(self, event):
        if self.mouseEnter:
            self.mouseEnter()

    def leaveEvent(self, event):
        if self.mouseLeave:
            self.mouseLeave()


    def connectRightClick(self, func: Callable):
        self.rightClicked = func

    def connectMiddleClick(self, func: Callable):
        self.middleClicked = func

    def connectLeftClick(self, func: Callable):
        self.leftClicked = func

    def connectDoubleClick(self, func: Callable):
        self.doubleClicked = func

    def connectMouseRelease(self, func: Callable):
        self.mouseReleased = func

    def connectMouseEnter(self, func: Callable):
        self.mouseEnter = func

    def connectMouseLeave(self, func: Callable):
        self.mouseLeave = func

