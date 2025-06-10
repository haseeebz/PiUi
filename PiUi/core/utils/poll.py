


import subprocess
from typing import Callable
from .timer import Timer


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

		