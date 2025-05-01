from mothic import Thing, Rect, director, colors, Surface, draw, image
from mothic.visuals import text
import pygame


class UI(Thing):
    def __init__(self):
        super().__init__(
            rect=Rect(0, 0, 1920, 140),
            default_update_layer=9999,
            default_render_layer=9999
        )

        self.lastLives = None
        self.lastHealth = None

        self.livesRect = Rect(1920 - 190, 20, 170, 48)
        self.livesAlpha = 255

        self.healthRect = Rect(30, 30, 616, 104)
        self.health_cover = image.load_image("healthbarcover")
        self.health_back = image.load_image("healthbarbackside")
        self.health_segment = image.load_image("healthbarsegment")
        self.healthAlpha = 255

        self.image.fill(colors.transparent)

    def drawLives(self):
        player = director.scene.player

        rect = self.livesRect
        surface = Surface(rect.size, pygame.SRCALPHA)
        surface.set_alpha(self.livesAlpha)
        surface.fill((128, 128, 128, 128))

        playerImage : Surface = player.base_image
        playerImage = pygame.transform.scale(playerImage, (100, 48))

        lineWidth = 5
        linePadding = lineWidth / 2

        #horizontal border
        draw.line(surface, colors.black, (0, 0 + linePadding), (rect.width, 0 + linePadding), lineWidth)
        draw.line(surface, colors.black, (0, rect.height - linePadding), (rect.width, rect.height - linePadding), lineWidth)
        #vertical border
        draw.line(surface, colors.black, (0 + linePadding, 0), (0 + linePadding, rect.height), lineWidth)
        draw.line(surface, colors.black, (rect.width - linePadding, 0), (rect.width - linePadding, rect.height), lineWidth)

        surface.blit(playerImage, (0, 0))

        surf, textRect = text.render(f"x", colors.black, 'impact', 26)
        textRect.left = playerImage.width + 13
        textRect.bottom = playerImage.height / 2 + 12
        surface.blit(surf, textRect)

        surf, textRect = text.render(f"{player.lives}", colors.black, 'impact', 30)
        textRect.left = playerImage.width + 25 # 12 more than x
        textRect.bottom = playerImage.height / 2 + 12
        surface.blit(surf, textRect)

        self.image.fill(colors.transparent, rect)
        self.image.blit(surface, rect)

    def drawHealth(self):
        player = director.scene.player

        surface = Surface(self.healthRect.size, pygame.SRCALPHA)
        surface.set_alpha(self.healthAlpha)

        surface.blit(self.health_back, (0, 0))

        for n in range(player.health):
            surface.blit(self.health_segment, (164 + 28 * n, 34))

        surface.blit(self.health_cover, (0, 0))

        self.image.fill(colors.transparent, self.healthRect)
        self.image.blit(surface, self.healthRect.topleft)

    def update(self):
        player = director.scene.player
        if (player.rect.colliderect(self.rect)):
            self.image.set_alpha(90)
        else:
            self.image.set_alpha(255)

        if (self.lastLives != player.lives):
            self.lastLives = player.lives
            self.drawLives()
        
        if (self.lastHealth != player.health):
            self.lastHealth = player.health
            self.drawHealth()