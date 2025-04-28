from mothic import Rect, image, debug
from resources.things.enemy import Enemy
from scripts import DrawnInOrder
from scripts.lissajous import lissajous


class Patrol(Enemy, DrawnInOrder):
    def __init__(self, pos, depth, tick):
        Enemy.__init__(self,
            health=5,
            damage=1,
            score=50,
            rect=Rect(*pos, 100, 100)
        )
        DrawnInOrder.__init__(self, depth)
        self.image = image.load_image("patrol")
        self.rect.size = self.image.get_rect().size
        self.anchor = pos

        self.tick = tick

    def update(self):
        Enemy.update(self)

        debug.debug('enemy depth', f"{self.depth:.2f}")
        debug.debug('enemy app. depth', f"{self.apparent_depth:.2f}")

        self.rect.center = lissajous(self.anchor, 100, 400, 2, 3, self.tick, 600)
        self.tick = (self.tick + 1) % 600


class Satellite(Enemy):
    def __init__(self, pos):
        super().__init__(
            health=30,
            damage=2,
            score=250,
            rect=Rect(*pos, 100, 100)
        )
        self.image = image.load_image("satellite_wings_1")
        self.rect.size = self.image.get_rect().size



class Kamikaze(Enemy):
    def __init__(self, pos):
        super().__init__(
            health=3,
            damage=10,
            score=150,
            rect=Rect(*pos, 100, 100)
        )
        self.image = image.load_image("kamikaze_w")
        self.rect.size = self.image.get_rect().size


class Longshot(Enemy):
    def __init__(self, pos):
        super().__init__(
            health=45,
            damage=3,
            score=400,
            rect=Rect(*pos, 100, 100)
        )
        self.image = image.load_image("longshot")
        self.rect.size = self.image.get_rect().size


class Scute(Enemy):
    def __init__(self, pos):
        super().__init__(
            health=20,
            damage=0,
            score=300,
            rect=Rect(*pos, 100, 100)
        )
