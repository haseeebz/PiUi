
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from typing import Callable, Tuple
from PiUi.app.core import Screen


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


class ImageWidget(QFrame):

    def __init__(self):
        super().__init__()
        self.layoutBox = QHBoxLayout()
        self.label = QLabel()
        self.label.setScaledContents(True)
        self.layoutBox.addWidget(self.label)
        self.setLayout(self.layoutBox)
        self.pixmap: QPixmap

    def setImage(self, path: str):
        self.pixmap = QPixmap(path)
        self.label.setPixmap(self.pixmap)
        
        


def evalBarPosition(position: str,  size: int, screen: Screen) -> Tuple[int, int]:
    
    positions = {
        "top" : (0, 0),
        "bottom" : (0, screen.y - size),
        "left" : (0, 0),
        "right" : (screen.x - size, 0)
    }

    if position in positions:
        return positions[position]
    else:
        print("Incorrect Position for PiBar, Defaulting to Bottom.")
        return positions["bottom"]

def evalBarSize(position: str,  size: int, screen: Screen) -> Tuple[int, int]:

    sizes = {
        "top" : (screen.x , size),
        "bottom" : (screen.x, size),
        "left" : (size, screen.y),
        "right" : (size, screen.y)
    }

    if position in sizes:
        return sizes[position]
    else:
        print("Incorrect Position for PiBar, Defaulting to Bottom.")
        return sizes["bottom"]


def clearLayout(layout: QHBoxLayout):

    if layout is None:
        return
    
    while layout.count():

        item = layout.itemAt(0)

        widget = item.widget()
        if widget is not None:
            widget.setParent(None)
        else:
            layout = item.layout()
            if layout:
                clearLayout(layout)


