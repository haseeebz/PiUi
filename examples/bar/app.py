
from PiUi.core import AppCore

from PiUi.components.window import PiBar, Strut
from PiUi.components.widgets import PiBox


def main():
    
    core = AppCore()


    leftBox = PiBox(

    )

    midBox = PiBox(

    )

    rightBox = PiBox(

    )


    root = PiBox(
        None,
        "horizontal",
        [leftBox, midBox, rightBox]
    )


    bar = PiBar(
        "bar",
        position = "bottom",
        size = 40,
        rootWidget = root,
        strut = Strut((0,0,0,40), core.screen),
        screen = core.screen
    )

    bar.show()

    core.setStyleSheet("style.qss")
    core.run()
