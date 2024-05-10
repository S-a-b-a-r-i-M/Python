import asyncio
from time import perf_counter

from random import randint
from typing import AsyncIterable

from HTTP_req_sync_async import http_get_sync, http_get_async

# INTRO 
async def dog():
    await asyncio.sleep(1)
    print('wow')

async def cat():
    await asyncio.sleep(2)
    print('meow')

async def main():
    start_time = perf_counter()
    # await dog()
    # await cat()
    await asyncio.gather(dog(), cat())
    print(f'Time taken {perf_counter() - start_time : .2f}')

# if __name__ == '__main__':
#     asyncio.run(main())


# WITH EXTERNAL APIS
MAX_POKEMON = 898

def get_pokemon_name_sync() -> str:
    id = randint(1,MAX_POKEMON)
    poke_url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    res = http_get_sync(poke_url)
    return str(res['name'])

async def get_pokemon_name_async():
    id = randint(1,MAX_POKEMON)
    poke_url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    res = await http_get_async(poke_url)
    return str(res['name'])

async def next_pokemon_name(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        name = await get_pokemon_name_async()
        yield name


async def main():
    # synchronous method 
    start_time = perf_counter()
    for _ in range(10):
        poke_name = get_pokemon_name_sync()
        print(poke_name)
    print(f'Time taken by synchronous program : {perf_counter() - start_time :.2f} seconds')

    # asynchronous method using asyncio.gather
    """
    asyncio.gather function is used to concurrently execute multiple coroutine objects (async operations) and gather their results. 
    By passing the list of coroutine objects as arguments using the * operator, asyncio.gather schedules them to run concurrently.
    """
    start_time = perf_counter()
    # The * operator is known as the "unpacking" operator or the "star" operator
    poke_names = await asyncio.gather(*[get_pokemon_name_async() for _ in range(10)])
    print(poke_names)
    print(f'Time taken by async program (gather): {perf_counter() - start_time :.2f} seconds')

    # asynchronous method using async generator
    ''' start_time = perf_counter()
    async for name in next_pokemon_name(10):
        print(name)
    print(f'Time taken by async program (generator): {perf_counter() - start_time :.2f} seconds')'''

asyncio.run(main())