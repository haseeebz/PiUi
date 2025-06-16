
from PiUI.app.core import AppCore
from PiUI.components.window import PiBar, Strut, PiWindow

from PiUI.components.widgets import PiBox, PiLabel
from PiUI.app.utils import Alignment
core = AppCore()

import widgets


bar = PiWindow(
    name = "bar",
    position = (0, core.screen.y - 40),
    size = (core.screen.x, 40),
    strut = Strut(core.screen, bottom = 42),

    widget = PiBox(
        orientation = "horizontal",
        widgets = [
            widgets.workspaces,
            widgets.clock
        ]
    )
)

bar.show()

core.setStyleSheet("style.qss")
core.run()