
from PiUI.components.window import PiWindow
from PiUI.components.widgets import PiTextInput

import Xlib
class PiLockScreen(PiWindow):

	def __init__(self) -> None:
		super().__init__(
			name = "lock",
			position = (0,0),
			size = (1920, 1080),
			transparent = True,
			focusable = True,
			widget = PiTextInput(placeHolderText = "Works?")
		)
		self.show()
