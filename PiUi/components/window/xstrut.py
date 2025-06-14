
from typing import Tuple
from Xlib import Xatom, display
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt


class Strut():
	
    def __init__(self, strut: Tuple[int, int, int, int], screen):
        
        self.strut_main = strut

        self.strut_partial = [
            *strut,
            0,0,
            0,0,
            0,0,
            0,0
        ]

        #automatically assigns strut_partial based on user arg. 
        for i in range(4):
            if self.strut_main[i] != 0:
                self.strut_partial[5+(i*2)] = screen.y if i > 2 else screen.x


