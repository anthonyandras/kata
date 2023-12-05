class Point:
    def __init__(self, x, y):
        self.x = Coordinate()
        self.y = Coordinate()


class Coordinate:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        try:
            instance.__dict__[self._name] = float(value)
            print("Validated")
        except ValueError:
            raise ValueError(
                f'"{self._name}" must be a number'
            ) from None
