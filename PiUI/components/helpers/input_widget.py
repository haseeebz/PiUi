
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from typing import Callable


class InputWidget(QLineEdit):

	def __init__(self):
		super().__init__()
		self.onEnterPress: Callable = None
		self.onKeyPress: Callable = None

	def setEnterFunc(self, func: Callable):
		self.onEnterPress = func
		self.returnPressed.connect(lambda : self.onEnterPress(self.text()))

	def setChangeFunc(self, func: Callable):
		self.onKeyPress = func
		self.textEdited.connect(lambda : self.onKeyPress(self.text()))

	def setPasswordEcho(self):
		self.setEchoMode(QLineEdit.EchoMode.Password)
		self.setStyleSheet("QLineEdit { letter-spacing: 4px }")