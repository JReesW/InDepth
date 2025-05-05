from mothic import Scene, colors, display, Surface
from mothic.visuals import text


class CreditsScene(Scene):
    def __init__(self):
        super().__init__()

        screen = Surface(display.get_surface().get_size()).convert_alpha()
        screen.fill((180, 180, 180))

        surf, rect = text.render("Credits", colors.white, "consolamono-bold", 120, bold=True)
        rect.center = screen.get_width() / 2, 200
        screen.blit(surf, rect)

    def render(self, surface: Surface):
        surface.fill((180, 180, 180))


