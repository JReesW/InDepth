from typing import Union
from math import e
from mothic import director, Thing


__DrawnInOrderThing = Union[Thing, "DrawnInOrder"]
__draw_order: list[__DrawnInOrderThing] = []


def add_thing(thing: __DrawnInOrderThing):
    __draw_order.append(thing)
    reorder()


def reorder():
    __draw_order.sort(key=lambda t: t.apparent_depth, reverse=True)


def get_order():
    return __draw_order


def remove_thing(thing: __DrawnInOrderThing):
    __draw_order.remove(thing)


class DrawnInOrder:
    """
    Anything with a depth that requires being drawn in order.
    In addition to a depth value (their actual z-axis position), they hold an apparent depth.
    The apparent depth is their depth in the repeating space, and their drawing order (descending).
    """

    def __init__(self, depth: float):
        self.depth = depth

        add_thing(self)

    @property
    def apparent_depth(self) -> float:
        player = getattr(director.scene, 'player', None)

        if player is None or player is self:
            return 1

        return (player.apparent_depth + (self.depth - player.depth)) % 6


def scale_factor(z) -> float:
    """
    Return the scaling factor for an image with apparent depth z
    """
    return (0.02 * ((z - 6) * (z - 6))) + 0.5


def transparency_factor(z) -> float:
    """
    Return the transparency degree for an image with apparent depth z
    """
    if z < 1:
        return 1 / (1 + (e ** (-9 * (z - 0.5))))
    return (-0.07 * ((z - 1) ** 2)) + 1
