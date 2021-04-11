from abc import ABC, abstractmethod
from chapter3.ds.vector import Vector
from chapter3.ds.steering_output import SteeringOutput


class Kinematic(ABC):
    position: Vector
    orientation: float
    velocity: Vector
    rotation: float

    @abstractmethod
    def update(self, steeringOutput):
        pass

