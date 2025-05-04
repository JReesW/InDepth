from pygame.sprite import Sprite
from pygame import Surface, Rect

from mothic.util.types import LayerAlias
from mothic.visuals import colors


class Thing(Sprite):
    """
    The basic actor of a scene
    """

    def __init__(self, 
                 image: Surface = None, 
                 rect: Rect = None, 
                 *,
                 default_event_layer: LayerAlias = 0,
                 default_update_layer: LayerAlias = 0,
                 default_render_layer: LayerAlias = 0):
        Sprite.__init__(self)

        self.rect = rect if rect is not None else Rect(50, 50, 10, 10)
        self.base_image = None

        if image is None:
            self.image = Surface(self.rect.size).convert_alpha()
        else:
            self.image = image
        
        # Default layers within a scene's cake
        self.default_event_layer = default_event_layer
        self.default_update_layer = default_update_layer
        self.default_render_layer = default_render_layer

    def handle_events(self, events, **kwargs):
        """
        Handle user input
        """
        pass

    def early_update(self, *args, **kwargs):
        """
        Update the image and the rect (and other properties if needed) earlier than the regular update
        TODO: Determine necessity, considering the cake
        """
        pass

    def update(self, *args, **kwargs):
        """
        Update the image and the rect (and other properties if needed)
        """
        pass
