


from typing import Callable
from .widget import PiWidget
from PiUI.core.tools.binder import Binding
from PiUI.core.tools.poller import Poll
from PiUI.core.tools import Alignment
from PiUI.core.tools.helper import enforceType
from PySide6.QtWidgets import QHBoxLayout

from PiUI.components.helpers import EventWidget, clearLayout



class PiEventBox(PiWidget):
    
    def __init__(
        self,
        *,
        name: str | None = None,
        widget: PiWidget | Binding | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = None,
        vAlign: Alignment.V | None = None,
        state: str | Binding | Poll | None = None,
        onRightClick: Callable | None = None,
        onLeftClick: Callable | None = None,
        onMiddleClick: Callable | None = None,
        onDoubleClick: Callable | None = None,
        onMouseRelease: Callable | None = None,
        onMouseEnter: Callable | None = None,
        onMouseLeave: Callable | None = None,
        stretch: int = 1
        ):

        super().__init__(EventWidget, name, height, width, hAlign, vAlign, state, stretch)
        self._backend: EventWidget


        if onRightClick:
            self._backend.connectRightClick(onRightClick)

        if onLeftClick:
            self._backend.connectLeftClick(onLeftClick)

        if onMiddleClick:
            self._backend.connectMiddleClick(onMiddleClick)

        if onMouseRelease:
            self._backend.connectMouseRelease(onMouseRelease)

        if onDoubleClick:
            self._backend.connectDoubleClick(onDoubleClick)

        if onMouseEnter:
            self._backend.connectMouseEnter(onMouseEnter)

        if onMouseLeave:
            self._backend.connectMouseLeave(onMouseLeave)


        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self._backend.setLayout(layout)
        self._backend.setContentsMargins(0,0,0,0)

        enforceType(widget, (PiWidget, Binding, type(None)), "widget")
        if widget:
                self.applyAttribute(
                    self.setWidget,
                    widget
                )


    def setWidget(self, widget: PiWidget):
        layout = self._backend.layout()
        clearLayout(layout)
        if layout and widget:
            if widget.alignment:
                layout.addWidget( 
                    widget._backend,
                    stretch = 1,   # type: ignore # *
                    alignment = widget.alignment # type: ignore # None Handled
                    )
            else:
                layout.addWidget( 
                    widget._backend,
                    stretch = 1,   # type: ignore 
                    )
        

