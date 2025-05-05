from mothic import colors

Enemy = tuple[str, tuple[float, float], float, list, list]


class Subsequence:
    """
    Sequence of enemies with a delay before the next starts
    """

    def __init__(self, enemies: list[Enemy], delay: int):
        self.enemies = enemies  # blueprints
        self.e_objs = []  # enemy objects
        self.delay = delay
        self.ticks = 0
        self.used = False

    def update(self):
        self.ticks += 1

    def done(self) -> bool:
        """
        Return whether this subsequence has run for enough ticks
        """
        return self.ticks >= self.delay


class Sequence:
    """
    Sequence of subsequences separated by the clearing of all enemies
    """

    def __init__(self, subsequences: list[Subsequence]):
        self.subsequences = subsequences
        self.pointer = 0

    def update(self):
        self.subsequences[self.pointer].update()

    def done(self) -> bool:
        """
        Return whether all enemies in all subsequences have been defeated
        """
        return all(all(e.dead for e in s.e_objs) for s in self.subsequences) and self.pointer >= len(self.subsequences) - 1


class Level:
    """
    Sequences of enemies followed by a boss, with other level settings too
    """

    def __init__(self, sequences: list[Sequence], background: str, tint: colors.Color):
        self.sequences = sequences
        self.pointer = 0

        self.background = background
        self.tint = tint

    def update(self):
        self.sequences[self.pointer].update()
