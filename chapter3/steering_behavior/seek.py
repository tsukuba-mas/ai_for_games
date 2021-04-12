from chapter3.ds.kinematic import Kinematic
from chapter3.ds.steering_output import SteeringOutput


class Seek:
    @staticmethod
    def get_steering(
            character: Kinematic,
            target: Kinematic,
            max_acceleration: float
    ) -> SteeringOutput:
        res = SteeringOutput()

        # 加速度を計算する
        res.linear = target.position - character.position
        res.linear.normalize()
        res.linear *= max_acceleration

        res.angular = 0
        return res
