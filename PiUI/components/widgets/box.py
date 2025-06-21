

from .widget import PiWidget

from PiUI.components.helpers import clearLayout
from PiUI.core.tools.binder import Binding
from PiUI.core.tools.poller import Poll
from PiUI.core.tools import Alignment
from PiUI.core.tools.helper import enforceType

from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QSizePolicy,
    QWidget,
    QSpacerItem
)

from PySide6.QtCore import Qt

from typing import Literal, Any


class PiBox(PiWidget):
    
    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        orientation: Literal["horizontal", "vertical"] | None = "horizontal",
        widgets: list[Any] | Binding | None = None,
        spacing: int | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = None,
        vAlign: Alignment.V | None = None,
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

        if not (widgets and layout):
            return
        
        for widget in widgets:
            enforceType(widget, (PiWidget, Binding), "widget")
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

    # * QLayout doesnt have stretch but its subclasses: QVboxLayout and QHboxLayout do have this parameter