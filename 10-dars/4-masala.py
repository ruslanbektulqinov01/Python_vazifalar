import math
class Circle:
    def __init__(self, area):
        self.area = area

    def radius(self):
        return math.sqrt(self.area / 2)


circle = Circle(10)
print(circle.radius())
