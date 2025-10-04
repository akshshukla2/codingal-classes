class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


r1 = Rectangle(5, 3)
print("Area of rectangle:", r1.area())

t1 = Triangle(4, 6)
print("Area of triangle:", t1.area())
