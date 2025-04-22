from pygame import image, Surface, BLEND_RGBA_MAX
from mothic import colors


__images = {}


def load_image(name: str) -> Surface:
    """
    Load a PNG image by its name from the resources/images folder
    """
    if name not in __images:
        __images[name] = image.load(f"resources/images/{name}.png").convert_alpha()
    return __images[name].copy()


def unload_image(name: str) -> None:
    """
    Unload an image by its name
    """
    if name in __images:
        del __images[name]


def unload_all_images() -> None:
    """
    Unload all currently loaded images
    """
    for name in list(__images.keys()):
        del __images[name]


def recolor(surf: Surface, col: colors.Color) -> Surface:
    _surf = surf.copy()
    r, g, b, _ = col
    _surf.fill((r, g, b, 0), special_flags=BLEND_RGBA_MAX)
    return _surf
