


from PiUI.core.tools.binder import Binding
from PiUI.core.tools.poller import Poll
from PiUI.core.tools import Alignment

from PySide6.QtWidgets import QFrame
from .widget import PiWidget

class PiSpacer(PiWidget):

	def __init__(
		self,
		*,
		name: str | Binding | Poll | None = None,
		height: int | Binding | Poll | None = None,
		width: int | Binding | Poll | None = None,
		hAlign: Alignment.H | None = None,
		vAlign: Alignment.V | None = None,
		state: str | Binding | Poll | None = None 
		):

		super().__init__(QFrame, name, height, width, hAlign, vAlign, state)
		self._backend: QFrame
