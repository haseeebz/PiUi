
import shutil
from PiUI.core.tools import Shell	

class BrightnessInfo():

	def __init__(self):
		if shutil.which("brightnessctl") is None:
			raise Exception("brightnessctl is not installed on your system! Cannot start system.brightness")
	
	def getCurrentValue(self) -> int | None:
		current = Shell("brightnessctl get")
		if current[1]:
			return int(current[0])
		else:
			return None

	def getTotalValue(self) -> int | None:
		total = Shell("brightnessctl max")
		if total[1]:
			return int(total[0])
		else:
			return None
		
	def getPerc(self) -> int | None:
		current = self.getCurrentValue()
		total = self.getTotalValue()

		if current and total:
			perc = (current / total) * 100
			return int(perc)
		else:
			return None
	
	def setValue(self, value: int):
		Shell(f"brightnessctl set {value}%")
			
