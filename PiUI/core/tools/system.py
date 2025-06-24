
from .sysinfo import BatteryInfo, BrightnessInfo

class System():

	def __init__(self) -> None:
		
		bat = BatteryInfo()
		self.battery: BatteryInfo | None = bat if bat.checkBatteries() else None
		
		self.brightness: BrightnessInfo = BrightnessInfo()


