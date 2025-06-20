
from .sysinfo import BatteryInfo

class System():

	def __init__(self, dire) -> None:
		bat = BatteryInfo()
		self.bat: BatteryInfo | None = bat if bat.checkBatteries() else None
		


