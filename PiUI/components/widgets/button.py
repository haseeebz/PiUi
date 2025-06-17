


from typing import Callable
from .widget import PiWidget
from PiUI.core.tools.binder import Binding
from PiUI.core.tools.poller import Poll
from PiUI.core.tools import Alignment
from PySide6.QtWidgets import QPushButton

    
class PiButton(PiWidget):

    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        text: str | Binding | None = None,
        onClick: Callable | Binding | None = None,
        onRelease: Callable | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = None,
        vAlign: Alignment.V | None = None,
        state: str | Binding | Poll | None = None
    ):

        super().__init__(QPushButton, name, height, width, hAlign, vAlign, state)
        self._backend : QPushButton
    
        if text:
            self.applyAttribute(
                self._backend.setText,
                text
            )

        if onClick:
            self.applyAttribute(
                self._backend.clicked.connect,
                onClick
            )

        if onRelease:
            self.applyAttribute(
                self._backend.released.connect,
                onRelease
            )



