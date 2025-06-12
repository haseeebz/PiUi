
from PySide6.QtWidgets import QApplication
from typing import Tuple

class Screen():

	def __init__(self, app: QApplication):
		self.pair: Tuple[int, int] = app.primaryScreen().size().toTuple()
		self.x: int = self.pair[0]
		self.y: int	= self.pair[1]