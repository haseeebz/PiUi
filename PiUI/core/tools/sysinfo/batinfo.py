

import os

from PiUI.core.logger import getLogger
log = getLogger("core")

class BatteryInfo():

	def __init__(self) -> None:
		self._power_path = "/sys/class/power_supply/"
		self._batteries: list[str] = []
		self._count = 0

	def checkBatteries(self) -> bool:

		if not os.path.exists(self._power_path):
			return False

		batteries = []
		for directory in os.listdir(self._power_path):
			if "BAT" in directory:
				batteries.append(os.path.join(self._power_path, directory))
		
		if len(batteries) > 0:
			self._batteries = batteries
			self._batteries.sort()
			self._count = len(batteries)
			return True
		else:
			return False
		
	def status(self, bat: int) -> str:
		
		if self._count <= bat:
			bat = self._count - 1

		path = os.path.join(self._batteries[bat] , "status")

		try:
			with open(path) as file:
				status = file.read().strip()
		except Exception as e:
			log.error(str(e))

		return status

	def capacity(self, bat: int) -> int:

		if self._count <= bat:
			bat = self._count - 1

		path = os.path.join(self._batteries[bat] , "capacity")

		try:
			with open(path) as file:
				capacity = int(file.read().strip())
		except Exception as e:
			log.error(str(e))

		return capacity

	def count(self):
		return self._count
	
	def totalCapacity(self):
		now = 0
		full = 0

		#now sum
		for bat in self._batteries:
			now_path = os.path.join(bat, "energy_now")
			now_path2 = os.path.join(bat, "charge_now")

			if os.path.exists(now_path):
				with open(now_path) as file:
					now += int(file.read().strip())

			elif os.path.exists(now_path2):
				with open(now_path2) as file:
					now += int(file.read().strip())

			else:
				log.critical(f"Could not parse energy now for {bat}")

		#full sum
		for bat in self._batteries:
			full_path = os.path.join(bat, "energy_full")
			full_path2 = os.path.join(bat, "charge_full")

			if os.path.exists(full_path):
				with open(full_path) as file:
					full += int(file.read().strip())

			elif os.path.exists(full_path2):
				with open(full_path2) as file:
					full += int(file.read().strip())

			else:
				log.critical(f"Could not parse energy full for {bat}")

		if full <= 0:
			log.critical(f"Got full energy capacity of both values as {full}. Defaulting to zero on total charge.")

		return (now/full)*100


