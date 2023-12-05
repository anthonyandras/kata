import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(radius=diameter / 2)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"{self.__class__.__name__}(radius={self.radius})"


if __name__ == "__main__":
    circle = Circle(42)
    print(circle.area())
    print(circle.perimeter())

    circle = Circle.from_diameter(84)
    print(circle.area())
