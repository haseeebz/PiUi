

from .widget import PiWidget
from PiUi.core.utils import Binding, Poll, Alignment
from PySide6.QtWidgets import QLabel


class PiLabel(PiWidget):
    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        text: str | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str | Binding | Poll | None = None    
    ):
        
        super().__init__(QLabel, name, height, width, hAlign, vAlign, state)
        self.qt: QLabel

        if text:
            self.applyAttribute(
                self.qt.setText,
                text
            )
        
        