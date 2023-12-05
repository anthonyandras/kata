class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        """passing objects to print will return this string, intended for human consumption"""
        return f"a {self.color} car"

    def __repr__(self):
        """unambiguous - be as explict as possible about what this object is"""
        return f"{self.__class__.__name__}({self.color}, {self.mileage})"


if __name__ == '__main__':
    my_car = Car('red', 37281)
    print(my_car)
