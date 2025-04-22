from dataclasses import dataclass
from math import dist, atan2, cos, sin

from mothic.util.decorators import polymorph


type Point = tuple[float, float]


@dataclass
class Triangle:
    """
    A 2D triangle, defined by three points
    """
    a: Point
    b: Point
    c: Point

    @polymorph(Point)
    def __contains__(self, point: Point) -> bool:
        def _sign(p1: Point, p2: Point, p3: Point):
            return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

        d1 = _sign(point, self.a, self.b)
        d2 = _sign(point, self.b, self.c)
        d3 = _sign(point, self.c, self.a)

        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

        return not (has_neg and has_pos)
    
    @property
    def centroid(self):
        return Point((self.a.x + self.b.x + self.c.x) / 3, (self.a.y + self.b.y + self.c.y) / 3)


@dataclass
class Circle:
    """
    A 2D circle, defined by a center point and a radius
    """
    center: Point
    radius: float

    @polymorph(Point)
    def __contains__(self, point: Point):
        return point.dist(self) <= 0

    @polymorph(Point)
    def dist(self, point: Point) -> float:
        return point.dist(self)
    
    @polymorph("Circle")
    def dist(self, circle: "Circle") -> float:
        return max(self.center.dist(circle.center) - self.radius - circle.radius, 0)
    

def lerp(start: Point, end: Point, alpha: float) -> Point:
    """
    Return the point between a given start point and a given end point, at a given proportional distance.
    Distance closer to 0 is closer to a, distance closer to 1 is closer to b, distance 0.5 is exactly halfway.
    """
    ax, ay = start
    bx, by = end

    distance = dist(start, end) * alpha
    angle = atan2(ay - by, ax - bx)
    return ax - (cos(angle) * distance), ay - (sin(angle) * distance)
