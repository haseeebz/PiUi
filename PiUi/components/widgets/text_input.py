


from .widget import PiWidget
from PiUi.app.utils.binder import Binding
from PiUi.app.utils.poller import Poll
from PiUi.app.utils import Alignment

from typing import Callable

from PiUi.components.helpers import InputWidget

class PiTextInput(PiWidget):
    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        placeHolderText: str | Binding | Poll | None = None,
        onEnter: Callable | Binding | Poll | None = None,
        onChange:  Callable | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str | Binding | Poll | None = None    
    ):
        super().__init__(InputWidget, name, height, width, hAlign, vAlign, state)
        self._backend: InputWidget

        self.applyAttribute(
            self._backend.setPlaceholderText,
            placeHolderText,
        )

        self.applyAttribute(
            self._backend.setEnterFunc,
            onEnter
        )

        self.applyAttribute(
            self._backend.setChangeFunc,
            onChange
        )

