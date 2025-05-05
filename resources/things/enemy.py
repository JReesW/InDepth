from mothic import Thing, director, Surface, Rect, colors, debug

from scripts.draw_order import DrawnInOrder


class Enemy(Thing, DrawnInOrder):
    def __init__(self, health, damage, score, rect, depth, entry_movements, repeat_movements):
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

        self.entry_movements = entry_movements
        self.emp = 0  # Pointer for which entry movement is in progress
        self.entry_movements[0].set_anchor((*self.pos, self.depth))
        self.entry_busy = True
        self.repeat_movements = repeat_movements
        self.rmp = 0  # Pointer for which repeat movement is in progress

    def move(self):
        """
        Controls the movement, reimplement per enemy type
        """
        if self.entry_busy:
            x, y, d = self.entry_movements[self.emp].move()
            self.pos, self.depth = (x, y), d

            if self.entry_movements[self.emp].done:
                self.emp += 1
                if self.emp >= len(self.entry_movements):
                    self.entry_busy = False
                    self.repeat_movements[self.rmp].set_anchor((*self.pos, self.depth))
                else:
                    self.entry_movements[self.emp].set_anchor((*self.pos, self.depth))
        else:
            x, y, d = self.repeat_movements[self.rmp].move()
            self.pos, self.depth = (x, y), d

            if self.repeat_movements[self.rmp].done:
                self.rmp = (self.rmp + 1) % len(self.repeat_movements)
                self.repeat_movements[self.rmp].reset()
                self.repeat_movements[self.rmp].set_anchor((*self.pos, self.depth))


    def attack(self):
        """
        Controls attacking, reimplement per enemy type
        """

    def update(self):
        self.move()
        self.attack()

        debug.debug('enemy pos', self.pos)

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
