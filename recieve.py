import aiohttp
from aiofile import async_open

async def aiohttp_fetch(url: str, content: bool = False) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if content:
                return await response.content.read()
            else:
                return await response.text()

async def recieve_time_table_bvt(group:str, user_id:str ) -> None:
    response = await aiohttp_fetch("https://mtuci.ru/time-table/")
    data = (group[:-4], group[3:])
    

'''async def recieve_time_table(group: str) -> None:
    response = await aiohttp_fetch("https://mtuci.ru/time-table/")
    data = (group[:-4], group[3:])
    match data:
        case "бвт", number:
            a = response.find('09.03.01')
            with open('table.xlsx', 'wb') as table:
                table.write(await aiohttp_fetch('https://mtuci.ru/' + response[a - 29: a + 52], True))
            return data
        case "бфи", number:
            a = response.find('02.03.02')
            with open('table.xlsx', 'wb') as table:
                table.write(await aiohttp_fetch('https://mtuci.ru/' + response[a - 29: a + 71], True))
            return data
        case "бст", number:
            a = response.find('09.03.02')
            with open('table.xlsx', 'wb') as table:
                table.write(await aiohttp_fetch('https://mtuci.ru/' + response[a - 29: a + 51], True))
            return data'''