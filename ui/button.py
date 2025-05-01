import pygame
from pygame import Rect

from mothic import Thing, draw, colors
from mothic.visuals import text


class Button(Thing):
    def __init__(self, label, size, center, color, border=colors.black):
        super().__init__(
            rect=Rect(0, 0, *size),
            default_render_layer=99
        )

        self.rect.center = center

        # self.image = Surface.convert_alpha(self.image)
        self.image.fill(color)
        draw.rect(self.image, border, (0, 0, *self.rect.size), 3, 5)

        surf, rect = text.render(label, colors.black, "impact", 28)
        rect.center = self.rect.width / 2, self.rect.height / 2
        self.image.blit(surf, rect)

        self.func = None
        self.args = []

    def set_func(self, func, *args):
        self.func = func
        self.args = args
        return self

    def handle_events(self, events, **kwargs):
        mouse = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(*mouse):
                    self.func(*self.args)
