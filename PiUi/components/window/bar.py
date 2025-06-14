
from .window import PiWindow
from .xstrut import Strut

from PiUi.app.core import Screen
from PiUi.components.widgets.widget import PiWidget
from PiUi.components.helpers import evalBarPosition, evalBarSize

from PiUi.app.utils.helper import enforceType

from typing import Literal


class PiBar(PiWindow):

    def __init__(        
        self,
        *,
        name: str | None = None,
        side: Literal["top", "bottom", "left", "right"],
        size: int,
        widget: PiWidget = None,
        strut: Strut = None,
        screen: Screen,
        focusable: bool = False
        ):
        
        enforceType(widget, (PiWidget, type(None)), "rootWidget")
        super().__init__(
            name = name, 
            position = evalBarPosition(side, size, screen), 
            size = evalBarSize(side, size, screen) , 
            strut = strut,
            widget = widget,
            windowType= "dock",
            ground = "fg",
            focusable= focusable
            )
