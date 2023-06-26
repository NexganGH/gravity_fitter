from .body import Body
import numpy as np


def evolve(dt: float, body: Body) -> None:
    """
    Evolve the body of a certain interval of time.
    :param dt: Interval to evolve the body in seconds.
    :param body:
    """
    position = body.get_position()
    velocity = body.get_velocity()
    acceleration = body.get_acceleration()
    new_pos = position + velocity * dt + 0.5 * acceleration * dt ** 2
    body.set_position(new_pos)
    new_vel = velocity + acceleration * dt
    body.set_velocity(new_vel)
