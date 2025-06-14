
from PySide6.QtWidgets import QHBoxLayout

def clearLayout(layout: QHBoxLayout):

    if layout is None:
        return
    
    while layout.count():

        item = layout.itemAt(0)

        widget = item.widget()
        if widget is not None:
            widget.setParent(None)
        else:
            layout = item.layout()
            if layout:
                clearLayout(layout)

