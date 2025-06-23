



from PiUI.core.tools.binder import Binding
from PiUI.core.tools.poller import Poll
from PiUI.core.tools import Alignment

from PySide6.QtWidgets import QWidget, QStackedLayout

from .widget import PiWidget
from PiUI.core.tools.helper import enforceType
from PiUI.components.helpers import clearLayout

from typing import Any

from PiUI.core.logger import getLogger
log = getLogger("component")

class PiOverlay(PiWidget):

	def __init__(
		self,
		*,
		name: str | Binding | Poll | None = None,
		height: int | Binding | Poll | None = None,
		width: int | Binding | Poll | None = None,
		hAlign: Alignment.H | None = None,
		vAlign: Alignment.V | None = None,
		state: str | Binding | Poll | None = None,
		widgets: list[Any] | Binding | None = None,
		):
		super().__init__(QWidget, name, height, width, hAlign, vAlign, state)
		self._backend: QWidget

		self._backend.layoutBox = QStackedLayout()
		self._backend.layoutBox.setStackingMode(QStackedLayout.StackingMode.StackAll)

		self._backend.layoutBox.setContentsMargins(0,0,0,0)
		self._backend.setContentsMargins(0,0,0,0)
		self._backend.setLayout(self._backend.layoutBox)	

		if widgets:
			self.applyAttribute(
				self.setWidgets,
				widgets
			)

	def setWidgets(self, widgets: list[PiWidget]):
		layout = self._backend.layout()
		clearLayout(layout)

		if not (widgets and layout):
			return
		
		for widget in widgets:
			enforceType(widget, (PiWidget, Binding), "widget")

			layout.addWidget( 
				widget._backend,
				)