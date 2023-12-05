import math


class PolarPoint:
    def __init__(self, distance, angle):
        self.distance = distance
        self.angle = angle

    @classmethod
    def from_cartesian(cls, x, y):
        distance = math.dist((0, 0), (x, y))
        angle = math.degrees(math.atan2(x, y))
        return cls(distance, angle)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(distance={self.distance:.1f},angle={self.angle:.1f})"
        )


if __name__ == '__main__':
    p = PolarPoint(13, 22.6)
    p1 = PolarPoint.from_cartesian(x=12, y=5)