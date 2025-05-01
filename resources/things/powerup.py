from mothic import image, Surface, director


EXTRA_LIFE = 0
HEALTH_KIT = 1
SHIELD = 2
TRIPLE_SHOT = 3
GATLING_GUN = 4
HOLLOW_POINT = 5

images = {
    EXTRA_LIFE:"extralife",
    HEALTH_KIT:"heal",
    SHIELD:"shield",
    TRIPLE_SHOT:"triple_shot",
    GATLING_GUN:"gatling_gun",
    HOLLOW_POINT:"hollow_point",
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
            director.scene.player.health = min(director.scene.player.health + 5, director.scene.player.maxHealth)
        if (self.id == SHIELD):
            director.scene.player.shielded = True
        if (self.id == TRIPLE_SHOT):
            director.scene.player.triple_shot = True
        if (self.id == GATLING_GUN):
            director.scene.player.gatling_gun = True
        if (self.id == HOLLOW_POINT):
            director.scene.player.hollow_point = True

    def render(self, surface : Surface):
        surface.blit(self.image, self.rect)