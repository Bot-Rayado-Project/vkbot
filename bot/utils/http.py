import aiohttp


async def aiohttp_fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def post_request(url: str, data: dict) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, json=data) as response:
            return await response.text()
