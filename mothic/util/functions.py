"""
Miscellaneous functions
"""

import pygame
from mothic.maths.numbers import remap
from mothic.util.exceptions import Quit


def quit():
    raise Quit


def convert_mouse_click_events(events, old_size, new_size):
    for event in events:
        if event.type in (pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
            px, py = event.pos
            ox, oy = old_size
            nx, ny = new_size
            rx = int(remap(px, 0, ox, 0, nx))
            ry = int(remap(py, 0, oy, 0, ny))
            event.pos = (rx, ry)
