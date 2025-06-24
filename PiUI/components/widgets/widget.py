


from PiUI.core.tools.binder import Binding
from PiUI.core.tools.poller import Poll
from PiUI.core.tools import Alignment

from PySide6.QtWidgets import QWidget
from typing import Callable


from PiUI.core.logger import getLogger
log = getLogger("component")

class PiWidget():

	def __init__(
		self,
		qt,
		name: str | Binding | Poll | None = None,
		height: int | Binding | Poll | None = None,
		width: int | Binding | Poll | None = None,
		hAlign: Alignment.H | None = None,
		vAlign: Alignment.V | None = None,
		state: str | Binding | Poll | None = None,
		stretch: int = 1
		):

		self._backend: QWidget = qt()
		
		if name:
			self.applyAttribute(
				self._backend.setObjectName,
				name
			)

		if height:
			self.applyAttribute(
				self._backend.setFixedHeight,
				height
			)
			
		if width:
			self.applyAttribute(
				self._backend.setFixedWidth,
				width
			)
		
		if hAlign and vAlign:
			self.alignment = hAlign.value | vAlign.value
		elif hAlign:
			self.alignment = hAlign.value
		elif vAlign:
			self.alignment = vAlign.value
		else:
			self.alignment = None

		if stretch > 0:
			self.stretch = stretch
		else:
			self.stretch = 1
			
		if state:
			self.applyAttribute(
				self.setState,
				state
			)

		self._backend.setContentsMargins(0,0,0,0)
	

	def setState(self, value:str):
		self._backend.setProperty("state", value)
		self._backend.style().unpolish(self._backend)
		self._backend.style().polish(self._backend)


	def applyAttribute(self, setter: Callable, value):
		if isinstance(value, Binding):
			value.bind(setter)
			log.debug(f"Binding '{value.key}' was binded to setter: {setter}")
		elif isinstance(value, Poll):
			value.bind(setter)
		else:
			setter(value)



