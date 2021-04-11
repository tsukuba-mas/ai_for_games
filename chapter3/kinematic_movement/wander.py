from random import random
from chapter3.ds.static import Static, to_vector
from chapter3.ds.steering_output import KinematicSteeringOutput
from chapter3.kinematic_movement.util import new_orientation


class KinematicWander:
    @staticmethod
    def random_binominal() -> float:
        return random() - random()

    @staticmethod
    def get_steering(
            character: Static,
            max_speed: float,
            max_rotation: float,
    ) -> KinematicSteeringOutput:
        res = KinematicSteeringOutput()

        # 今向いている方向を　速度に変換する
        res.velocity = to_vector(character.orientation) * max_speed

        # 回転量を計算する
        res.rotation = KinematicWander.random_binominal() * max_rotation

        return res
