import aiohttp
import asyncio

from time import perf_counter

from HTTP_req_sync_async import http_get_sync

# SYNC
# def fetch_data():
#     print("Sync - fetch 15 pokemon names--->")
#     before = perf_counter()
#     poke_name = []
#     for i in range(1,16):
#         poke_url = f"https://pokeapi.co/api/v2/pokemon/{i}"
#         res = http_get_sync(poke_url)
#         poke_name.append(res['name'])
#     print("Time taken for sync method:",perf_counter()-before)
#     print(poke_name)

# fetch_data()

# ASYNC
# async def fetch_data():
#     print("Async - fetch 15 pokemon names--->")
#     before = perf_counter()
#     poke_name = []
#     async with aiohttp.ClientSession() as session:
#         for i in range(1,16):
#             poke_url = f"https://pokeapi.co/api/v2/pokemon/{i}"
#             async with session.get(poke_url) as response:
#                res = await response.json()
#                poke_name.append(res['name'])

#     print("Time taken for async method:",perf_counter()-before)
#     print(poke_name)


# ASYNC - WITH AIOHTTP AND ASYNCIO.GATHER
async def get_data(session, url):
    async with session.get(url) as response:
        response = await response.json()
        return response['name']

async def fetch_data():
    """
    asyncio.ensure_future -> function schedules the execution of the asynchronous task,
    allowing the program to continue executing other tasks concurrently
    """
    print("Async with gather- fetch 15 pokemon names---->")
    before = perf_counter()
    poke_name = []
    actions = []

    async with aiohttp.ClientSession() as session:
        for i in range(1,16):
            poke_url = f"https://pokeapi.co/api/v2/pokemon/{i}"
            actions.append(asyncio.ensure_future(get_data(session, poke_url)))

        poke_name = await asyncio.gather(*actions)

    print(poke_name)
    print("Time taken for async method:",perf_counter()-before)

if __name__ == '__main__':
    asyncio.run(fetch_data())


