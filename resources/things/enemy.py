from mothic import Thing, Rect, image as Image

class Enemy(Thing):
    def __init__(self, health = 100, image = None, rect = None, *, default_event_layer = 0, default_update_layer = 2, default_render_layer = 0):
        super().__init__(
            rect=rect,
            default_update_layer=default_update_layer
        )
        self.health = health
        self.speed = 5
        self.image = Image.load_image("player")

    def update(self):
        if self.rect.left <= 0:
            self.speed = 5
        elif self.rect.left >= 1920:
            self.speed = -5
        self.rect.left += self.speed