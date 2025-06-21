
import os
#from PiUI.core.logger import getLogger
#log = getLogger("core")

class Resource():

	def __init__(self) -> None:
		self.directories: list[str] = []
		self.files: dict[""]

	def registerDirs(self, *args):
		for arg in args:
			if not os.path.isdir(arg):
				continue
			self.directories.append(arg)
			files = os.listdir(arg)
			for file in files:
				absFile = os.path.join(arg, file)
				if os.path.isfile(absFile):

	def __getitem__(self, key: str):
		pass

