
# Windows

Don't need much explaining here. They are windows. Here are the current implemented types:

## PiWindow

The most basic window that you can initialize.

### Properties
+ name : Name of the window, used for referencing.
+ position : (x, y) tuple of the position of the top left corner of the window on the screen.
+ size : (w, h) tuple of size of the window.
+ widget : The root widget
+ strut : The strut or the amount of space reserved just for the window. Useful for bars.
+ windowType: Currently only supports "desktop" and "dock". The former is for desktop widgets while the latter might be preferred for anything that is infront of everything.
+ ground : Either "fg" or "bg".
+ focusable : Whether the window should be focusable (for textboxes)
+ transparent : Make the window fully transparent. If you want to add slight tranparency, then change the color/transparency of the root widget.

## PiBar

Subclass of PiWindow for slightly easier bar making.

### Properties

+ name : Same as PiWindow
+ widget : Same as PiWindow
+ side : The edge on which you want the bar to be.
+ size : The size of the bar. It is the height of the bar if the edge is top or bottom, otherwise it's the width of the bar
+ strut : Same as PiWindow
+ screen : The screen on which the bar is displayed.
+ focusable : Same as PiWindow
+ transparent : Same as PiWindow

## PiLockScreen

Another subclass of PiWindow but with the twist that it steals all your keys.

+ name: Same as PiWindow
+ screen: Same as PiWindow
+ transparent: Same as PiWindow
+ focusable: Same as PiWindow
+ widget: Same as PiWindow
+ passwordBox: PiPasswordBox widget which will act as your input box.

> The passwordBox argument does NOT add the textbox to the PiLockScreen, it is used just to send keys to it. You must add the PasswordBox yourself to the Lockscreen UI.