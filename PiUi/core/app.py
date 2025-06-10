



import sys
from typing import Tuple


from PySide6.QtWidgets import (
	QApplication
)


class AppCore():

	def __init__(self):
		self.__app = QApplication(sys.argv)
		self.stylesheet: str = None
		self.screen = Screen(self.__app)

	def run(self):
		sys.exit(self.__app.exec())

	def applyStyleSheet(self, style_path: str):
		try:
			with open(style_path) as file:
				self.stylesheet = file.read()
			self.__app.setStyleSheet(self.stylesheet)
		except FileNotFoundError:
			print(f"Stylesheet file not found: {style_path}")


class Screen():

	def __init__(self, app: QApplication):
		self.pair: Tuple[int, int] = app.primaryScreen().size().toTuple()
		self.x: int = self.pair[0]
		self.y: int	= self.pair[1]