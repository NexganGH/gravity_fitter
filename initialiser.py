import numpy as np
from simulation import Body

SECONDS = 150  # How long will the simulation last
CHECKS = 150  # How many checks there will be for each test
DESIRED_DISTANCE = 300
STARTING_VELOCITY = (0, 80)
SIM_SPEED = 10 #  Speed up the simulation in the charts (does not influence the fit)
STEP = 0.5  # How long each step, in seconds. The lesser, the more accurate the software is.


def create_bodies(velx, vely):
    p1 = Body(10 * np.float_power(10, 15), np.array([500, 500]), np.array([0, 0]))
    p2 = Body(10 * np.float_power(10, 13), np.array([500 + DESIRED_DISTANCE, 500]), np.array([velx, vely]))

    return [p1, p2]