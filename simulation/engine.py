from .body import Body
from .constants import G
import numpy as np
import numpy.linalg as alg


def apply_gravity(b1: Body, b2: Body) -> None:
    dist = b2.get_position() - b1.get_position()
    versor = dist / alg.norm(dist)
    module = G * b1.get_mass() * b2.get_mass() / (alg.norm(dist) ** 2)
    b1.add_force(module * versor)
    b2.add_force(-module * versor)
    return


def evolve(dt: float, body: Body) -> None:
    """
    Evolve the body of a certain interval of time.
    :param dt: Interval to evolve the body in seconds.
    :param body:
    """
    position = body.get_position()
    velocity = body.get_velocity()
    acceleration = body.get_force() / body.get_mass()
    new_pos = position + velocity * dt + 0.5 * acceleration * dt ** 2
    body.set_position(new_pos)
    new_vel = velocity + acceleration * dt
    body.set_velocity(new_vel)

    # All forces must be reset
    body.reset_forces()
