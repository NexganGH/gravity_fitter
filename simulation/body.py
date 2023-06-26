import numpy as np
from numpy import ndarray


class Body:
    def __init__(self, mass: float, position: ndarray, velocity: ndarray):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.force = np.array([0, 0])

    def get_mass(self) -> float:
        return self.mass

    def set_position(self, position: ndarray) -> None:
        self.position = position

    def get_position(self) -> ndarray:
        return self.position

    def get_velocity(self) -> ndarray:
        return self.velocity

    def set_velocity(self, velocity: ndarray) -> None:
        self.velocity = velocity

    def get_force(self) -> ndarray:
        return self.force

    def set_force(self, force: ndarray) -> None:
        self.force = force

    def add_force(self, force: ndarray) -> None:
        self.force = self.force + force

    def reset_forces(self) -> None:
        self.force = np.array([0, 0], dtype=float)
