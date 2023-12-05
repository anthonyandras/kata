class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def what_am_i(self):
        return 'Rectangle'


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def what_am_i(self):
        return 'Triangle'


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def what_am_i(self):
        return 'Square'


class Cube(Square):
    def surface_area(self):
        face_area = self.area()
        return face_area * 6

    def volume(self):
        face_area = super().area()  # ignores any implementation in the current class
        return face_area * self.length

    def what_am_i(self):
        return 'Cube'

    def family_tree(self):
        return f"{self.what_am_i()} child of {super().what_am_i()}"


if __name__ == '__main__':
    square = Square(4)
    print(square.length)
    print(square.area())
    print(dir(square))

    rectangle = Rectangle(2, 4)
    print(rectangle.area())
    print(rectangle.perimeter())
    print(rectangle.what_am_i())

    cube = Cube(5)
    print(cube.what_am_i())
    print(cube.family_tree())
