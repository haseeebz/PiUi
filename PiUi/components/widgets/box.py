
from typing import Literal
from .widget import PiWidget
from PiUi.core.utils import Binding, Poll, Alignment
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout
)




class PiBox(PiWidget):
    
    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        orientation: Literal["horizontal", "vertical"] | None,
        spacing: int | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        widgets: list[PiWidget] | Binding | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str | Binding | Poll | None = None
        ):

        super().__init__(QWidget, name, height, width, hAlign, vAlign, state)
        self.qt: QWidget
        
        if orientation == "horizontal":
            self.layout = QHBoxLayout()
        elif orientation == "vertical":
            self.layout = QVBoxLayout()
        else:
            print("Incorrect or Left out orientation for PiBox!\nDefaulting to horizontal.")
            self.layout = QHBoxLayout()
        
        self.qt.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)


        if widgets:
            for widget in widgets:
                self.layout.addWidget(widget.qt, alignment= (widget.hAlign.value | widget.vAlign.value))
        

        if spacing:
            self.applyAttribute(
                self.layout.setSpacing,
                spacing
            )
