from mothic import Scene, colors, director, quit, Surface, display, image, Rect, Thing
from mothic.util.functions import split
from pygame import transform

from ui.button import Button
from random import random, randint


ships = {
    'patrol': image.load_image('patrol'),
    'satellite': image.load_image('satellite'),
    'satellite_dive': image.load_image('satellite_wings_2'),
    'longshot': image.load_image('longshot'),
    'gunship': image.load_image('gunship')
}

speeds = {
    'patrol': 10,
    'satellite': 7,
    'satellite_dive': 13,
    'longshot': 8,
    'gunship': 5
}

LEFT = -1
RIGHT = 1


class Ship(Thing):
    def __init__(self, ship: str, pos: tuple[int, int], direction: int, depth: float):
        super().__init__()

        flip = direction == RIGHT
        self.image = transform.flip(transform.scale_by(ships[ship], depth), flip_y=False, flip_x=flip)
        self.rect.center = pos

        self.pos = pos
        self.speed = speeds[ship]
        self.direction = direction
        self.depth = depth
        self.done = False

    def update(self, *args, **kwargs):
        self.pos = self.pos[0] + self.direction * self.speed * self.depth, self.pos[1]
        self.rect.center = self.pos

        if self.direction == LEFT and self.pos[0] < -400:
            self.done = True
        elif self.direction == RIGHT and self.pos[1] > 2320:
            self.done = True


class MainMenuScene(Scene):
    def __init__(self):
        super().__init__()

        self.centerx = display.get_surface().get_rect().centerx

        self.cake.insert_many([
            Button('Start', (200, 60), center=(self.centerx, 500)).set_func(director.set_scene, "LevelIntroScene", 1),
            Button('How to Play', (330, 60), center=(self.centerx, 600)).set_func(director.set_scene, "HowToPlayScene"),
            Button('Credits', (200, 60), center=(self.centerx, 700)).set_func(director.set_scene, "CreditsScene"),
            Button('Quit', (200, 60), center=(self.centerx, 800)).set_func(quit),
        ])
        self.ships = []

        self.title_image = image.load_image("indepth_title")

    def generate_ship(self):
        shiptype = list(ships.keys())[randint(0, 4)]
        depth = (random() * 0.3) + 0.5
        direction = [LEFT, RIGHT][randint(0, 1)]
        y = randint(100, 980)
        x = -400 if direction == RIGHT else 2320
        ship = Ship(shiptype, (x, y), direction, depth)
        self.ships.append(ship)
        self.ships.sort(key=lambda s: s.depth)

    def handle_events(self, events):
        self.cake.handle_events(events)

    def update(self):
        self.cake.update()

        for ship in self.ships:
            ship.update()

        self.ships = [ship for ship in self.ships if not ship.done]

        if randint(1, 150) == 1:
            self.generate_ship()

    def render(self, surface: Surface):
        surface.fill((180, 180, 180))

        for ship in self.ships:
            surface.blit(ship.image, ship.rect)

        rect = Rect(0, 0, *self.title_image.get_size())
        rect.center = self.centerx, 250
        surface.blit(self.title_image, rect)

        self.cake.render(surface)
