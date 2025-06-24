# Server
The object which handles the CLI. This is really useful because you can make your own bindings. By default it binds to "~/tmp/piui.sock" but in Pi.init(), you can change the socket path.

> If a socket path is already taken by a process and you start another PiUI process which binds to the same socket path, then the socket of the previous one will be overwritten. So make sure you keep a note of the socket paths.

## Methods

### defineCommand
This is the only method you should care about. It allows you to define a command that the server can accept. 
+ cmd : The string which is the command you will use in the cli.
+ func : The function which gets called on receiving the cmd. All strings after the cmd will be sent as string arguments to this function. You have to type cast them manually
+ info : Useful for personal documentation.

### internalCall
Used to give a command to the server internally. Not really recommended for usage.
+ msg : The command you want to execute.

## Example
Make a command and bind it to a function as:
```python
def change_brightness(value:str):
	value = int(value)
	...

Pi.server.defineCommand(
	"change_brightness", 
	change_brightness, 
	"Change the brightness. ARGS: value:int"
)
```
And then using the CLI:
```bash
pi-ctl change_brightness 90
```