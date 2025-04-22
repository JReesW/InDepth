from mothic import Rect, Surface

class Bullet():
    def __init__(self, rect : Rect, velocity, lifespan, surface):
        self.rect = rect
        self.velocity = velocity
        self.lifespan = lifespan
        self.alive = True
        self.surface = surface
    
    def update(self):
        pass

    def render(self, surface : Surface):
        surface.blit(self.surface, self.rect)