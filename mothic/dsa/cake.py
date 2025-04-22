from bisect import insort

from pygame.sprite import Group

from mothic.util.types import LayerAlias
from mothic.util.exceptions import CakeError
from mothic.system.things import Thing


"""
This is (what probably (doesn't) constitutes) a very basic ECS.
This will in all likelihood be replaced with a better (actual) ECS.
"""


# Should things only be allowed in one layer at a time? I can't think of a use case for a thing found in multiple layers...
# For now, if a thing is added while already being in another layer, it removes it from the first layer and adds it to the new one
class _CakeComponent:
    """
    Component for managing multiple layers of sprite groups
    """
    
    def __init__(self):
        self._layers: dict[int, Group] = {}
        self._layer_order: list[int] = []
        self._things: dict[int, int] = {}

    def insert(self, thing: Thing, layer: int = 0):
        """
        Insert a given thing into a given layer. Defaults to layer 0.
        """
        
        # Remove it from its layer if it already existed within
        if id(thing) in self._things:
            self.remove(thing)

        # Add the layer if it not yet existed
        if layer not in self._layers:
            insort(self._layer_order, layer)
            self._layers[layer] = Group()
        
        # Add the thing to the layer and thing register
        self._layers[layer].add(thing)
        self._things[id(thing)] = layer

    def remove(self, thing: Thing):
        """
        Remove a given thing from this cake
        """

        # Raise error if the cake doesn't contain the given thing
        if id(thing) not in self._things:
            raise CakeError("Can't remove a thing from a cake it isn't in")

        # Remove the thing from the layer it is in and the thing register
        layer = self._things[id(thing)]
        self._layers[layer].remove(thing)
        del self._things[id(thing)]
        
        # If the layer is now empty, remove it
        if not self._layers[layer]:
            del self._layers[layer]
            self._layer_order.remove(layer)


class _Updater(_CakeComponent):
    """
    Cake component that handles updating things
    """
    
    def __init__(self):
        _CakeComponent.__init__(self)


class _Renderer(_CakeComponent):
    """
    Cake component that handles rendering things
    """

    def __init__(self):
        _CakeComponent.__init__(self)


class _EventHandler(_CakeComponent):
    """
    Cake component that handles passing events to things
    """

    def __init__(self):
        _CakeComponent.__init__(self)


class Cake:
    """
    Manages multiple layers of sprite groups for updating and rendering things in specific orders
    """
    
    def __init__(self, *, aliases: dict[str, int] = None):
        self._updater = _Updater()
        self._renderer = _Renderer()
        self._event_handler = _EventHandler()
        self._aliases = {} if aliases is None else aliases
    
    def add_alias(self, alias: str, layer: int):
        """
        Add an alias for a layer number
        """
    
        self._aliases[alias] = layer

    def remove_alias(self, alias: str):
        """
        Remove an alias from the alias register
        """

        if alias in self._aliases:
            del self._aliases[alias]

    def insert_many(self, things: list[Thing], update_layer: LayerAlias = None, render_layer: LayerAlias = None, event_layer: LayerAlias = None):
        for thing in things:
            self.insert(thing, event_layer, update_layer, render_layer)
    
    def insert(self, thing: Thing, event_layer: LayerAlias = None, update_layer: LayerAlias = None, render_layer: LayerAlias = None):
        """
        Insert a given thing into the layers of the cake. Target layers can be given, uses default layers if nothing is given.
        """
        # Check if the given layer is an alias string
        if isinstance(update_layer, str):
            # Raise an error if it's an unregistered alias
            if update_layer not in self._aliases:
                raise CakeError(f"Alias {update_layer} is not registered as an alias of a layer in this cake")
            update_layer = self._aliases[update_layer]
        # Use thing's default layer if none is provided to the function
        elif update_layer is None:
            update_layer = thing.default_update_layer
        
        # Idem for render cake
        if isinstance(render_layer, str):
            if render_layer not in self._aliases:
                raise CakeError(f"Alias {render_layer} is not registered as an alias of a layer in this cake")
            render_layer = self._aliases[render_layer]
        elif render_layer is None:
            render_layer = thing.default_render_layer
        
        # Idem for event cake
        if isinstance(event_layer, str):
            if event_layer not in self._aliases:
                raise CakeError(f"Alias {event_layer} is not registered as an alias of a layer in this cake")
            event_layer = self._aliases[event_layer]
        elif event_layer is None:
            event_layer = thing.default_event_layer

        self._updater.insert(thing, update_layer)
        self._renderer.insert(thing, render_layer)
        self._event_handler.insert(thing, event_layer)
    
    def handle_events(self, events):
        for layer in self._event_handler._layer_order:
            for thing in self._event_handler._layers[layer]:
                thing.handle_events(events)
    
    def update(self):
        for layer in self._updater._layer_order:
            for thing in self._updater._layers[layer]:
                thing.update()

    def render(self, surface):
        for layer in self._renderer._layer_order:
            group = self._renderer._layers[layer]
            group.draw(surface)
  