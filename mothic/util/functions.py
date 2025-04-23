"""
Miscellaneous functions
"""

import pygame
from mothic.maths.numbers import remap
from mothic.util.exceptions import Quit

from typing import Callable


def quit():
    raise Quit


def convert_mouse_click_events(events, old_size, new_size):
    """
    Convert the positions stored inside mouse click events from one screensize to another
    """
    for event in events:
        if event.type in (pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
            px, py = event.pos
            ox, oy = old_size
            nx, ny = new_size
            rx = int(remap(px, 0, ox, 0, nx))
            ry = int(remap(py, 0, oy, 0, ny))
            event.pos = (rx, ry)


def split(ls: list, predicate: Callable[[], bool]) -> tuple[list, list]:
    """
    Split a list according to a given predicate into a sublist of items that follow the predicate and a sublist of items that don't 
    """
    yes, no = [], []
    for n in ls:
        yes.append(n) if predicate(n) else no.append(n)
    return yes, no
