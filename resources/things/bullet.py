from mothic import Rect, Surface, Thing


class Bullet(Thing):
    def __init__(self, rect : Rect, velocity, lifespan):
        super().__init__(
            rect=rect,
            default_update_layer=1,
            default_render_layer=9
            )
        self.velocity = velocity
        self.lifespan = lifespan
        self.dead = False
    
    def update(self):
        self.lifespan -= 1
        if (self.lifespan < 0):
            self.dead = True
        
        self.rect.left += self.velocity[0]
        self.rect.top += self.velocity[1]
