
from operator import pos
from PySide6.QtWidgets import QHBoxLayout, QWidget
from PySide6.QtCore import Qt

from .xstrut import Strut
from .x11 import XBackEnd
from PiUI.components.widgets.widget import PiWidget
from PiUI.core.tools.helper import enforceType

from typing import Tuple, Literal

from PiUI.core.logger import getLogger
log = getLogger("component")

class PiWindow():

	def __init__(
		self,
		*,
		name: str,
		position: Tuple[int, int],
		size: Tuple[int, int],
		widget: PiWidget | None = None,
		strut: Strut | None = None,    
		windowType: Literal["desktop", "dock"] = "dock",
		ground: Literal["fg", "bg"] = "fg",
		focusable: bool = False,
		transparent: bool = False
		):

		# TYPE CHECKS

		enforceType(widget, (PiWidget, type(None)), "widget")
		enforceType(strut, (Strut, type(None)), "strut")

		if windowType not in ("dock", "desktop"):
			raise ValueError(f"Invalid Window Type! (name={name}). Valid Types are: 'dock', 'desktop'")
		if ground not in ("fg", "bg"):
			raise ValueError(f"Invalid Window Ground! (name={name}). Valid Types are: 'fg', 'bg'")

		
		#BACKEND INIT

		self._backend: XBackEnd = XBackEnd(name, windowType, ground, strut, focusable, transparent) #type:ignore 
		#None Handled internally
		log.info(f"PiWindow with name '{name}' has X id: {self._backend.win_id}")
	

		#WINDOW

		if name:
			self._name: str = name
			self._backend.setObjectName(name)

		self._pos = position
		self._size = size
		self._setGeometry()
		self._setWidget(widget)

		
		
	def _setGeometry(self):
		self._backend.setGeometry(*self._pos, *self._size)
		self._backend.setFixedSize(*self._size)

		log.info(f"PiWindow '{self._name}' setup with dimensions: ({*self._pos, *self._size})")

	def _setWidget(self, widget):
		layout = QHBoxLayout()
		
		if widget:

			if widget.alignment:
				layout.addWidget(widget._backend, alignment= widget.alignment) #type:ignore #None Handled
			else:
				layout.addWidget(widget._backend)

			log.debug(f"PiWindow '{self._name}' has a root widget.")

		else:
			log.debug(f"PiWindow '{self._name}' does not have a root widget.")

		layout.setContentsMargins(0,0,0,0)
		self._backend.setLayout(layout)
		self._backend.setContentsMargins(0,0,0,0)

	def show(self):
		self._backend.move(*self._pos)
		self._backend.show()
		log.info(f"PiWindow '{self._name}' shown.")

	def hide(self):
		self._backend.hide()

	def toggle(self):
		if self._backend.isHidden():
			self.show()
		else:
			self.hide()

	def ignoreWM(self):
		self._backend.setWindowFlag(Qt.WindowType.BypassWindowManagerHint)
		log.info(f"PiWindow '{self._name}' now bypasses the window manager.")

	def name(self):
		return self._backend.objectName()
	


