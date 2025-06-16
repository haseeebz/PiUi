

from .widget import PiWidget

from PiUI.components.helpers import clearLayout
from PiUI.app.utils.binder import Binding
from PiUI.app.utils.poller import Poll
from PiUI.app.utils import Alignment
from PiUI.app.utils.helper import enforceType

from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QSizePolicy,
    QWidget
)

from PySide6.QtCore import Qt

from typing import Literal


class PiBox(PiWidget):
    
    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        orientation: Literal["horizontal", "vertical"] | None = "horizontal",
        widgets: list[PiWidget] | Binding | None = None,
        spacing: int | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str | Binding | Poll | None = None
        ):

        super().__init__(QWidget, name, height, width, hAlign, vAlign, state)
        self._backend: QWidget
        
        enforceType(widgets, (list, Binding, type(None)), "widgets")

        if orientation == "horizontal":
            layout = QHBoxLayout()
        elif orientation == "vertical":
            layout = QVBoxLayout()
        else:
            print("Incorrect or Left out orientation for PiBox!\nDefaulting to horizontal.")
            layout = QHBoxLayout()
        
        layout.setContentsMargins(0,0,0,0)
        
        self._backend.setLayout(layout)
        self._backend.setContentsMargins(0,0,0,0)
        if spacing:
            self.applyAttribute(
                self._backend.layout().setSpacing, # type: ignore # None Handled
                spacing
            )
        
        if widgets:
            self.applyAttribute(
                self.setWidgets,
                widgets
            )

    def setWidgets(self, widgets: list[PiWidget]):
        layout = self._backend.layout()
        clearLayout(layout)
        if widgets and layout:
            for widget in widgets:
                self._backend.layout().addWidget( # type: ignore # None Handled
                    widget._backend,
                    stretch = 1,   # type: ignore # *
                    alignment = (widget.hAlign.value | widget.vAlign.value) # type: ignore # None Handled
                    )
        
    # * QLayout doesnt have stretch but its subclasses: QVboxLayout and QHboxLayout do have this parameter