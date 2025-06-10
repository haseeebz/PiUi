


import subprocess
from PySide6.QtCore import QTimer, Qt
from typing import Callable, List

from shiboken6 import Shiboken
from enum import Enum


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


class Binder():
	
	def __init__(self):
		self.bindings: dict[str, Binding] = {}

	def bind(self, key: str):
		binding = Binding()
		self.bindings[key] = binding
		return binding
	
	def update(self, key: str, value):
		self.bindings[key].setter(value)


class Binding():
	def __init__(self):
		self.setter: Callable = None
	
	def bind(self, setter: Callable):
		self.setter = setter


class Poller():

	def __init__(self):
		self.polls = []
	
	def poll(self, interval: int, *, func: Callable = None, shell: str = None, typeCastForShell = None):
		poll = Poll(interval, func= func, shell= shell, typeCastForShell= typeCastForShell)
		self.polls.append(poll)
		return poll


class Poll():

	def __init__(self, interval: int, *, func: Callable = None, shell: str = None, typeCastForShell = None):

		self.interval = interval
		self.func = func
		self.shell = shell
		self.typeCast = typeCastForShell

		self.run: Callable = None
		if func:
			self.run = self.func_run
		elif shell:
			self.run = self.shell_run

		self.setter: Callable = None
		self.timer = Timer(self.interval, self.run)

	def func_run(self):
		self.setter(self.func())

	def shell_run(self):
		output = subprocess.run(self.shell.split(" "), capture_output= True).stdout
		if self.typeCast:
			self.setter(self.typeCast(output))
		else:
			self.setter(output)
	
	def bind(self, setter: Callable):
		self.setter = setter
		self.run()
		self.timer.start()

		
class Alignment(Shiboken.Object):

	class H(Enum):
		left = Qt.AlignmentFlag.AlignLeft
		right = Qt.AlignmentFlag.AlignRight
		center = Qt.AlignmentFlag.AlignHCenter

	class V(Enum):
		top = Qt.AlignmentFlag.AlignTop
		bottom = Qt.AlignmentFlag.AlignBottom
		center = Qt.AlignmentFlag.AlignVCenter