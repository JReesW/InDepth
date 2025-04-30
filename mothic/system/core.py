import sys

import pygame
import pygame.freetype

from mothic.system import director, debug
from mothic.visuals.text import find_fonts
from mothic.util import etypes, keys
from mothic.util.functions import convert_mouse_click_events
from mothic.util.exceptions import Quit


class Game:
    """
    A game which runs at 60fps
    """

    def __init__(self, 
                 starting_scene: str, 
                 *, 
                 starting_scene_args: list = None, 
                 starting_scene_kwargs: dict = None, 
                 caption="A Mothic Game",
                 scenes_folder="resources/scenes",
                 things_folder="resources/things",
                 surface_size=None,
                 screen_size=(1920, 1080),
                 display_flags=pygame.RESIZABLE,
                 smoothscale=True,
                 fps: int=60
                 ):
        
        if starting_scene_args is None:
            starting_scene_args = {}

        if surface_size is None:
            surface_size = screen_size

        self.__equal_surface_screen_size = screen_size == surface_size

        pygame.init()
        pygame.freetype.init()

        self.surface_size = surface_size
        self.screen = pygame.display.set_mode(screen_size, display_flags)
        pygame.display.set_caption(caption)
        self.smoothscale = smoothscale

        self.fps = fps
        self.clock = pygame.time.Clock()

        director.settings = {
            'surface_size': surface_size,
            'screen_size': screen_size,
            'fps': fps
        }

        find_fonts()
        director.find_scenes(scenes_folder)
        director.find_things(things_folder)
        starting_scene_args = [] if starting_scene_args is None else starting_scene_args
        starting_scene_kwargs = {} if starting_scene_kwargs is None else starting_scene_kwargs
        director.set_scene(starting_scene, *starting_scene_args, **starting_scene_kwargs)

    def frame(self):
        self.clock.tick(self.fps)

        surface = pygame.Surface(self.surface_size, pygame.SRCALPHA)

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == etypes.KEYDOWN and event.key == keys.K_BACKQUOTE:
                debug.disable() if debug.is_active() else debug.enable()

        if not self.__equal_surface_screen_size:
            convert_mouse_click_events(events, director.settings['screen_size'], director.settings["surface_size"])

        # Call the necessary scene functions of the active scene
        director.scene._Scene__handle_events(events)
        director.scene._Scene__update()
        director.scene._Scene__render(surface)

        if debug.is_active():
            debug.render(surface)

        if not self.__equal_surface_screen_size:
            if self.smoothscale:
                scaled = pygame.transform.smoothscale(surface, self.screen.get_size())
            else:
                scaled = pygame.transform.scale(surface, self.screen.get_size())
            self.screen.blit(scaled, (0, 0))
        else:
            self.screen.blit(surface, (0, 0))

        # Draw the surface to the screen
        pygame.display.flip()
    
    def start(self):
        try:
            while True:
                self.frame()
        except Quit:
            print("Thank you for using Mothic!")
