
from PiUI.app.core import AppCore
from PiUI.components.window import PiBar, Strut, PiWindow

from PiUI.components.widgets import PiBox, PiLabel
from PiUI.app.utils import Alignment

core = AppCore(logfile= "test.log")

import widgets


bar = PiBar(
    name = "bar",
    side = "bottom",
    size = 40,
    screen = core.screen,
    strut = Strut(core.screen, bottom = 42),

    widget = PiBox(
        orientation = "horizontal",
        width = core.screen.x,
        widgets = [

            PiBox(
                hAlign = Alignment.H.left,
                orientation = "horizontal",
                widgets = [
                    widgets.workspaces
                ],
                    
            ),

            PiBox(
                orientation = "horizontal",
                hAlign = Alignment.H.center,
                widgets = [
                    widgets.clock
                ]

            ),

            PiBox(
                hAlign = Alignment.H.right,
                orientation = "horizontal",
            )
        ]
    )
)

bar.show()
core.setStyleSheet("style.qss")
core.run()