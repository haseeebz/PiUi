
from .widget import PiWidget
from PiUi.components.helpers import ImageWidget
from PiUi.app.utils.binder import Binding
from PiUi.app.utils.poller import Poll
from PiUi.app.utils import Alignment

    
class PiImage(PiWidget):

    def __init__(
        self,
        *,
        name: str | Binding | Poll | None = None,
        path: str | Binding | Poll | None = None,
        height: int | Binding | Poll | None = None,
        width: int | Binding | Poll | None = None,
        hAlign: Alignment.H | None = Alignment.H.center,
        vAlign: Alignment.V | None = Alignment.V.center,
        state: str | Binding | Poll | None = None
    ):

        super().__init__(ImageWidget, name, height, width, hAlign, vAlign, state)
        self._backend : ImageWidget

        self.applyAttribute(
            self._backend.setImage,
            path
        )