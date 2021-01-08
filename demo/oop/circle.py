import math


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    # returns a string
    def __str__(self):
        return f"{self.x},{self.y},{self.radius}"

    # returns boolean
    def __eq__(self, other):
        print('__eq__')
        return self.x == other.x and self.y == other.y and self.radius == other.radius

    def __lt__(self, other):
        area1 = math.pi * self.radius * self.radius
        area2 = math.pi * other.radius * other.radius
        return area1 < area2


c1 = Circle(10, 20, 5)
c2 = Circle(10, 20, 5)
print(c1 == c2)  # c1.__eq__(c2)
print(c1)  # str(c1) --> c1.__str__()
c3 = Circle(10, 10, 6)
print(c1 < c3)
