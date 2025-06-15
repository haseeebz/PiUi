
from PySide6.QtWidgets import QScrollArea, QScrollBar
from PySide6.QtCore import QTimer

from typing import Callable

class ScrollWidget(QScrollArea):

    def __init__(self):
        super().__init__()
        self.scroll_bar = QScrollBar()
        self.scroll_bar.setObjectName("#ScrollBar")
        self.on_scroll_func: Callable | None = None

        self.styleScrollBar()
        self.setWidgetResizable(True)

    def makeHorizontal(self):
        self.setHorizontalScrollBar(self.scroll_bar)

    def makeVertical(self):
        self.setVerticalScrollBar(self.scroll_bar)

    def styleScrollBar(self):
        self.setStyleSheet(scrollbar_style)

    def _hideScrollBar(self):
        self.timer = QTimer(interval = 500, singleShot = True)
        self.timer.timeout.connect(
            lambda: self.scroll_bar.setHidden(True)
        )
        self.timer.start()

    def _showScrollBar(self):
        self.timer = QTimer(interval = 250, singleShot = True)
        self.timer.timeout.connect(
            lambda: self.scroll_bar.setHidden(False)
        )
        self.timer.start()

    def leaveEvent(self, event):
        self._hideScrollBar()
        return super().leaveEvent(event)
    
    def enterEvent(self, event):
        self._showScrollBar()
        return super().enterEvent(event)
    
    def wheelEvent(self, arg__1):
        self._showScrollBar()
        if self.on_scroll_func:
            self.on_scroll_func()
        return super().wheelEvent(arg__1)

    def setOnScroll(self, func: Callable):
        if func:
            self.on_scroll_func = func


#stolen lol
scrollbar_style = """
QScrollBar:vertical {
    background: transparent;
    width: 6px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background: rgba(255, 255, 255, 0.15);
    min-height: 20px;
    border-radius: 3px;
}

QScrollBar::handle:vertical:hover {
    background: rgba(255, 255, 255, 0.35);
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical,
QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: none;
    height: 0px;
}

QScrollBar:horizontal {
    background: transparent;
    height: 6px;
    margin: 0px;
}

QScrollBar::handle:horizontal {
    background: rgba(255, 255, 255, 0.15);
    min-width: 20px;
    border-radius: 3px;
}

QScrollBar::handle:horizontal:hover {
    background: rgba(255, 255, 255, 0.35);
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal,
QScrollBar::add-page:horizontal,
QScrollBar::sub-page:horizontal {
    background: none;
    width: 0px;
}
"""