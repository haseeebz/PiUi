

from PySide6.QtWidgets import QApplication

from PiUI.components.window import PiWindow

from .controller import Controller
from .server import PiServer
from .logger import getLogger, setupLogger, logging

from .tools import (
	Alignment,
	Binder,
	Poller,
	Screen,
	Shell,
	Timer,
	Debounce,
	System
)

from typing import Literal, Any
import os

class Singleton():

	def __init__(self) -> None:
		
		self._app = QApplication()

		self._intern_log: logging.Logger = None #type:ignore
		self.log: logging.Logger = None #type:ignore

		self.controller = Controller()
		self.server: PiServer = None #type:ignore

		self.binder = Binder()
		self.poller = Poller()
		self.screen = Screen(self._app)
		self.system = System()

		self.Shell = Shell
		self.Timer = Timer
		self.Debounce = Debounce
		self.Alignment = Alignment
		
		self.variables: dict[str, Any] = {}

		self._stylesheets: list[str] = []
		
	def init(
		self,
		*,
		logfile: str = "~/.cache/PiUI/main.log",
		loglevel: Literal["info", "debug", "warning", "critical"] = "info",
		socket_path: str = "/tmp/piui.sock",
		stylesheets: list[str] = []
		):
		
		setupLogger(logfile, loglevel)

		self._intern_log = getLogger("core")
		self.log = getLogger("user")

		self.server = PiServer(socket_path)

		if len(stylesheets) > 0:
			self.applyStylesheet(*stylesheets)

		# important bindings

		self.server.defineCommand(
			"show", 
			self.controller.showWindow,
			"Shows the window. ARGS: module/window name"
		)

		self.server.defineCommand(
			"hide", 
			self.controller.hideWindow,
			"Hides the window. ARGS: module/window name"
		)

		self.server.defineCommand(
			"quit",
			self.quitApp,
			"Ends the PiUI server. ARGS: None"
		)

		self.server.defineCommand(
			"reload_style",
			lambda: self.applyStylesheet(*self._stylesheets),
			"Reload the Stylesheet/s. ARGS: None"
		)
		
	def run(self):
		self.server.run()
		self._app.exec()

	def applyStylesheet(self, *stylesheets: str):
		style = ""
		for stylesheet in stylesheets:
			try:
				with open(stylesheet) as file: 
					style += file.read()
			except FileNotFoundError:
				self._intern_log.warning(f"StyleSheet Path '{stylesheet}' could not be resolved!")

		self._stylesheets = stylesheets #type:ignore / will be caught above
		self._app.setStyleSheet(style)

	def quitApp(self):
		self._intern_log.info("Quit command was sent to the server. Shutting down app.")
		os.remove(self.server.SOCKET_PATH)
		self._app.exit(0)


Pi = Singleton()