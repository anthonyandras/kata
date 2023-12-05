from shapes import Square, Triangle


class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def what_am_i(self):
        return 'RightPyramid'


if __name__ == '__main__':
    rightpyramid = RightPyramid(2, 4)
    print(super(RightPyramid, rightpyramid).what_am_i())
    print(rightpyramid.__class__)  # print class of instance
    print(rightpyramid.__class__.__bases__)  # print super classes
    print(RightPyramid.__mro__)  # print inheritance tree (determines order of name lookup)
