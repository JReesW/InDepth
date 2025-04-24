from mothic import Thing, Rect, director, colors, Surface, draw
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
        self.lastScore = None

        #having these accessible we could change the alpha whenever or move it
        self.healthRect = Rect(20, 20, 200, 108 - 60)
        self.healthSurface = Surface(self.healthRect.size, pygame.SRCALPHA)

        self.image.fill(colors.transparent)

    def drawLives(self):
        pass

    def drawHealth(self):
        player = director.scene.player

        rect = self.healthRect
        surface = self.healthSurface
        surface.fill(colors.transparent)

        lineWidth = 5
        linePadding = lineWidth / 2

        draw.line(surface, colors.black, (0, 0 + linePadding), (rect.width, 0 + linePadding), lineWidth)
        draw.line(surface, colors.black, (0, rect.height - linePadding), (rect.width, rect.height - linePadding), lineWidth)

        draw.line(surface, colors.black, (0 + linePadding, 0), (0 + linePadding, rect.height), lineWidth)
        draw.line(surface, colors.black, (rect.width - linePadding, 0), (rect.width - linePadding, rect.height), lineWidth)

        #a bunch of extra math to make sure your health isnt overlapping the border nor ever hidden by the border, depending on if you draw lines first or not
        healthMaxWidth = rect.width - lineWidth * 2
        hpRect = Rect(lineWidth, lineWidth, healthMaxWidth * (player.health / player.maxHealth), rect.height - lineWidth * 2)

        surface.fill(colors.red, hpRect)

        draw.line(surface, colors.black, (healthMaxWidth / 2 + hpRect.left - 1, hpRect.top), (healthMaxWidth / 2 + hpRect.left - 1, hpRect.top + hpRect.height / 2), lineWidth)

        self.healthSurface = surface
        self.image.blit(surface, rect)

    def drawScore(self):
        pass

    def update(self):
        player = director.scene.player

        if (self.lastLives != player.lives):
            self.lastLives = player.lives
            self.drawLives()
        
        if (self.lastHealth != player.health):
            self.lastHealth = player.health
            self.drawHealth()
        
        if (self.lastScore != director.scene.score):
            self.lastScore = director.scene.score
            self.drawScore()