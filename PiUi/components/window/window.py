
from .xstrut import Strut
from .x11 import XBackEnd

from PiUi.components.widgets.widget import PiWidget
from PiUi.app.utils.helper import enforceType

from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtCore import Qt

from typing import Tuple, Literal


class PiWindow():

    def __init__(
        self,
        *,
        name: str | None = None,
        position: Tuple[int, int],
        size: Tuple[int, int],
        widget: PiWidget = None,
        strut: Strut = None,    
        windowType: Literal["desktop", "dock"] = "dock",
        ground: Literal["fg", "bg"] = "fg",
        focusable: bool = False
        ):

        enforceType(widget, (PiWidget, type(None)), "widget")
        enforceType(strut, (Strut, type(None)), "strut")

        
 
        if windowType not in ("dock", "desktop"):
            raise ValueError(f"Invalid Window Type! (name={name}). Valid Types are: 'dock', 'desktop'")
        if ground not in ("fg", "bg"):
            raise ValueError(f"Invalid Window Ground! (name={name}). Valid Types are: 'fg', 'bg'")

        
        if True:
            self._backend: XBackEnd = XBackEnd(windowType, ground, strut, focusable)
        else: 
            pass #wayland


        self._backend.setGeometry(*position, *size)
        self._backend.setFixedSize(*size)

        if name:
            self._backend.setObjectName(name)

        # Root Widget Setup

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        
        if widget:
            layout.addWidget(widget._backend, alignment= widget.hAlign.value | widget.vAlign.value)

        self._backend.setLayout(layout)
        self._backend.setContentsMargins(0,0,0,0)


    def close(self):
        self._backend.close()

    def show(self):
        self._backend.show()

    def hide(self):
        self._backend.hide()

    def toggle(self):
        if self._backend.isHidden():
            self.show()
        else:
            self.hide()

    def ignoreWM(self):
        self._backend.setWindowFlag(Qt.WindowType.BypassWindowManagerHint)