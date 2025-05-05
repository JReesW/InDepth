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
                        (
                            "Patrol", (2500, 300), 1, [
                            Line((1600, 300, 1), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        ),
                        (
                            "Patrol", (2500, 700), 1, [
                                Line((1600, 700, 1), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        )
                    ],
                    delay=150
                ),
                Subsequence(
                    enemies=[
                        (
                            "Patrol", (2500, 300), 4, [
                                Line((1600, 300, 4), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        ),
                        (
                            "Patrol", (2500, 700), 4, [
                                Line((1600, 700, 4), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        )
                    ],
                    delay=150
                )
            ]
        ),
        Sequence(
            subsequences=[
                Subsequence(
                    enemies=[
                        (
                            "Patrol", (2500, 700), 1, [
                                Line((1600, 700, 1), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        )
                    ],
                    delay=240
                ),
                Subsequence(
                    enemies=[
                        (
                            "Patrol", (2500, 300), 0, [
                                Line((1600, 300, 0.5), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        ),
                        (
                            "Patrol", (2500, 700), 1, [
                                Line((1600, 700, 1), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        ),
                        (
                            "Patrol", (2500, 500), 2, [
                                Line((1600, 500, 1.5), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        )
                    ],
                    delay=240
                ),
                Subsequence(
                    enemies=[
                        (
                            "Satellite", (2500, 450), 4, [
                                Line((800, 450, 1), 150),
                                Line((1800, 450, 1), 90)
                            ], [
                                Lissajous(100, 500, 2, 4, 600)
                            ]
                        )
                    ],
                    delay=150
                )
            ]
        ),
        Sequence(
            subsequences=[
                Subsequence(
                    enemies=[
                        (
                            "Patrol", (2200, -300), 1, [
                                Line((1600, 300, 1), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        ),
                        (
                            "Patrol", (2200, -300), 3, [
                                Line((1600, 500, 3), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        ),
                        (
                            "Patrol", (2200, -300), 5, [
                                Line((1600, 700, 5), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        ),
                    ],
                    delay=150
                ),
                Subsequence(
                    enemies=[
                        (
                            "Satellite", (2500, 450), 4, [
                                Line((800, 450, 1), 150),
                                Line((1800, 450, 1), 90)
                            ], [
                                Lissajous(100, 300, 2, 4, 600)
                            ]
                        ),
                        (
                            "Satellite", (2500, 450), 1, [
                                Line((800, 450, 4), 150),
                                Line((1800, 450, 4), 90)
                            ], [
                                Lissajous(100, 300, 2, 4, 600)
                            ]
                        ),
                        (
                            "Satellite", (2500, 450), 3, [
                                Line((800, 450, 0), 150),
                                Line((1800, 450, 0), 90)
                            ], [
                                Lissajous(100, 300, 2, 4, 600)
                            ]
                        ),
                    ],
                    delay=150
                )
            ]
        )
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
                        (
                            "Patrol", (2200, 300), 1, [
                                Line((1600, 300, 4), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        ),
                        (
                            "Patrol", (2200, 300), 0, [
                                Line((1600, 500, 4), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        ),
                        (
                            "Patrol", (2200, 300), 2, [
                                Line((1600, 700, 4), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        ),
                        (
                            "Patrol", (2200, 300), 3, [
                                Line((1600, 500, 1), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        ),
                        (
                            "Patrol", (2200, 300), 4, [
                                Line((1600, 700, 1), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        ),
                        (
                            "Patrol", (2200, 300), 5, [
                                Line((1600, 300, 1), 180)
                            ], [
                                Lissajous(300, 100, 2, 4, 600)
                            ]
                        )
                    ],
                    delay=300
                )
            ]
        ),
        Sequence(
            subsequences=[
                Subsequence(
                    enemies=[
                        (
                            "Satellite", (2600, 450), 3, [
                                Line((800, 450, 1), 150),
                                Line((1600, 450, 1), 90)
                            ], [
                                Lissajous(100, 500, 2, 4, 600)
                            ]
                        )
                    ],
                    delay=300
                ),
                Subsequence(
                    enemies=[
                        (
                            "Satellite", (2500, -200), 5, [
                                Line((800, 300, 1), 150),
                                Line((1800, 300, 1), 90)
                            ], [
                                Lissajous(100, 300, 2, 4, 600)
                            ]
                        ),
                        (
                            "Satellite", (2500, 1200), 5, [
                                Line((800, 600, 1), 150),
                                Line((1800, 600, 1), 90)
                            ], [
                                Lissajous(100, 300, 2, 4, 600)
                            ]
                        )
                    ],
                    delay=150
                )
            ]
        ),
        Sequence(
            subsequences=[
                Subsequence(
                    enemies=[
                        (
                            "Patrol", (2200, -800), 0, [
                                Line((1600, 450, 3), 180)
                            ], [
                                Lissajous(100, 500, 2, 8, 600)
                            ]
                        ),
                        (
                            "Patrol", (2900, 450), 0, [
                                Line((1400, 450, 3), 180)
                            ], [
                                Lissajous(100, 500, 2, 8, 600)
                            ]
                        ),
                        (
                            "Patrol", (2200, 1500), 0, [
                                Line((1200, 450, 3), 180)
                            ], [
                                Lissajous(100, 500, 2, 8, 600)
                            ]
                        ),
                    ],
                    delay=150
                )
            ]
        ),
        Sequence(
            subsequences=[
                Subsequence(
                    enemies=[
                        (
                            "Longshot", (1300, -300), 3, [
                                Line((1600, 450, 3), 240)
                            ], [
                                Lissajous(300, 500, 2, 3, 600)
                            ]
                        ),
                    ],
                    delay=150
                )
            ]
        )
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
                        (
                            "Satellite", (2500, -200), 5, [
                                Line((800, 450, 1), 150),
                                Line((1800, 450, 1), 90)
                            ], [
                                Lissajous(100, 300, 2, 4, 600)
                            ]
                        ),
                        (
                            "Satellite", (2500, 1200), 0, [
                                Line((800, 450, 4), 150),
                                Line((1800, 450, 4), 90)
                            ], [
                                Lissajous(100, 300, 2, 4, 600)
                            ]
                        )
                    ],
                    delay=300
                ),
                Subsequence(
                    enemies=[
                        (
                            "Patrol", (2900, 450), 0, [
                                Line((1600, 300, 1), 180)
                            ], [
                                Lissajous(100, 500, 2, 8, 600)
                            ]
                        )
                    ],
                    delay=120
                ),
                Subsequence(
                    enemies=[
                        (
                            "Patrol", (2900, 450), 0, [
                                Line((1600, 600, 4), 180)
                            ], [
                                Lissajous(100, 500, 2, 8, 600)
                            ]
                        )
                    ],
                    delay=120
                ),
                Subsequence(
                    enemies=[
                        (
                            "Patrol", (2900, 450), 0, [
                                Line((1600, 600, 1), 180)
                            ], [
                                Lissajous(100, 500, 2, 8, 600)
                            ]
                        )
                    ],
                    delay=120
                ),
                Subsequence(
                    enemies=[
                        (
                            "Patrol", (2900, 450), 0, [
                                Line((1600, 300, 4), 180)
                            ], [
                                Lissajous(100, 500, 2, 8, 600)
                            ]
                        )
                    ],
                    delay=120
                )
            ]
        ),
        Sequence(
            subsequences=[
                Subsequence(
                    enemies=[
                        (
                            "Patrol", (2200, 450), 1, [
                                Line((1600, 450, 1), 180)
                            ], [
                                Lissajous(300, 500, 2, 8, 600)
                            ]
                        )
                    ],
                    delay=300
                ),
                Subsequence(
                    enemies=[
                        (
                            "Longshot", (1300, -300), 1, [
                                Line((1600, 300, 1), 240),
                                Line((1600, 450, 0), 120)
                            ], [
                                Lissajous(300, 300, 2, 3, 600)
                            ]
                        ),
                        (
                            "Longshot", (1300, 1500), 1, [
                                Line((1600, 600, 1), 240),
                                Line((1600, 450, 2), 120)
                            ], [
                                Lissajous(300, 300, 2, 3, 600)
                            ]
                        )
                    ],
                    delay=300
                )
            ]
        ),
        Sequence(
            subsequences=[
                Subsequence(
                    enemies=[
                        (
                            "Satellite", (2500, -200), 0, [
                                Line((800, 300, 3), 180),
                                Line((1800, 450, 3), 90)
                            ], [
                                Lissajous(100, 300, 2, 4, 600)
                            ]
                        ),
                        (
                            "Satellite", (2500, 1200), 0, [
                                Line((800, 450, 3), 150),
                                Line((1800, 450, 3), 90)
                            ], [
                                Lissajous(100, 300, 2, 4, 600)
                            ]
                        ),
                        (
                            "Satellite", (2500, 1200), 0, [
                                Line((800, 600, 3), 120),
                                Line((1800, 450, 3), 90)
                            ], [
                                Lissajous(100, 300, 2, 4, 600)
                            ]
                        )
                    ],
                    delay=150
                )
            ]
        ),
        Sequence(
            subsequences=[
                Subsequence(
                    enemies=[
                        (
                            "Longshot", (1300, -300), 1, [
                                Line((1600, 300, 3), 340)
                            ], [
                                Lissajous(300, 200, 2, 3, 600)
                            ]
                        ),
                        (
                            "Longshot", (1300, 1500), 1, [
                                Line((1600, 600, 3), 240)
                            ], [
                                Lissajous(300, 200, 2, 3, 600)
                            ]
                        )
                    ],
                    delay=150
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