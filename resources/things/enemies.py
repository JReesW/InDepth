from mothic import Rect, image, debug, director
from resources.things.enemy import Enemy
from scripts import DrawnInOrder
from scripts.lissajous import lissajous

class Patrol(Enemy):
    def __init__(self, pos, depth, tick):
        Enemy.__init__(self,
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
    
        self.attackTimer = 0

    def update(self):
        Enemy.update(self)

        self.attackTimer += 1
        if (self.attackTimer > 60):
            director.scene.bullet_manager.shoot(Rect(self.rect.centerx, self.rect.centery, 10, 5), (-20, 0), 600, self.depth, self.team, self.damage)
            self.attackTimer = 0

        # self.pos = lissajous(self.anchor, 100, 400, 2, 3, self.tick, 600)
        # self.tick = (self.tick + 1) % 600

        # if self.pos[0] <= 0:
        #     self.speed = 5
        # elif self.pos[1] >= 1920:
        #     self.speed = -5
        # x, y = self.pos
        # x += self.speed
        # self.pos = (x, y)

class Satellite(Enemy):
    def __init__(self, pos, depth):
        super().__init__(
            health=30,
            damage=2,
            score=250,
            rect=Rect(*pos, 100, 100),
            depth=depth
        )
        self.base_image = image.load_image("satellite_wings_1")
        self.rect.size = self.image.get_rect().size
        self.attackTimer = 0

    def update(self):
        self.attackTimer += 1
        if (self.attackTimer > 60):
            director.scene.bullet_manager.shoot(Rect(self.rect.centerx, self.rect.centery, 10, 5), (-20, 0), 600, self.team, self.damage)
            self.attackTimer = 0

        if self.rect.left <= 0:
            self.speed = 5
        elif self.rect.left >= 1920:
            self.speed = -5
        self.rect.left += self.speed

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
