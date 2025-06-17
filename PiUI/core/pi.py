

from PySide6.QtWidgets import (
	QApplication
)
from typing import Literal
import threading

import logging, sys

from .logger import getLogger, setupLogger
from .controller import Controller
from PiUI.core.tools import Poller, Binder, Shell, Timer, Screen, Debounce

class PiSingleton():

	def __init__(self) -> None:
		self._app = QApplication(sys.argv)
		
		self._pilog: logging.Logger  = None #type: ignore
		self.log: logging.Logger  = None #type: ignore

		self.screen = Screen(self._app)
		self.binder = Binder()
		self.poller = Poller()
		self.controller = Controller()
		self.Timer = Timer
		self.Shell = Shell
		self.Debounce = Debounce

		self.lock = threading.Lock()
	
	def init(
		self,
		*,
		logfile: str = "~/.cache/PiUI/main.log", 
		loglevel: Literal["info", "debug", "warning", "critical"] = "info"
		):

		setupLogger(logfile, loglevel)

		self._pilog = getLogger("core")
		self.log = getLogger("user")

	def setStylesheet(self, style_path: str):
		try:
			with open(style_path) as file:
				self.stylesheet = file.read()
			self._app.setStyleSheet(self.stylesheet)
		except FileNotFoundError:
			self._pilog.warning(f"StyleSheet Path '{style_path}' could not be resolved!")

	def run(self):
		self.controller.run()
		self._app.exec()

Pi = PiSingleton()