

import os

class BatteryInfo():

    def __init__(self) -> None:
        self._power_path = "/sys/class/power_supply/"
        self._batteries: list[str] = []
        self._count = 0

    def countBatteries(self) -> bool:

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
        
    def checkStatus(self, bat: int) -> str:
        
        if self._count <= bat:
            bat = self._count - 1

        path = os.path.join(self._batteries[bat] , "status")

        try:
            with open(path) as file:
                status = file.read().strip()

        except FileNotFoundError:
            return "File Not Found!"
        except Exception as e:
            return str(e)

        return status

    def getCapacity(self, bat: int) -> int:

        if self._count <= bat:
            bat = self._count - 1

        path = os.path.join(self._batteries[bat] , "capacity")

        try:
            with open(path) as file:
                capacity = int(file.read().strip())
        except FileNotFoundError:
            return "File Not Found!"
        except Exception as e:
            return str(e)

        return capacity


    def count(self):
        return self._count



bat = BatteryInfo()
if bat.countBatteries():
    print(bat._batteries)
    print()
    print(bat.checkStatus(0))
    print(bat.checkStatus(1))


