from math import sin, pi
from pygame import Vector3


pos = tuple[float, float]
pos3 = tuple[float, float, float]


def sine_transition(n):
    """
    Gives a smooth transition from [0, 1] for an input from [0, 1]
    """
    return (sin(pi * (n - 0.5)) / 2) + 0.5


class Movement:
    """
    Defines a movement from a given starting anchor position for a given duration
    """

    def __init__(self, duration: int):
        self.anchor = (0, 0, 0)
        self.duration = duration
        self.ticks = 0
        self.done = False

    def set_anchor(self, anchor: pos3):
        self.anchor = anchor

    def reset(self):
        self.ticks = 0
        self.done = False

    def move(self):
        """
        Returns the position for the movement at the current tick
        """
        self.ticks += 1
        self.done = self.ticks >= self.duration


class Line(Movement):
    """
    A smoothened linear movement towards a given target position
    """

    def __init__(self, target: pos3, duration: int):
        super().__init__(duration)
        self.target = target

    def move(self):
        super().move()

        direction = Vector3(self.target) - Vector3(self.anchor)
        rx, ry, rd = direction * sine_transition(self.ticks / self.duration)
        ax, ay, ad = self.anchor
        return rx + ax, ry + ay, rd + ad


class Lissajous(Movement):
    def __init__(self, duration: int):
        super().__init__(duration)

    def move(self):
        super().move()

