from mothic.maths.numbers import remap
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
    """
    A single loop through a lissajous curve,
    given the width and height of the curve, as well as the horizontal and vertical frequencies.
    Starts and ends in the center (if center exists)
    """
    def __init__(self, width: int, height: int, hor_freq: int, ver_freq: int, duration: int):
        super().__init__(duration)

        self.width = width // 2
        self.height = height // 2
        self.hor_freq = hor_freq
        self.ver_freq = ver_freq

    def move(self):
        super().move()

        theta = remap(self.ticks, 0, self.duration, 0, 2 * pi)
        dx = self.width * sin(self.ver_freq * theta)
        dy = self.height * sin(self.hor_freq * theta)

        ax, ay, ad = self.anchor
        return dx + ax, dy + ay, ad

