import collections
import time
import multiprocessing
import os
from pprint import pprint

Scientist = collections.namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])


def transform(x: Scientist):
    print(f"Process {os.getpid()} working on record {x.name}")
    result = {'name': x.name, 'age': 2023 - x.born}
    print(f"Process {os.getpid()} done processing record {x.name}")
    return result


scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Noether', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

if __name__ == '__main__':
    start = time.time()
    pool = multiprocessing.Pool(processes=2, maxtasksperchild=1)
    result = pool.map(transform, scientists)

    # result = tuple(map(
    #     transform,
    #     scientists
    # ))

    end = time.time()

    print(f"\nTime to complete: {end - start}s\n")
    pprint(result)
