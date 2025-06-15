
from PySide6.QtWidgets import QLayout

def clearLayout(layout: QLayout | None):

    if layout is None:
        return
    
    while layout.count():

        item = layout.itemAt(0)

        widget = item.widget() # type: ignore #None Handled
        if widget is not None:
            widget.setParent(None)
        else:
            layout = item.layout() # type: ignore #None Handled
            if layout:
                clearLayout(layout)

