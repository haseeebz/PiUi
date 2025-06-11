

from typing import Callable


class Binder():
	
	def __init__(self):
		self.bindings: dict[str, Binding] = {}

	def Bind(self, key: str):
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

