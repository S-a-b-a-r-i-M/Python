import asyncio
import time

'''
async def greet():
    print('Hello universe')
    await asyncio.sleep(1)  # HERE asyncio.sleep CREATES A <coroutine object sleep at 0x7f8f68707610> OBJECT AND AWAIT WILL EXECUTES THE COROUTINE OBJECT
   # obj = leaving()
    task = asyncio.create_task(leaving()) # THIS WILL TELL EXECUTE THE TASK AS SOON AS POSSIBLE ,MEANWHILE MOVE TO ANOTHER TASK CONCURRENTLY (or) Creates an asynchronous task for the leaving coroutine. This task will execute leaving() concurrently while greet() continues.
    # await task

    print('im leaving\n', task)
    await asyncio.sleep(5)

async def leaving():
    print('bye bye!!!')
    await asyncio.sleep(5)
    print('see you again')


asyncio.run(greet())  # HERE greet() fun RETURNS  AN COROUTINE OBJ. asyncio.run() -> CREATES AN EVENT LOOP
# print('you can see the coroutine object here :',greet())
'''
async def hello():
    for i in range(10):
        continue
    await asyncio.sleep(1)
    return True



async def start():
    print('set.. ')
    task1 = asyncio.create_task(count())
    print('Go...')
    await asyncio.sleep(1)
    print('Finished!!!!')
    await task1


async def count():
    print('counting....')
    for i in range(6):
        print(i)
        await asyncio.sleep(0.25)


async def get():
    print('get.')
    res = await hello()
    await start()


# CREATING AN EVENT LOOP
asyncio.run(get())


# ------------------------ REAL TIME DIFFERENCE OF NORMAL FUNCTION AND ASYNC FUNCTION-------------------------------

async def async_30000():
    print("async_30000 is invoked")
    for i in range(1, 300000000):
        continue
    print("async_30000 is completed")


async def async_fun():
    res1 =  asyncio.create_task(async_30000())
    for i in ['a-sync']*10:
        print(i, end=' ')
    return True


def sync_30000():
    print("sync_30000 is invoked")
    for i in range(1, 300000000):
        continue
    print("sync_30000 is completed")


def sync_fun():
    print()
    sync_30000()
    for i in ['sync']*10:
        print(i, end=' ')
    return True


async def comparison_start():
    if await async_fun():
        print('async finished')
    if sync_fun():
        print('sync finished')


# asyncio.run(comparison_start())
