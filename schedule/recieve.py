import re
import aiofile

from typing import NamedTuple
from bs4 import BeautifulSoup

""" from utils.aiohttp_requests import aiohttp_fetch_schedule
from utils.terminal_codes import print_error """

import os
import sys
sys.path.append(os.path.abspath('./utils'))
from aiohttp_requests import aiohttp_fetch_schedule
from terminal_codes import print_error


class GroupInfo(NamedTuple):
    stream: str
    group: str


async def recieve_time_table(group: str, user_id: str) -> None:
    '''Парсит сайт с расписаниями, скачивает таблицу по запросу потока group. Записывает в файл table_{USER_ID}
    При успешной скачке и записи в файл возвращает NamedTuple data (GroupInfo) с ключами stream, group. Пример ("бвт","2103")'''
    responce = await aiohttp_fetch_schedule("https://mtuci.ru/time-table/")
    soup = BeautifulSoup(responce, 'lxml')
    data = GroupInfo(re.sub('[^а-я]', '', group), re.sub('[^0-9]', '', group))
    STREAM_ID: dict = {'бвт': '09.03.01', 'бст': '09.03.02', 'бфи': '02.03.02', 'биб': '10.03.01'}
    for link in soup.find_all('a'):
        _link = link.get('href')
        try:
            if _link.startswith('/upload/') and "IT" in _link and "1-kurs" in _link and STREAM_ID[data.stream] in _link:
                async with aiofile.async_open('tables/table_{}.xlsx'.format(user_id), 'wb') as table:
                    await table.write(await aiohttp_fetch_schedule('https://mtuci.ru' + _link, True))
                return data
        except AttributeError:
            pass
        except KeyError:
            print_error("Ошибка скачмванмя таблицы.")
            return None
