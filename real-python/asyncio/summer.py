"""
Application to demonstrate a more "real-world" example of using asyncio
"""
import asyncio
import json
import time

import aiohttp


async def worker(name, n, session):
    print(f"worker-{name}")
    url = f"https://qrng.anu.edu.au/API/jsonI.php?length={n}&type=uint16"
    response = await session.request(method="GET", url=url)
    result = await json.loads(response.text())
    return sum(result['data'])


async def main():
    async with aiohttp.ClientSession() as session:
        sums = await asyncio.gather(*( worker(f'w{i}', n, session) for i, n in enumerate(range(2,5))))
        print(f"sums: {sums}")


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"execution time: {elapsed}")
