import numpy as np
from random import random, seed
import tkinter
from PIL import Image, ImageTk, ImageDraw
from time import time
import matplotlib.pyplot as plt

G = 6.673e-11
SOLAR_MASS = 1.98892e30


class Body:
    def __init__(self, rx, ry, vx, vy, mass, softening, color=None):
        self._rx = rx
        self._ry = ry
        self._vx = vx
        self._vy = vy
        self._fx = 0.0
        self._fy = 0.0
        self._mass = mass
        self.softening = softening
        self._color = color

    @property
    def rx(self):
        return self._rx

    @property
    def ry(self):
        return self._ry

    @property
    def vx(self):
        return self._vx

    @property
    def vy(self):
        return self._vy

    @property
    def fx(self):
        return self._fx

    @property
    def fy(self):
        return self._fy

    @property
    def mass(self):
        return self._mass

    @property
    def color(self):
        return self._color

    def update(self, dt):
        """
        Params:
        ---------
        dt: timestep

        Returns:
        updated position and velocity
        -----
        """
        self._vx += dt * self._fx / self._mass
        self._vy += dt * self._fy / self._mass
        self._rx += dt * self._vx
        self._ry += dt * self._vy

    def distance_to(self, other_body):
        dx = self._rx - other_body._rx
        dy = self._ry - other_body._ry
        return np.sqrt(dx**2 + dy**2)

    def reset_force(self):
        self._fx = 0.0
        self._fy = 0.0

    def add_force(self, other_body):
        dx = other_body._rx - self._rx
        dy = other_body._ry - self._ry
        distance = np.sqrt(dx**2 + dy**2)
        force = (G * self._mass * other_body._mass) / \
            (distance**2 + self.softening**2)
        self._fx += force * dx / distance
        self._fy += force * dy / distance

    def add(self, other_body):
        total_mass = self.mass + other_body.mass
        new_rx = ((self.rx * self.mass) +
                  (other_body.mass * other_body.rx)) / total_mass
        new_ry = ((self.ry * self.mass) +
                  (other_body.mass * other_body.ry)) / total_mass
        new_body = Body(new_rx, new_ry, self.vx, self.vy,
                        total_mass, self.softening)
        return new_body

    def print_body(self):
        print("{}, {}, {}, {}, {}".format(
            self._rx, self._ry, self._vx, self._vy, self._mass))

    def is_in(self, quadrant):
        return quadrant.contains_point(self._rx, self._ry)


def main():
    print("Hello world")


if __name__ == "__main__":
    main()
