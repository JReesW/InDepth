from mothic import Rect, Thing, director, image

from scripts.draw_order import DrawnInOrder
from pygame import Vector2, transform


class Bullet(Thing, DrawnInOrder):
    def __init__(self, rect : Rect, velocity, lifespan, depth, team=0, damage = 1):
        Thing.__init__(self,
                        rect=rect,
                        default_update_layer=1,
                        default_render_layer=8
                        )
        DrawnInOrder.__init__(self, depth)
        self.pos = self.rect.center
        self.velocity = velocity
        self.lifespan = lifespan
        self.dead = False
        # 0 = no team, 1 = from player, 2 = from enemy
        self.team = team
        self.damage = damage
        if (self.team == 1):
            self.info_of_bullet()
        else:
            self.base_image = image.load_image("bullet")

        self.image = self.base_image.copy()
        self.apply_image_rect_effects()

        # self.x = self.rect.centerx
        # self.y = self.rect.centery


        # self.update()

    def info_of_bullet(self):
        triple = director.scene.player.triple_shot
        gatling = director.scene.player.gatling_gun
        hollow = director.scene.player.hollow_point

        image_path = "bullet_"
        if triple:
            image_path += "t"
        if gatling:
            image_path += "g"
        if hollow:
            image_path += "h"
            self.damage += 1
        
        if image_path[-1] == "_":
            image_path = image_path[:-1]

        self.base_image = image.load_image(image_path)
        center = self.rect.center
        self.rect.size = self.image.size
        self.rect.center = center

        if triple:
            vel = Vector2(self.velocity)
            angle = vel.angle_to(Vector2(1, 0))
            self.base_image = transform.rotate(self.base_image, angle)
    
    def update(self):
        self.lifespan -= 1
        if (self.lifespan < 0):
            self.dead = True

        self.pos = self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1]
        # self.x += self.velocity[0]
        # self.y += self.velocity[1]

        self.apply_image_rect_effects()

        if (self.team == 1):
            for enemy in director.scene.enemy_manager.enemies:
                if (self.rect.colliderect(enemy.rect) and enemy.collide_depth(self.apparent_depth)):
                    if (not enemy.shielded):
                        enemy.health -= self.damage
                    self.dead = True
        
        if (self.team == 2):
            if (self.rect.colliderect(director.scene.player.hitbox) and director.scene.player.collide_depth(self.apparent_depth)):
                if (not director.scene.player.shielded):
                    director.scene.player.health -= self.damage
                    director.scene.audio_manager.play_sound("player_damaged")
                self.dead = True
