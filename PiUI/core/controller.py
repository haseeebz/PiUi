

from PiUI.components.window import PiWindow
from PySide6.QtCore import Signal, QObject

import socket
import os, sys, time, threading
from typing import Callable


from .logger import getLogger
log = getLogger("controller") 

#NOTE since Controller.loop() which runs in a seperate thread also needs to log, all logging in this class must be done with its lock. Everything else is safe to access.



SOCKET_PATH = "/tmp/piui.sock"


class SignalBridge(QObject): #this class's entire purpose is to not pollute Controller with useless shit
	cmdReceived = Signal(str)
	def __init__(self, func: Callable):
		super().__init__()
		self.cmdReceived.connect(func)


class Controller():
	
	cmdReceived = Signal(str)

	def __init__(self) -> None:
		super().__init__()

		self.server: socket.socket = self.setupServer()
		self.windows: dict[str, PiWindow] = {}
		self.handlers: dict[str, Callable[..., str | None]] = {}
		
		self.signal = SignalBridge(self.execCommand)

		self.lock = threading.Lock()
	

	def setupServer(self):

		if os.path.exists(SOCKET_PATH):
			log.critical("Another Instance of PiUI has already been created. Overwriting the pervious instance's socket.")
			os.remove(SOCKET_PATH)

		self.server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
		self.server.bind(SOCKET_PATH)
		self.server.listen(1)

		log.info("Controller server has been initiated.")
		return self.server


	def run(self):
		self.defineCommand("help", self.helpCommand)
		self.t = threading.Thread(target = self._loop)
		self.t.start()


	def _loop(self):

		with self.lock:
			log.debug("Controller server is now running in a seperate thread.")

		try:
			
			while True:
	
				time.sleep(0.1)
				conn, _ = self.server.accept()
				data = conn.recv(1024)

				if not data:
					conn.close()

				msg = data.decode()

				if msg == "help":
					output = self.helpCommand()
					conn.sendall(output.encode())
				elif msg == "quit":
					conn.close()
					self.signal.cmdReceived.emit(msg)
					break
				else:
					self.signal.cmdReceived.emit(msg)

				conn.close()

		except Exception as e:
			with self.lock:
				log.critical(f"Controller Server error encountered: {str(e)}")
		finally:
			self.server.close()       


	def execCommand(self, msg: str) -> str | None:

		log.info(f"Controller server received command : {msg}")

		parts = msg.split()
		
		cmd = parts[0]
		arguments = parts[1:]

		
		if cmd not in self.handlers.keys():
			return "Unknown command: Check for typos."
			
		try:
			output = self.handlers[cmd](*arguments)

			if isinstance(output, str): output = output.replace("\n", " ") 

		except Exception as e:
			with self.lock:
				log.error(str(e))
		
		if output: #only log if th function returned a string. To prevent useless garbage in the log
			with self.lock:
				log.debug(f"Controller on receiving command '{cmd}', called the binded function '{self.handlers[cmd]}' with arguments: {arguments}. The function returned output (newlines removed): {output}")


	def defineCommand(self, cmd: str, func: Callable):
		self.handlers[cmd] = func


	def registerWindow(self, *args: PiWindow):

		for arg in args:
			if isinstance(arg, PiWindow):
				self.windows.update({arg.name(): arg})
			else:
				log.warning("An argument was passed to Pi.controller.registerWindows() that was not a PiWindow or any of its subclasses. Ignored.")

		self.defineCommand("show", self.showWindow)
		self.defineCommand("hide", self.hideWindow)


	def showWindow(self, name: str):
		
		if name not in self.windows.keys():
			with self.lock:
				log.warning(f"Could not show window '{name}'. Either it does not exist or wasn't registered by the controller.'")
		
		self.windows[name].show()
		with self.lock:
			log.info(f"Successfully shown window '{name}'")
	

	def hideWindow(self, name: str):

		if name not in self.windows.keys():
			with self.lock:
				log.warning(f"Could not hide window '{name}'. Either it does not exist or wasn't registered by the controller.'")
		
		self.windows[name].hide()
		with self.lock:
			log.info(f"Successfully closed window '{name}'")


	def helpCommand(self) -> str:
		msg = help_msg + "\n".join(self.handlers.keys()) + "\n"
		return msg
	
	
		
help_msg = """
<PiUI CLI interface>

Defined Commands:

"""