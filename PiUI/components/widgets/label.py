

from .widget import PiWidget

from PiUI.core.tools.binder import Binding
from PiUI.core.tools.poller import Poll
from PiUI.core.tools import Alignment

from PySide6.QtWidgets import QLabel, QHBoxLayout, QSizePolicy


class PiLabel(PiWidget):
    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        text: str | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = None,
        vAlign: Alignment.V | None = None,
        state: str | Binding | Poll | None = None    
    ):
        
        super().__init__(QLabel, name, height, width, hAlign, vAlign, state)
        self._backend: QLabel

        if text:
            self.applyAttribute(
                self._backend.setText,
                text
            )
        

        


