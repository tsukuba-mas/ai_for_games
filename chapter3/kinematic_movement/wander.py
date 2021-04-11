from random import random
from chapter3.ds.static import Static, to_vector
from chapter3.ds.steering_output import KinematicSteeringOutput
from chapter3.kinematic_movement.util import new_orientation


class KinematicWander:
    character: Static
    max_speed: float
    max_rotation: float

    @staticmethod
    def random_binominal() -> float:
        return random() - random()

    def get_steering(self) -> KinematicSteeringOutput:
        res = KinematicSteeringOutput()

        # 今向いている方向を　速度に変換する
        res.velocity = to_vector(self.character.orientation) * self.max_speed

        # 回転量を計算する
        res.rotation = KinematicWander.random_binominal() * self.max_rotation

        return res
