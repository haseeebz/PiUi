
# Pi

Pi is a sshared object you can import from anywhere, it allows you to create UI without having to pass tools like binder, poller etc throughout your code. Instead you can just import it as:

```python
from PiUI.core import Pi
```

## Methods and Attributes

### init
This is setups stuff like logs, server and stylesheet info.
#### Arguments
logfile -> The text file where you want your logs. Default: "~/.cache/PiUI/main.log",
loglevel -> The level upto which you want to see your logs. Default = "info",
socket_path -> The socket to which the app must bind. Useful if you want to run different instances (though it is not recomended). Default: "/tmp/piui.sock",
stylesheets -> List of stylesheets you want to apply to the application. Default = []

### applyStylesheet
Obvious enough. Takes a bunch of stylesheet paths and applies it to the app.
# Arguments
*stylesheets -> path to stylesheets

### run
Runs the app, put it at the end

### quitApp
Ends the application. Its not recommended to call this since it just ends the GUI thread but does not end the server thread. Use the cli to exit the app gracefully as:
```bash
pi-ctl quit
```