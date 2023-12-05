from dataclasses import dataclass, field


# @dataclass(frozen=True)
@dataclass()
class Position:
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})


@dataclass()
class Capital(Position):
    """If parent has default values, all fields in child must have default values"""
    country: str = 'Unknown'


if __name__ == '__main__':
    pos = Position('Chicago', 0.0, 0.0)
    print(pos.lat)
    pos.lat = 53.2  # not allowed
