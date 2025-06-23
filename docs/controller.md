
# Controller
The main object for controlling windows by name. You can use it to access any window from anywhere as long as it was added to it.
It will support further utilities in the future.

## Methods

### addWindow
Adds a window to the controller.
+ win: The PiWindow to be added

### getWindow
Get a window by its "name" property.
+ name: Name of the window

### showWindow
Show a window by its name. Not really needed since you can call the above method and then .show() the window
+ name: Name of the window

### hideWindow
Hide a window by its name. Not really needed since you can call the above method and then .hide() the window
+ name: Name of the window