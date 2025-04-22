"""
Text rendering module

TODO:
 - Write a function that handles multiline text rendering
 - Standardize how fonts are accessed via names (lowercase, underscores, etc.)
 - Integrate project settings, like font folder path
 - Move font loading to a better place
"""


from pygame import Surface, Rect, freetype
import pygame

from mothic.visuals.colors import Color

import os
from pathlib import Path


if not freetype.get_init():
    freetype.init()


__font_names = {}
__fonts = {}


def find_fonts(path: os.PathLike = "resources/fonts"):
    if os.path.isdir(path):
        # TODO: Add failure detection for missing fonts folder
        for file in os.listdir(path):
            if file.endswith(('.ttf', '.otf')):
                filename = file.split('.')[0].lower().replace(' ', '_')
                __font_names[filename] = path + f"/{file}"
            else:
                raise Exception("At the moment, only TTF and OTF files are supported")
    else:
        print(f'MOTHIC ERR: Given font folder "{path}" does not exist!')


def render(text: str, color: Color, font: str, size: int, bold=False, italic=False) -> tuple[Surface, Rect]:
    font = font.lower().replace(' ', '_')
    if (font, size) not in __fonts:
        if font in __font_names:
            __fonts[(font, size)] = freetype.Font(__font_names[font], size)
        else:
            __fonts[(font, size)] = freetype.SysFont(font, size, bold=bold, italic=italic)

    return __fonts[(font, size)].render(text, color)


# TODO: Replace with Pygame-CE functionalities, which supports multiline rendering
def multiline_render(surface: Surface, pos: (int, int), text: str, color: Color, font: str, size: int, bold=False, italic=False) -> (Surface, Rect):
    if (font, size) not in __fonts:
        __fonts[(font, size)] = freetype.SysFont(font, size, bold=bold, italic=italic)

    f = __fonts[(font, size)]

    # https://stackoverflow.com/a/42015712
    words = [word.split(' ') for word in text.splitlines()]
    space = f.render(' ', (0, 0, 0))[0].get_size()[0]
    print(space)
    max_width, max_height = surface.get_size()
    x, y = pos
    word_height = 0
    for line in words:
        for word in line:
            word_surface, _ = f.render(word, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

    return surface, surface.get_rect()


# def multiline_render(surface: Surface, pos: (int, int), text: str, color: Color, font: str, size: int, bold=False, italic=False) -> (Surface, Rect):
#     if (font, size) not in __fonts:
#         __fonts[(font, size)] = freetype.SysFont(font, size, bold=bold, italic=italic)
#
#     f = __fonts[(font, size)]
#
#     # https://stackoverflow.com/a/42015712
#     words = [word.split(' ') for word in text.splitlines()]
#     space = f.render(' ', (0, 0, 0))[0].get_size()[0]
#     print(space)
#     max_width, max_height = surface.get_size()
#     x, y = pos
#     word_height = 0
#     for line in words:
#         for word in line:
#             word_surface, _ = f.render(word, color)
#             word_width, word_height = word_surface.get_size()
#             if x + word_width >= max_width:
#                 x = pos[0]  # Reset the x.
#                 y += word_height  # Start on new row.
#             surface.blit(word_surface, (x, y))
#             x += word_width + space
#         x = pos[0]  # Reset the x.
#         y += word_height  # Start on new row.
#
#     return surface, surface.get_rect()
