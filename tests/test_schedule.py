import asyncio
from urllib import response
import pytest


from schedule.sheethandler import sheethandler
# Закомментировать для локального тестирования
""" import os
import sys
sys.path.append(os.path.abspath('../schedule'))
import sheethandler """
# Раскоментить для локального тестирования, также раскоментить соответсвующее во всех файлах schedule


@pytest.mark.asyncio  # Общий тест для всех групп на сегодня или завтра, на просто вывод
@pytest.mark.parametrize('day, group, week_type, excepted',
                         [('завтра', 'бвт2101', 'текущая неделя', 'None'),
                          ('завтра', 'бвт2102', 'текущая неделя', 'None'),
                             ('завтра', 'бвт2103', 'текущая неделя', 'None'),
                             ('завтра', 'бвт2104', 'текущая неделя', 'None'),
                             ('завтра', 'бвт2105', 'текущая неделя', 'None'),
                             ('завтра', 'бвт2106', 'текущая неделя', 'None'),
                             ('завтра', 'бвт2107', 'текущая неделя', 'None'),
                             ('завтра', 'бвт2108', 'текущая неделя', 'None'),
                             ('завтра', 'бфи2101', 'текущая неделя', 'None'),
                             ('завтра', 'бфи2102', 'текущая неделя', 'None'),
                             ('завтра', 'бст2101', 'текущая неделя', 'None'),
                             ('завтра', 'бст2102', 'текущая неделя', 'None'),
                             ('завтра', 'бст2103', 'текущая неделя', 'None'),
                             ('завтра', 'бст2104', 'текущая неделя', 'None'),
                             ('завтра', 'бст2105', 'текущая неделя', 'None'),
                             ('завтра', 'бст2106', 'текущая неделя', 'None'),
                             ('завтра', 'бэи2101', 'текущая неделя', 'None'),
                             ('завтра', 'бэи2102', 'текущая неделя', 'None'),
                             ('завтра', 'бэи2103', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2101', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2102', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2103', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2104', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2105', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2106', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2107', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2108', 'текущая неделя', 'None'),
                             ('сегодня', 'бфи2101', 'текущая неделя', 'None'),
                             ('сегодня', 'бфи2102', 'текущая неделя', 'None'),
                             ('сегодня', 'бст2101', 'текущая неделя', 'None'),
                             ('сегодня', 'бст2102', 'текущая неделя', 'None'),
                             ('сегодня', 'бст2103', 'текущая неделя', 'None'),
                             ('сегодня', 'бст2104', 'текущая неделя', 'None'),
                             ('сегодня', 'бст2105', 'текущая неделя', 'None'),
                             ('сегодня', 'бст2106', 'текущая неделя', 'None'),
                             ('сегодня', 'бэи2101', 'текущая неделя', 'None'),
                             ('сегодня', 'бэи2102', 'текущая неделя', 'None'),
                             ('сегодня', 'бэи2103', 'текущая неделя', 'None')])
async def test_schedule(day, group, week_type, excepted):
    assert excepted not in await sheethandler.print_schedule(day, group, '123', week_type)


@pytest.mark.asyncio  # Тест на количество пар, проверяю через количество разделений пар,
# так как их энивей больше 7 быть не может(не должно)
@pytest.mark.parametrize('day, group, week_type, excepted',
                         [('завтра', 'бвт2101', 'текущая неделя', '7'),
                          ('завтра', 'бвт2102', 'текущая неделя', '7'),
                             ('завтра', 'бвт2103', 'текущая неделя', '7'),
                             ('завтра', 'бвт2104', 'текущая неделя', '7'),
                             ('завтра', 'бвт2105', 'текущая неделя', '7'),
                             ('завтра', 'бвт2106', 'текущая неделя', '7'),
                             ('завтра', 'бвт2107', 'текущая неделя', '7'),
                             ('завтра', 'бвт2108', 'текущая неделя', '7'),
                             ('завтра', 'бфи2101', 'текущая неделя', '7'),
                             ('завтра', 'бфи2102', 'текущая неделя', '7'),
                             ('завтра', 'бст2101', 'текущая неделя', '7'),
                             ('завтра', 'бст2102', 'текущая неделя', '7'),
                             ('завтра', 'бст2103', 'текущая неделя', '7'),
                             ('завтра', 'бст2104', 'текущая неделя', '7'),
                             ('завтра', 'бст2105', 'текущая неделя', '7'),
                             ('завтра', 'бст2106', 'текущая неделя', '7'),
                             ('завтра', 'бэи2101', 'текущая неделя', '7'),
                             ('завтра', 'бэи2102', 'текущая неделя', '7'),
                             ('завтра', 'бэи2103', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2101', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2102', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2103', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2104', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2105', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2106', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2107', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2108', 'текущая неделя', '7'),
                             ('сегодня', 'бфи2101', 'текущая неделя', '7'),
                             ('сегодня', 'бфи2102', 'текущая неделя', '7'),
                             ('сегодня', 'бст2101', 'текущая неделя', '7'),
                             ('сегодня', 'бст2102', 'текущая неделя', '7'),
                             ('сегодня', 'бст2103', 'текущая неделя', '7'),
                             ('сегодня', 'бст2104', 'текущая неделя', '7'),
                             ('сегодня', 'бст2105', 'текущая неделя', '7'),
                             ('сегодня', 'бст2106', 'текущая неделя', '7'),
                             ('сегодня', 'бэи2101', 'текущая неделя', '7'),
                             ('сегодня', 'бэи2102', 'текущая неделя', '7'),
                             ('сегодня', 'бэи2103', 'текущая неделя', '7')])
async def test_count_pars_schedule(day, group, week_type, excepted):
    response = await sheethandler.print_schedule(day, group, '123', week_type)
    count_pars = response.count('⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n')
    assert count_pars <= int(excepted)


@pytest.mark.asyncio  # Тест, что выводит все дни недели и не выводит лишних, а также правильно дни недели выводит и не выводит пустых ячеек
@pytest.mark.parametrize('day, group, week_type, excepted',
                         [('вся неделя', 'бвт2101', 'текущая неделя', ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                          ('вся неделя', 'бвт2102', 'текущая неделя',
                           ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2103', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2104', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2105', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2106', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2107', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2108', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бфи2101', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бфи2102', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2101', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2102', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2103', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2104', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2105', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2106', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                              ('вся неделя', 'бэи2101', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бэи2102', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бэи2103', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2101', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2102', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2103', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2104', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2105', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2106', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2107', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2108', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бфи2101', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бфи2102', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2101', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2102', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2103', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2104', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2105', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2106', 'следующая неделя', 
                             ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бэи2101', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бэи2102', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бэи2103', 'следующая неделя', 
                             ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None'])])
async def test_full_schedule(day, group, week_type, excepted):
    response = await sheethandler.print_schedule(day, group, '123', week_type)
    assert (excepted[0] in response[1]
            and excepted[1] in response[2]
            and excepted[2] in response[3]
            and excepted[3] in response[4]
            and excepted[4] in response[5]
            and excepted[5] in response[6]
            and excepted[6] not in response[1]
            and excepted[6] not in response[2]
            and excepted[6] not in response[3]
            and excepted[6] not in response[4]
            and excepted[6] not in response[5]
            and excepted[6] not in response[6])
