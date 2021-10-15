import aiohttp


async def get(*args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.get(*args, **kwargs) as resp:
            return await resp.json()


async def post(*args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(*args, **kwargs) as resp:
            return await resp.json()