

from PySide6.QtCore import Signal, QObject
import socket
import os, time, threading
from typing import Callable

from .logger import getLogger
log = getLogger("socket") 




class SignalBridge(QObject): #this class's entire purpose is to not pollute PiServer with useless shit
	cmdReceived = Signal(str)
	def __init__(self, func: Callable):
		super().__init__()
		self.cmdReceived.connect(func)


class PiServer():
	
	cmdReceived = Signal(str)

	def __init__(self, socket_path: str) -> None:
		super().__init__()
		self.SOCKET_PATH = socket_path
		self.socket: socket.socket
		self.setupsocket()

		self.handlers: dict[str, tuple[Callable[..., str | None], str]] = {}
		
		self.signal = SignalBridge(self.execCommand)
		self.lock = threading.Lock()
	
	def setupsocket(self):

		if os.path.exists(self.SOCKET_PATH):
			log.critical("Another Instance of PiUI has already been created. Overwriting the pervious instance's socket.")
			os.remove(self.SOCKET_PATH)

		self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
		self.socket.bind(self.SOCKET_PATH)
		self.socket.listen(1)

		log.info("PiServer socket has been initiated.")
		return self.socket

	def run(self):
		self.t = threading.Thread(target = self._loop)
		self.t.start()


	def _loop(self):

		with self.lock:
			log.debug("PiServer loop is now running in a seperate thread.")

		try:
			
			while True:
				time.sleep(0.1)
				conn, _ = self.socket.accept()
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
				log.critical(f"Controller socket error encountered: {str(e)}")
		finally:
			self.socket.close()       

	def execCommand(self, msg: str) -> str | None:

		parts = msg.split()
		
		cmd = parts[0]
		arguments = parts[1:]

		
		if cmd not in self.handlers.keys():
			return "Unknown command: Check for typos."
			
		try:
			output = self.handlers[cmd][0](*arguments)
			if isinstance(output, str): output = output.replace("\n", " ") 

		except Exception as e:
			with self.lock:
				log.error(str(e))
				return
		
		with self.lock:
			log.debug(f"Controller on receiving command '{cmd}', called the binded function '{self.handlers[cmd]}' with arguments: {arguments}. The function returned output (newlines removed): {output}")


	def defineCommand(self, cmd: str, func: Callable, info: str):
		self.handlers[cmd] = (func, info)


	def helpCommand(self) -> str:

		help_msg = """
		<PiUI CLI interface>

		[COMMAND] [ARGS...]

		Defined Commands:

		"""
		commands = [f"{func} : {info}" for func, info in self.handlers.keys()]
		msg = help_msg + "\n".join(commands) + "\n"
		return msg
	
	
		
