
from .window import PiWindow
from .xstrut import Strut


from PiUI.components.widgets.widget import PiWidget
from PiUI.components.helpers import evalBarPosition, evalBarSize

from PiUI.utils.helper import enforceType
from PiUI.utils import Screen
from typing import Literal

from PiUI.core.logger import getLogger


class PiBar(PiWindow):

    def __init__(        
        self,
        *,
        name: str,
        side: Literal["top", "bottom", "left", "right"],
        size: int,
        widget: PiWidget,
        strut: Strut | None = None,
        screen: Screen,
        focusable: bool = False
        ):
        log = getLogger("window")
        log.info(f"PiBar '{name}' is being initalized. Now will be known as PiWindow {name}.")
        enforceType(widget, (PiWidget, type(None)), "widget")
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
