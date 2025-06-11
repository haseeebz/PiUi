

from PySide6.QtWidgets import (
	QApplication
)

from .utils import Binder, Poller, Timer
import sys
from typing import Callable, Tuple


class AppCore():

	def __init__(self):

		self._app___ = QApplication(sys.argv)
		self.stylesheet: str = None

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


class Screen():

	def __init__(self, app: QApplication):
		self.pair: Tuple[int, int] = app.primaryScreen().size().toTuple()
		self.x: int = self.pair[0]
		self.y: int	= self.pair[1]