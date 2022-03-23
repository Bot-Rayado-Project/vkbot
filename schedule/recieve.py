import re
import os
import aiofile
import glob

from entry import default_keys

from typing import NamedTuple
from bs4 import BeautifulSoup

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


async def recieve_time_table(group: str, user_id: str) -> None:
    '''Парсит сайт с расписаниями, скачивает таблицу по запросу потока group. Записывает в файл table_{USER_ID}
    При успешной скачке и записи в файл возвращает NamedTuple data (GroupInfo) с ключами stream, group. Пример ("бвт","2103")'''
    responce = await aiohttp_fetch_schedule("https://mtuci.ru/time-table/")
    soup = BeautifulSoup(responce, 'lxml')
    data = GroupInfo(re.sub('[^а-я]', '', group), re.sub('[^0-9]', '', group))
    print_info('Обработка скачки.')
    STREAM_ID: dict = {'бвт': '09.03.01', 'бст': '09.03.02', 'бфи': '02.03.02', 'биб': '10.03.01', 'бэи': '09.03.03', 'бин': '11.03.02',
                       'бмп': '01.03.04', 'зрс': '10.05.02', 'бап': '15.03.04', 'бут': '27.03.04', 'брт': '11.03.01'}
    for link in soup.find_all('a'):
        _link = link.get('href')
        try:
            print_info(data.stream)
            print_info(STREAM_ID[data.stream])
            if _link.startswith('/upload/') and ("IT" in _link or "KiIB" in _link or 'SiSS' in _link or 'RiT' in _link) and "1-kurs" in _link and STREAM_ID[data.stream] in _link:
                path = False if len(glob.glob(f'tables/table_{user_id}_*.xlsx')) == 0 else glob.glob(f'tables/table_{user_id}_*.xlsx')[0]
                if path == False:
                    print_info('Файла нет')
                    async with aiofile.async_open('tables/table_{0}_{1}.xlsx'.format(user_id, data.stream), 'wb') as table:
                        await table.write(await aiohttp_fetch_schedule('https://mtuci.ru' + _link, True))
                    return data
                else:
                    if path[-8:-5] == data.stream:
                        print(default_keys)
                        key = default_keys[data.stream]
                        print_info('Выбран тот же поток, что и скачан')
                        if _link[15:18] == key:
                            print_info('Сравнение равен ли текущий ключ тому, что в хранилище')  # поместить новый ключ в хранилище
                            return data
                        else:
                            print_info('Ключ на сайте изменился')
                            default_keys.update({data.stream: _link})
                            async with aiofile.async_open('tables/table_{0}_{1}.xlsx'.format(user_id, data.stream), 'wb') as table:
                                await table.write(await aiohttp_fetch_schedule('https://mtuci.ru' + _link, True))
                            return data
                    else:
                        print_info('Выбран другой поток')
                        os.remove(path)
                        async with aiofile.async_open('tables/table_{0}_{1}.xlsx'.format(user_id, data.stream), 'wb') as table:
                            await table.write(await aiohttp_fetch_schedule('https://mtuci.ru' + _link, True))
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
