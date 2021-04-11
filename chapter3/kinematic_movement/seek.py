from chapter3.ds.static import Static
from chapter3.ds.steering_output import KinematicSteeringOutput
from chapter3.kinematic_movement.util import new_orientation


class KinematicSeek:
    character: Static
    target: Static
    max_speed: float

    def get_steering(self) -> KinematicSteeringOutput:
        res = KinematicSteeringOutput()

        # 速度を計算して最大速度にする
        res.velocity = self.target.position - self.character.position
        res.velocity.normalize()
        res.velocity *= self.max_speed

        # 向きを計算する
        self.character.orientation = new_orientation(
            self.character.orientation,
            res.velocity
        )
        res.rotation = 0
        return res
