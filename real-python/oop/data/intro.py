from dataclasses import dataclass
import attr


@dataclass
class DataClassCard:
    rank: str
    suit: str


@attr.s
class AttrsCard:
    """Alternative to data classes in which data classes drew inspiration from: http://www.attrs.org"""
    rank = attr.ib()
    suit = attr.ib()


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(rank={self.rank!r}, suit={self.suit!r})")

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)


if __name__ == '__main__':
    queen_of_hearts = DataClassCard('Q', 'Hearts')
    print(queen_of_hearts.rank)

    from collections import namedtuple

    NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])
    queen_of_hearts = NamedTupleCard('Q', 'Hearts')
    # theoretically, at the surface, this will take the place of a data classes -
    # though we lose a lot from not using them
