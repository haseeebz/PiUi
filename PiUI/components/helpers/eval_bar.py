

from typing import Tuple

def evalBarPosition(position: str,  size: int, screen) -> Tuple[int, int]:
    
    positions = {
        "top" : (0, 0),
        "bottom" : (0, screen.y - size),
        "left" : (0, 0),
        "right" : (screen.x - size, 0)
    }

    if position in positions:
        return positions[position]
    else:
        print("Incorrect Position for PiBar, Defaulting to Bottom.")
        return positions["bottom"]


def evalBarSize(position: str,  size: int, screen) -> Tuple[int, int]:

    sizes = {
        "top" : (screen.x , size),
        "bottom" : (screen.x, size),
        "left" : (size, screen.y),
        "right" : (size, screen.y)
    }

    if position in sizes:
        return sizes[position]
    else:
        print("Incorrect Position for PiBar, Defaulting to Bottom.")
        return sizes["bottom"]

