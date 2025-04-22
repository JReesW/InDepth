"""
Some UI widgets
"""


import pygame
from pygame import Surface, Rect

from engine import colors, text, debug

from typing import Callable


class Input:
    def __init__(self,
                 rect: Rect,
                 on_change: Callable,
                 border_color: colors.Color = colors.black,
                 selected_color: colors.Color = colors.cyan,
                 invalid_color: colors.Color = colors.red,
                 default_text: str = "",
                 allowed_chars=None,
                 validate: Callable = None):

        self.rect = rect
        self.selected = False
        self.text = default_text
        self.on_change = on_change
        self.allowed_chars = allowed_chars
        self.validate = validate

        self.border_color = border_color
        self.selected_color = selected_color
        self.invalid_color = invalid_color

    def handle_events(self, events):
        mouse = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(*mouse):
                    self.selected = True
                else:
                    self.selected = False
            if self.selected and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif self.allowed_chars is not None and event.unicode in self.allowed_chars:
                    self.text += event.unicode
                self.on_change()

    def render(self, surface: Surface):
        pygame.draw.rect(surface, colors.white, self.rect)
        color = self.invalid_color if not self.validate(self.text) else self.selected_color if self.selected else self.border_color
        pygame.draw.rect(surface, color, self.rect, 3)

        # Text
        surf, rect = text.render(self.text, colors.black, "Arial", 3 * self.rect.height // 5)
        _surf = Surface((self.rect.width - 20, self.rect.height), pygame.SRCALPHA)
        _rect = _surf.get_rect()
        rect.centery, rect.right = _rect.centery, _rect.right
        _surf.blit(surf, rect)
        surface.blit(_surf, Rect(self.rect.left + 10, self.rect.top, *self.rect.size))
