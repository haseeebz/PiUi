
import struct, threading
from typing import Callable
from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Qt, Signal, QObject
from Xlib import display, Xatom, X, XK
from Xlib.protocol import event
from PySide6.QtCore import QTimer
from .xstrut import Strut
from PiUI.core.logger import getLogger

log = getLogger("xbackend")

class XBackEnd(QFrame):

	ATOMS = {}
	display = display.Display()
	root = display.screen().root

	def __init__(self, name: str, win_type: str, ground: str, strut: Strut, focusable: bool, transparent: bool):
		super().__init__()

		if transparent:
			self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
		
		#this needs to be done before the x11 tampering otherwise...it doesnt work for some reason.
		

		self.win_id = self.winId()
		self.xwin = self.display.create_resource_object("window", self.win_id)
		self.strut = strut
		self.xwin.change_attributes(event_mask = X.KeyPressMask | X.KeyReleaseMask | X.PointerMotionMask | X.StructureNotifyMask | X.ClientMessage)
		self.inputhandler = InputHandler(self.display)
		log.debug(f"X Window initialized with id: {self.win_id}")

		if not self.ATOMS:
			self.ATOMS["desktop"] = self.display.intern_atom("_NET_WM_DESKTOP")
			self.ATOMS["win_type"]= self.display.intern_atom("_NET_WM_WINDOW_TYPE")
			self.ATOMS["win_state"] = self.display.intern_atom("_NET_WM_STATE")
			self.ATOMS["motif_hints"] = self.display.intern_atom("_MOTIF_WM_HINTS")
			self.ATOMS["strut"] = self.display.intern_atom("_NET_WM_STRUT")
			self.ATOMS["strut_partial"] = self.display.intern_atom("_NET_WM_STRUT_PARTIAL")
			self.ATOMS["cardinal"] = self.display.intern_atom("CARDINAL")
			self.ATOMS["input"] = self.display.intern_atom("_NET_WM_INPUT")
			self.ATOMS["class"] = self.display.intern_atom("_NET_WM_CLASS")
	


		self._setWinType(win_type)
		self._setWinStates(ground)

		self._disableDeco()

		self._setFocus(focusable)

		self._setNames(name, win_type)

		self._should_steal_input = False

		self.display.sync()


	def initAtom(self, name: str):
		return self.display.intern_atom(name) #type: ignore #Will be initiatalized
	
	def _setNames(self, name: str, win_type: str):
		self.xwin.set_wm_class(win_type, "PiUI")
		self.xwin.set_wm_name(name)

	def _setWinType(self, win_type: str):
		
		win_types = {
			"dock" : "_NET_WM_WINDOW_TYPE_DOCK",
			"desktop" : "_NET_WM_WINDOW_TYPE_DESKTOP"
		}

		type_atom = self.initAtom(win_types[win_type])
		self.xwin.change_property(self.ATOMS["win_type"], Xatom.ATOM, 32, [type_atom])

		log.debug(f"Set X Win ({self.win_id}) type to{win_types[win_type]}")

	
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

		log.debug(f"States applied to X Win ({self.win_id}): {win_grounds[ground]} , _NET_WM_STATE_STICKY")

	
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
		
		log.debug(f"Disabled Decorations for X Win ({self.win_id})")


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
		
		log.debug(f"Applied Strut {self.strut.strut_main} owned by X Win ({self.win_id})")
		self.display.flush() #type: ignore #will be intialized

	def _setFocus(self, t: bool):

		if t:
			self.xwin.change_property(self.ATOMS["input"], self.ATOMS["cardinal"], 32, [1])
			self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
			log.debug(f"Applied focus for X Win ({self.win_id})")

		else:
			self.xwin.change_property(self.ATOMS["input"], self.ATOMS["cardinal"], 32, [0])
			self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
			log.debug(f"Applied focus for X Win ({self.win_id})")

	def _stealInput(self):
		keyctrl = self.xwin.grab_keyboard(
			True,
			X.GrabModeAsync,
			X.GrabModeAsync,
			X.CurrentTime
		)
		 
		if keyctrl != X.GrabSuccess:
			log.critical(f"Could not grab keyboard for xwin {self.win_id}.")

	def _unstealInput(self):
		self.display.ungrab_keyboard(X.CurrentTime)

	def _afterShow(self):
		self._setStrut()
		if self._should_steal_input:
			self.inputhandler.start()
			self._stealInput()

	def _afterHide(self):
		self.xwin.delete_property(self.ATOMS["strut"])
		self.xwin.delete_property(self.ATOMS["strut_partial"])

		if self._should_steal_input:
			self._unstealInput()
			ev = event.ClientMessage(
				window = self.root,
				client_type = 0,
				data=(32, [0, 0, 0, 0, 0])
			)
			self.display.send_event(self.win_id, ev, X.StructureNotifyMask)
			
		self.display.flush() 

	def showEvent(self, event):
		super().showEvent(event)
		self.timer = QTimer(interval=100, singleShot=True)
		self.timer.timeout.connect(self._afterShow)
		self.timer.start()

	def hideEvent(self, event):
		super().hideEvent(event)
		self._afterHide()
		
	
	def closeEvent(self, event):
		super().closeEvent(event)
		self._afterHide()
		


class InputHandler(QObject):

	keyReceived = Signal(str)

	def __init__(self, display: display.Display):
		super().__init__()
		self.display = display
		self.func = None
	
	def connectPasswordBox(self, func):
		self.func = func
		self.keyReceived.connect(self.func)

	def start(self):
		self.t = threading.Thread(target = self.loop)
		self.t.start()
		
	def stop(self):
		self.t.join()

	def loop(self):
		while True:
			event = self.display.next_event()
			if event.type == X.ClientMessage:
				break
			if event.type == X.KeyPress:
				shift = event.state & X.ShiftMask
				keycode = event.detail
				keysym = self.display.keycode_to_keysym(keycode, 1 if shift else 0)
				char = XK.keysym_to_string(keysym)
				self.keyReceived.emit(char)

