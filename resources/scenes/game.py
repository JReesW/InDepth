from mothic import Scene, keys
from pygame import SRCALPHA

from scripts.draw_order import get_order, reorder, clear_order
from scripts.levels import levels
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

        self.level = levels[director.state['level']]()
        self.level_tint = Surface((1920, 1080), SRCALPHA)
        self.level_tint.fill(self.level.tint)

        self.background = image.load_image(self.level.background)
        self.background_offset = 0

        self.player_ui = director.create_thing("UI")
        self.cake.insert(self.player_ui)
        self.depth_measure = director.create_thing("DepthMeasure")
        self.cake.insert(self.depth_measure)

        self.powerupManager = director.create_thing("PowerupManager")
        self.bullet_manager = director.create_thing("BulletManager")
        self.enemy_manager = director.create_thing("EnemyManager")

        # self.enemy_manager.spawn(*longshot)

        self.grace = 120
        self.done = False

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
        self.background_offset = (self.background_offset + 1) % (1920 * 3)

        if self.grace <= 0 and not self.done:
            self.spawn()
            self.level.update()
        else:
            self.grace -= 1

    def render(self, surface: Surface):
        surface.fill((100, 100, 100))

        surface.blit(self.background, (-self.background_offset / 3, 1080 - self.background.get_height()))
        surface.blit(self.background, (-self.background_offset / 3 + 1920, 1080 - self.background.get_height()))

        # This instead of rendering the cake
        for thing in get_order():
            surface.blit(thing.image, thing.rect)
        
        surface.blit(self.level_tint)

        surface.blit(self.player_ui.image, self.player_ui.rect)
        surface.blit(self.depth_measure.image, self.depth_measure.rect)
        # self.cake.render(surface)

    def spawn(self):
        seq = self.level.sequences[self.level.pointer]
        subseq = seq.subsequences[seq.pointer]

        if not subseq.used:
            for enemy in seq.subsequences[seq.pointer].enemies:
                e = self.enemy_manager.spawn(*enemy)
                seq.subsequences[seq.pointer].e_objs.append(e)
                seq.subsequences[seq.pointer].used = True
        else:
            if subseq.done() and seq.pointer < len(seq.subsequences) - 1:
                seq.pointer += 1
            elif seq.done() and self.level.pointer < len(self.level.sequences):
                self.level.pointer += 1

                if self.level.pointer >= len(self.level.sequences):
                    self.done = True
                    director.set_scene("LevelClearOverlay", self)

