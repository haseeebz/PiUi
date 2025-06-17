
from PySide6.QtWidgets import QApplication
from typing import Tuple
from PiUI.app.core.logger import getLogger



class Screen():

	def __init__(self, app: QApplication):
		self.pair: Tuple[int, int] = app.primaryScreen().size().toTuple() #type: ignore # self-explanatory
		self.x: int = self.pair[0]
		self.y: int	= self.pair[1]
		log = getLogger("utils")
		log.info(f"Screen object intialized with the dimensions: {self.x}x{self.y}.")