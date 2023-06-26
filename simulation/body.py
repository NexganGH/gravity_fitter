import numpy as np
from numpy import ndarray


class Body:
    def __init__(self, mass: float, position: ndarray, velocity: ndarray):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = np.array([0, 0])

    def set_position(self, position: ndarray) -> None:
        self.position = position

    def get_position(self) -> ndarray:
        return self.position

    def get_velocity(self) -> ndarray:
        return self.velocity

    def set_velocity(self, velocity: ndarray) -> None:
        self.velocity = velocity

    def get_acceleration(self) -> ndarray:
        return self.acceleration

    def set_acceleration(self, acceleration: ndarray) -> None:
        self.acceleration = acceleration
