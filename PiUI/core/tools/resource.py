
import os

class Resource():

	def __init__(self, app) -> None:
		self.directories: list[str] = []
		self.stylesheets: list[str] = []
		self._app = app

	def get(self, asset: str) -> str:
		for directory in self.directories:
			files = os.listdir(directory)
			if asset in files:
				path = os.path.join(directory, asset)
				return path
		raise FileNotFoundError(f"Asset {asset} not found in any of the added resource folders.")				

	def has(self, asset: str) -> bool:
		for directory in self.directories:
			files = os.listdir(directory)
			if asset in files:
				return True
		return False
					
	def addResource(self, directory: str):
		self.directories.append(directory)
		for root, directories, files in os.walk(directory):
			for subdir in directories:
				self.addResource(os.path.join(directory, subdir))
				
	def find(self, *, extension: str = None, name: str = None):
		assets = []
		
		for directory in self.directories:
			files = os.listdir(directory)
			for file in files:
				root, ext = os.path.splitext(file)

				name_match = True if name is None else name == root
				ext_match = True if name is None else ext == extension

				if name_match and ext_match:
					assets.append(os.path.join(directory, file))

		return assets

	def applyStylesheet(self, *stylesheets: str):
		style = ""
		for stylesheet in stylesheets:
			with open(stylesheet) as file: 
				style += file.read()
				
		self.stylesheets = stylesheets #type:ignore / will be caught above
		self._app.setStyleSheet(style)
