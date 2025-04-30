"""
Basic debug screen
"""


from pygame import Surface, Rect
import pygame.freetype
from typing import Any

from mothic.visuals import colors


if not pygame.freetype.get_init():
    pygame.freetype.init()

font = pygame.freetype.SysFont("Arial", 18)

__debugs = {}
__active = False


def debug(name: str, value: Any):
    __debugs[name] = value


def enable():
    global __active
    __active = True


def disable():
    global __active, __debugs
    __active = False
    __debugs = {}


def is_active():
    return __active


def render(surface: Surface):
    if __debugs:
        names = [font.render(name, colors.white) for name in __debugs.keys()]
        values = [font.render(str(value), colors.white) for value in __debugs.values()]

        widest_name = max(names, key=lambda n: n[1].width)[1]
        widest_value = max(values, key=lambda v: v[1].width)[1]

        total_width = widest_name.width + widest_value.width + 26
        total_height = sum(r.height for _, r in names) + 20

        surf = Surface((total_width, total_height), pygame.SRCALPHA)
        surf.fill((0, 0, 0, 120))
        pygame.draw.line(surf, (255, 255, 255), (widest_name.width + 12, 10), (widest_name.width + 12, total_height - 10))

        for y, ((s1, r1), (s2, r2)) in enumerate(zip(names, values)):
            r1.right = widest_name.width + 8
            r2.left = widest_name.width + 18
            r1.top = r2.top = (y * widest_name.height) + 10
            surf.blit(s1, r1)
            surf.blit(s2, r2)

        left = surface.get_width() - surf.get_width()
        rect = Rect(left, 0, *surf.get_size())
        rect.bottom = surface.get_height()
        surface.blit(surf, rect)
