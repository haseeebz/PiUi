
import struct
from PySide6.QtWidgets import QFrame
from Xlib import display, Xatom, X
from PySide6.QtCore import QTimer
from .xstrut import Strut


class XBackEnd(QFrame):

    ATOMS = {}
    display = None
    root = None

    def __init__(self, win_type: str, ground: str, strut: Strut):
        super().__init__()
        self.display = display.Display()
        self.root = self.display.screen().root

        self.win_id = self.winId()
        self.xwin = self.display.create_resource_object("window", self.win_id)
        self.strut = strut

        if not self.ATOMS:
            self.ATOMS["desktop"] = self.display.intern_atom("_NET_WM_DESKTOP")
            self.ATOMS["win_type"]= self.display.intern_atom("_NET_WM_WINDOW_TYPE")
            self.ATOMS["win_state"] = self.display.intern_atom("_NET_WM_STATE")
            self.ATOMS["motif_hints"] = self.display.intern_atom("_MOTIF_WM_HINTS")
            self.ATOMS["strut"] = self.display.intern_atom("_NET_WM_STRUT")
            self.ATOMS["strut_partial"] = self.display.intern_atom("_NET_WM_STRUT_PARTIAL")
            self.ATOMS["cardinal"] = self.display.intern_atom("CARDINAL")
    
        
        self._setWinType(win_type)
        self._setWinStates(ground)
        self._disableDeco()

        self.display.sync()


    def initAtom(self, name: str):
        return self.display.intern_atom(name)
    

    def _setWinType(self, win_type: str):
        
        win_types = {
            "dock" : "_NET_WM_WINDOW_TYPE_DOCK",
            "desktop" : "_NET_WM_WINDOW_TYPE_DESKTOP"
        }

        type_atom = self.initAtom(win_types[win_type])
        self.xwin.change_property(self.ATOMS["win_type"], Xatom.ATOM, 32, [type_atom])

    
    def _setWinStates(self, ground: str):

        win_grounds = {
            "fg" : "_NET_WM_STATE_ABOVE",
            "bg" : "_NET_WM_STATE_BELOW",
            # : "_NET_WM_STATE_FULLSCREEN"
        }

        ground_atom = self.initAtom(win_grounds[ground])
        sticky_atom = self.initAtom("_NET_WM_STATE_STICKY")

        self.xwin.change_property(self.ATOMS["win_state"],  Xatom.ATOM, 32, [ground_atom, sticky_atom], X.PropModeReplace)

        self.xwin.change_property(self.ATOMS["desktop"], self.ATOMS["cardinal"], 32, [0xFFFFFFFF])

    
    def _disableDeco(self):

        hints = struct.pack("LLLLL",
            2,  # Flags: "we are setting decorations"
            0,  # Decorations: "remove all"
            0,  # Input mode (irrelevant here)
            0,  # Status (also irrelevant)
            0   # Extra (unused)
        )

        self.xwin.change_property(
            self.ATOMS["motif_hints"], 
            self.ATOMS["motif_hints"], 
            32, 
            hints, 
            X.PropModeReplace)


    def _setStrut(self):

        if not self.strut:
            return

        self.xwin.change_property(
            self.ATOMS["strut"],
            self.ATOMS["cardinal"], 
            32, 
            self.strut.strut_main
            )
        
        self.xwin.change_property(
            self.ATOMS["strut_partial"],
            self.ATOMS["cardinal"],
            32, 
            self.strut.strut_partial
            )
        
        self.display.flush()

    
    def showEvent(self, event):
        super().showEvent(event)
        self.timer = QTimer(interval=2, singleShot=True)
        self.timer.timeout.connect(self._setStrut)
        self.timer.start()

    def hideEvent(self, event):
        super().hideEvent(event)
        self.xwin.delete_property(self.ATOMS["strut"])
        self.xwin.delete_property(self.ATOMS["strut_partial"])
        self.display.flush()