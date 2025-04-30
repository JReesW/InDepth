from mothic import Thing, Rect, Surface, draw, colors, image

from resources.things.enemy import Enemy
from scripts.draw_order import get_order


class DepthMeasure(Thing):
    """
    Shows the depth of enemies relative to the player, like a radar
    """

    def __init__(self):
        super().__init__(
            rect=Rect(20, 290, 30, 500)
        )

        self.base_image = Surface(self.rect.size).convert_alpha()
        self.base_image.fill(colors.dark_grey)
        draw.rect(self.base_image, colors.grey, Rect(0, 0, 30, 500), 3)
        draw.line(self.base_image, colors.grey, (15, 0), (15, 500), 1)

        self.image = self.base_image.copy()

    def update(self, *args, **kwargs):
        self.image = self.base_image.copy()

        for thing in get_order():
            if isinstance(thing, Enemy):
                img = image.load_image("enemy_indicator")
                y = 500 - (thing.apparent_depth / 6) * 500
                self.image.blit(img, (0, y - 15))

        img = image.load_image("player_indicator")
        y = 500 - (1 / 6) * 500
        self.image.blit(img, (0, y - 15))
