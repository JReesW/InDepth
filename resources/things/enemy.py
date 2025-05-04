from mothic import Thing, director, Surface, Rect, colors
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
        self.dead = False
        self.score = score
        self.speed = 5
        self.base_image = None
        self.team = 2
        self.shielded = False
        self.shield_timer_max = 600
        self.shield_timer = 0
        self.shield_radius = 3

    def update(self):
        self.apply_image_rect_effects()

        if self.collide_depth(director.scene.player.apparent_depth):
            indicator = Surface(self.rect.size).convert_alpha()
            indicator.fill(colors.white)
            indicator.set_alpha(100)
            indicator.fill(colors.transparent, Rect(5, 5, self.rect.w - 10, self.rect.h - 10))
            indicator.fill(colors.transparent, Rect(20, 0, self.rect.w - 40, 5))
            indicator.fill(colors.transparent, Rect(20, self.rect.h - 5, self.rect.w - 40, 5))
            indicator.fill(colors.transparent, Rect(0, 20, 5, self.rect.h - 40))
            indicator.fill(colors.transparent, Rect(self.rect.w - 5, 20, 5, self.rect.h - 40))
            self.image.blit(indicator)        
