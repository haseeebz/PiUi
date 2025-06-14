

from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel
from PySide6.QtGui import QPixmap



class ImageWidget(QFrame):

    def __init__(self):
        super().__init__()
        self.layoutBox = QHBoxLayout()
        self.label = QLabel()
        self.label.setScaledContents(True)
        self.layoutBox.addWidget(self.label)
        self.setLayout(self.layoutBox)
        self.pixmap: QPixmap

    def setImage(self, path: str):
        self.pixmap = QPixmap(path)
        self.label.setPixmap(self.pixmap)
        
