from .body import Body
from .constants import G
from .engine import evolve, apply_gravity
import numpy as np
import numpy.linalg as alg
import copy

def simulate_radius(bodies: np.ndarray[Body], time: np.ndarray[float], step: float,
                    v1: np.ndarray, v2: np.ndarray
                    ) -> np.ndarray[float]:
    """
    Simulate gravity between bodies and return the radius (distance) between first two.
    :param v1: Velocity of first body.
    :param v2: Velocity of second body.
    :param bodies:
    :param time: The time in which the radius must be calculated, in seconds.
    :param step: Time interval to use in the simulation. The smaller, the more accurate. In seconds.
    :return: the radius.
    """
    print('simulate with ' + str(v1) + ' ' + str(v2))

    max_time: float = np.max(time)

    old_0 = copy.copy(bodies[0])
    old_1 = copy.copy(bodies[1])

    bodies[0].set_velocity(v1)
    bodies[1].set_velocity(v2)
    current_time = 0
    results = []
    while current_time < max_time:
        for i in range(0, len(bodies) - 1):
            for j in range(i+1, len(bodies)):
                apply_gravity(bodies[i], bodies[j])

        for body in bodies:
            evolve(step, body)

        current_time += step

        radius = alg.norm(bodies[0].get_position() - bodies[1].get_position())

        keep = np.ones(time.shape, dtype=bool)
        for index, t in enumerate(time):
            if current_time >= t:
                results.append(radius)
                keep[index] = False

        time = time[keep]

    print('results (mean)=' + str(np.mean(results)) + ' #=' + str(len(results)))
    return np.array(results)
