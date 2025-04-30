from mothic import Thing, Rect, director, Surface
from mothic.util.functions import split
from resources.things.powerup import *

class PowerupManager(Thing):
    def __init__(self, image = None, rect = None, *, default_event_layer = 0, default_update_layer = 2, default_render_layer = 10):
        super().__init__(
            rect=Rect(0, 0, 0, 0),
            default_update_layer=1
        )
        self.powerups = []

    def spawn(self, powerupType: int, pos: tuple[float, float]):
        self.powerups.append(Powerup(powerupType, pos))

    def update(self):
        for powerup in self.powerups:
            powerup.update()

        collided, self.powerups = split(self.powerups, lambda p: p.collidePlayer())

        for powerup in collided:
            powerup.apply()
    
    def render(self, surface: Surface):
        for p in self.powerups:
            p.render(surface)