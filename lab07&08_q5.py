class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


rectangle = Rectangle(5, 3)
circle = Circle(2)

print("Rectangle:")
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")

print("\nCircle:")
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")


print("\nDemonstrating inheritance")
print(f"Is Rectangle a Shape? {isinstance(rectangle, Shape)}")
print(f"Is Circle a Shape? {isinstance(circle, Shape)}")
