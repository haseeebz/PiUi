
from .widget import PiWidget
from PiUI.components.helpers import ImageWidget
from PiUI.app.utils.binder import Binding
from PiUI.app.utils.poller import Poll
from PiUI.app.utils import Alignment

    
class PiImage(PiWidget):

    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        path: str | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = None,
        vAlign: Alignment.V | None = None,
        state: str | Binding | Poll | None = None
    ):

        super().__init__(ImageWidget, name, height, width, hAlign, vAlign, state)
        self._backend : ImageWidget

        self.applyAttribute(
            self._backend.setImage,
            path
        )