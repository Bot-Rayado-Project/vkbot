from datetime import datetime, timedelta
import openpyxl
import os
import glob

from schedule.recieve import recieve_time_table
from utils.terminal_codes import print_error, print_info
from utils.constants_schedule import week_columns_groups
from utils.constants_blueprint import group_matching_schedule, group_matching_full_schedule
from schedule.streams.KIIB.zrc import get_full_schedule_zrc, get_schedule_zrc

import schedule.whataweek as whataweek

start_time = datetime.now() - timedelta(hours=3)
request_time: dict = {'бвт': start_time, 'бст': start_time, 'бфи': start_time, 'биб': start_time, 'бэи': start_time, 'бик': start_time, 'бмп': start_time,
                      'зрс': start_time, 'бап': start_time, 'бут': start_time, 'брт': start_time, 'бээ': start_time, 'бби': start_time, 'бэр': start_time,
                      'бин': start_time}


async def check_right_input(day_input: str, group_input: str, week_type: str) -> bool:

    days = ('сегодня', 'завтра', 'вся неделя')
    groups = ('бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106',
              'бвт2107', 'бвт2108', 'бфи2101', 'бфи2102', 'бст2101', 'бст2102',
              'бст2103', 'бст2104', 'бст2105', 'бст2106', 'бэи2101', 'бэи2102',
              'бэи2103', 'биб2101', 'биб2102', 'биб2103', 'биб2104', 'бмп2101',
              'зрс2101', 'зрс2102', 'бап2101', 'бут2101', 'брт2101', 'брт2102',
              'бик2101', 'бик2102', 'бик2103', 'бик2104', 'бик2105', 'бик2106',
              'бик2107', 'бик2108', 'бик2109', 'бээ2101', 'бби2101', 'бэр2101',
              'бин2101', 'бин2102', 'бин2103', 'бин2104', 'бин2105', 'бин2106',
              'бин2107', 'бин2108', 'бин2109', 'бин2110')
    weeks = ('текущая неделя', 'следующая неделя')

    if day_input in days and group_input in groups and week_type in weeks:
        return True
    else:
        return False


async def week_check(week_type: str) -> str | bool:

    checked = await whataweek.get_week()
    if checked == False:
        print_error('Ошибка в чётности недели')
        return False

    if week_type == 'текущая неделя':
        return checked

    else:
        if checked == 'четная':
            return 'нечетная'

        else:
            return 'четная'  # Тут и тупой поймёт чо происходит


async def get_sheet(group: str, stream: str, temp_number: str) -> openpyxl.Workbook | bool:
    global request_time

    if not os.path.isdir("tables"):
        os.mkdir("tables")

    print_info(f'Последнее время запроса таблцы: {request_time[stream]}. Текущее время: {datetime.now()}')
    print_info(f'Разность времени: {abs(request_time[stream].timestamp() - datetime.now().timestamp())}')
    if abs(request_time[stream].timestamp() - datetime.now().timestamp()) > 300.0:  # 300 секунд
        print_info("Между запросами прошло больше минуты. Отправлен запрос в recieve_time_table.")
        await recieve_time_table(group)  # Запрос на скачку таблицы
        request_time.update({stream: datetime.now()})
        print_info(f"Таблица скачана. Текущее состояния ключа времени запроса: {request_time[stream]}")
    else:
        print_info("Между запросами прошло меньше 5 минут. Скачка отменена.")
        path = False if len(glob.glob(f'tables/table_{stream}.xlsx')) == 0 else glob.glob(f'tables/table_{stream}.xlsx')[0]
        if path == False:
            print_info("Файла не существует. Форсированная скачка таблицы.")
            await recieve_time_table(group)
        else:
            print_info("Игнорирование скачивания. Проход дальше.")
            pass

    try:
        path = glob.glob(f'tables/table_{stream}.xlsx')[0]
        wb_obj = openpyxl.load_workbook(path)
    except:
        print_error('Ошибка в получении таблицы')
        # Проверка вторая так как иногда ссылки меняют, и есть вероятность простого парса еррор сайта
        return False

    wb_obj.active = temp_number  # Задача листа таблицы
    sheet = wb_obj.active  # Выборка правильной таблицы

    return sheet


async def print_schedule(day_input: str, group_input: str, id: str, week_type: str) -> str | tuple | bool:
    dat = datetime.now()

    if (('бвт' in group_input and int(group_input[-1]) < 5) or ('бфи' in group_input) or ('бст' in group_input and int(group_input[-1]) < 4)
        or ('бэи' in group_input) or ('биб' in group_input) or ('бмп' in group_input)
        or ('бап' in group_input) or ('бут' in group_input) or ('зрс' in group_input and int(group_input[-1]) == 1)
        or ('брт' in group_input) or ('бик' in group_input and int(group_input[-1]) < 4) or ('бээ' in group_input) or ('бби' in group_input)
            or ('бэр' in group_input) or ('бин' in group_input and int(group_input[-1]) < 5)):
        group_list = 0
    elif (('бвт' in group_input and int(group_input[-1]) > 4) or ('бст' in group_input and int(group_input[-1]) > 3)
          or ('зрс' in group_input and int(group_input[-1]) == 2)
          or ('бик' in group_input and int(group_input[-1]) > 3 and int(group_input[-1]) < 7)
          or ('бин' in group_input and int(group_input[-1]) > 4 and int(group_input[-1]) < 8)):
        group_list = 1
    else:
        group_list = 2  # Выборка номера листа для каждой группы разный от условия

    if ((day_input == 'завтра' and datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) == 5)
            or (day_input == 'сегодня' and datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) == 6)):
        return 'Занятий нет'

    if check_right_input(day_input, group_input, week_type):

        if (day_input == 'завтра' and datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) == 6):
            week_checked = await week_check('следуюящая неделя')

        else:
            week_checked = await week_check(week_type)

        schedule = await get_sheet(group_input, group_input[0:3], group_list)

        if week_checked == False:
            print_error('Ошибка в sheethandler.py')
            return False  # Проверка ошибки в чётности недели
        if schedule == False:
            print_error('Ошибка в sheethandler.py')
            return False  # Проверка ошибки в скачке расписания

        if day_input == 'вся неделя':
            if group_input[0:3] == 'зрс':
                print_info('Sheethandler ' + str(datetime.now() - dat))
                return await get_full_schedule_zrc(group_input, week_checked, schedule)
            else:
                print_info('Sheethandler ' + str(datetime.now() - dat))
                return await group_matching_full_schedule[group_input[0:3]](group_input, week_checked, schedule, week_columns_groups[group_input])
        else:
            if group_input[0:3] == 'зрс':
                print_info('Sheethandler ' + str(datetime.now() - dat))
                return await get_schedule_zrc(day_input, group_input, week_checked, schedule)
            else:
                print_info('Sheethandler ' + str(datetime.now() - dat))
                return await group_matching_schedule[group_input[0:3]](day_input, group_input, week_columns_groups[group_input], week_checked, schedule)

    else:
        print_error('Ошибка в сопоставлении ввода и потока, sheethandler')
        return False
