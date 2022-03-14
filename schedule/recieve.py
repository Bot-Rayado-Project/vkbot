from aiofile import async_open
#from utils.aiohttp_requests import aiohttp_fetch_schedule
import os
import sys
sys.path.append(os.path.abspath('../utils'))
from aiohttp_requests import aiohttp_fetch_schedule


async def recieve_time_table(group: str, user_id: str) -> None:
    response = await aiohttp_fetch_schedule("https://mtuci.ru/time-table/")
    data = (group[:-4], group[3:])
    match data:
        case "бвт", number:
            a = response.find('09.03.01')
            async with async_open('tables/table_{}.xlsx'.format(user_id), 'wb') as table:
                await table.write(await aiohttp_fetch_schedule('https://mtuci.ru/' + response[a - 29: a + 54], True))
            return data
        case "бфи", number:
            a = response.find('02.03.02')
            async with async_open('tables/table_{}.xlsx'.format(user_id), 'wb') as table:
                await table.write(await aiohttp_fetch_schedule('https://mtuci.ru/' + response[a - 29: a + 76], True))
            return data
        case "бст", number:
            a = response.find('09.03.02')
            async with async_open('tables/table_{}.xlsx'.format(user_id), 'wb') as table:
                await table.write(await aiohttp_fetch_schedule('https://mtuci.ru/' + response[a - 29: a + 53], True))
            return data
