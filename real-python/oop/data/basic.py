from dataclasses import dataclass, field, fields
from typing import Any
from math import asin, cos, radians, sin, sqrt


@dataclass(order=True)
class Position:
    name: str
    sort_index: int = field(init=False, repr=False)
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})

    def distance_to(self, other):
        r = 6371
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2) ** 2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2)
        return 2 * r * asin(sqrt(h))

    # def __post_init(self):
    #     self.sort_index =


@dataclass
class WithoutExplicitTypes:
    """Do not do this unless it's necessary"""
    name: Any
    value: Any = 42


if __name__ == '__main__':
    pos = Position('Oslo', 10.8, 59.9)
    print(pos)
    print(pos.lat)
    print(f"{pos.name} is at {pos.lat}N, {pos.lon}E")
    print(fields(Position))
