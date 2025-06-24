

from PySide6.QtCore import Signal, QObject
import socket
import os, time, threading, json, shlex
from typing import Callable

from .logger import getLogger
log = getLogger("server") 




class SignalBridge(QObject): #this class's entire purpose is to not pollute PiServer with useless shit
	cmdReceived = Signal(dict)
	def __init__(self, func: Callable):
		super().__init__()
		self.cmdReceived.connect(func)


class PiServer():
	
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
				fmsg = json.loads(msg)

				if fmsg["cmd"] == "help":
					output = self.helpCommand()
					conn.sendall(output.encode())
				elif fmsg["cmd"] == "quit":
					conn.close()
					self.signal.cmdReceived.emit(fmsg)
					break
				else:
					self.signal.cmdReceived.emit(fmsg)

				conn.close()

		except Exception as e:
			with self.lock:
				log.critical(f"Controller socket error encountered: {str(e)}")
		finally:
			self.socket.close()       

	def execCommand(self, fmsg: dict) -> str | None:

		cmd = fmsg["cmd"]

		arguments = fmsg["args"] if "args" in fmsg.keys() else []
		
		if cmd not in self.handlers.keys():
			return "Unknown command: Check for typos."
			
		try:
			output = self.handlers[cmd][0](*arguments)
			if isinstance(output, str): output = output.replace("\n", " ") 

		except Exception as e:
			with self.lock:
				log.critical((f"Server on receiving command '{cmd[0]}', called the binded function '{self.handlers[cmd]}' with arguments: {arguments}. The function failed: {str(e)}"))
				return str(e)
		
		with self.lock:
			log.debug(f"Controller on receiving command '{cmd[0]}', called the binded function '{self.handlers[cmd]}' with arguments: {arguments}. The function returned output (newlines removed): {output}")

		if output:
			return output

	def defineCommand(self, cmd: str, func: Callable, info: str):
		self.handlers[cmd] = (func, info)

	def internalCall(self, s: str):
		args = shlex.split(s)

		OPTIONS = [
				"--socket"
			]
		
		msg = {}
		t = len(args)
		i = 0

		while True:
			if i >= t:
				if "cmd" not in msg.keys():
					log.warning("No Command Specified!")
					return
				break
			
			if args[i] in OPTIONS:
				try:
					msg[args[i].lstrip("--")] = args[i+1]
				except IndexError:
					log.warning(f"No argument passed for {args[i]}")
					return
				i += 2
			else:
				msg["cmd"] = args[i]
				msg["args"] = args[i+1:]
				break
		
		fmsg = json.loads(msg)
		self.execCommand(fmsg)

	def helpCommand(self) -> str:
		commands = [f"{item[0]:<20} : {item[1][1]}" for item in self.handlers.items()]
		msg = help_msg + "\n".join(commands) + "\n"
		return msg
	
			
help_msg = """
<PiUI CLI interface>

[OPTIONS] [COMMAND] [ARGS...]

Options:

--socket path/to/socket.sock

Defined Commands:

"""