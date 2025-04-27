from mothic import Thing, image, Rect, director
from mothic.util.functions import split


class BulletManager(Thing):
    def __init__(self):
        super().__init__(
            rect=Rect(0, 0, 0, 0),
            default_update_layer=2
        )
        self.bullets = []

    def shoot(self, rect, velocity, lifetime = 600, team = 0, damage = 1):
        bullet = director.create_thing("Bullet", rect, velocity, lifetime, team, damage)
        self.bullets.append(bullet)
        director.scene.cake.insert(bullet)

    def update(self):
        dead, self.bullets = split(self.bullets, lambda b: b.dead)

        for d in dead:
            director.scene.cake.remove(d)
