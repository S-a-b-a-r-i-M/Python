import asyncio
import requests

def http_get_sync(url: str):
    response = requests.get(url=url)
    return response.json()


async def http_get_async(url: str):
    return await asyncio.to_thread(http_get_sync, url)