
from .window import PiWindow
from .xstrut import Strut
from typing import Literal
from PiUi.core import Screen
from PiUi.components.widgets.widget import PiWidget
from PiUi.components.helpers import evalBarPosition, evalBarSize

from PiUi.core.utils.helper import enforceType

class PiBar(PiWindow):

    def __init__(        
        self,
        name: str | None,
        position: Literal["top", "bottom", "left", "right"],
        size: int,
        *,
        rootWidget: PiWidget = None,
        strut: Strut = None,
        screen: Screen
        ):
        
        enforceType(rootWidget, (PiWidget, type(None)), "rootWidget")
        super().__init__(
            name, 
            position = evalBarPosition(position, size, screen), 
            size = evalBarSize(position, size, screen) , 
            strut = strut,
            rootWidget = rootWidget
            )
