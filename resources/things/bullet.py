from mothic import Rect, Thing, director

from scripts.draw_order import DrawnInOrder


class Bullet(Thing, DrawnInOrder):
    def __init__(self, rect : Rect, velocity, lifespan, depth, team=0, damage = 1):
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
        self.damage = damage
    
    def update(self):
        self.lifespan -= 1
        if (self.lifespan < 0):
            self.dead = True
        
        self.rect.left += self.velocity[0]
        self.rect.top += self.velocity[1]

        if (self.team == 1):
            for enemy in director.scene.enemy_manager.enemies:
                if (self.rect.colliderect(enemy.rect) and enemy.collide_depth(self.apparent_depth)):
                    if (not enemy.shielded):
                        enemy.health -= self.damage
                    self.dead = True
        
        if (self.team == 2):
            if (self.rect.colliderect(director.scene.player.rect)):
                if (not director.scene.player.shielded):
                    director.scene.player.health -= self.damage
                self.dead = True
