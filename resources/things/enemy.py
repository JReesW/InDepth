from mothic import Thing, Rect, image as Image
from pygame import transform, Vector2

from scripts.draw_order import DrawnInOrder, scale_factor, transparency_factor


class Enemy(Thing, DrawnInOrder):
    def __init__(self, health, damage, score, rect, depth):
        Thing.__init__(
            self,
            rect=rect,
            default_update_layer=2,
            default_render_layer=9
        )
        DrawnInOrder.__init__(self, depth)
        self.pos = self.rect.center
        self.health = health
        self.damage = damage
        self.score = score
        self.speed = 5
        self.base_image = None
        self.team = 2

    def update(self):
        self.image = transform.scale_by(self.base_image, scale_factor(self.apparent_depth))

        x, y = self.pos
        vec = Vector2(x - 960, y - 540) * scale_factor(self.apparent_depth)
        self.rect.center = vec.x + 960, vec.y + 540

        self.image.set_alpha(transparency_factor(self.apparent_depth) * 255)
