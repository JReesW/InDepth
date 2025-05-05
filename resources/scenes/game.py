from mothic import Scene, keys
from pygame import SRCALPHA

from scripts.draw_order import get_order, reorder, clear_order
from scripts.levels import enemy, satellite
from resources.things.powerup import *


class GameScene(Scene):
    def init(self):
        clear_order()

        self.player = director.create_thing("Player")
        self.cake.insert(
            self.player
        )

        sounds = ["player_damaged", "player_shot", "patrol_shot", "gunship_shot", "explosion", "satellite_shot"]
        for sound in sounds:
            self.audio_manager.add_sound(sound, sound + '.wav')

        self.level_tint = Surface((1920, 1080), SRCALPHA)
        self.level_tint.fill((0, 0, 255, 25))

        self.player_ui = director.create_thing("UI")
        self.cake.insert(self.player_ui)
        self.depth_measure = director.create_thing("DepthMeasure")
        self.cake.insert(self.depth_measure)

        self.powerupManager = director.create_thing("PowerupManager")
        self.bullet_manager = director.create_thing("BulletManager")
        self.enemy_manager = director.create_thing("EnemyManager")

        self.enemy_manager.spawn(*satellite)
        # self.enemy_manager.spawn("Patrol", (1400, 640), 0, 0)
        # self.enemy_manager.spawn("Patrol", (1600, 340), 2, 0)
        # self.enemy_manager.spawn("Patrol", (1500, 440), 3, 0)
        # self.enemy_manager.spawn("Patrol", (1100, 540), 4, 0)
        # self.enemy_manager.spawn("Satellite", (1700, 440), 1)
        # self.enemy_manager.spawn("Longshot", (0, 440))
        # self.enemy_manager.spawn("Kamikaze", (0, 540))

        # self.powerupManager.spawn(SHIELD, (500, 340), 1)
        # self.powerupManager.spawn(TRIPLE_SHOT, (500, 440), 1)
        # self.powerupManager.spawn(GATLING_GUN, (500, 540), 1)
        # self.powerupManager.spawn(HOLLOW_POINT, (500, 640), 1)

    def handle_events(self, events):
        self.cake.handle_events(events)

        pressed = keys.get_pressed()
        if pressed[keys.K_y]:
            for enemy in self.enemy_manager.enemies:
                enemy.depth += 0.03
        if pressed[keys.K_h]:
            for enemy in self.enemy_manager.enemies:
                enemy.depth -= 0.03

        if pressed[keys.K_ESCAPE]:
            director.set_scene("PauseOverlay", self)

    def update(self):
        self.cake.update()
        self.powerupManager.update()
        self.bullet_manager.update()
        self.enemy_manager.update()
        reorder()

    def render(self, surface: Surface):
        surface.fill((100, 100, 100))

        # This instead of rendering the cake
        for thing in get_order():
            surface.blit(thing.image, thing.rect)
        
        surface.blit(self.level_tint)

        surface.blit(self.player_ui.image, self.player_ui.rect)
        surface.blit(self.depth_measure.image, self.depth_measure.rect)
        # self.cake.render(surface)
        
