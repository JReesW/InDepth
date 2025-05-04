from mothic import colors
from resources.things.enemy import Enemy


class Subsequence:
    """
    Sequence of enemies with a delay before the next starts
    """

    def __init__(self, enemies: list[Enemy], delay: int):
        self.enemies = enemies
        self.delay = delay
        self.ticks = 0

    def update(self):
        self.ticks += 1

    def finished(self) -> bool:
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
        self.current_subsequence = subsequences[0]

    def update(self):
        self.current_subsequence.update()

    def cleared(self) -> bool:
        """
        Return whether all enemies in all subsequences have been defeated
        """
        return all(all(e.dead for e in s.enemies) for s in self.subsequences)


class Level:
    """
    Sequences of enemies followed by a boss, with other level settings too
    """

    def __init__(self, sequences: list[Sequence], boss: str, background: str, tint: colors.Color):
        self.sequences = sequences
        self.current_sequence = sequences[0]

        self.boss = boss
        self.background = background
        self.tint = tint

    def update(self):
        self.current_sequence.update()
