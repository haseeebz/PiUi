

from typing import Callable
from PiUi.core.utils.bind import Binding
from PiUi.core.utils.poll import Poll
from PiUi.core.utils.alignment import Alignment
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

        self.__qt__: QWidget = qt()
        
        if name:
            self.applyAttribute(
                self.__qt__.setObjectName,
                name
            )

        if height:
            self.applyAttribute(
                self.__qt__.setFixedHeight,
                height
            )
            
        if width:
            self.applyAttribute(
                self.__qt__.setFixedWidth,
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
        self.__qt__.setProperty("state", value)
        self.__qt__.style().unpolish(self.qt)
        self.__qt__.style().polish(self.qt)


    def applyAttribute(self, setter: Callable, value):
        if isinstance(value, (Binding, Poll)):
            value.bind(setter)
        else:
            setter(value)



