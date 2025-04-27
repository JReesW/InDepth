from mothic import Thing, Rect, image as Image


class Enemy(Thing):
    def __init__(self, health, damage, score, rect):
        super().__init__(
            rect=rect,
            default_update_layer=2,
            default_render_layer=9
        )
        self.health = health
        self.damage = damage
        self.score = score
        self.speed = 5
        self.team = 2
        self.image = Image.load_image("player")

    def update(self):
        if self.rect.left <= 0:
            self.speed = 5
        elif self.rect.left >= 1920:
            self.speed = -5
        self.rect.left += self.speed
