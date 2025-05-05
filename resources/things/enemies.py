from mothic import Rect, image, director
from resources.things.enemy import Enemy
from pygame import Vector2
from scripts import DrawnInOrder
from scripts.lissajous import lissajous

from random import random, randint


class Patrol(Enemy):
    def __init__(self, pos, depth, tick):
        Enemy.__init__(
            self,
            health=5,
            damage=1,
            score=50,
            rect=Rect(*pos, 100, 100),
            depth=depth
        )
        self.base_image = image.load_image("patrol")
        self.rect.size = self.image.get_rect().size
        self.anchor = pos

        self.tick = tick
    
        self.cooldown = 0
        self.cooldown_reset = 40

        self.shotspeed = 20

    def move(self):
        pass
        # self.pos = lissajous(self.anchor, 100, 400, 2, 3, self.tick, 600)
        # self.tick = (self.tick + 1) % 600

        # if self.pos[0] <= 0:
        #     self.speed = 5
        # elif self.pos[1] >= 1920:
        #     self.speed = -5
        # x, y = self.pos
        # x += self.speed
        # self.pos = (x, y)

    def attack(self):
        if self.cooldown == 0:
            if randint(1, 30) == 1:
                target = Vector2(director.scene.player.pos)
                direction = (Vector2(self.pos) - target).normalize() * -self.shotspeed

                director.scene.bullet_manager.shoot(Rect(*self.rect.center, 10, 5), direction, 120, self.depth, self.team, self.damage)
                self.cooldown = self.cooldown_reset
                director.scene.audio_manager.play_sound('patrol_shot')
        else:
            self.cooldown -= 1


class Satellite(Enemy):
    def __init__(self, pos, depth):
        super().__init__(
            health=30,
            damage=2,
            score=250,
            rect=Rect(*pos, 100, 100),
            depth=depth
        )
        self.base_image = image.load_image("satellite")
        self.rect.size = self.image.get_rect().size

        self.cooldown = 0
        self.cooldown_reset = 40

        self.shotspeed = 12

    def move(self):
        pass

    def attack(self):
        if self.cooldown == 0:
            if randint(1, 30) == 1:
                target = Vector2(director.scene.player.pos)
                direction = (Vector2(self.pos) - target).normalize() * -self.shotspeed
                directions = [direction.rotate(-7), direction, direction.rotate(7)]

                for d in directions:
                    director.scene.bullet_manager.shoot(Rect(*self.rect.center, 10, 5), d, 180, self.depth, self.team, self.damage)
                self.cooldown = self.cooldown_reset
                director.scene.audio_manager.play_sound('satellite_shot')
        else:
            self.cooldown -= 1


class Kamikaze(Enemy):
    def __init__(self, pos, depth):
        super().__init__(
            health=3,
            damage=10,
            score=150,
            rect=Rect(*pos, 100, 100),
            depth=depth
        )
        self.base_image = image.load_image("kamikaze_w")
        self.rect.size = self.image.get_rect().size


class Longshot(Enemy):
    def __init__(self, pos, depth):
        super().__init__(
            health=45,
            damage=3,
            score=400,
            rect=Rect(*pos, 100, 100),
            depth=depth
        )
        self.base_image = image.load_image("longshot")
        self.rect.size = self.image.get_rect().size


class Scute(Enemy):
    def __init__(self, pos, depth):
        super().__init__(
            health=20,
            damage=0,
            score=300,
            rect=Rect(*pos, 100, 100),
            depth=depth
        )
