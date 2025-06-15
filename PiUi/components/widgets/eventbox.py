


from typing import Callable
from .widget import PiWidget
from PiUi.app.utils.binder import Binding
from PiUi.app.utils.poller import Poll
from PiUi.app.utils import Alignment
from PiUi.app.utils.helper import enforceType
from PySide6.QtWidgets import QHBoxLayout

from PiUi.components.helpers import EventWidget, clearLayout



class PiEventBox(PiWidget):
    
    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        widget: PiWidget | Binding | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str | Binding | Poll | None = None,
        onRightClick: Callable | Binding | Poll | None = None,
        onLeftClick: Callable | Binding | Poll | None = None,
        onMiddleClick: Callable | Binding | Poll | None = None,
        onDoubleClick: Callable | Binding | Poll | None = None,
        onMouseRelease: Callable | Binding | Poll | None = None,
        onMouseEnter: Callable | Binding | Poll | None = None,
        onMouseLeave: Callable | Binding | Poll | None = None,
        ):

        super().__init__(EventWidget, name, height, width, hAlign, vAlign, state)
        self._backend: EventWidget

        
        if onRightClick:
            self.applyAttribute(
                self._backend.connectRightClick,
                onRightClick
            )

        if onLeftClick:
            self.applyAttribute(
                self._backend.connectLeftClick,
                onLeftClick
            )

        if onMiddleClick:
            self.applyAttribute(
                self._backend.connectMiddleClick,
                onMiddleClick
            )

        if onMouseRelease:
            self.applyAttribute(
                self._backend.connectMouseRelease,
                onMouseRelease
            )

        if onDoubleClick:
            self.applyAttribute(
                self._backend.connectDoubleClick,
                onDoubleClick
            )

        if onMouseEnter:
            self.applyAttribute(
                self._backend.connectMouseEnter,
                onMouseEnter
            )

        if onMouseLeave:
            self.applyAttribute(
                self._backend.connectMouseLeave,
                onMouseLeave
            )


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
            self._backend.layout().addWidget( # type: ignore # None Handled
                widget._backend, 
                alignment= (widget.hAlign.value | widget.vAlign.value) # type: ignore # None Handled
                )
        

