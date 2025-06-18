
from PySide6.QtWidgets import QProgressBar
from PySide6.QtCore import Qt

from .widget import PiWidget
from PiUI.core.tools.binder import Binding
from PiUI.core.tools.poller import Poll
from PiUI.core.tools import Alignment

from typing import Callable, Literal


class PiProgress(PiWidget):

	def __init__(
		self,
		*,
		name: str | Binding | Poll | None = None,
		value: int | Binding | Poll | None = None,
		orientation: Literal["horizontal", "vertical"] | Binding | Poll | None = "horizontal",
		onChange: Callable | None = None,
		height: int | Binding | Poll | None = None,
		width: int | Binding | Poll | None = None,
		hAlign: Alignment.H | None = None,
		vAlign: Alignment.V | None = None,
		state: str | Binding | Poll | None = None    
	):
		super().__init__(QProgressBar, name, height, width, hAlign, vAlign, state)
		self._backend: QProgressBar

		if value:
			self.applyAttribute(
				self._backend.setValue,
				value
			)

		if orientation:
			self.applyAttribute(
				self._orientation,
				orientation
			)
			
		if onChange:
			self.applyAttribute(
				self._backend.valueChanged.connect,
				onChange
			)
			
		self._backend.setTextVisible(False)

	def _orientation(self, o: Literal["horizontal", "vertical"]):
		orientations = {
			"horizontal" : Qt.Orientation.Horizontal,
			"vertical" : Qt.Orientation.Vertical
		}
		self._backend.setOrientation(orientations[o])

		