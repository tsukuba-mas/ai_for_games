from typing import Optional
from chapter3.ds.kinematic import Kinematic
from chapter3.ds.steering_output import SteeringOutput


class Arrive:
    @staticmethod
    def get_steering(
            character: Kinematic,
            target: Kinematic,
            max_acceleration: float,
            max_speed: float,
            target_radius: float,
            slow_radius: float,
            time_to_target: float = 0.1
    ) -> Optional[SteeringOutput]:
        res = SteeringOutput()
        direction = target.position - character.position
        distance = direction.length()

        if distance < target_radius:
            return None  # 到達したら終了

        # 減速半径内なら減速させる
        target_speed = max_speed \
            if distance > slow_radius \
            else max_speed * distance / slow_radius

        # ターゲット方向の速度を計算する
        target_velocity = direction
        target_velocity.normalize()
        target_velocity *= target_speed

        # 加速度を計算する
        res.linear = target_velocity - character.velocity
        res.linear /= time_to_target

        if res.linear.length() > max_acceleration:
            res.linear.normalize()
            res.linear *= max_acceleration

        res.angular = 0
        return res
