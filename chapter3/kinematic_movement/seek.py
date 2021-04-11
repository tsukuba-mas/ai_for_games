from chapter3.ds.static import Static
from chapter3.ds.steering_output import KinematicSteeringOutput
from chapter3.kinematic_movement.util import new_orientation


class KinematicSeek:
    @staticmethod
    def get_steering(
            character: Static,
            target: Static,
            max_speed: float
    ) -> KinematicSteeringOutput:
        res = KinematicSteeringOutput()

        # 速度を計算して最大速度にする
        res.velocity = target.position - character.position
        res.velocity.normalize()
        res.velocity *= max_speed

        # 向きを計算する
        character.orientation = new_orientation(
            character.orientation,
            res.velocity
        )
        res.rotation = 0
        return res
