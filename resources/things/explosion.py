from mothic import Thing, director, Surface, Rect, colors, image
from pygame import transform, Vector2

from scripts.draw_order import DrawnInOrder, scale_factor, transparency_factor, remove_thing

class Explosion(Thing, DrawnInOrder):
    def __init__(self, rect, depth):
        Thing.__init__(
            self,
            rect=rect,
            default_update_layer=2,
            default_render_layer=9
        )
        DrawnInOrder.__init__(self, depth)
        self.pos = self.rect.center
        self.base_image = None
        self.explosion = image.load_image("small_ship_explosion_core")
        self.shockwave = image.load_image("small_ship_explosion_shell")
        self.image.fill(colors.transparent)
        self.timer = 0
        self.phase = 0
        self.speed = 2.5
        self.explosionScale = 1
        self.shockwaveScale = -0.5
        self.alpha = 255

    def update(self):
        self.timer += 1
        # print(self.timer)
        # print(self.shockwaveScale)
        # print(self.explosionScale)

        if (self.explosionScale <= 0 and self.phase == 0):
            self.phase = 1
        if (self.timer > 100 / self.speed):
            self.alpha -= 2 * self.speed
        if (self.alpha <= 0):
            director.scene.cake.remove(self)
            remove_thing(self)
            return

        if (self.phase == 0):
            self.explosionScale -= 0.05 * self.speed
        elif (self.phase == 1):
            self.explosionScale += 0.01 * self.speed
            self.shockwaveScale += 0.02 * self.speed

        doExplosion = self.explosionScale > 0
        doShockwave = self.shockwaveScale > 0
        if (doExplosion):
            explosion = transform.scale_by(self.explosion, self.explosionScale)
        if (doShockwave):
            shockwave = transform.scale_by(self.shockwave, self.shockwaveScale)
        
        explosionSize = explosion.size if doExplosion else (0, 0)
        shockwaveSize = shockwave.size if doShockwave else (0, 0)
        width = max(explosionSize[0], shockwaveSize[0])
        height = max(explosionSize[1], shockwaveSize[1])
        rect = Rect(self.pos[0], self.pos[1], width, height)
        rect.center = self.pos

        surf = Surface(rect.size).convert_alpha()
        surf.fill(colors.transparent)
        surfRect = surf.get_rect()
        if (doShockwave):
            shockwaveRect = shockwave.get_rect()
            shockwaveRect.center = surfRect.center
            surf.blit(shockwave, shockwaveRect)
        if (doExplosion):
            explosionRect = explosion.get_rect()
            explosionRect.center = surfRect.center
            surf.blit(explosion, explosionRect)

        # self.base_image = surf
        # self.apply_image_rect_effects()

        # I'd wanna straighten this out, but later (or never lmao)

        scaledSurf = transform.scale_by(surf, scale_factor(self.apparent_depth))
        self.rect = scaledSurf.get_rect()

        x, y = self.pos
        vec = Vector2(x - 960, y - 540) * scale_factor(self.apparent_depth)
        self.rect.center = vec.x + 960, vec.y + 540

        scaledSurf.set_alpha(transparency_factor(self.apparent_depth) * self.alpha)
        self.image = scaledSurf