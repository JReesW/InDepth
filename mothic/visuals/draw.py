from pygame import Rect, Surface, surfarray, SRCALPHA
from pygame.draw import aaline, aalines, arc, circle, ellipse, line, lines, polygon, rect
# from pygame.math import lerp

from mothic import colors
from mothic.maths.geometry import lerp

import numpy as np


def bezier(surface: Surface, points: list[tuple[int, int]], steps: int, color: colors.Color = colors.black):
    """
    Draw a bezier curve for the given list of anchor points.
    """
    bezier_points = []
    
    # De Casteljau's Algorithm
    for t in (i / steps for i in range(steps + 1)):
        _points = points[:]

        while len(_points) > 1:
            next_points = []

            for a, b in zip(_points, _points[1:]):
                next_points.append(lerp(a, b, t))
            
            _points = next_points
        
        bezier_points.append(_points[0])
    
    aalines(surface, color, False, bezier_points)


def linear_gradient(surface: Surface, rect: Rect, color1: colors.Color, color2: colors.Color, horizontal: bool = False):
    """
    Adds a linear gradient from color1 to color2 onto the given surface at a given rect.
    """
    if horizontal:
        width, height = rect.size
    else:
        height, width = rect.size
        
    image = np.zeros((height, width, 4), dtype=np.uint8)
    gradient = np.linspace(color1, color2, height, dtype=np.uint8)

    gradient_expanded = gradient[:, np.newaxis, :]
    image[:] = gradient_expanded

    if not horizontal:
        image = image.transpose((1, 0, 2))
    
    rgb = image[:, :, :3]
    alpha = image[:, :, 3]

    _surface = surfarray.make_surface(rgb).convert_alpha()
    surfarray.pixels_alpha(_surface)[:, :] = alpha

    surface.blit(_surface, rect)
