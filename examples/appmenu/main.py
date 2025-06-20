
from PiUI.core import Pi

from PiUI.components.window import PiWindow
from PiUI.components.widgets import PiBox, PiTextInput


menu = PiWindow(

	name = "menu",
	position = ( Pi.screen.x//2 - 300, Pi.screen.y//2 - 100),
	size = (600, 200),
	focusable = True,
	transparent = True,
	widget = PiBox(
		orientation = 'vertical',
		widgets = [

			PiTextInput(
				name = "input",
				placeHolderText = "Enter app name...",
				onChange = 
			)
		] 
		)
)