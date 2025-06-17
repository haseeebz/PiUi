import socket
import os
import threading
from typing import Callable, Any

SOCKET_PATH = "/tmp/piui.sock"

from .logger import getLogger
log = getLogger("core")
from PiUI.components.window import PiWindow

class Controller():

    def __init__(self) -> None:

        self.server: socket.socket = self._setupServer()
        self.windows: dict[str, PiWindow] = {}
        self.handlers: dict[str, Callable[[Any], str]] = {}
        
        self.lock = threading.Lock()
        
    def _setupServer(self):
        if os.path.exists(SOCKET_PATH):
            log.debug(f"SOCKET PATH: {SOCKET_PATH} already exists. Overwriting.")
            os.remove(SOCKET_PATH)

        self.server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server.bind(SOCKET_PATH)
        self.server.listen(1)
        log.info("Controller server has been initiated.")
        return self.server

    def run(self):
        self.t = threading.Thread(target = self.loop)
        self.t.start()

    def loop(self):

        with self.lock:
            log.debug("Controller server is now running in a seperate thread.")

        try:
            while True:
                conn, _ = self.server.accept()
                
                data = conn.recv(1024)
                if data:
                    output = self._execCommand(data)
                    conn.sendall(output.encode())
                conn.close()

        except Exception as e:
            with self.lock:
                log.critical(f"Controller Server error encountered: {str(e)}")
        finally:
            self.server.close()       


    def _execCommand(self, data) -> str:
        msg: str = data.decode()

        with self.lock:
            log.info(f"Controller server received command : {msg}")

        parts = msg.split()
        
        cmd = parts[0]
        arguments = parts[1:]

        with self.lock:
            if cmd not in self.handlers.keys():
                return "Unknown command: Check for typos."
            
        try:
            output = self.handlers[cmd](*arguments)
            log.info(f"Controller on receiving command '{cmd}', called the binded function '{self.handlers[cmd]}' with arguments: {arguments} ")
        except Exception as e:
            return str(e)
        
        return output

    def defineCommand(self, cmd: str, func: Callable[[Any], str]):
        with self.lock:
            self.handlers[cmd] = func

    def internalCall(self, cmd: str):
        self._execCommand(cmd)
    
    def showWindow(self, name: str) -> str:
        with self.lock:
            if name not in self.windows.keys():
                return f"Could not show window '{name}'. Either it does not exist or wasn't registered by the controller.'"
            
            self.windows[name].show()
            return f"Successfully shown window '{name}'"
        
    def hideWindow(self, name: str) -> str:
        with self.lock:
            if name not in self.windows.keys():
                return f"Could not hide window '{name}'. Either it does not exist or wasn't registered by the controller.'"
            
            self.windows[name].hide()
            return f"Successfully closed window '{name}'"

    def registerWindows(self, *args: PiWindow):
        for arg in args:
            if isinstance(arg, PiWindow):
                self.windows.update({arg.name(): arg})
            else:
                log.warning("An argument was passed to Pi.controller.registerWindows() that was not a PiWindow or any of its subclasses. Ignored.")

        self.defineCommand("show", self.showWindow)
        self.defineCommand("hide", self.hideWindow)