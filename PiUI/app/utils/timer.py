

from PySide6.QtCore import QTimer
from typing import Callable


class Timer():

	def __init__(self, interval: int, func: Callable, singleshot: bool = False):
		self.qt = QTimer(interval= interval*1000, singleShot = singleshot)
		self.qt.timeout.connect(func)
		
	def start(self):
		self.qt.start()

	def stop(self):
		self.qt.stop()

	def kill(self):
		self.qt.killTimer()
