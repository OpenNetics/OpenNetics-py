
import redwrenlib as rw

d1 = rw.Device()
if not d1.connect(username="", password=""):
    print("error connecting to the system")


def clap_action() -> None:
    pass

def raise_action() -> None:
    pass

def round_action() -> None:
    d1.write("1101") # turn LED1 on


d1.add_gesturefile(
    gesturefile = "/path/to/clap/gesture/file.ges",
    match = {"accel.x":0, "accel.y":1, "accel.z":2, "pressure1":3},
    action = clap_action
)

d1.add_gesturefile(
    gesturefile = "/path/to/raise/gesture/file.ges",
    match = {"accel.y":1},
    action = raise_action
)

d1.add_gesturefile(
    gesturefile = "/path/to/round/gesture/file.ges",
    match = {"accel.x":0, "accel.y":1},
    action = round_action
)
