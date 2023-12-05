import collections
import time
import concurrent.futures
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
    """
        Because of the global interpreter lock, process parallelism 
        is better. No two threads can execute at the same time, and the 
        executing thread must be blocked in order for the waiting thread
        to pick up executing
    """
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = executor.map(transform, scientists)
    end = time.time()

    print(f"\nTime to complete: {end - start}s\n")

    pprint(tuple(result))
