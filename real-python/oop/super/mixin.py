from shapes import Square, Triangle


class SurfaceAreaMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:  # we assume "inheriting" class has 'surfaces' property defined
            surface_area += surface.area(self)

        return surface_area


class RightPyramid(Square, Triangle, SurfaceAreaMixin):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        self.height = slant_height
        self.length = base
        self.width = base

        self.surfaces = [Square, Triangle, Triangle, Triangle, Triangle]


class Cube(Square, SurfaceAreaMixin):
    def __init__(self, length):
        super().__init__(length)
        self.surfaces = [Square, Square, Square, Square, Square]


if __name__ == '__main__':
    p = RightPyramid(5, 14)
    print(p.surface_area())

    c = Cube(5)
    print(c.surface_area())
