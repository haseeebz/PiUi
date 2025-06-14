

from .widget import PiWidget

from PiUi.app.utils.binder import Binding
from PiUi.app.utils.poller import Poll
from PiUi.app.utils import Alignment

from PySide6.QtWidgets import QLabel, QHBoxLayout


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
        self._backend: QLabel

        if text:
            self.applyAttribute(
                self._backend.setText,
                text
            )
        
        self._backend.setLayout(QHBoxLayout())


