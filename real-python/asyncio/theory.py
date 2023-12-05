"""
We start with generators, produces a sequence of values (objects)
After, we move into coroutines, building up a foundational understanding of asyncio
"""

from random import randint
import time
import asyncio


def odds(start, stop):
    """
    Not really odd, but this works for playing around
    """
    for odd in range(start, stop + 1, 2):
        yield odd  # return out the first value, then pause, then caller will ask to resume


# def randn():
#     """Not a coroutine, simple function"""
#     time.sleep(3)
#     return randint(1,10)


async def randn():
    """coroutine, simple function"""
    await asyncio.sleep(3)  # async calls require await - any call after this function will not happen
    # until this resolves
    return randint(1, 10)


async def square_odds(start, stop):
    """asynchronous generator example"""
    for odd in odds(start, stop):
        await asyncio.sleep(2)  # mock io
        yield odd ** 2


async def main():
    odd_values = [odd for odd in odds(3, 15)]
    odds2 = tuple(odds(21, 29))
    print(odd_values)
    print(odds2)

    # start_time = time.perf_counter()
    # r = await randn()
    # elapsed = time.perf_counter() - start_time
    # print(f"{r} took {elapsed:0.2f} seconds")

    start_time = time.perf_counter()
    # r = await asyncio.gather(*(randn() for _ in range(10000)))
    elapsed = time.perf_counter() - start_time
    # print(f"{r} took {elapsed:0.2f} seconds")

    async for so in square_odds(11, 17):
        print('so:', so)

if __name__ == '__main__':
    asyncio.run(main())
