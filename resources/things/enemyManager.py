from mothic import Thing, Rect, director
from mothic.util.functions import split

class EnemyManager(Thing):
    def __init__(self, image = None, rect = None, *, default_event_layer = 0, default_update_layer = 2, default_render_layer = 10):
        super().__init__(
            rect=Rect(0, 0, 0, 0),
            default_update_layer=2
        )
        self.enemies = []

    def spawn(self, enemyType: str, pos):
        enemy = director.create_thing(enemyType, pos)
        self.enemies.append(enemy)
        director.scene.cake.insert(enemy)

    def update(self):
        dead, self.enemies = split(self.enemies, lambda e: e.health <= 0)

        for d in dead:
            director.scene.cake.remove(d)
