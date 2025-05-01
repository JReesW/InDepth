from mothic import Thing, Rect, director, keys, image, etypes, debug, draw, Surface
import pygame
from scripts import DrawnInOrder
import numpy as np


class Player(Thing, DrawnInOrder):
    def __init__(self):
        Thing.__init__(self,
            rect=Rect(250, 250, 50, 50),
            default_render_layer=10
        )
        DrawnInOrder.__init__(self, 1)

        self.lives = 3
        self.maxHealth = 15
        self.health = self.maxHealth

        self.base_image = image.load_image("player")
        self.rect.size = self.base_image.get_rect().size
        #self.test_image()

        self.firing_cooldown = 10

        self.damage = 1
        self.team = 1
        self.shielded = False
        self.shield_timer_max = 600
        self.shield_timer = 0
        self.shield_radius = 3

        self.triple_shot = False
        self.gatling_gun = False
        self.hollow_point = False

    def get_not_close_pixels(self, surface, target_color, threshold):
        arr = pygame.surfarray.array3d(surface)
        alpha = pygame.surfarray.array_alpha(surface)
        r, g, b = target_color

        color_diff = (
            (arr[:, :, 0].astype(np.int32) - r) ** 2 +
            (arr[:, :, 1].astype(np.int32) - g) ** 2 +
            (arr[:, :, 2].astype(np.int32) - b) ** 2
        )

        mask = color_diff > (threshold ** 2)

        del arr
        del alpha
        return mask

    def test_image(self):
        baseColor = (236, 236, 236)
        #newColor = (210, 37, 37)
        newColor = (247, 66, 66)
        difference = tuple(base - new for base, new in zip(baseColor, newColor))

        mask = self.get_not_close_pixels(self.image, baseColor, 150)
        arr = pygame.surfarray.pixels3d(self.image)

        for c in range(3):
            arr[:, :, c][mask] = np.clip(arr[:, :, c][mask].astype(np.int16) - difference[c], 0, 255).astype(np.uint8)

    def get_outline(self, surface):
        alpha = pygame.surfarray.pixels_alpha(surface)
        rgb = pygame.surfarray.pixels3d(surface)

        padded = np.pad(alpha, 1, mode='constant', constant_values=0)

        mask = (
            (alpha != 0) &
            (
                (padded[0:-2, 0:-2] == 0) |  # top-left
                (padded[0:-2, 1:-1] == 0) |  # top
                (padded[0:-2, 2:  ] == 0) |  # top-right
                (padded[1:-1, 0:-2] == 0) |  # left
                (padded[1:-1, 2:  ] == 0) |  # right
                (padded[2:  , 0:-2] == 0) |  # bottom-left
                (padded[2:  , 1:-1] == 0) |  # bottom
                (padded[2:  , 2:  ] == 0)    # bottom-right
            )
        )
        
        del alpha
        del rgb

        return mask

    def handle_events(self, events):
        pressed = pygame.key.get_pressed()

        if pressed[keys.K_w]:
            self.rect.top -= 10
        if pressed[keys.K_s]:
            self.rect.top += 10
        if pressed[keys.K_a]:
            self.rect.left -= 10
        if pressed[keys.K_d]:
            self.rect.left += 10

        if pressed[keys.K_r]:
            self.depth += 0.03
        if pressed[keys.K_f]:
            self.depth -= 0.03

        for event in events:
            if event.type == etypes.KEYUP:
                if event.key == keys.K_k:
                    self.health -= 1
                if event.key == keys.K_l:
                    self.health = min(self.health + 1, self.maxHealth)

        if pressed[keys.K_SPACE]:
            if self.firing_cooldown == 0:
                self.firing_cooldown = 10
                director.scene.bullet_manager.shoot(Rect(self.rect.centerx, self.rect.centery, 10, 5), (20, 0), 600, self.depth, self.team, self.damage)
    
    def update(self):
        self.image = self.base_image.copy()
        debug.debug('player depth', f"{self.depth:.2f}")
        debug.debug('player app. depth', f"{self.apparent_depth:.2f}")
        if self.firing_cooldown > 0:
            self.firing_cooldown -= 1
        
        if (self.shielded):
            self.shield_timer += 1
            self.shield_radius += 5 + (1 - 5) * (self.shield_timer / self.shield_timer_max)
            
            if (self.shield_radius > max(*self.image.size) / 1.5):
                self.shield_radius = 0
            surface = Surface(self.image.size, pygame.SRCALPHA)

            draw.circle(surface, (66, 206, 245, 64), self.image.get_rect().center, self.shield_radius, 5)

            alpha_a = pygame.surfarray.pixels_alpha(self.image)
            alpha_b = pygame.surfarray.pixels_alpha(surface)

            alpha_b[alpha_a == 0] = 0

            del alpha_b

            tint = Surface(self.image.size, pygame.SRCALPHA)
            tint.fill((0, 221, 255, 20))

            alpha_b = pygame.surfarray.pixels_alpha(tint)
            alpha_b[alpha_a == 0] = 0

            del alpha_b

            mask = self.get_outline(self.image)

            rgb = pygame.surfarray.pixels3d(self.image)

            rgb[mask] = (66, 206, 245)
            alpha_a[mask] = 255

            del alpha_a
            del rgb

            self.image.blit(surface)
            self.image.blit(tint)

            if (self.shield_timer > self.shield_timer_max):
                self.shielded = False
                self.shield_timer = 0

        
