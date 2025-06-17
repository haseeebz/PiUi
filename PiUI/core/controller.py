import socket
import os
import threading
from typing import Callable

SOCKET_PATH = "/tmp/piui.sock"

from .logger import getLogger
log = getLogger("core")

class Controller():

    def __init__(self) -> None:

        self.server: socket.socket = self.setupServer()

        self.bindings: dict[str, Callable[[], str]] = {}
        self.t = threading.Thread(target = self.run)
        self.lock = threading.Lock()
        self.t.start()

    def setupServer(self):
        if os.path.exists(SOCKET_PATH):
            log.debug(f"SOCKET PATH: {SOCKET_PATH} already exists. Overwriting.")
            os.remove(SOCKET_PATH)

        self.server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server.bind(SOCKET_PATH)
        self.server.listen(1)
        log.info("Controller server has been initiated.")
        return self.server

    def run(self):

        with self.lock:
            log.debug("Controller server is now running in a seperate thread.")

        try:
            while True:
                conn, _ = self.server.accept()
                
                data = conn.recv(1024)
                if data:
                    output = self.parseCommand(data)
                    conn.sendall(output.encode())
                conn.close()

        except Exception as e:
            with self.lock:
                log.critical(f"Controller Server error encountered: {str(e)}")
        finally:
            self.server.close()       

    def parseCommand(self, data) -> str:
        msg: str = data.decode()

        with self.lock:
            log.info(f"Controller server received command : {msg}")

        parts = msg.split()
        
        event = parts[0]
        arguments = parts[1:]

        with self.lock:
            if event not in self.bindings.keys():
                return "Unknown Event: Check for typos."
            
            try:
                output = self.bindings[event](*arguments)
                log.info(f"Controller on receiving event '{event}', called the binded function '{self.bindings[event]}' with arguments: {arguments} ")
            except Exception as e:
                return str(e)
            
            return output

        

        