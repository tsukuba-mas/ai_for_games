import math
from chapter3.ds.vector import Vector


def new_orientation(current: float, velocity: Vector) -> float:
    if velocity.length() > 0:
        return math.atan2(-velocity.x, velocity.z)
    else:
        return current
