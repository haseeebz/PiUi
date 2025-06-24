
from .widget import PiWidget
from PiUI.components.helpers import ImageWidget
from PiUI.core.tools.binder import Binding
from PiUI.core.tools.poller import Poll
from PiUI.core.tools import Alignment

	
class PiImage(PiWidget):

	def __init__(
		self,
		*,
		name: str | None = None,
		path: str | Binding | Poll | None = None,
		rounding: int = 0,
		preserveAspectRatio: bool = True,
		height: int | Binding | Poll | None = None,
		width: int | Binding | Poll | None = None,
		hAlign: Alignment.H | None = None,
		vAlign: Alignment.V | None = None,
		state: str | Binding | Poll | None = None,
		stretch: int = 1
	):

		super().__init__(ImageWidget, name, height, width, hAlign, vAlign, state, stretch)
		self._backend : ImageWidget

		if preserveAspectRatio:
			self._backend.preserveRatio()
		
		if rounding:
			self._backend.rounding(rounding)

		self.applyAttribute(
			self._backend.setImage,
			path
		)