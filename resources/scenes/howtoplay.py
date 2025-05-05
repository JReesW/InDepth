from mothic import Scene, colors, director, Surface, draw, Rect, image
from mothic.visuals import text

from ui.button import Button


FONT = "consolamono-bold"

texts = [
    "It's a regular Shoot 'em Up, but \"3D\"",
    "Use WASD to move",
    "Use R and F to change depth, or",
    "for dual-handing, use I and K",
    "Use the space bar to shoot",
    "Hittable enemies are marked"
]


class HowToPlayScene(Scene):
    def __init__(self):
        super().__init__()

        self.screen = Surface((1920, 1080)).convert_alpha()
        self.screen.fill((180, 180, 180))

        cx = self.screen.get_width() / 2

        surf, rect = text.render("How To Play", colors.white, FONT, 100, bold=True)
        rect.center = cx, 150
        self.screen.blit(surf, rect)

        surf, rect = text.render(texts[0], colors.white, FONT, 32, bold=True)
        rect.centerx, rect.top = cx, 300
        self.screen.blit(surf, rect)

        # KEYS
        draw.rect(self.screen, colors.white, Rect(600, 500, 80, 80), 3, 10)
        draw.rect(self.screen, colors.white, Rect(700, 500, 80, 80), 3, 10)
        draw.rect(self.screen, colors.white, Rect(700, 400, 80, 80), 3, 10)
        draw.rect(self.screen, colors.white, Rect(800, 500, 80, 80), 3, 10)

        draw.rect(self.screen, colors.white, Rect(1000, 400, 80, 80), 3, 10)
        draw.rect(self.screen, colors.white, Rect(1000, 500, 80, 80), 3, 10)
        draw.rect(self.screen, colors.white, Rect(1200, 400, 80, 80), 3, 10)
        draw.rect(self.screen, colors.white, Rect(1200, 500, 80, 80), 3, 10)

        draw.rect(self.screen, colors.white, Rect(700, 750, 520, 80), 3, 10)

        # WASD SPACE
        surf, rect = text.render("W", colors.white, FONT, 48, bold=True)
        rect.center = 740, 440
        self.screen.blit(surf, rect)
        surf, rect = text.render("A", colors.white, FONT, 48, bold=True)
        rect.center = 640, 540
        self.screen.blit(surf, rect)
        surf, rect = text.render("S", colors.white, FONT, 48, bold=True)
        rect.center = 740, 540
        self.screen.blit(surf, rect)
        surf, rect = text.render("D", colors.white, FONT, 48, bold=True)
        rect.center = 840, 540
        self.screen.blit(surf, rect)
        surf, rect = text.render("SPACE", colors.white, FONT, 48, bold=True)
        rect.center = 960, 790
        self.screen.blit(surf, rect)

        # RFIK
        surf, rect = text.render("R", colors.white, FONT, 48, bold=True)
        rect.center = 1040, 440
        self.screen.blit(surf, rect)
        surf, rect = text.render("F", colors.white, FONT, 48, bold=True)
        rect.center = 1040, 540
        self.screen.blit(surf, rect)
        surf, rect = text.render("I", colors.white, FONT, 48, bold=True)
        rect.center = 1240, 440
        self.screen.blit(surf, rect)
        surf, rect = text.render("K", colors.white, FONT, 48, bold=True)
        rect.center = 1240, 540
        self.screen.blit(surf, rect)

        # texts
        surf, rect = text.render(texts[1], colors.white, FONT, 32)
        rect.topleft = 600, 600
        self.screen.blit(surf, rect)

        surf, rect = text.render(texts[2], colors.white, FONT, 32)
        rect.topleft = 1000, 600
        self.screen.blit(surf, rect)

        surf, rect = text.render(texts[3], colors.white, FONT, 32)
        rect.topleft = 1000, 650
        self.screen.blit(surf, rect)

        surf, rect = text.render(texts[4], colors.white, FONT, 32)
        rect.center = 960, 860
        self.screen.blit(surf, rect)

        surf, rect = text.render("The depth measure", colors.white, FONT, 32)
        rect.topleft = 150, 860
        self.screen.blit(surf, rect)

        surf, rect = text.render(texts[5], colors.white, FONT, 32)
        rect.topleft = 150, 900
        self.screen.blit(surf, rect)

        surf, rect = text.render("<-- Deeper", colors.white, FONT, 32)
        rect.left, rect.centery = 1300, 440
        self.screen.blit(surf, rect)

        surf, rect = text.render("<-- Less deep", colors.white, FONT, 32)
        rect.left, rect.centery = 1300, 540
        self.screen.blit(surf, rect)

        img = image.load_image("depth_explain")
        self.screen.blit(img, (200, 300))

        self.cake.insert(
            Button("Back to Menu", (350, 60), (960, 1000)).set_func(director.set_scene, "MainMenuScene")
        )

    def handle_events(self, events):
        self.cake.handle_events(events)

    def update(self):
        self.cake.update()

    def render(self, surface: Surface):
        surface.blit(self.screen)

        self.cake.render(surface)
