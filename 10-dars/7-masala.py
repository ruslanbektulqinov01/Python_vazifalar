import math


class GeometricArithmetic:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    @property
    def arithmetic(self):
        return (self.first + self.second) / 2

    @property
    def geometric(self):
        return math.sqrt(self.first * self.second)


geometric_arithmetic = GeometricArithmetic(5, 6)
print(geometric_arithmetic.arithmetic)
print(geometric_arithmetic.geometric)
