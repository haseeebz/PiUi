


from PiUI.app.utils.binder import Binding
from PiUI.app.utils.poller import Poll
from PiUI.app.utils import Alignment

from PySide6.QtWidgets import QWidget, QSizePolicy
from typing import Callable

class PiWidget():

    def __init__(
        self,
        qt,
        name: str | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str | Binding | Poll | None = None 
        ):

        self._backend: QWidget = qt()
        
        if name:
            self.applyAttribute(
                self._backend.setObjectName,
                name
            )

        if height:
            self.applyAttribute(
                self._backend.setFixedHeight,
                height
            )
            
        if width:
            self.applyAttribute(
                self._backend.setFixedWidth,
                width
            )
        
        self.hAlign = hAlign
        self.vAlign = vAlign

        if state:
            self.applyAttribute(
                self.setState,
                state
            )

        self._backend.setContentsMargins(0,0,0,0)
        self._backend.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)


    def setState(self, value:str):
        self._backend.setProperty("state", value)
        self._backend.style().unpolish(self._backend)
        self._backend.style().polish(self._backend)


    def applyAttribute(self, setter: Callable, value):
        if isinstance(value, (Binding, Poll)):
            value.bind(setter)
        else:
            setter(value)



