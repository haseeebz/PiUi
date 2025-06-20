
import os
import configparser
import shlex
import dataclasses

PATHS = [
	"/usr/share/applications",
    os.path.expanduser("~/.local/share/applications")
]
TERMINAL = "gnome-terminal"

@dataclasses.dataclass
class Application():
	name: str
	exe: str
	icon: str
	categories: list
	terminal: bool
		
class Menu():

	def __init__(self) -> None:
		self.applications: dict[str, Application] = {}
		self.configParser = configparser.ConfigParser(interpolation= None)


	def parse(self):
		for path in PATHS:
			files = os.listdir(path)
			for file in files:
				app = self.parse_desktop_file(os.path.join(path, file))
				if app: self.applications[app.name] = app
				print(app)


	def parse_desktop_file(self, file: str):
		self.configParser.read(file)

		if "Desktop Entry" not in self.configParser:
			return None
		
		entry = self.configParser["Desktop Entry"]

		if not entry.get("Exec"):
			return None

		name = entry.get("Name", "")
		exe = entry.get("Exec", "")
		icon = entry.get("Icon", "")
		categories = entry.get("Categories")
		terminal = entry.get("Terminal")
		print(type(categories))
		if terminal == "true":
			exe = f"{TERMINAL} -- {exe}" 

		app = Application(name, exe, icon, categories, terminal) #type: ignore
		return app

	def make_boxes(self):
		pass
		


menu = Menu()
menu.parse()