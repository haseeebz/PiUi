
from PiUI.components.window import PiWindow
from PiUI.components.widgets.widget import PiWidget
from PiUI.components.widgets import PiPasswordBox

from PiUI.core.tools.screen import Screen

from PySide6.QtCore import QCoreApplication

class PiLockScreen(PiWindow):

	def __init__(
		self,
		*,
		name: str,
		screen: Screen,
		transparent: bool = False,
		focusable: bool = True,
		widget: PiWidget,
		passwordBox: PiPasswordBox
		) -> None:
		super().__init__(
			name = name,
			position = (0,0),
			size = screen.pair,
			transparent = transparent,
			focusable = focusable,
			widget = widget
		)
		self._backend._should_steal_input = True
		self._backend.inputhandler.connectPasswordBox(passwordBox._receiveKey)
		self.ignoreWM()
		