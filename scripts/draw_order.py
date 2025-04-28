from typing import Union
from mothic import director, Thing


__DrawnInOrderThing = Union[Thing, "DrawnInOrder"]
__draw_order: list[__DrawnInOrderThing] = []


def add_thing(thing: __DrawnInOrderThing):
    __draw_order.append(thing)


def reorder():
    __draw_order.sort(key=lambda t: t.apparent_depth, reverse=True)


class DrawnInOrder:
    def __init__(self, depth: float):
        self.depth = depth

    @property
    def apparent_depth(self) -> float:
        player = getattr(director.scene, 'player', None)

        if player is None or player is self:
            return 1

        return (player.apparent_depth + (self.depth - player.depth)) % 6
