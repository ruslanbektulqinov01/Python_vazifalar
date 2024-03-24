import math


class Triangle:
    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = math.sqrt(first_side**2 + second_side**2)

    @property
    def area(self):
        return (self.first_side * self.second_side) / 2

    @property
    def perimeter(self):
        return self.first_side + self.second_side + self.third_side


if __name__ == '__main__':
    triangle = Triangle(3, 4)
    print(triangle.area)
    print(triangle.perimeter)
