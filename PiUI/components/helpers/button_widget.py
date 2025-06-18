
from PySide6.QtWidgets import QPushButton

from typing import Callable

class ButtonWidget(QPushButton):

    def __init__(self):
        super().__init__()
        self.onClick: Callable | None = None
        self.onRelease: Callable | None = None

    def setOnClick(self, func: Callable):
        self.onClick = func
        self.clicked.connect(lambda _: self.onClick()) #type: ignore #Assigned

    def setOnRelease(self, func: Callable):
        self.onRelease = func
        self.clicked.connect(lambda _: self.onRelease()) #type: ignore #Assigned
    