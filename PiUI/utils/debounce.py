
from PySide6.QtCore import QTimer
from typing import Callable

func_map: dict[str, QTimer] = {}

def Debounce(interval: int | float):
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            if func not in func_map.keys():
                result = func(*args, **kwargs)
                func_map[func] = QTimer(interval=int(interval*1000), singleShot=True) 
                func_map[func].start()
                

            else:
                if func_map[func].remainingTimeAsDuration() > 0:
                    return None
                
                result = func(*args, **kwargs)
                func_map[func].setInterval(int(interval*1000))
                func_map[func].start()

            return result
        return wrapper
    return decorator

