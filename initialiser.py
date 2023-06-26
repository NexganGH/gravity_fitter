import numpy as np
from simulation import Body

SECONDS = 100  # How long will the simulation last
CHECKS = 100  # How many checks there will be for each test
DESIRED_DISTANCE = 600
STARTING_VELOCITY = (20, 80)
SIM_SPEED = 10 #  Speed up the simulation in the charts (does not influence the fit)
STEP = 0.5  # How long each step, in seconds. The lesser, the more accurate the software is.

M1 = 10 * pow(10, 16)
M2 = 10 * pow(10, 13)
def create_bodies(velx, vely, m1, m2):
    p1 = Body(m1, np.array([1000, 1000]), np.array([0, 0]))
    p2 = Body(m2, np.array([1000 + DESIRED_DISTANCE, 1000]), np.array([velx, vely]))

    return [p1, p2]
