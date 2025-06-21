

from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel
from PySide6.QtGui import QPixmap



class ImageWidget(QLabel):

    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.setScaledContents(True)
        self.pixmap: QPixmap

    def setImage(self, path: str):
        self.pixmap = QPixmap(path)
        self.setPixmap(self.pixmap)
        
