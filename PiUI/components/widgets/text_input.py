
from .widget import PiWidget
from PiUI.core.tools.binder import Binding
from PiUI.core.tools.poller import Poll
from PiUI.core.tools import Alignment

from typing import Callable

from PiUI.components.helpers import InputWidget


class PiTextInput(PiWidget):
	def __init__(
		self,
		*,
		name: str | None = None,
		placeHolderText: str | Binding | Poll | None = None,
		text: str | Binding | Poll | None = None,
		onEnter: Callable | None = None,
		onChange:  Callable | None = None,
		password: bool = False,
		height: int | Binding | Poll | None = None,
		width: int | Binding | Poll | None = None,
		hAlign: Alignment.H | None = None,
		vAlign: Alignment.V | None = None,
		state: str | Binding | Poll | None = None    
	):
		super().__init__(InputWidget, name, height, width, hAlign, vAlign, state)
		self._backend: InputWidget

		self.applyAttribute(
			self._backend.setPlaceholderText,
			placeHolderText,
		)

		if password:
			self._backend.setPasswordEcho()
		
		if onEnter:
			self._backend.setEnterFunc(onEnter)

		if onChange:
			self._backend.setChangeFunc(onChange)
		
		if text:
			self.applyAttribute(
				self._backend.setText,
				text
			)

