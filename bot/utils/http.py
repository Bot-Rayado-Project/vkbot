import aiohttp


async def aiohttp_fetch(url: str) -> str:
    '''[GET] запрос на получения данных с какого-либо сайта с возвратом текста'''
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def post_request(url: str, data: dict) -> str:
    '''[POST] запрос на какой-либо сайт с возвратом результата запроса'''
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, json=data) as response:
            return await response.text()
