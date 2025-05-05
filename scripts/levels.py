from scripts.movement import Line, Lissajous


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
