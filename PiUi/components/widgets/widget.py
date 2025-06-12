

from typing import Callable
from PiUi.app.utils.binder import Binding
from PiUi.app.utils.poller import Poll
from PiUi.app.utils import Alignment
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

        self._qt___.setContentsMargins(0,0,0,0)


    def setState(self, value:str):
        self._qt___.setProperty("state", value)
        self._qt___.style().unpolish(self._qt___)
        self._qt___.style().polish(self._qt___)


    def applyAttribute(self, setter: Callable, value):
        if isinstance(value, (Binding, Poll)):
            value.bind(setter)
        else:
            setter(value)



