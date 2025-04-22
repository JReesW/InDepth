from dataclasses import is_dataclass

from mothic.util.exceptions import PolymorphismError


def apply(func: callable) -> callable:
    """
    Decorator that applies a given function over the fields of a given class when the class is instantiated.

    Currently supports the following object types:
     - Dataclasses
     - Named tuples
    """
    def decorator[C](cls: C) -> C:
        if not is_dataclass(cls):
            raise TypeError("Apply only applies on dataclasses. Tried to apply to a non-dataclass")
        original_init = cls.__init__
        def new_init(self: C, *args):
            new_args = []
            for arg in args:
                new_args.append(func(arg))
            original_init(self, *new_args)
        cls.__init__ = new_init
        return cls
    return decorator


# Would be nice if this could handle functions with multiple inputs
def polymorph(t: type, _morphisms={}):
    """
    Assign a polymorphism to a method based on a single input type

    Based on: https://stackoverflow.com/a/78439791
    """
    def decorator(func: callable):
        def wrapper(self, t):
            for cls in type(self).__mro__:
                if func := _morphisms.get((f'{cls.__qualname__}.{name}', str(type(t).__name__))):
                    return func(self, t)
            raise PolymorphismError(f'Function {qualname} is not implemented for an input of type {type(t)}')
        name = func.__name__
        qualname = func.__qualname__
        if type(t) == str:
            _morphisms[func.__qualname__, t] = func
        else:
            _morphisms[func.__qualname__, t.__name__] = func
        return wrapper
    return decorator
