


from PiUI.components.widgets import PiBox, PiLabel, PiButton

from PiUI.app.utils import Binder, Poller, Shell


def get_workspaces(binder: Binder):
    output = Shell("wmctrl -d")[0]
    boxes = []

    for i, line in enumerate(output.splitlines()):
        box = PiButton(
            name = "ws-box",
            width = 18,
            height = 18,
            onClick = lambda _, x=i: Shell(f"wmctrl -s {x}"),
            state = binder.Bind(f"ws{i}")
        )
        binder.update(f"ws{i}", "off")
        boxes.append(box)

    return boxes


def update_workspaces(binder: Binder):
    output = Shell("wmctrl -d")[0]
    for i, line in enumerate(output.splitlines()):
        if "*" in line:
            binder.update(f"ws{i}", "on")
        else:
            binder.update(f"ws{i}", "off")

    
    


