from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget
)
from typing import Callable, Literal, Tuple
from PiUi.core.utils import Binding, Alignment, Poll
from PiUi.components.helpers import CustomEventWidget


class PiWidget():

    def __init__(
        self,
        qt,
        name: str | None = None,
        height: int | None = None,
        width: int | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str = None
        ):
        self.qt: QWidget = qt()
        
        if name:
            self.applyAttribute(
                self.qt.setObjectName,
                name
            )

        if height:
            self.applyAttribute(
                self.qt.setFixedHeight,
                height
            )
            
        if width:
            self.applyAttribute(
                self.qt.setFixedWidth,
                width
            )
        
        self.hAlign = hAlign
        self.vAlign = vAlign

        if state:
            self.applyAttribute(
                self.setState,
                state
            )


    def setState(self, value:str):
        self.qt.setProperty("state", value)
        self.qt.style().unpolish(self.qt)
        self.qt.style().polish(self.qt)


    def applyAttribute(self, setter: Callable, value):
        if isinstance(value, (Binding, Poll)):
            value.bind(setter)
        else:
            setter(value)



class PiBox(PiWidget):
    
    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        orientation: Literal["horizontal", "vertical"] | None,
        spacing: int | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        widgets: list[PiWidget] | Binding | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str | Binding | Poll | None = None
        ):

        super().__init__(QWidget, name, height, width, hAlign, vAlign, state)
        self.qt: QWidget
        
        if orientation == "horizontal":
            self.layout = QHBoxLayout()
        elif orientation == "vertical":
            self.layout = QVBoxLayout()
        else:
            print("Incorrect or Left out orientation for PiBox!\nDefaulting to horizontal.")
            self.layout = QHBoxLayout()
        
        self.qt.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)


        if widgets:
            for widget in widgets:
                self.layout.addWidget(widget.qt, alignment= (widget.hAlign.value | widget.vAlign.value))
        

        if spacing:
            self.applyAttribute(
                self.layout.setSpacing,
                spacing
            )



class PiLabel(PiWidget):
    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        text: str | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str | Binding | Poll | None = None    
    ):
        
        super().__init__(QLabel, name, height, width, hAlign, vAlign, state)
        self.qt: QLabel

        if text:
            self.applyAttribute(
                self.qt.setText,
                text
            )
        
        

class PiButton(PiWidget):

    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        text: str | Binding | None = None,
        onClick: Callable | Binding | None = None,
        onRelease: Callable | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str | Binding | Poll | None = None
    ):

        super().__init__(QPushButton, name, height, width, hAlign, vAlign, state)
        self.qt : QPushButton
    
        if text:
            self.applyAttribute(
                self.qt.setText,
                text
            )

        if onClick:
            self.applyAttribute(
                self.qt.clicked.connect,
                onClick
            )

        if onRelease:
            self.applyAttribute(
                self.qt.released.connect,
                onRelease
            )




class PiEventBox(PiWidget):
    
    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str | Binding | Poll | None = None,
        widget: PiWidget | Binding | None = None,
        onRightClick: Callable | Binding | Poll | None = None,
        onLeftClick: Callable | Binding | Poll | None = None,
        onMiddleClick: Callable | Binding | Poll | None = None,
        onDoubleClick: Callable | Binding | Poll | None = None,
        onMouseRelease: Callable | Binding | Poll | None = None,
        onMouseEnter: Callable | Binding | Poll | None = None,
        onMouseLeave: Callable | Binding | Poll | None = None,
        ):

        super().__init__(CustomEventWidget, name, height, width, hAlign, vAlign, state)
        self.qt: CustomEventWidget

        
        if onRightClick:
            self.applyAttribute(
                self.qt.connectRightClick,
                onRightClick
            )

        if onLeftClick:
            self.applyAttribute(
                self.qt.connectLeftClick,
                onLeftClick
            )

        if onMiddleClick:
            self.applyAttribute(
                self.qt.connectMiddleClick,
                onMiddleClick
            )

        if onMouseRelease:
            self.applyAttribute(
                self.qt.connectMouseRelease,
                onMouseRelease
            )

        if onDoubleClick:
            self.applyAttribute(
                self.qt.connectDoubleClick,
                onDoubleClick
            )

        if onMouseEnter:
            self.applyAttribute(
                self.qt.connectMouseEnter,
                onMouseEnter
            )

        if onMouseLeave:
            self.applyAttribute(
                self.qt.connectMouseLeave,
                onMouseLeave
            )


        self.layout = QHBoxLayout()
        self.qt.setLayout(self.layout)
        self.qt.setContentsMargins(0,0,0,0)

        if widget:
            self.layout.addWidget(widget.qt)


