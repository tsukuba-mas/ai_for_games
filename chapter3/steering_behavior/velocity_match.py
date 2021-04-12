from typing import Optional
from chapter3.ds.kinematic import Kinematic
from chapter3.ds.steering_output import SteeringOutput


class VelocityMatching:
    @staticmethod
    def get_steering(
            character: Kinematic,
            target: Kinematic,
            max_acceleration: float,
            time_to_target: float = 0.1
    ) -> Optional[SteeringOutput]:
        res = SteeringOutput()

        # 速度の差を計算し加速度とする
        res.linear = target.velocity - character.velocity
        res.linear /= time_to_target

        if res.linear.length() > max_acceleration:
            res.linear.normalize()
            res.linear *= max_acceleration

        res.angular = 0
        return res
