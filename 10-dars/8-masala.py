from masala_5 import Coordinate


class RectangleCoordinatesArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


if __name__ == '__main__':
    x1 = 4
    y1 = 5

    x2 = 4
    y2 = 5

    x3 = 4
    y3 = 5

    x4 = 4
    y4 = 5
    height = Coordinate(x1, y1, x2, y2)
    width = Coordinate(x3, y3, x4, y4)

    rectancle_area = RectangleCoordinatesArea(width, height)

    print(rectancle_area.area)



