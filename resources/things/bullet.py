from mothic import Rect, Surface, Thing, director

from scripts.draw_order import DrawnInOrder


class Bullet(Thing, DrawnInOrder):
    def __init__(self, rect : Rect, velocity, lifespan, depth, team=0):
        Thing.__init__(self,
                       rect=rect,
                       default_update_layer=1,
                       default_render_layer=8
                       )
        DrawnInOrder.__init__(self, depth)
        self.velocity = velocity
        self.lifespan = lifespan
        self.dead = False
        # 0 = no team, 1 = from player, 2 = from enemy
        self.team = team
    
    def update(self):
        self.lifespan -= 1
        if (self.lifespan < 0):
            self.dead = True
        
        self.rect.left += self.velocity[0]
        self.rect.top += self.velocity[1]

        if (self.team == 1):
            for enemy in director.scene.enemy_manager.enemies:
                if (self.rect.colliderect(enemy.rect)):
                    enemy.health -= 1
                    self.dead = True
