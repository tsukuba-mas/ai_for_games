from abc import ABC, abstractmethod
from chapter3.ds.vector import Vector
from chapter3.ds.steering_output import SteeringOutput


class IKinematic(ABC):
    position: Vector
    orientation: float
    velocity: Vector
    rotation: float

    @abstractmethod
    def update(self, steeringOutput, max_speed: float, time: float):
        pass
