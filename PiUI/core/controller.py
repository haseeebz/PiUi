
from PiUI.components.window import PiWindow

from .logger import getLogger
log = getLogger("controller")

class Controller():

	def __init__(self) -> None:
		self.windows: dict[str, PiWindow] = {}

	def addWindow(self, win: PiWindow):
		if isinstance(win, PiWindow):
			self.windows[win.name()] = win
		else:
			log.warning("An argument was passed to Pi.controller.addWindow that was not a PiWindow (or its subclass) instance. Ignored")

	def getWindow(self, name: str) -> PiWindow:
		if name in self.windows.keys():
			return self.windows[name]
		else:
			raise KeyError(f"{name} PiWindow not registered by controller. May not be added.")
		
	def showWindow(self, name: str):

		if name not in self.windows.keys():
			log.warning(f"Could not show window '{name}'. Either it does not exist or wasn't registered by the controller.'")
		
		self.windows[name].show()
		log.info(f"Window '{name}' Shown")
		
	def hideWindow(self, name: str):

		if name not in self.windows.keys():
			log.warning(f"Could not hide window '{name}'. Either it does not exist or wasn't registered by the controller.'")
		
		self.windows[name].hide()
		log.info(f"Window '{name}' Hidden")

