

from typing import Callable
from PiUi.core.utils import Binding, Poll, Alignment
from PySide6.QtWidgets import QWidget


class PiWidget():

    def __init__(
        self,
        qt,
        name: str | None = None,
        height: int | None = None,
        width: int | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str = None
        ):
        self.qt: QWidget = qt()
        
        if name:
            self.applyAttribute(
                self.qt.setObjectName,
                name
            )

        if height:
            self.applyAttribute(
                self.qt.setFixedHeight,
                height
            )
            
        if width:
            self.applyAttribute(
                self.qt.setFixedWidth,
                width
            )
        
        self.hAlign = hAlign
        self.vAlign = vAlign

        if state:
            self.applyAttribute(
                self.setState,
                state
            )


    def setState(self, value:str):
        self.qt.setProperty("state", value)
        self.qt.style().unpolish(self.qt)
        self.qt.style().polish(self.qt)


    def applyAttribute(self, setter: Callable, value):
        if isinstance(value, (Binding, Poll)):
            value.bind(setter)
        else:
            setter(value)


