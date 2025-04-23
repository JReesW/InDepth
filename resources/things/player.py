from mothic import Thing, Rect, director, keys, image
import pygame

class Player(Thing):
    def __init__(self):
        super().__init__(
            rect=Rect(250, 250, 50, 50),
            default_render_layer=10
        )

        self.image = image.load_image("player")

        self.bullet_manager = director.create_thing("BulletManager")
        director.scene.cake.insert(self.bullet_manager)

        self.firing_cooldown = 10

        self.team = 1

    def handle_events(self, events):
        pressed = pygame.key.get_pressed()

        if pressed[keys.K_w]:
            self.rect.top -= 5
        if pressed[keys.K_s]:
            self.rect.top += 5
        if pressed[keys.K_a]:
            self.rect.left -= 5
        if pressed[keys.K_d]:
            self.rect.left += 5
        
        parallax = director.state['parallax']
        if pressed[keys.K_r]:
            parallax.depth = parallax.depth + 0.01
        if pressed[keys.K_f]:
            parallax.depth = parallax.depth - 0.01

        if pressed[keys.K_SPACE]:
            if self.firing_cooldown == 0:
                self.firing_cooldown = 10
                self.bullet_manager.shoot(self.rect.center, self.team)
    
    def update(self):
        if self.firing_cooldown > 0:
            self.firing_cooldown -= 1