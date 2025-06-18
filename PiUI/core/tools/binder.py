

from typing import Callable
from threading import Lock


from PiUI.core.logger import getLogger
log = getLogger("core")
from threading import Lock

class Binder:
    def __init__(self):
        self._lock = Lock()
        self.bindings: dict[str, Binding] = {}

    def Bind(self, key: str):
        with self._lock:
            binding = Binding(key)
            self.bindings[key] = binding
        log.info(f"Binding created: {key}")
        return binding

    def update(self, key: str, value):
        with self._lock:
            binding = self.bindings.get(key)
        if binding and binding.setter:
            binding.setter(value)

    def combine(self, other: "Binder"):
        with self._lock, other._lock:
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
