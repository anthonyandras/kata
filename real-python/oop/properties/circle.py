class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get Radius")
        return self._radius

    def _set_radius(self, value):
        print("Set Radius")
        self._radius = value

    def _del_radius(self):
        print("Delete Radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius
    )


if __name__ == '__main__':
    circle = Circle(42.0)
    print(circle.radius)
    circle.radius = 43.0
    del circle.radius
