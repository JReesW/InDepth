from mothic import Scene, Surface, colors, director
from mothic.visuals import text

from resources.things.player import Player
from resources.things.parallax import Parallax


class GameScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cake.insert(
            Player()
        )

        self.parallax = Parallax()
        director.state['parallax'] = self.parallax
    
    def handle_events(self, events):
        self.cake.handle_events(events)

    def update(self):
        self.parallax.update()

    def render(self, surface: Surface):
        surface.fill(colors.gainsboro)

        self.parallax.render(surface)

        surf, rect = text.render(f"depth: {self.parallax.depth:.2f}", colors.black, 'arial', 14)
        rect.topleft = (20, 20)
        surface.blit(surf, rect)

        self.cake.render(surface)
