

from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel
from PySide6.QtGui import QPixmap, QBitmap, QPainter
from PySide6.QtCore import Qt


class ImageWidget(QLabel):

	def __init__(self):
		super().__init__()
		self.setContentsMargins(0,0,0,0)
		self._preserve_aspect_ratio = False
		self._rounding = 0
	
	def preserveRatio(self):
		self._preserve_aspect_ratio = True

	def rounding(self, num: int):
		self._rounding = num
		
	def setImage(self, path: str):
		pix = QPixmap(path)

		if self._preserve_aspect_ratio:
			scaled = pix.scaled(self.size(), aspectMode = Qt.AspectRatioMode.KeepAspectRatio, mode = Qt.TransformationMode.SmoothTransformation)
		else:
			scaled = pix.scaled(self.size(), mode = Qt.TransformationMode.SmoothTransformation)

		if self._rounding <= 0:
			self.setPixmap(scaled)
			return
		
		self.map = QBitmap(self.size())
		self.map.fill(Qt.GlobalColor.color0)

		self._painter = QPainter(self.map)
		self._painter.setBrush(Qt.GlobalColor.color1)
		self._painter.drawRoundedRect(
			0, 0,
			self.width(), self.height(),
			self._rounding, self._rounding
		)
		self._painter.end()

		scaled.setMask(self.map)
		self.setPixmap(scaled)


		
