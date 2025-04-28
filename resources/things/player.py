from mothic import Thing, Rect, director, keys, image, etypes, debug
import pygame
from scripts import DrawnInOrder


class Player(Thing, DrawnInOrder):
    def __init__(self):
        Thing.__init__(self,
            rect=Rect(250, 250, 50, 50),
            default_render_layer=10
        )
        DrawnInOrder.__init__(self, 1)

        self.maxLives = 3
        self.lives = self.maxLives
        self.maxHealth = 15
        self.health = self.maxHealth

        self.image = image.load_image("testplayer")
        self.rect.size = self.image.get_rect().size

        self.bullet_manager = director.create_thing("BulletManager")
        director.scene.cake.insert(self.bullet_manager)

        self.firing_cooldown = 10

        self.team = 1

    def handle_events(self, events):
        pressed = pygame.key.get_pressed()

        if pressed[keys.K_w]:
            self.rect.top -= 10
        if pressed[keys.K_s]:
            self.rect.top += 10
        if pressed[keys.K_a]:
            self.rect.left -= 10
        if pressed[keys.K_d]:
            self.rect.left += 10

        if pressed[keys.K_r]:
            self.depth += 0.03
        if pressed[keys.K_f]:
            self.depth -= 0.03

        for event in events:
            if event.type == etypes.KEYDOWN:
                if event.key == keys.K_k:
                    self.health -= 1
                if event.key == keys.K_l:
                    self.health = min(self.health + 1, self.maxHealth)

        if pressed[keys.K_SPACE]:
            if self.firing_cooldown == 0:
                self.firing_cooldown = 10
                self.bullet_manager.shoot(self.rect.center, self.apparent_depth, self.team)
    
    def update(self):
        debug.debug('player depth', f"{self.depth:.2f}")
        debug.debug('player app. depth', f"{self.apparent_depth:.2f}")
        if self.firing_cooldown > 0:
            self.firing_cooldown -= 1
