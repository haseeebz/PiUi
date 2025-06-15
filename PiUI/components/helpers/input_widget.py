


from PySide6.QtWidgets import  QLineEdit
from typing import Callable



class InputWidget(QLineEdit):

    def __init__(self):
        super().__init__()
        self.onEnterPress: Callable = None
        self.onKeyPress: Callable = None



    def setEnterFunc(self, func: Callable):
        if func:
            self.onEnterPress = func
            self.returnPressed.connect(lambda : self.onEnterPress(self.text()))
        else:
            self.returnPressed.disconnect()

    def setChangeFunc(self, func: Callable):
        if func:
            self.onKeyPress = func
            self.textEdited.connect(lambda : self.onKeyPress(self.text()))
        else:
            self.textEdited.disconnect()

        