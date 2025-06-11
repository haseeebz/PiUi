


from typing import Callable
from .widget import PiWidget
from PiUi.core.utils.bind import Binding
from PiUi.core.utils.poll import Poll
from PiUi.core.utils.alignment import Alignment
from PiUi.core.utils.helper import enforceType
from PySide6.QtWidgets import QHBoxLayout

from PiUi.components.helpers import CustomEventWidget


class PiEventBox(PiWidget):
    
    def __init__(
        self,
        name: str | Binding | Poll | None = None,
        widget: PiWidget | Binding | None = None,
        *,
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

        super().__init__(CustomEventWidget, name, height, width, hAlign, vAlign, state)
        self._qt___: CustomEventWidget

        
        if onRightClick:
            self.applyAttribute(
                self._qt___.connectRightClick,
                onRightClick
            )

        if onLeftClick:
            self.applyAttribute(
                self._qt___.connectLeftClick,
                onLeftClick
            )

        if onMiddleClick:
            self.applyAttribute(
                self._qt___.connectMiddleClick,
                onMiddleClick
            )

        if onMouseRelease:
            self.applyAttribute(
                self._qt___.connectMouseRelease,
                onMouseRelease
            )

        if onDoubleClick:
            self.applyAttribute(
                self._qt___.connectDoubleClick,
                onDoubleClick
            )

        if onMouseEnter:
            self.applyAttribute(
                self._qt___.connectMouseEnter,
                onMouseEnter
            )

        if onMouseLeave:
            self.applyAttribute(
                self._qt___.connectMouseLeave,
                onMouseLeave
            )


        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self._qt___.setLayout(layout)
        self._qt___.setContentsMargins(0,0,0,0)

        enforceType(widget, [PiWidget, Binding, type(None)], "widget")
        if widget:
                self.applyAttribute(
                    self.setWidgets,
                    widget
                )


    def setWidgets(self, widget: PiWidget):
        self._qt___.layout().addWidget(
            widget._qt___, 
            alignment= (widget.hAlign.value | widget.vAlign.value)
            )
        

