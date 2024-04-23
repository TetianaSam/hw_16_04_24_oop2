import pickle

class Shape:
    def __init__(self):
        pass

    def Show(self):
        pass

    def Save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def Load(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

class Square(Shape):
    def __init__(self, x, y, side_length):
        super().__init__()
        self.x = x
        self.y = y
        self.side_length = side_length

    def Show(self):
        print(f"Square: Upper left corner at ({self.x}, {self.y}), Side length = {self.side_length}")

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"Rectangle: Upper left corner at ({self.x}, {self.y}), Width = {self.width}, Height = {self.height}")

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    def Show(self):
        print(f"Circle: Center at ({self.x}, {self.y}), Radius = {self.radius}")

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"Ellipse: Top corner of circumscribed rectangle at ({self.x}, {self.y}), Width = {self.width}, Height = {self.height}")

shapes = [
    Square(0, 0, 5),
    Rectangle(2, 2, 4, 3),
    Circle(0, 0, 3),
    Ellipse(0, 0, 4, 2)
]

filename = 'shapes.pkl'
for shape in shapes:
    shape.Save(filename)
loaded_shapes = [Shape.Load(filename) for _ in range(len(shapes))]


for shape in loaded_shapes:
    shape.Show()

