
from .widget import PiWidget
from PiUI.core.tools.binder import Binding
from PiUI.core.tools.poller import Poll
from PiUI.core.tools import Alignment

from typing import Callable

from PiUI.components.helpers import InputWidget


class PiPasswordBox(PiWidget):
	def __init__(
		self,
		*,
		name: str | None = None,
		placeHolderText: str | Binding | Poll | None = None,
		text: str | Binding | Poll | None = None,
		onEnter: Callable | None = None,
		onChange:  Callable | None = None,
		height: int | Binding | Poll | None = None,
		width: int | Binding | Poll | None = None,
		hAlign: Alignment.H | None = None,
		vAlign: Alignment.V | None = None,
		state: str | Binding | Poll | None = None,
		stretch: int = 1    
	):
		super().__init__(InputWidget, name, height, width, hAlign, vAlign, state, stretch)
		self._backend: InputWidget

		self.applyAttribute(
			self._backend.setPlaceholderText,
			placeHolderText,
		)

		self._backend.setPasswordEcho()
		
		if onEnter:
			self._backend.setEnterFunc(lambda x: (self._backend.setText(""), onEnter(x)))

		if onChange:
			self._backend.setChangeFunc(onChange)
		
		if text:
			self.applyAttribute(
				self._backend.setText,
				text
			)

	def _receiveKey(self, key: str):
		self._backend.setFocus()
		text = self._backend.text()
		length = len(text)
		match key:
			case '\r':
				self._backend.returnPressed.emit()
			case '\b':
				if length >= 1:
					self._backend.setText(text[0:-2])
			case _:
				self._backend.setText(text + str(key))