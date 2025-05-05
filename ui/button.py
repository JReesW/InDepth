from mothic import Thing, draw, colors, director, Rect, etypes, Surface, debug
from mothic.visuals import text

from math import sin, pi


def bar_growth(n):
    return (sin(pi * (n - 0.5)) / 2) + 0.5


class Button(Thing):
    def __init__(self, label, size, center):
        super().__init__(
            rect=Rect(0, 0, *size),
            default_render_layer=99
        )

        self.rect.center = center
        self.focused = False
        self.focus_timer = 0

        self.base_image = Surface(size).convert_alpha()
        self.base_image.fill(colors.transparent)

        surf, rect = text.render(label, colors.white, "consolamono-bold", 48, bold=True)
        rect.center = self.rect.width / 2, self.rect.height / 2
        self.base_image.blit(surf, rect)
        self.image = self.base_image.copy()

        self.func = None
        self.args = []

    def set_func(self, func, *args):
        self.func = func
        self.args = args
        return self

    def update(self, *args, **kwargs):
        if self.focused and self.focus_timer < 30:
            self.focus_timer += 1
        elif not self.focused and self.focus_timer > 0:
            self.focus_timer -= 1

        if self.focus_timer > 0:
            self.image = self.base_image.copy()
            width = self.rect.width * bar_growth(self.focus_timer / 30)
            draw.rect(self.image, colors.white, Rect(0, self.rect.height - 10, width, 10))

    def handle_events(self, events, **kwargs):
        mouse = director.get_mouse_pos()

        if self.rect.collidepoint(*mouse):
            self.focused = True

            for event in events:
                if event.type == etypes.MOUSEBUTTONUP:
                    self.func(*self.args)
        else:
            self.focused = False
