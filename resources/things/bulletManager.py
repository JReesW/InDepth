from mothic import Thing, image, Rect
from resources.things.bullet import Bullet

class BulletManager():
    def __init__(self):
        self.bullets : list[Bullet] = []

    def update(self):
        deadBullets = []
        for bulletIndex in range(len(self.bullets)):
            bullet = self.bullets[bulletIndex]
            bullet.update()
            if (not bullet.alive):
                deadBullets.append(bulletIndex)
        for bulletIndex in deadBullets:
            self.bullets.pop(bulletIndex)
    
    def render(self, surface):
        for bullet in self.bullets:
            bullet.render(surface)

bulletManager = BulletManager()