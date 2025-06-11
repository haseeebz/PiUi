
from typing import Literal
from .widget import PiWidget
from PiUi.core.utils.bind import Binding
from PiUi.core.utils.poll import Poll
from PiUi.core.utils.alignment import Alignment
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFrame
)




class PiBox(PiWidget):
    
    def __init__(
        self,
        name: str | Binding | Poll | None = None,
        orientation: Literal["horizontal", "vertical"] | None = "horizontal",
        widgets: list[PiWidget] | Binding | None = None,
        *,
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
            self.layout = QHBoxLayout()
        elif orientation == "vertical":
            self.layout = QVBoxLayout()
        else:
            print("Incorrect or Left out orientation for PiBox!\nDefaulting to horizontal.")
            self.layout = QHBoxLayout()
        
        self._qt___.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)


        if widgets:
            for widget in widgets:
                self.layout.addWidget(widget._qt___, alignment= (widget.hAlign.value | widget.vAlign.value))
        

        if spacing:
            self.applyAttribute(
                self.layout.setSpacing,
                spacing
            )
