from PySide6.QtCore import Qt
from enum import Enum


class Alignment:
    base = Qt.AlignmentFlag.AlignJustify
    class H(Enum):
        left = Qt.AlignmentFlag.AlignLeft
        right = Qt.AlignmentFlag.AlignRight
        center = Qt.AlignmentFlag.AlignHCenter

    class V(Enum):
        top = Qt.AlignmentFlag.AlignTop
        bottom = Qt.AlignmentFlag.AlignBottom
        center = Qt.AlignmentFlag.AlignVCenter

