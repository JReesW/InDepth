from mothic import Rect, image, director
from resources.things.enemy import Enemy
from pygame import Vector2
from scripts.draw_order import scale_factor

from random import random, randint


class Patrol(Enemy):
    def __init__(self, pos, depth, entry_movements, repeat_movements):
        Enemy.__init__(
            self,
            health=5,
            damage=1,
            score=50,
            rect=Rect(*pos, 100, 100),
            depth=depth,
            entry_movements=entry_movements,
            repeat_movements=repeat_movements
        )
        self.base_image = image.load_image("patrol")
        self.rect.size = self.image.get_rect().size
    
        self.cooldown = 0
        self.cooldown_reset = 40

        self.shotspeed = 20

    def move(self):
        super().move()

    def attack(self):
        if self.cooldown == 0:
            if randint(1, 30) == 1:
                target = Vector2(director.scene.player.pos)
                direction = (Vector2(self.pos) - target).normalize() * -self.shotspeed

                t, l = self.rect.topleft
                director.scene.bullet_manager.shoot(Rect(t + 17, l + 38, 10, 5), direction, 120, self.depth, self.team, self.damage)
                director.scene.bullet_manager.shoot(Rect(t + 11, l + 44, 10, 5), direction, 120, self.depth, self.team, self.damage)
                self.cooldown = self.cooldown_reset
                director.scene.audio_manager.play_sound('patrol_shot')
        else:
            self.cooldown -= 1


class Satellite(Enemy):
    def __init__(self, pos, depth, entry_movements, repeat_movements):
        super().__init__(
            health=30,
            damage=2,
            score=250,
            rect=Rect(*pos, 100, 100),
            depth=depth,
            entry_movements=entry_movements,
            repeat_movements=repeat_movements
        )
        self.base_image = image.load_image("satellite_wings_2")
        self.rect.size = self.image.get_rect().size

        self.cooldown = 0
        self.cooldown_reset = 40

        self.shotspeed = 12
        self.unfold_timer = 10
        self.unfold_flag = 0

    def move(self):
        super().move()

        if self.emp == 1 and self.unfold_flag == 0:
            self.base_image = image.load_image("satellite_wings_1")
            self.unfold_flag = 1
        elif self.unfold_flag == 1:
            if self.unfold_timer <= 0:
                self.base_image = image.load_image("satellite")
                self.unfold_flag = 2
            self.unfold_timer -= 1

    def attack(self):
        if self.cooldown <= 0 and self.unfold_flag > 0:
            if randint(1, 30) == 1 or self.unfold_flag == 1:
                target = Vector2(director.scene.player.pos)
                direction = (Vector2(self.pos) - target).normalize() * -self.shotspeed
                directions = [direction.rotate(-7), direction, direction.rotate(7)]

                l, t = self.rect.left + 6, self.rect.top + self.base_image.get_height() // 2
                for d in directions:
                    director.scene.bullet_manager.shoot(Rect(l, t, 10, 5), d, 180, self.depth, self.team, self.damage)
                self.cooldown = self.cooldown_reset
                director.scene.audio_manager.play_sound('satellite_shot')
        else:
            self.cooldown -= 1


class Kamikaze(Enemy):
    def __init__(self, pos, depth, entry_movements, repeat_movements):
        super().__init__(
            health=3,
            damage=10,
            score=150,
            rect=Rect(*pos, 100, 100),
            depth=depth,
            entry_movements=entry_movements,
            repeat_movements=repeat_movements
        )
        self.base_image = image.load_image("kamikaze_w")
        self.rect.size = self.image.get_rect().size


class Longshot(Enemy):
    def __init__(self, pos, depth, entry_movements, repeat_movements):
        super().__init__(
            health=50,
            damage=3,
            score=400,
            rect=Rect(*pos, 100, 100),
            depth=depth,
            entry_movements=entry_movements,
            repeat_movements=repeat_movements
        )
        self.base_image = image.load_image("longshot")
        self.rect.size = self.image.get_rect().size

        self.shotspeed = 16

        self.cooldown = 0
        self.bullets_shot = 0
        self.firing = False
        self.depth_velocity = 0

    # def move(self):
    #     super().move()
    #
    #     a_d = self.apparent_depth
    #     closer_apparent = 1 if a_d < 3.5 else 6
    #     fake_target = self.depth + (closer_apparent - a_d)
    #     force = (fake_target - self.depth) * 0.07
    #     self.depth_velocity = (self.depth_velocity + force) * 0.95
    #     self.depth += self.depth_velocity

    def attack(self):
        if not self.entry_busy:
            if self.firing:
                if self.bullets_shot >= 24:
                    self.firing = False
                    self.cooldown = 240
                    self.bullets_shot = 0
                elif self.cooldown <= 0:
                    target = Vector2(director.scene.player.pos)
                    direction = (target - Vector2(self.pos)).normalize() * self.shotspeed
                    direction = direction.rotate(random() * 10 - 5)

                    l, t = self.rect.left + 54, self.rect.top + 27
                    director.scene.bullet_manager.shoot(Rect(l, t, 10, 5), direction, 180, self.depth, self.team, self.damage)
                    director.scene.audio_manager.play_sound('gunship_shot')
                    self.cooldown = 10
                    self.bullets_shot += 1
                else:
                    self.cooldown -= 1
            else:
                if self.cooldown <= 0:
                    self.firing = True
                else:
                    self.cooldown -= 1

class Scute(Enemy):
    def __init__(self, pos, depth, entry_movements, repeat_movements):
        super().__init__(
            health=20,
            damage=0,
            score=300,
            rect=Rect(*pos, 100, 100),
            depth=depth,
            entry_movements=entry_movements,
            repeat_movements=repeat_movements
        )


class Gunship(Enemy):
    def __init__(self):
        super().__init__()
