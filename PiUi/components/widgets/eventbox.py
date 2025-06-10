


from typing import Callable
from .widget import PiWidget
from PiUi.core.utils import Binding, Poll, Alignment
from PySide6.QtWidgets import QHBoxLayout

from ..helpers import CustomEventWidget


class PiEventBox(PiWidget):
    
    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str | Binding | Poll | None = None,
        widget: PiWidget | Binding | None = None,
        onRightClick: Callable | Binding | Poll | None = None,
        onLeftClick: Callable | Binding | Poll | None = None,
        onMiddleClick: Callable | Binding | Poll | None = None,
        onDoubleClick: Callable | Binding | Poll | None = None,
        onMouseRelease: Callable | Binding | Poll | None = None,
        onMouseEnter: Callable | Binding | Poll | None = None,
        onMouseLeave: Callable | Binding | Poll | None = None,
        ):

        super().__init__(CustomEventWidget, name, height, width, hAlign, vAlign, state)
        self.qt: CustomEventWidget

        
        if onRightClick:
            self.applyAttribute(
                self.qt.connectRightClick,
                onRightClick
            )

        if onLeftClick:
            self.applyAttribute(
                self.qt.connectLeftClick,
                onLeftClick
            )

        if onMiddleClick:
            self.applyAttribute(
                self.qt.connectMiddleClick,
                onMiddleClick
            )

        if onMouseRelease:
            self.applyAttribute(
                self.qt.connectMouseRelease,
                onMouseRelease
            )

        if onDoubleClick:
            self.applyAttribute(
                self.qt.connectDoubleClick,
                onDoubleClick
            )

        if onMouseEnter:
            self.applyAttribute(
                self.qt.connectMouseEnter,
                onMouseEnter
            )

        if onMouseLeave:
            self.applyAttribute(
                self.qt.connectMouseLeave,
                onMouseLeave
            )


        self.layout = QHBoxLayout()
        self.qt.setLayout(self.layout)
        self.qt.setContentsMargins(0,0,0,0)

        if widget:
            self.layout.addWidget(widget.qt)


