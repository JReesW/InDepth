from mothic import Thing, Rect, director, colors, Surface, draw
from mothic.visuals import text
import pygame

class UI(Thing):
    def __init__(self, image = None, rect = None, *, default_event_layer = 0, default_update_layer = 9999, default_render_layer = 9999):
        super().__init__(
            rect=Rect(0, 0, 1920, 108),
            default_update_layer=default_update_layer,
            default_render_layer=default_render_layer
        )

        self.lastLives = None
        self.lastHealth = None

        self.livesRect = Rect(1920 - 190, 20, 170, 48)
        self.livesAlpha = 255

        self.healthRect = Rect(20, 20, 200, 48)
        self.healthAlpha = 255

        self.image.fill(colors.transparent)

    def drawLives(self):
        player = director.scene.player

        rect = self.livesRect
        surface = Surface(rect.size, pygame.SRCALPHA)
        surface.set_alpha(self.livesAlpha)
        surface.fill((128, 128, 128, 128))

        playerImage : Surface = player.image
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

        rect = self.healthRect
        surface = Surface(rect.size, pygame.SRCALPHA)
        surface.set_alpha(self.healthAlpha)
        surface.fill(colors.transparent)

        lineWidth = 5
        linePadding = lineWidth / 2

        #horizontal border
        draw.line(surface, colors.black, (0, 0 + linePadding), (rect.width, 0 + linePadding), lineWidth)
        draw.line(surface, colors.black, (0, rect.height - linePadding), (rect.width, rect.height - linePadding), lineWidth)
        #vertical border
        draw.line(surface, colors.black, (0 + linePadding, 0), (0 + linePadding, rect.height), lineWidth)
        draw.line(surface, colors.black, (rect.width - linePadding, 0), (rect.width - linePadding, rect.height), lineWidth)

        #a bunch of extra math to make sure your health isnt overlapping the border nor ever hidden by the border, depending on if you draw lines first or not
        healthMaxWidth = rect.width - lineWidth * 2
        hpRect = Rect(lineWidth, lineWidth, healthMaxWidth * (player.health / player.maxHealth), rect.height - lineWidth * 2)

        surface.fill(colors.red, hpRect)

        #draw.line(surface, colors.black, (healthMaxWidth / 2 + hpRect.left - 1, hpRect.top), (healthMaxWidth / 2 + hpRect.left - 1, hpRect.top + hpRect.height / 2), lineWidth)

        self.image.fill(colors.transparent, rect)
        self.image.blit(surface, rect)

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