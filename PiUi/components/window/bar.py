
from .window import PiWindow
from .xstrut import Strut
from typing import Literal
from ...core.app import Screen
from ..widgets.widget import PiWidget

from ..helpers import evalBarPosition, evalBarSize


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
        
        super().__init__(
            name, 
            position = evalBarPosition(position, size, screen), 
            size = evalBarSize(position, size, screen) , 
            strut = strut,
            rootWidget = rootWidget
            )
