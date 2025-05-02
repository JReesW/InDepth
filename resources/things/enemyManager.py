from mothic import Thing, Rect, director
from mothic.util.functions import split

from scripts.draw_order import remove_thing


class EnemyManager(Thing):
    def __init__(self, image = None, rect = None, *, default_event_layer = 0, default_update_layer = 2, default_render_layer = 10):
        super().__init__(
            rect=Rect(0, 0, 0, 0),
            default_update_layer=2
        )
        self.enemies = []

    def spawn(self, enemyType: str, *args):
        enemy = director.create_thing(enemyType, *args)
        self.enemies.append(enemy)
        director.scene.cake.insert(enemy)

    def update(self):
        dead, self.enemies = split(self.enemies, lambda e: e.health <= 0)

        for d in dead:
            explosion = director.create_thing("Explosion", d.rect, d.depth)
            director.scene.cake.remove(d)
            director.scene.cake.insert(explosion)
            remove_thing(d)
