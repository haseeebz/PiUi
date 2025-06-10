
from PySide6.QtCore import Qt

from shiboken6 import Shiboken
from enum import Enum

		
class Alignment(Shiboken.Object):

	class H(Enum):
		left = Qt.AlignmentFlag.AlignLeft
		right = Qt.AlignmentFlag.AlignRight
		center = Qt.AlignmentFlag.AlignHCenter

	class V(Enum):
		top = Qt.AlignmentFlag.AlignTop
		bottom = Qt.AlignmentFlag.AlignBottom
		center = Qt.AlignmentFlag.AlignVCenter