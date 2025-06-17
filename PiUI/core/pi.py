
from PySide6.QtWidgets import (
	QApplication
)

from ..utils.screen import Screen
from .controller import Controller
from .logger import setupLogger, logging, getLogger
from PiUI.components.window import PiWindow
import sys
from typing import Callable, Tuple

from PiUI.app.utils import 

class AppCore():

	def __init__(self, *, logfile: str):

		setupLogger(logfile, logging.INFO)

		self._log = getLogger("core")
		self._app = QApplication(sys.argv)
		self._controller = Controller()

		self.screen = Screen(self._app)
		self.windows: dict[str, PiWindow] = {}
		

	def run(self):
		sys.exit(self._app.exec())

	def setStyleSheet(self, style_path: str):
		try:
			with open(style_path) as file:
				self.stylesheet = file.read()
			self._app.setStyleSheet(self.stylesheet)
		except FileNotFoundError:
			self._log.warning(f"StyleSheet Path '{style_path}' could not be resolved!")

	def registerWindows(self, *args: PiWindow):
		for arg in args:
			if isinstance(arg, PiWindow):
				self.windows.update({arg.name(): arg})
			else:
				self._log.warning("An argument was passed to AppCore.registerWindows() that was not a PiWindow or any of its subclasses. Ignored.")

	def setupController(self):
		pass


class Runtime():

	def __init__(self) -> None:
		self.binder 