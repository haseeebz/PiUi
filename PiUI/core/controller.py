
from PiUI.components.window import PiWindow
import importlib
from types import ModuleType

from .logger import getLogger
log = getLogger("controller")

class Controller():

	def __init__(self) -> None:
		self.windows: dict[str, PiWindow] = {}
		self.modules: dict[str, ModuleType]

	def load(self, module: str):
		mod = importlib.import_module(module)
		try:
			win = mod.main()
		except ModuleNotFoundError:
			pass
		except AttributeError:
			pass

		if not isinstance(win, PiWindow):
			raise ValueError(f"main() function defined by module {module} did not return a PiWindow object or any of its subclass!")

		self.modules[module] = mod
		self.windows[module] = win
	
	def _reload(self, module: str):
		self.windows[module].close()
		mod = importlib.reload(self.modules[module])

		try:
			win = mod.main()
		except ModuleNotFoundError:
			pass
		except AttributeError:
			pass

		if not isinstance(win, PiWindow):
			raise ValueError(f"main() function defined by module {module} did not return a PiWindow object or any of its subclass!")

		self.modules[module] = mod
		self.windows[module] = win

	def getWindow(self, name: str) -> PiWindow | None:
		if name in self.windows.keys():
			return self.windows[name]
		else:
			return None
		
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

