from mothic import Scene, Surface, colors, director, etypes, draw
from mothic.visuals import text

from resources.things.parallax import Parallax


class GameScene(Scene):
    def init(self):
        self.score = 0

        self.player = director.create_thing("Player")
        self.cake.insert(
            self.player
        )

        self.player_ui = director.create_thing("UI")
        self.cake.insert(self.player_ui)

        self.parallax = Parallax()
        director.state['parallax'] = self.parallax

        self.bullet_manager = director.create_thing("BulletManager")
        self.enemy_manager = director.create_thing("EnemyManager")

        self.enemy_manager.spawn("Patrol", (0, 540))
        self.enemy_manager.spawn("Longshot", (0, 640))

    def handle_events(self, events):
        self.cake.handle_events(events)

    def update(self):
        self.cake.update()
        self.parallax.update()
        self.bullet_manager.update()
        self.enemy_manager.update()

    def render(self, surface: Surface):
        surface.fill(colors.gainsboro)

        self.parallax.render(surface)

        surf, rect = text.render(f"depth: {self.parallax.depth:.2f}", colors.black, 'arial', 14)
        rect.topleft = (20, 20)
        surface.blit(surf, rect)

        self.cake.render(surface)
