

from typing import Callable
from threading import Lock


from PiUI.core.logger import getLogger
log = getLogger("core")

class Binder():
	
	def __init__(self):
		self.bindings: dict[str, Binding] = {}

	def Bind(self, key: str):
		binding = Binding(key)
		self.bindings[key] = binding
		log.info(f"Binding created: {key}")
		return binding
	
	def update(self, key: str, value):
		self.bindings[key].setter(value) #type: ignore / will be defined

	def combine(self, other: "Binder"):
		for key, value in other.bindings.items():
			self.bindings[key] = value
		return self


class Binding():

	def __init__(self, key):
		self.setter: Callable | None = None
		self.key: str = key
		self.type = None
	
	def bind(self, setter: Callable):
		self.setter = setter
