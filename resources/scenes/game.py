from mothic import Scene, Surface, colors, director, etypes, draw
from mothic.visuals import text

from resources.things.parallax import Parallax
from resources.things.powerup import *


class GameScene(Scene):
    def init(self):

        self.player = director.create_thing("Player")
        self.cake.insert(
            self.player
        )

        self.player_ui = director.create_thing("UI")
        self.cake.insert(self.player_ui)

        self.parallax = Parallax()
        director.state['parallax'] = self.parallax

        self.powerupManager = director.create_thing("PowerupManager")
        self.bullet_manager = director.create_thing("BulletManager")
        self.enemy_manager = director.create_thing("EnemyManager")

        self.enemy_manager.spawn("Patrol", (0, 340))
        self.enemy_manager.spawn("Satellite", (0, 640))
        self.enemy_manager.spawn("Longshot", (0, 440))
        self.enemy_manager.spawn("Kamikaze", (0, 540))

        self.powerupManager.spawn(HEALTH_KIT, (500, 740))

    def handle_events(self, events):
        self.cake.handle_events(events)

    def update(self):
        self.cake.update()
        self.parallax.update()
        self.powerupManager.update()
        self.bullet_manager.update()
        self.enemy_manager.update()

    def render(self, surface: Surface):
        surface.fill((150, 150, 150))

        self.parallax.render(surface)

        surf, rect = text.render(f"depth: {self.parallax.depth:.2f}", colors.black, 'arial', 14)
        rect.topleft = (20, 20)
        surface.blit(surf, rect)

        self.powerupManager.render(surface)

        self.cake.render(surface)
