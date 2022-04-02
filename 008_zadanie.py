# str. 84

"""

"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        return super().__init__(side, side)

if __name__ == "__main__":
    rect = Rectangle(2, 3)
    _ = rect.perimeter()
    print(f"perimeter: {_}")

    _ = rect.area()
    print(f"area: {_}")

    sq = Square(10)

    _ = sq.perimeter()
    print(f"perimeter: {_}")

    _ = sq.area()
    print(f"area: {_}")