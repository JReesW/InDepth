from mothic import Rect, Surface, colors
from resources.things.bullet import Bullet
from resources.things.gun import Gun

class PistolBullet(Bullet):
    def __init__(self, rect : Rect, velocity, lifespan):
        surface = Surface(rect.size)
        super().__init__(rect, velocity, lifespan, surface)
    
    def update(self):
        self.lifespan -= 1
        if (self.lifespan < 0):
            self.alive = False
            return None
        
        self.rect.left += self.velocity[0]
        self.rect.top += self.velocity[1]

class Pistol(Gun):
    def __init__(self):
        super().__init__()
    
    def shoot(self, pos, dir):
        bullet = PistolBullet(Rect(pos[0], pos[1], 10, 5), (dir * 3, 0), 10 * 60)
        super().shoot(bullet)