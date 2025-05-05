from mothic import Scene, director, Surface, colors, Rect, draw
from mothic.visuals import text
from math import sin, pi


titles = {
    1: "BIOSPHERE",
    2: "TECHNOSPHERE",
    3: "NEXOSPHERE"
}


def bar_width(n):
    return sin((n * pi) / 300) * 400


class LevelIntroScene(Scene):
    def __init__(self, level):
        super().__init__()

        self.level = level
        director.state['level'] = self.level

        self.surface = Surface((1920, 1080)).convert_alpha()
        self.cover = Surface((1920, 1080)).convert_alpha()

        surf, rect = text.render(f"Level {self.level}", colors.white, "consolamono-bold", 120)
        rect.center = 960, 400
        self.surface.blit(surf, rect)

        surf, rect = text.render(f"{titles[self.level]}", colors.white, "consolamono-bold", 48)
        rect.center = 960, 600
        self.surface.blit(surf, rect)

        self.timer = 300
        self.alpha = 240

    def update(self):
        self.timer -= 1

        if self.timer > 240:
            self.alpha -= 4
        if self.timer <= 60:
            self.alpha += 4
        self.cover.set_alpha(self.alpha)

        if self.timer == 0:
            director.set_scene("GameScene")

    def render(self, surface):
        surface.blit(self.surface)
        w = bar_width(self.timer)
        cx = 960
        draw.rect(surface, colors.white, Rect(cx - w, 500, w + w, 10))
        surface.blit(self.cover)
