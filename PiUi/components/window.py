
from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QApplication,
)
from PySide6.QtCore import Qt
from typing import Tuple, Literal

from Xlib import display, Xatom


class PiWindow():

    def __init__(
        self,
        *,
        name: str | None,
        position: Tuple[int, int],
        size: Tuple[int, int],
        rootWidget,
        strut: "Strut" = None
        ):

        self.qt = QMainWindow()

        self.qt.setGeometry(*position, *size)
        self.qt.setFixedSize(*size)
        
        self.qt.setWindowFlags(
            Qt.WindowType.BypassWindowManagerHint |
            Qt.WindowType.Tool |
            Qt.WindowType.FramelessWindowHint
        )

        if name:
            self.qt.setObjectName(name)

        self.qt.setCentralWidget(rootWidget.qt)
        self.qt.setContentsMargins(0,0,0,0)
        
        if strut:
            self.strut = strut
            strut.setup()

        self.show(True)

    def show(self, t: bool):
        if t:
            self.qt.show()
        else:
            self.qt.hide()
        




class Strut():
	
    def __init__(self, strut: Tuple[int, int, int, int], screen: Tuple[int, int]):
        
        self.screenHeight, self.screenWidth = screen

        self.strut = strut

        self.strut_partial = [
            *strut,
            0,0,
            0,0,
            0,0,
            0,0
        ]

        #automatically assigns strut_partial based on user arg. bruh.
        for i in range(4):
            if self.strut[i] != 0:
                self.strut_partial[5+(i*2)] = self.screenHeight if i > 2 else self.screenWidth


        self.d = display.Display()
        self.root = self.d.screen().root

        self.gwin = None
        self.xwin = None

        self.NET_WM_STRUT = self.d.intern_atom("_NET_WM_STRUT")
        self.NET_WM_STRUT_PARTIAL = self.d.intern_atom("_NET_WM_STRUT_PARTIAL")
        self.CARDINAL = self.d.intern_atom("CARDINAL")
        self.NET_WM_DESKTOP = self.d.intern_atom("_NET_WM_DESKTOP")

        self.NET_WM_WINDOW_TYPE = self.d.intern_atom("_NET_WM_WINDOW_TYPE")
        self.NET_WM_WINDOW_TYPE_DOCK = self.d.intern_atom("_NET_WM_WINDOW_TYPE_DOCK")


    def initGhostWin(self):

        win = QMainWindow()

        win.setGeometry(
            0,
            0,
            1,
            1
        )

        win.setFixedSize(1,1) 
        win.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        win.setWindowOpacity(0)
        style = "QMainWindow { background : transparent }"
        win.setStyleSheet(style)
        win.show()
        return win  

    def setup(self):

        self.gwin = self.initGhostWin()
        self.xwin = self.d.create_resource_object("window", self.gwin.winId())

        self.xwin.change_property(self.NET_WM_STRUT, self.CARDINAL, 32, self.strut)
        self.xwin.change_property(self.NET_WM_STRUT_PARTIAL, self.CARDINAL, 32, self.strut_partial)

        self.xwin.change_property(self.NET_WM_WINDOW_TYPE, Xatom.ATOM, 32, [self.NET_WM_WINDOW_TYPE_DOCK])
        self.d.flush()

        self.gwin.activateWindow()

    def close(self):
        self.gwin.close()
        self.xwin.destroy()



