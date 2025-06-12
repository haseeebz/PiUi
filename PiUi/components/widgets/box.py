
from typing import Literal
from .widget import PiWidget

from PiUi.components.helpers import clearLayout
from PiUi.app.utils.binder import Binding
from PiUi.app.utils.poller import Poll
from PiUi.app.utils import Alignment
from PiUi.app.utils.helper import enforceType

from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QFrame
)




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

        super().__init__(QFrame, name, height, width, hAlign, vAlign, state)
        self._qt___: QFrame
        
        if orientation == "horizontal":
            layout = QHBoxLayout()
        elif orientation == "vertical":
            layout = QVBoxLayout()
        else:
            print("Incorrect or Left out orientation for PiBox!\nDefaulting to horizontal.")
            layout = QHBoxLayout()
        
        layout.setContentsMargins(0,0,0,0)
        self._qt___.setLayout(layout)
        self._qt___.setContentsMargins(0,0,0,0)

        if spacing:
            self.applyAttribute(
                self._qt___.layout().setSpacing,
                spacing
            )
        
        enforceType(widgets, (list, Binding, type(None)), "widgets")
        if widgets:
            self.applyAttribute(
                self.setWidgets,
                widgets
            )

    def setWidgets(self, widgets: list[PiWidget]):
        layout = self._qt___.layout()
        clearLayout(layout)
        if widgets:
            for widget in widgets:
                self._qt___.layout().addWidget(
                    widget._qt___, 
                    alignment= (widget.hAlign.value | widget.vAlign.value)
                    )
        
    