import math


class Vector:
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        l = self.length()
        self.x /= l
        self.y /= l
        self.z /= l

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float):
        return self.__class__(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float):
        return self.__class__(self.x / other, self.y / other, self.z / other)
