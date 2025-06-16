
from typing import Tuple
from Xlib import Xatom, display
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt


class Strut():
	
    def __init__(
        self,
        screen,
        *,
        top: int = 0,
        bottom : int = 0,
        right:  int = 0 ,
        left:  int = 0 
        ):
        
        self.strut_main = [left, right, top, bottom]

        self.strut_partial = [
            *self.strut_main,
            0,0,
            0,0,
            0,0,
            0,0
        ]

        #automatically assigns strut_partial based on user arg. 
        for i in range(4):
            if self.strut_main[i] != 0:
                self.strut_partial[5+(i*2)] = screen.y if i > 2 else screen.x


