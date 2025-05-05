from mothic import Scene, colors, director, Surface
from mothic.visuals import text

from ui.button import Button


FONT = "consolamono-bold"

texts = [
    "JReesW - Project Lead",
    "Game designer, engine development, mechanics development, made sounds",
    "Curyde - Artist",
    "Drew all sprites and backgrounds, developed theme",
    "RDSSDR - Programmer",
    "Mechanics development, special effects, all-round programming",
    "Font: Consola Mono - Bold",
    "Sounds made with: https://sfxr.me/"
]


class CreditsScene(Scene):
    def __init__(self):
        super().__init__()

        self.screen = Surface((1920, 1080)).convert_alpha()
        self.screen.fill((180, 180, 180))

        cx = self.screen.get_width() / 2

        surf, rect = text.render("Credits", colors.white, FONT, 100, bold=True)
        rect.center = cx, 150
        self.screen.blit(surf, rect)

        # JReesW
        surf, rect = text.render(texts[0], colors.white, FONT, 48, bold=True)
        rect.topleft = 150, 300
        self.screen.blit(surf, rect)

        surf, rect = text.render(texts[1], colors.white, FONT, 32)
        rect.topleft = 150, 350
        self.screen.blit(surf, rect)

        # Curyde
        surf, rect = text.render(texts[2], colors.white, FONT, 48, bold=True)
        rect.topleft = 150, 450
        self.screen.blit(surf, rect)

        surf, rect = text.render(texts[3], colors.white, FONT, 32)
        rect.topleft = 150, 500
        self.screen.blit(surf, rect)

        # Lionz
        surf, rect = text.render(texts[4], colors.white, FONT, 48, bold=True)
        rect.topleft = 150, 600
        self.screen.blit(surf, rect)

        surf, rect = text.render(texts[5], colors.white, FONT, 32)
        rect.topleft = 150, 650
        self.screen.blit(surf, rect)

        # Fonts
        surf, rect = text.render(texts[6], colors.white, FONT, 32)
        rect.topleft = 150, 740
        self.screen.blit(surf, rect)

        # Sounds
        surf, rect = text.render(texts[7], colors.white, FONT, 32)
        rect.topleft = 150, 780
        self.screen.blit(surf, rect)

        self.cake.insert(
            Button("Back to Menu", (350, 60), (960, 900)).set_func(director.set_scene, "MainMenuScene")
        )

    def handle_events(self, events):
        self.cake.handle_events(events)

    def update(self):
        self.cake.update()

    def render(self, surface: Surface):
        surface.blit(self.screen)

        self.cake.render(surface)
