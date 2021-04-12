from typing import Optional
from math import pi, fmod
from chapter3.ds.kinematic import Kinematic
from chapter3.ds.steering_output import SteeringOutput


def map_to_range(radian: float):
    return fmod(radian, 2 * pi)


class Align:
    @staticmethod
    def get_steering(
            character: Kinematic,
            target: Kinematic,
            max_angular_acceleration: float,
            max_rotation: float,
            target_radius: float,
            slow_radius: float,
            time_to_target: float = 0.1
    ) -> Optional[SteeringOutput]:
        res = SteeringOutput()
        rotation = map_to_range(target.orientation - character.orientation)
        rotation_size = abs(rotation)
        if rotation_size < target_radius:
            return None

        # 目標回転速度
        target_rotation = max_rotation \
            if rotation_size > slow_radius \
            else max_rotation * rotation_size / slow_radius
        target_rotation *= rotation / rotation_size

        # 差を計算してAlignのための速度を計算
        res.angular = target_rotation - character.rotation
        res.angular /= time_to_target

        # クリッピング
        angular_acceleration = abs(res.angular)
        if angular_acceleration > max_angular_acceleration:
            res.angular /= angular_acceleration
            res.angular *= max_angular_acceleration

        res.linear = 0
        return res
