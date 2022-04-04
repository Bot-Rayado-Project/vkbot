import re
import aiofile
import glob
import requests

from typing import NamedTuple
from bs4 import BeautifulSoup
from datetime import datetime

from utils.aiohttp_requests import aiohttp_fetch_schedule
from utils.terminal_codes import print_error, print_info
from utils.constants import STREAMS_IDS, STREAMS


# Закомментировать для локального тестирования
'''import asyncio
import sys
import os
sys.path.append(os.path.abspath('./utils'))
from aiohttp_requests import aiohttp_fetch_schedule
from terminal_codes import print_error, print_info
from constants import STREAMS_IDS, STREAMS'''
# Раскоментить для локального тестирования


class GroupInfo(NamedTuple):
    stream: str
    group: str


def get_default_keys() -> dict | None:
    '''Задает стартовые сигнатуры для каждого потока. Вызывается единожды - при запуске бота.'''
    soup = BeautifulSoup(requests.get("https://mtuci.ru/time-table/").text, 'lxml')
    default_keys: dict = {}
    for link in soup.find_all('a'):
        _link = link.get('href')
        try:
            if _link.lower().startswith('/upload/') and "1-kurs" in _link.lower():
                for stream in STREAMS:
                    if STREAMS_IDS[stream] in _link.lower():
                        print_info(_link)
                        default_keys[stream] = _link[15:18]
        except AttributeError:
            pass
        except KeyError:
            print_error("Ошибка задания стартовых ключей ключей.")
            return None
    print_info(f'Стартовые сигнатуры заданы: {default_keys}')
    return default_keys


default_keys: dict = get_default_keys()


async def recieve_time_table(group: str) -> None:
    '''Парсит сайт с расписаниями, скачивает таблицу по запросу потока group. Записывает в файл table_{USER_ID}
    При успешной скачке и записи в файл возвращает NamedTuple data (GroupInfo) с ключами stream, group. Пример ("бвт","2103")'''
    start_time = datetime.now()
    print_info("Парсинг сайта.")
    responce = await aiohttp_fetch_schedule("https://mtuci.ru/time-table/")
    print_info(datetime.now() - start_time)
    soup = BeautifulSoup(responce, 'lxml')
    data = GroupInfo(re.sub('[^а-я]', '', group), re.sub('[^0-9]', '', group))
    print_info('Обработка скачки.')
    print_info("Перед входом в цикл поиска ссылок")
    print_info(datetime.now() - start_time)
    for link in soup.find_all('a'):
        _link = link.get('href')
        try:
            if _link.startswith('/upload/') and "1-kurs" in _link and STREAMS_IDS[data.stream] in _link.lower():
                path = False if len(glob.glob(f'tables/table_{data.stream}.xlsx')) == 0 else glob.glob(f'tables/table_{data.stream}.xlsx')[0]
                print_info(_link)
                if path == False:
                    print_info(f'Выбран {data.stream} поток, {STREAMS_IDS[data.stream]} направление. Таблица не скачана.')
                    async with aiofile.async_open(f'tables/table_{data.stream}.xlsx', 'wb') as table:
                        await table.write(await aiohttp_fetch_schedule('https://mtuci.ru' + _link, True))
                    print_info(datetime.now() - start_time)
                    return data
                else:
                    key = default_keys[data.stream]
                    print_info(f'Выбран {data.stream} поток, {STREAMS_IDS[data.stream]} направление. Таблица скачана.')
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
        res = await recieve_time_table('бик2101')
        print(res)
    asyncio.run(main())
'''
