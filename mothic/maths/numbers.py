from pygame.math import clamp, lerp, Vector2, Vector3


def sign(n: float, zero_sign: float = 0) -> float:
    """
    Return the sign of a number. Optional parameter zero_sign sets the sign for zero, 0 by default
    """
    return 1 if n > 0 else -1 if n < 0 else zero_sign


def is_numeric(s: str) -> bool:
    """
    Return whether the string is a valid float or not.
    Differs from str.isnumeric() by allowing a negative sign and decimal separator.
    """
    try:
        _ = float(s)
        return True
    except ValueError:
        return False


def remap(n, i_min, i_max, o_min, o_max):
    return (n - i_min) / (i_max - i_min) * (o_max - o_min) + o_min
