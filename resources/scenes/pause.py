from mothic import Scene, draw, colors, display, Rect, Surface, director
from mothic.visuals import text
import pygame

from ui.button import Button


class PauseOverlay(Scene):
    def __init__(self, scene_below: Scene):
        super().__init__()
        self.scene_below = scene_below

        self.audio_manager.add_sound("pause", "pause.wav")
        self.audio_manager.add_sound("pause_continue", "pause_continue.wav")
        self.audio_manager.play_sound("pause")

        cx, cy = display.get_surface().get_rect().center

        rect = Rect(0, 0, 450, 400)
        rect.center = cx, cy
        self.rect = rect
        self.surface = Surface(rect.size, pygame.SRCALPHA)

        draw.rect(self.surface, (180, 180, 180), Rect(0, 0, *rect.size), border_radius=20)
        draw.rect(self.surface, colors.light_slate_gray, Rect(0, 0, *rect.size), 4, border_radius=20)

        s, r = text.render("Paused", colors.white, "consolamono-bold", 48)
        r.center = self.rect.width / 2, 60
        self.surface.blit(s, r)

        self.cake.insert_many([
            Button("Continue", (250, 60), (cx, cy + 10)).set_func(self.back_to_scene),
            Button("Quit", (250, 60), (cx, cy + 110)).set_func(director.set_scene, "MainMenuScene")
        ])

    def back_to_scene(self):
        self.audio_manager.play_sound("pause_continue")
        self.audio_manager.execute()
        director.give_scene(self.scene_below)

    def handle_events(self, events):
        self.cake.handle_events(events)

    def update(self):
        self.cake.update()

    def render(self, surface: Surface):
        self.scene_below.render(surface)

        surface.blit(self.surface, self.rect)

        self.cake.render(surface)
