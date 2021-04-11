from typing import Optional
from chapter3.ds.static import Static
from chapter3.ds.steering_output import KinematicSteeringOutput
from chapter3.kinematic_movement.util import new_orientation


class KinematicArrive:
    character: Static
    target: Static
    max_speed: float
    radius: float  # たどり着いたと判定する半径
    time_to: float = 0.25  # ターゲットにたどり着くまでの希望時間

    def get_steering(self) -> Optional[KinematicSteeringOutput]:
        res = KinematicSteeringOutput()
        res.velocity = self.target.position - self.character.position

        # 円の中にたどり着いた場合
        if res.velocity.length() < self.radius:
            return None

        # time_to秒でたどり着くようにする
        res.velocity /= self.time_to

        # 最大速度内にクリッピング
        if res.velocity.length() > self.max_speed:
            res.velocity.normalize()
            res.velocity *= self.max_speed

        self.character.orientation = new_orientation(
            self.character.orientation,
            res.velocity
        )
        res.rotation = 0
        return res
