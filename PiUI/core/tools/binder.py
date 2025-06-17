

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

	def combine(self, other: "Binder"):
		for key, value in other.bindings.items():
			self.bindings[key] = value
		return self



class Binding():
	def __init__(self):
		self.setter: Callable = None
		self.type = None
	
	def bind(self, setter: Callable):
		self.setter = setter
