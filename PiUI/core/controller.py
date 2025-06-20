import socket
import os, sys, time
import threading
from typing import Callable, Any, Union

SOCKET_PATH = "/tmp/piui.sock"

from .logger import getLogger
from .tools import Timer
log = getLogger("core")
from PiUI.components.window import PiWindow

class Controller():

    def __init__(self) -> None:

        self.server: socket.socket = self._setupServer()
        self.windows: dict[str, PiWindow] = {}
        self.handlers: dict[str, Callable[..., str | None]] = {}
        
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
        self.defineCommand("help", self.helpCommand)
        self.t = threading.Thread(target = self.loop)
        self.t.start()


    def loop(self):

        with self.lock:
            log.debug("Controller server is now running in a seperate thread.")

        try:
            
            while True:
                time.sleep(0.1)
                conn, _ = self.server.accept()
                data = conn.recv(1024)

                if data:
                    output = self._execCommand(data)
                    if isinstance(output, str):
                        conn.sendall(output.encode())

                conn.close()

        except Exception as e:
            with self.lock:
                log.critical(f"Controller Server error encountered: {str(e)}")
        finally:
            self.server.close()       


    def _execCommand(self, data) -> str | None:

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

            if isinstance(output, str): output.replace("\n", " ") 

        except Exception as e:
            output =  str(e)
        

        with self.lock:
            log.debug(f"Controller on receiving command '{cmd}', called the binded function '{self.handlers[cmd]}' with arguments: {arguments}. The function returned output (newlines removed): {output}")

        return output


    def defineCommand(self, cmd: str, func: Callable[..., str]):
        with self.lock:
            self.handlers[cmd] = func


    def internalCall(self, cmd: str):
        self._execCommand(cmd)
    

    def registerWindows(self, *args: PiWindow):

        for arg in args:
            if isinstance(arg, PiWindow):
                self.windows.update({arg.name(): arg})
            else:
                log.warning("An argument was passed to Pi.controller.registerWindows() that was not a PiWindow or any of its subclasses. Ignored.")

        self.defineCommand("show", self.showWindow)
        self.defineCommand("hide", self.hideWindow)


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


    def helpCommand(self) -> str:
        msg = help_msg + "\n".join(self.handlers.keys())
        return msg
    
        
help_msg = """
<PiUI CLI interface>

Defined Commands:

"""