from chapter3.ds.ikinematic import IKinematic
from chapter3.ds.steering_output import SteeringOutput


class Kinematic(IKinematic):

    def update(self, steering: SteeringOutput, max_speed: float, time: float) -> None:
        self.position += self.velocity * time
        self.orientation += self.rotation * time

        self.velocity += steering.linear * time
        self.rotation += steering.angular * time

        if self.velocity.length() > max_speed:
            self.velocity.normalize()
            self.velocity *= max_speed
