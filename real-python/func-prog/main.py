import collections
import itertools
from functools import reduce
from pprint import pprint

"""
Mutable data structures can cause problems with parallelism.
You would have to lock the object to prevent mutations during parallel processing.
"""
scientists = [
    {'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
    {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False},
]

scientists[0]['name'] = 'Anthony'  # not great for functional programming

"""
collections lib has a namedtuple option for working with immutable datastructures
"""

Scientist = collections.namedtuple('Scientists', ['name', 'field', 'born', 'nobel'])
Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False)

"""
Mixing mutable and immutable datastructures?
"""
scientists = [
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
]

# still mutable, can modify the scientists list
del scientists[1]  # allowed - not great

# create a tuple instead!
scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Noether', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

# pprint(scientists)
"""
filter function
    - filter a list down to a given set of criteria
    - in Python 3, this returns a filter object (iterable object)
"""

fs = tuple(filter(lambda x: x.field == 'physics' and x.nobel is True, scientists))
# pprint(fs)

# list vs generator comprehensions
# list collects into memory at once
# generator lazily loads values - more memory efficient
# pprint(tuple([x for x in scientists if x.nobel is True]))
# pprint(tuple({x for x in scientists if x.nobel is True}))

"""
map function
    - apply a function to every element in an iterable
    - in Python 3, this returns a map object (iterable object)
"""
names_and_ages = tuple(map(
    lambda x: {'name': x.name, 'age': 2023 - x.born},
    scientists
))
# pprint(names_and_ages)
"""
    It is more "pythonic" to use list / generator comprehensions
"""
# pprint(tuple([{'name': x.name, 'age': 2023 - x.born} for x in scientists]))
# pprint(tuple({'name': x.name, 'age': 2023 - x.born} for x in scientists))


"""
reduce function
    - "aggregate" or "collect" value into a single value from an iterable
    - python3 requires this to be imported
"""

names_and_ages = tuple(
    {'name': x.name, 'age': 2023 - x.born}
    for x in scientists
)

total_age = reduce(lambda acc, val: acc + val['age'], names_and_ages, 0)
# pprint(names_and_ages)
# pprint(total_age)

# alernative 'pythonic' summation function
total_age = sum(x['age'] for x in names_and_ages)


# pprint(total_age)


def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc


scientsts_by_field = reduce(
    reducer,
    scientists,
    collections.defaultdict(list)
)
# pprint(scientsts_by_field)

scientsts_by_field = {
    item[0]: list(item[1])
    for item in itertools.groupby(scientists, lambda x: x.field)
}
# pprint(scientsts_by_field)
