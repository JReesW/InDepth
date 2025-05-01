import pygame
from pygame import Surface, display

from mothic import Scene, colors, director
from mothic.visuals import text

from ui.button import Button


class MainMenuScene(Scene):
    def __init__(self):
        super().__init__()

        centerx = display.get_surface().get_rect().centerx

        self.cake.insert_many([
            Button('Start', (200, 60), center=(centerx, 400), color=colors.teal).set_func(director.set_scene, "GameScene"),
            Button('Quit', (200, 60), center=(centerx, 500), color=colors.teal).set_func(pygame.quit),
        ])

    def handle_events(self, events):
        self.cake.handle_events(events)

    def update(self):
        self.cake.update()

    def render(self, surface: Surface):
        surface.fill(colors.teal)

        surf, rect = text.render("InDepth", colors.black, "impact", 48)
        rect.center = surface.get_rect().centerx, 150
        surface.blit(surf, rect)

        self.cake.render(surface)