import math

class Shape:
    def area(self):
        pass

    def __str__(self):
        return "This is a generic shape."

    def __int__(self):
        return self.area()

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle: radius={self.radius}"

class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Right Triangle: base={self.base}, height={self.height}"

class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __str__(self):
        return f"Trapezoid: base1={self.base1}, base2={self.base2}, height={self.height}"

# Приклад використання:
rectangle = Rectangle(5, 4)
print(str(rectangle))
print(int(rectangle))

circle = Circle(3)
print(str(circle))
print(int(circle))

triangle = RightTriangle(3, 4)
print(str(triangle))
print(int(triangle))

trapezoid = Trapezoid(2, 4, 5)
print(str(trapezoid))
print(int(trapezoid))
