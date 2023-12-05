class CumulativePowerFactory:
    def __init__(self, exponent=2, *, start=0):
        """Use optional arguments instead of multiple constructors"""
        self._exponent = exponent
        self.total = start

    def __call__(self, base):
        power = base ** self._exponent
        self.total += power
        return power


if __name__ == '__main__':
    square = CumulativePowerFactory()
    print(square(21))
    print(square(42))
    cube = CumulativePowerFactory(exponent=3)
    print(cube(3))
    initialized_cube = CumulativePowerFactory(3, start=2205)
    print(initialized_cube(42))
    print(initialized_cube.total)
