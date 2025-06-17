
import socket
import os


SOCKET_PATH = "/tmp/piui.sock"

client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client.connect(SOCKET_PATH)
client.sendall(b"hide bar")
res = client.recv(1024)
print(res.decode())
client.close()