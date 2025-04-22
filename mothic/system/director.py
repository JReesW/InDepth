import pygame

from mothic.system.scene import Scene
from mothic.maths.numbers import remap

import os
import importlib
import inspect
from pathlib import Path


scene = None
__scenes = {}

# For now a dict, but should probably become something more sophisticated
state = {}
settings = {}


def set_scene(_scene: str, *args, **kwargs) -> None:
    """
    Set the current scene to the given scene
    """
    global scene
    scene = __scenes[_scene](*args, **kwargs)


def find_scenes(path: os.PathLike = "resources/scenes"):
    """
    Automatically loads all scene classes found in the scenes folder
    """
    module_path = Path(path)

    # Check every file in the scenes module
    for file in os.listdir(module_path):
        # If it's a python file that isn't marked as protected
        if file.endswith('.py') and not file.startswith('__'):
            module_name = f".{file[:-3]}"
            relative_path = str(path).replace('/', '.')
            
            try:
                # Import the scene file
                module = importlib.import_module(module_name, package=relative_path)

                # Check for Scene derived classes, and store them
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, Scene) and obj is not Scene:
                        __scenes[name] = obj
            except Exception as e:
                print(f"Error loading scene from {module_name}: {e}")


def screen_to_surf(coords: tuple[int, int]) -> tuple[int, int]:
    # TODO: This is to circumvent mothics scaling click position problem, FIX
    x, y = coords
    ix, iy = settings['screen_size']
    ox, oy = settings['surface_size']
    return int(remap(x, 0, ix, 0, ox)), int(remap(y, 0, iy, 0, oy))


def get_mouse_pos():
    return screen_to_surf(pygame.mouse.get_pos())
