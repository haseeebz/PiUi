

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

        self._qt___: QWidget = qt()
        
        if name:
            self.applyAttribute(
                self._qt___.setObjectName,
                name
            )

        if height:
            self.applyAttribute(
                self._qt___.setFixedHeight,
                height
            )
            
        if width:
            self.applyAttribute(
                self._qt___.setFixedWidth,
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
        self._qt___.setProperty("state", value)
        self._qt___.style().unpolish(self._qt___)
        self._qt___.style().polish(self._qt___)


    def applyAttribute(self, setter: Callable, value):
        if isinstance(value, (Binding, Poll)):
            value.bind(setter)
        else:
            setter(value)



