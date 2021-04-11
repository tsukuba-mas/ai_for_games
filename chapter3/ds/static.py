import math
from chapter3.ds.vector import Vector


def to_vector(orientation: float) -> Vector:
    return Vector(math.sin(orientation), 0, math.cos(orientation))


class Static:
    position: Vector
    orientation: float
