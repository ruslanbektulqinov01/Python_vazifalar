import math


class Coordinate:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @property
    def distance(self):
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)


coordinates = Coordinate(2, 4, 6, 8)
print(coordinates.distance)

