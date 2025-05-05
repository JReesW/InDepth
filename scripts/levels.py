from scripts.movement import Line, Lissajous
from scripts.level import Level, Sequence, Subsequence


enemy = ("Patrol", (1700, 450), 1, [
    Line((1500, 550, 1), 120),
    Line((1500, 350, 1), 120)
], [
    Line((1700, 450, 4), 60),
    Line((1650, 450, 1), 60)
])


satellite = ("Satellite", (2200, 450), 1, [
    Line((800, 450, 1), 150),
    Line((1800, 450, 1), 90)
], [
    Lissajous(100, 300, 2, 4, 600)
])


longshot = ("Longshot", (1300, -300), 1, [
    Line((1600, 450, 1), 240)
], [
    Lissajous(300, 300, 2, 3, 600)
])


level1 = lambda: Level(
    sequences=[
        Sequence(
            subsequences=[
                Subsequence(
                    enemies=[
                        ("Patrol", (2200, 300), 1, [
                            Line((1600, 300, 1), 180)
                        ], [
                            Lissajous(300, 100, 2, 4, 600)
                        ])
                    ],
                    delay=300
                )
            ])
    ],
    background="level_1_bg",
    tint=(0, 255, 0, 25)
)

level2 = lambda: Level(
    sequences=[
        Sequence(
            subsequences=[
                Subsequence(
                    enemies=[
                        ("Patrol", (2200, 300), 1, [
                            Line((1600, 300, 1), 180)
                        ], [
                            Lissajous(300, 100, 2, 4, 600)
                        ])
                    ],
                    delay=300
                )
            ])
    ],
    background="level_2_bg",
    tint=(0, 0, 255, 15)
)

level3 = lambda: Level(
    sequences=[
        Sequence(
            subsequences=[
                Subsequence(
                    enemies=[
                        ("Patrol", (2400, 300), 1, [
                            Line((1600, 300, 1), 180)
                        ], [
                            Lissajous(300, 100, 2, 4, 600)
                        ])
                    ],
                    delay=300
                ),
                Subsequence(
                    enemies=[
                        ("Patrol", (2400, 400), 3, [
                            Line((1600, 400, 3), 180)
                        ], [
                            Lissajous(300, 100, 2, 4, 600)
                        ])
                    ],
                    delay=300
                )
            ]
        ),
        Sequence(
            subsequences=[
                Subsequence(
                    enemies=[
                        ("Patrol", (2200, 500), 1, [
                            Line((1600, 500, 1), 180)
                        ], [
                             Lissajous(300, 100, 2, 4, 600)
                         ])
                    ],
                    delay=300
                ),
                Subsequence(
                    enemies=[
                        ("Patrol", (2200, 600), 1, [
                            Line((1600, 600, 1), 180)
                        ], [
                            Lissajous(300, 100, 2, 4, 600)
                        ])
                    ],
                    delay=300
                )
            ]
        )
    ],
    background="level_3_bg",
    tint=(255, 255, 255, 25)
)


levels = {
    1: level1,
    2: level2,
    3: level3
}