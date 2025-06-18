

from PySide6.QtCore import QTimer
from typing import Callable

from PiUI.core.logger import getLogger
log = getLogger("core")

class Timer():

	def __init__(self, interval: int | float, func: Callable, singleshot: bool = False, checkCondition: Callable | None = None):
		self.qt = QTimer(interval= int(interval*1000), singleShot = singleshot)
		self.check = checkCondition
		self.func = func
		log.debug(f"Made timer which executes func {func} with interval {interval}s. Singleshot={singleshot}.  Check function is {checkCondition}")
		self.qt.timeout.connect(func)
	
	def execute(self):
		if self.check is not None:
			if self.check():
				self.func() #if check defined, only run func if check returns true
		else:
			self.func()
		
	def start(self):
		self.qt.start()

	def stop(self):
		self.qt.stop()

	#def kill(self):
	#	self.qt.killTimer()
