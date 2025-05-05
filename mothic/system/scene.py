import pygame

from mothic.dsa.cake import Cake
from mothic.media.audio import AudioManager


class Camera:
    """
    Controls relative positioning and scaling of all visualised objects
    """

    def __init__(self, pos, screen_size, x_bounds=(-10000, 10000), y_bounds=(-10000, 10000)):
        self.pos = pos
        self.screen_size = screen_size
        self.x_bounds = x_bounds[0], x_bounds[1] - self.rect.width
        self.y_bounds = y_bounds[0], y_bounds[1] - self.rect.height

    @property
    def top(self):
        return self.pos[1]

    @property
    def left(self):
        return self.pos[0]

    @property
    def rect(self):
        return pygame.Rect(self.left, self.top, *self.screen_size)

    @staticmethod
    def bound(val, bounds):
        return max(min(val, bounds[1]), bounds[0])

    def set_center(self, pos: tuple[float, float]):
        """
        Set the center of the camera to the given coords
        """
        top = pos[0] - self.screen_size[0] / 2
        left = pos[1] - self.screen_size[1] / 2
        self.pos = top, left

    def move(self, dx: int, dy: int):
        """
        Move the camera by the given amount of pixels
        :param dx: the change in pixels along the x-axis
        :param dy: the change in pixels along the y-axis
        """
        self.pos = (
            self.bound(self.left + dx, self.x_bounds),
            self.bound(self.top + dy, self.y_bounds)
        )

    def translate(self, pos: tuple[int, int]) -> tuple[int, int]:
        """
        Translate a given world position to a screen position
        :param pos: A world position
        :return: A screen position
        """
        x, y = pos
        newpos = (x - self.left), (y - self.top)
        return newpos

    def untranslate(self, pos: tuple[int, int]) -> tuple[int, int]:
        """
        Reverse of Camera.translate() above
        """
        x, y = pos
        newpos = (x + self.left), (y + self.top)
        return newpos

    def visible(self, rect: pygame.Rect) -> bool:
        """
        Return whether a given rect falls within the view of the camera
        :param rect: A rectangle
        :return: A boolean
        """
        return self.rect.colliderect(rect)

    def __str__(self):
        return f"Camera<{self.pos} | {self.screen_size[0]}x{self.screen_size[1]}>"


class Scene:
    def __init__(self,
                 **kwargs):
        self.camera = Camera((0, 0), (0, 0))
        self.cake = Cake()
        self.audio_manager = AudioManager()

    def init(self, *args, **kwargs):
        """
        Initalize the state of the Scene
        """
        pass

    def __handle_events(self, events):
        """
        Base version of handle_events, not meant to be reimplemented
        """
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_CTRL:
                pygame.quit()
                quit()

        self.handle_events(events)
    
    def __update(self):
        """
        Base version of update, not meant to be reimplemented
        """
        self.update()
        self.audio_manager.execute()

    def __render(self, surface):
        """
        Base version of render, not meant to be reimplemented
        """
        self.render(surface)

    def handle_events(self, events):
        """
        Handles the given list of pygame events
        """
        pass

    def update(self):
        """
        Update the state
        """
        pass

    def render(self, surface):
        """
        Render everything to the given surface
        """
        pass
