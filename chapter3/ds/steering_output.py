from chapter3.ds.vector import Vector


class SteeringOutput:
    """加速度と角速度."""
    linear: Vector
    angular: float


class KinematicSteeringOutput:
    """速度と回転.

    Notes
    -----
    3.2.1, 3.2.2章の Kinematic **Movement** algorithm
    ムーブメントであり、位置と速度のみで角速度は出てこないことに注意する。
    """
    velocity: Vector
    rotation: float
