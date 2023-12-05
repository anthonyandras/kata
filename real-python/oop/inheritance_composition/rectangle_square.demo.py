class Rectangle:
    def __init__(self, length, height):
        self._length = length
        self._height = height

    @property
    def area(self):
        return self._length * self._height

    def resize(self, length, height):
        """Note that square and rectangle require different interfaces"""
        self._length = length
        self._height = height


class Square(Rectangle):
    def __init__(self, side_size):
        super().__init__(side_size, side_size)


if __name__ == '__main__':
    rectangle = Rectangle(2, 4)
    assert rectangle.area == 8
    square = Square(2)
    assert square.area == 4

    print("Ok!")
