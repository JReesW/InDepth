from mothic import Scene, draw, colors, display, Rect, Surface, director
from mothic.visuals import text
import pygame


class LevelClearOverlay(Scene):
    def __init__(self, scene_below: Scene):
        super().__init__()
        self.scene_below = scene_below

        self.audio_manager.add_sound('level_complete', 'level_complete.wav')
        self.audio_manager.play_sound('level_complete')

        cx, cy = display.get_surface().get_rect().center

        rect = Rect(0, 0, 450, 200)
        rect.center = cx, cy
        self.rect = rect
        self.surface = Surface(rect.size, pygame.SRCALPHA)

        draw.rect(self.surface, (180, 180, 180), Rect(0, 0, *rect.size), border_radius=20)
        draw.rect(self.surface, colors.light_slate_gray, Rect(0, 0, *rect.size), 4, border_radius=20)

        prompt = "Game Complete!" if director.state['level'] == 3 else "Level Complete!"
        s, r = text.render(prompt, colors.white, "consolamono-bold", 48)
        r.center = self.rect.width / 2, self.rect.height / 2
        self.surface.blit(s, r)

        self.timer = 180

    def update(self):
        self.scene_below.background_offset = (self.scene_below.background_offset + 1) % (1920 * 3)

        self.timer -= 1
        if self.timer == 0:
            if director.state['level'] == 3:
                director.set_scene("CreditsScene")
            else:
                director.set_scene("LevelIntroScene", director.state['level'] + 1)

    def render(self, surface: Surface):
        self.scene_below.render(surface)

        surface.blit(self.surface, self.rect)
