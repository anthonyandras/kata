class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("delete radius")
        del self._radius


if __name__ == '__main__':
    circle = Circle(42.0)
    print(circle.radius)
    circle.radius = 43.0
    del circle.radius
