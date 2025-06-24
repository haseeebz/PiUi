
# Widgets

Every widget inherits from PiWidget. They all have the following same properties:

+ name : Name of the widget, used for styling.
+ height : Sets the fixed height
+ width : Sets the fixed width
+ hAlign : Sets the horizontal alignment in a PiBox
+ vAlign : Sets the vertical alignment in a PiBox
+ state : Sets the state of the widget. See [styling.md](docs/styling.md)

Following are the widgets currently implemented:

## PiBox

A container that arranges widgets in a row or column.

### Properties

+ orientation : "horizontal" or "vertical". Default is "horizontal".
+ widgets : List of widgets to place inside the box. Can be binded.
+ spacing : The space between widgets.



## PiButton

A button widget, duh.

### Properties

+ text : The label displayed on the button. Can be binded.
+ onClick : Function to call when button is pressed. No arguments are passed to the function.
+ onRelease : Function to call when button is released. No arguments are passed to the function.

## PiEventBox

Useful for catching different mouse events. Can be wrapped around another widget.

### Properties

+ widget : The wrapped widget. Can be binded.
+ onRightClick : Callback for right click.
+ onLeftClick : Callback for left click.
+ onMiddleClick : Callback for middle click.
+ onDoubleClick : Callback for double click.
+ onMouseRelease : Callback for mouse release.
+ onMouseEnter : Callback when mouse enters.
+ onMouseLeave : Callback when mouse leaves.

## PiImage

Displays an image.

### Properties

+ path : Path to the image file. Can be binded and polled.
+ rounding : Rounding radius for the corners.
+ preserveAspectRatio : Whether to maintain aspect ratio. Default is True.


## PiLabel

Displays a line of text.

### Properties

+ text : The string to be displayed. Can be binded and polled.
+ xAlign : Horizontal alignment of text inside the label.
+ yAlign : Vertical alignment of text inside the label.



## PiOverlay

Stacks multiple widgets on top of each other. The widget at the first index is displayed at the top while the widget at the last index is at the bottom.

### Properties

+ widgets : List of widgets to overlay.


## PiPasswordBox

A textbox designed for passwords. Obscures input by default and integrates with PiLockScreen. If you want to make an input box for your lock screen, you must use this!

### Properties

+ placeHolderText : Hint text when the field is empty. Can be binded and polled.
+ text : Current value of the input. Can be binded and polled.
+ onEnter : Callback on Enter key.
+ onChange : Callback on value change.



## PiProgress

A visual progress bar.

### Properties

+ value : Current progress value. Can be binded and polled.
+ orientation : "horizontal" or "vertical". Default is "horizontal".
+ onChange : Callback on value change.


## PiScrollBox

A scrollable container. ix its height (or width depending on orientation) to get a good result.

### Properties

+ orientation : "horizontal" or "vertical". Default is "horizontal".
+ widget : The scrollable child. Can be binded.
+ onScroll : Callback for scroll events.


## PiSpacer

An invisible widget that just takes up space. Simply a wrapper around PiWidget.



## PiTextInput

A single-line input box.

### Properties

+ placeHolderText : Hint text when the field is empty. Can be binded and polled.
+ text : Current text value. Can be binded and polled.
+ onEnter : Callback when Enter is pressed.
+ onChange : Callback on text change.
+ password : Whether to hide the characters. Default is False.

