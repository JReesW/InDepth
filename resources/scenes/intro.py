from mothic import Surface, display, Scene, colors, director, image, etypes, keys
from mothic.visuals import text


class IntroScene(Scene):
    def __init__(self):
        super().__init__()

        display_rect = display.get_surface().get_rect()
        self.centerx = display_rect.centerx
        self.centery = display_rect.centery

        self.llp = image.load_image("lowlandpalms")

        self.llp_alpha = 0

        self.timer = 0
        self.phase = 0

    def handle_events(self, events):
        for event in events:
            if event.type == etypes.KEYDOWN:
                if event.key in [keys.K_SPACE, keys.K_RETURN]:
                    director.set_scene("MainMenuScene")

    def update(self):
        self.timer += 1

        if self.timer > 60 and self.phase == 0:
            self.timer = 0
            self.phase = 1
        if self.timer > 255 and self.phase == 1:
            self.timer = 0
            self.phase = 2
        if self.timer > 255 and self.phase == 2:
            director.set_scene("MainMenuScene")
        
        self.cake.update()

    def render(self, surface: Surface):
        surface.fill(colors.black)
        if self.phase == 0:
            surface.fill(colors.black)
        elif self.phase == 1:
            rect = self.llp.get_rect()
            rect.center = (self.centerx, self.centery)
            self.llp_alpha += 1

            surf, textRect = text.render("Presents", colors.white, "impact", 50)
            textRect.center = surface.get_rect().centerx, rect.bottom + 100

            self.llp.set_alpha(self.llp_alpha)
            surf.set_alpha(self.llp_alpha)

            surface.blit(self.llp, rect)
            surface.blit(surf, textRect)
        elif self.phase == 2:
            rect = self.llp.get_rect()
            rect.center = (self.centerx, self.centery)
            self.llp_alpha -= 1

            surf, textRect = text.render("Presents", colors.white, "impact", 50)
            textRect.center = surface.get_rect().centerx, rect.bottom + 100

            self.llp.set_alpha(self.llp_alpha)
            surf.set_alpha(self.llp_alpha)

            surface.blit(self.llp, rect)
            surface.blit(surf, textRect)