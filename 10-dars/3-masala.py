class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_length(self):
        return 2 * 3.141592653589793 * self.radius

    def area(self):
        return 3.141592653589793 * (self.radius ** 2)


circle = Circle(4)
print(circle.circle_length())
print(circle.area())


