import re
import os
import aiofile
import glob

from entry import default_keys

from typing import NamedTuple
from bs4 import BeautifulSoup
from datetime import datetime

from utils.aiohttp_requests import aiohttp_fetch_schedule
from utils.terminal_codes import print_error, print_info

# Закомментировать для локального тестирования
'''
import asyncio
import sys
sys.path.append(os.path.abspath('./utils'))
from aiohttp_requests import aiohttp_fetch_schedule
from terminal_codes import print_error'''
# Раскоментить для локального тестирования


class GroupInfo(NamedTuple):
    stream: str
    group: str


async def recieve_time_table(group: str) -> None:
    '''Парсит сайт с расписаниями, скачивает таблицу по запросу потока group. Записывает в файл table_{USER_ID}
    При успешной скачке и записи в файл возвращает NamedTuple data (GroupInfo) с ключами stream, group. Пример ("бвт","2103")'''
    start_time = datetime.now()
    responce = await aiohttp_fetch_schedule("https://mtuci.ru/time-table/")
    soup = BeautifulSoup(responce, 'lxml')
    data = GroupInfo(re.sub('[^а-я]', '', group), re.sub('[^0-9]', '', group))
    print_info('Обработка скачки.')
    STREAM_ID: dict = {'бвт': '09.03.01', 'бст': '09.03.02', 'бфи': '02.03.02', 'биб': '10.03.01', 'бэи': '09.03.03', 'бин': '11.03.02',
                       'бмп': '01.03.04', 'зрс': '10.05.02', 'бап': '15.03.04', 'бут': '27.03.04', 'брт': '11.03.01', 'бээ': '38.03.01',
                       'бби': '38.03.05', 'бэр': '42.03.01'}
    FACULTIES: list = ["it", "kiib", "siss", "rit", "tseimk"]
    for link in soup.find_all('a'):
        _link = link.get('href')
        try:
            if _link.startswith('/upload/') and any(fac in _link.lower() for fac in FACULTIES) and "1-kurs" in _link and STREAM_ID[data.stream] in _link:
                path = False if len(glob.glob(f'tables/table_{data.stream}.xlsx')) == 0 else glob.glob(f'tables/table_{data.stream}.xlsx')[0]
                if path == False:
                    print_info(f'Выбран {data.stream} поток, {STREAM_ID[data.stream]} направление. Таблица не скачана.')
                    async with aiofile.async_open(f'tables/table_{data.stream}.xlsx', 'wb') as table:
                        await table.write(await aiohttp_fetch_schedule('https://mtuci.ru' + _link, True))
                    print_info(datetime.now() - start_time)
                    return data
                else:
                    key = default_keys[data.stream]
                    print_info(f'Выбран {data.stream} поток, {STREAM_ID[data.stream]} направление. Таблица скачана.')
                    if _link[15:18] == key:
                        print_info('Сигнатура таблицы равна сигнатуре с сайта.')  # поместить новый ключ в хранилище
                        print_info(datetime.now() - start_time)
                        return data
                    else:
                        print_info(f'Сигнатура {key} изменилась на {_link[15:18]}.')
                        default_keys.update({data.stream: _link[15:18]})
                        async with aiofile.async_open(f'tables/table_{data.stream}.xlsx', 'wb') as table:
                            await table.write(await aiohttp_fetch_schedule('https://mtuci.ru' + _link, True))
                        print_info(datetime.now() - start_time)
                        return data
        except AttributeError:
            pass
        except KeyError:
            print_error("Ошибка скачивания таблицы.")
            return None

# Раскоментировать для локального тестирования
'''if __name__ == '__main__':
    async def main():
        res = await recieve_time_table('бин2101', '3123123')
        print(res)
    asyncio.run(main())
'''
