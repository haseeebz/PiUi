
from PiUI.core import Pi

from PiUI.components.window import PiWindow
from PiUI.components.widgets import PiLabel, PiBox

from datetime import datetime

Pi.init()

clock = PiLabel(
	name = "clock",
	text = Pi.poller.Poll(10, func = lambda: datetime.now().strftime("%I:%M")),
	yAlign = Pi.Alignment.V.bottom
)

m = PiLabel(
	name = "m",
	text = Pi.poller.Poll(10, func = lambda: datetime.now().strftime("%p")),
	yAlign = Pi.Alignment.V.bottom
)

win = PiWindow(
	name = "win",
	position = ( Pi.screen.x//2 - 250, Pi.screen.y//2 - 400),
	size = (500, 160),
	windowType = "desktop",
	ground = "bg",
	transparent = True,

	widget = PiBox(
		orientation = "horizontal",

		widgets = [
			clock,
			m
		]
	)
)

win.show()

Pi.setStylesheet("style.css")
Pi.controller.registerWindows(win)
Pi.run()