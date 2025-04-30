from mothic import image, Surface, director


EXTRA_LIFE = 0
HEALTH_KIT = 1
SHIELD = 2
TRIPLE_SHOT = 3
GATLING_GUN = 4
HOLLOW_POINT = 5

images = {
    EXTRA_LIFE:"extralife",
    HEALTH_KIT:"extralife",
    SHIELD:"extralife",
    TRIPLE_SHOT:"extralife",
    GATLING_GUN:"extralife",
    HOLLOW_POINT:"extralife",
    }

class Powerup():
    def __init__(self, id = 0, pos : tuple[float, float] = (0, 0)):
        #0 extra life, 1 health kit, 2 shield, 3 triple shot, 4 gatling gun, 5 hollow point
        self.id = id
        self.image = image.load_image(images[self.id])
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def collidePlayer(self) -> bool:
        return self.rect.colliderect(director.scene.player.rect)

    def update(self):
        self.rect.left -= 1

    def apply(self):
        if (self.id == EXTRA_LIFE):
            director.scene.player.lives += 1
        if (self.id == HEALTH_KIT):
            director.scene.player.health += 5
        

    def render(self, surface : Surface):
        surface.blit(self.image, self.rect)