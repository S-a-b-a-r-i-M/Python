import asyncio
from time import perf_counter

from random import randint

from http_req_sync_async import http_get_sync, http_get_async

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


async def main():
    start_time = perf_counter()
    for _ in range(20):
        id = randint(1,MAX_POKEMON)
        poke_name = get_pokemon_name_sync()
        print(poke_name)
    print('Time taken by sync program : ', perf_counter() - start_time)

    start_time = perf_counter()
    poke_names = await asyncio.gather(get_pokemon_name_async() for _ in range(20))
    print(poke_names)
    print('Time taken by async program : ', perf_counter() - start_time)

asyncio.run(main())