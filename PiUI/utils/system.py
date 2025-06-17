
import os


class System():

    def __init__(self, dire) -> None:
        for file in os.listdir(dire):
            try:
                with open(os.path.join(dire, file)) as f:
                    print(f"{file} ::")
                    print(f.read())
                    print("\n////\n")
            except IsADirectoryError:
                print(f"{file} is a directory")
                print("\n////\n")
        


system = System("/sys/class/power_supply/BAT0")