




from .widget import PiWidget
from PiUI.core.tools.binder import Binding
from PiUI.core.tools.poller import Poll
from PiUI.core.tools import Alignment

from typing import Callable, Literal

from PiUI.components.helpers import ScrollWidget, clearLayout
from PiUI.core.tools.helper import enforceType

class PiScrollBox(PiWidget):
    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        orientation: Literal["horizontal", "vertical"] | None = "horizontal",
        widget: PiWidget | Binding | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = None,
        vAlign: Alignment.V | None = None,
        state: str | Binding | Poll | None = None,
        onScroll: Callable | None = None,
    ):
        super().__init__(ScrollWidget, name, height, width, hAlign, vAlign, state)
        self._backend: ScrollWidget

        if orientation == "horizontal":
            self._backend.makeHorizontal()
        elif orientation == "vertical":
            self._backend.makeVertical()
        else:
            self._backend.makeHorizontal()
        
        
        enforceType(widget, (PiWidget, Binding, type(None)), "widget")

        if widget:
            self._backend.setWidget(widget._backend) # type: ignore #already handled above

        if onScroll:
            self.applyAttribute(
                self._backend.setOnScroll,
                onScroll
            )
                
    
