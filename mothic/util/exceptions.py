class UnsupportedError(Exception):
    """
    Raised when certain unsupported actions are attempted
    """


class PolymorphismError(Exception):
    """
    Raised when a method is called with an unsupported input type
    """


class CakeError(Exception):
    """
    Raised when illegal actions are attempted related to a cake
    """


class Quit(Exception):
    """
    Raised when the game is quit to stop the game loop
    """


class SwitchScene(Exception):
    """
    Prevents an old scene from continuing once it has been switched out
    """
