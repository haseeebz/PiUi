
import subprocess
from typing import Tuple, Literal


def Shell(cmd: str | list[str]) -> Tuple[str, bool]:

    try:
        if not isinstance(cmd, list):
            cmd = cmd.split()

        output = subprocess.run(cmd, capture_output=True, text= True)

        if output.returncode == 0:
            return (output.stdout.strip(), True)
        else:
            return (output.stderr.strip(),  False)
        
    except Exception as e:
        return (str(e), False)