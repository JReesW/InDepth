from mothic import image, Surface, draw, colors, Rect
from mothic.visuals import text
import pygame
import random
from math import floor


SIZE = 60


def f(n):
    return SIZE * (1 - (1 / (2**n)))


class Parallax:
    def __init__(self):
        self.scroll = 0
        self.depth = 0

        self.depths = {i: [] for i in range(5)}
        self.depths[1].append({'scroll': 0})
        self.depths[1].append({'scroll': 300})
        self.depths[1].append({'scroll': 670})
        self.depths[2].append({'scroll': 500})
        self.depths[2].append({'scroll': 1000})
        self.depths[3].append({'scroll': 380})
        self.depths[4].append({'scroll': 750})
        self.depths[0].append({'scroll': 400})
        self.depths[3].append({'scroll': 50})

        self.building_img = image.load_image("building")
        self.building_cooldown = 0
    
    def update(self):
        pass

    def render(self, surface: Surface):
        w, h = surface.get_size()
        ls = [int((5 - n - 1 - round(self.depth, 2)) % 5) for n in range(5)]

        surf, rect = text.render(str(ls), colors.black, 'arial', 14)
        rect.topleft = (20, 40)
        surface.blit(surf, rect)

        for _i in range(5):
            # i = int((5 - _i - 1 - self.depth) % 5)
            i = ls[_i]
            d = f((4 - _i - (self.depth % 1)))
            r = Rect(0, h - d, w, d)
            c = colors.lerp(colors.black, colors.gainsboro, d / SIZE)

            draw.rect(surface, c, r)

        for i in ls[::-1]:
            d = f((4 - i - self.depth) % 5)
            c = colors.lerp(colors.black, colors.gainsboro, d / SIZE)

            for building in self.depths[i]:
                # img = pygame.transform.scale(image.recolor(self.building_img, c), )
                img = image.recolor(self.building_img, c)
                rc = Rect(0, 0, *img.get_size())
                rc.right = w - building['scroll']
                rc.bottom = h - d
                surface.blit(img, rc.topleft)

