from mothic import Thing, Rect, director, keys, image
from resources.things.pistol import Pistol
import pygame

class Player(Thing):
    def __init__(self):
        super().__init__(
            rect=Rect(250, 250, 50, 50),
            default_render_layer=10
        )

        self.image = image.load_image("player")
        self.guns = [Pistol()]
        self.selectedGun = 0

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

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                print(event.button)
                if event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    if (mousePos[0] > self.rect.centerx):
                        direction = 1
                    else:
                        direction = -1
                    self.guns[self.selectedGun].shoot(self.rect.center, direction)