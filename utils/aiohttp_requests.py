import aiohttp


async def aiohttp_fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def aiohttp_fetch_schedule(url: str, content: bool = False) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if content:
                return await response.content.read()
            else:
                return await response.text()
