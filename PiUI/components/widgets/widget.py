


from PiUI.core.tools.binder import Binding
from PiUI.core.tools.poller import Poll
from PiUI.core.tools import Alignment

from PySide6.QtWidgets import QWidget
from typing import Callable

class PiWidget():

    def __init__(
        self,
        qt,
        name: str | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = None,
        vAlign: Alignment.V | None = None,
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
        

        self.alignment = Alignment.base
        if hAlign:
            self.alignment |= hAlign.value
        if vAlign:
            self.alignment |= vAlign.value


        if state:
            self.applyAttribute(
                self.setState,
                state
            )

        self._backend.setContentsMargins(0,0,0,0)
    

    def setState(self, value:str):
        self._backend.setProperty("state", value)
        self._backend.style().unpolish(self._backend)
        self._backend.style().polish(self._backend)


    def applyAttribute(self, setter: Callable, value):
        if isinstance(value, (Binding, Poll)):
            value.bind(setter)
        else:
            setter(value)



