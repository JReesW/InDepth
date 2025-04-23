from mothic import Rect
from resources.things.enemy import Enemy


class Patrol(Enemy):
    def __init__(self, pos):
        super().__init__(
            health=5,
            damage=1,
            score=50,
            rect=Rect(*pos, 100, 100)
        )


class Satellite(Enemy):
    def __init__(self, pos):
        super().__init__(
            health=30,
            damage=2,
            score=250,
            rect=Rect(*pos, 100, 100)
        )


class Kamikaze(Enemy):
    def __init__(self, pos):
        super().__init__(
            health=3,
            damage=10,
            score=150,
            rect=Rect(*pos, 100, 100)
        )


class Longshot(Enemy):
    def __init__(self, pos):
        super().__init__(
            health=45,
            damage=3,
            score=400,
            rect=Rect(*pos, 100, 100)
        )


class Scute(Enemy):
    def __init__(self, pos):
        super().__init__(
            health=20,
            damage=0,
            score=300,
            rect=Rect(*pos, 100, 100)
        )
