

from PiUI.components.widgets import PiBox, PiLabel

from PiUIutils import Binder, Poller, Alignment, Timer

from datetime import datetime

import tools

poller = Poller()
binder = Binder()


clock = PiLabel(
    name = "clock", 
    text = poller.Poll(20, func = lambda: datetime.now().strftime("%I:%M"))
)



workspaces = PiBox(
    name = "workspaces",
    orientation = "horizontal",
    spacing = 22,
    widgets = tools.get_workspaces(binder),
)

timer = Timer(0.1, lambda: tools.update_workspaces(binder))
timer.start()