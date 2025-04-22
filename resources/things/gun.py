from mothic import Thing
from resources.things.bullet import Bullet
from resources.things.bulletManager import bulletManager

class Gun(Thing):
    def __init__(self):
        super().__init__()

    def shoot(self, bullet : Bullet):
        bulletManager.bullets.append(bullet)