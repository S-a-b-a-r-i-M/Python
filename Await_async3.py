import asyncio
import requests 

from time import perf_counter


async def counter(num: int):
    for i in range(num):
        await asyncio.sleep(0.700)
        print(i,' Waiting...')


def send_request(url: str) -> int:
    print('GET request sent')
    before = perf_counter()
    responce = requests.get(url)
    print('Time taken by request is', perf_counter() - before)
    return responce.status_code


async def send_async_request(url: str) -> int:
    # RUNNING AN SYNC FUN AS ASYNC FUN
    return await asyncio.to_thread(send_request, url)


async def main():
    url = "https://google.com/"
    # IN THIS SECTION ONCE THE COUNTER WILL EXECUTE AFTER THE send_request() completed
    '''print(send_request(url))
    await counter(5)'''

    # USING to_thread()
    '''print('status code:',await send_async_request(url))
    await counter(5)'''

    # USING AN task WITH to_thread()
    # NOTE : in this example you can see the cpu executes task1 little bit then task2 little bit,like that
    '''task = asyncio.create_task(counter(5))
    print('status code:',await send_async_request(url))
    await task'''

    # USING asyncio.gather()
    await asyncio.gather(send_async_request(url),counter(5))


asyncio.run(main())