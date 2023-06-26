from initialiser import create_bodies
import simulation
import numpy as np


def fit_func(x: np.ndarray[float], v2x: float, v2y: float):
    bodies = create_bodies(v2x, v2y)
    return simulation.simulate_radius(np.array(bodies), x, 0.5, np.array([0, 0]), np.array([v2x, v2y]))