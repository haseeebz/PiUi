
from PySide6.QtWidgets import (
	QApplication
)

from PiUI.app.utils import Binder, Poller, Timer
from .screen import Screen
import sys
from typing import Callable, Tuple


class AppCore():

	def __init__(self):

		self._app___ = QApplication(sys.argv)
		self.stylesheet: str | None = None

		self.screen = Screen(self._app___)

		self.binder = Binder()
		self.poller = Poller()
		self.Timer = Timer

	def run(self):
		sys.exit(self._app___.exec())

	def setStyleSheet(self, style_path: str):
		try:
			with open(style_path) as file:
				self.stylesheet = file.read()
			self._app___.setStyleSheet(self.stylesheet)
		except FileNotFoundError:
			print(f"Stylesheet file not found: {style_path}")
