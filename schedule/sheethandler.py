from datetime import datetime, timedelta
import openpyxl
import os
import glob


import schedule.whataweek as whataweek
from schedule.recieve import recieve_time_table
from utils.terminal_codes import print_error, print_info, print_warning
from utils.constants_schedule import week_columns_groups
from schedule.streams.IT.bvt import get_full_schedule_bvt, get_schedule_bvt
from schedule.streams.IT.bst import get_full_schedule_bst, get_schedule_bst
from schedule.streams.IT.bei import get_full_schedule_bei, get_schedule_bei
from schedule.streams.IT.bfi import get_full_schedule_bfi, get_schedule_bfi
from schedule.streams.KIIB.bib import get_full_schedule_bib, get_schedule_bib
from schedule.streams.KIIB.bmp import get_full_schedule_bmp, get_schedule_bmp
from schedule.streams.KIIB.zrc import get_full_schedule_zrc, get_schedule_zrc
from schedule.streams.KIIB.bap import get_full_schedule_bap, get_schedule_bap
from schedule.streams.KIIB.but import get_full_schedule_but, get_schedule_but
from schedule.streams.RIT.brt import get_full_schedule_brt, get_schedule_brt
from schedule.streams.RIT.bik import get_full_schedule_bik, get_schedule_bik
from schedule.streams.TCEIMK.bee import get_full_schedule_bee, get_schedule_bee
from schedule.streams.TCEIMK.bbi import get_full_schedule_bbi, get_schedule_bbi
from schedule.streams.TCEIMK.ber import get_full_schedule_ber, get_schedule_ber


async def check_right_input(day_input: str, group_input: str, week_type: str) -> bool:

    days = ('сегодня', 'завтра', 'вся неделя')
    groups = ('бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106',
              'бвт2107', 'бвт2108', 'бфи2101', 'бфи2102', 'бст2101', 'бст2102',
              'бст2103', 'бст2104', 'бст2105', 'бст2106', 'бэи2101', 'бэи2102',
              'бэи2103', 'биб2101', 'биб2102', 'биб2103', 'биб2104', 'бмп2101',
              'зрс2101', 'зрс2102', 'бап2101', 'бут2101', 'брт2101', 'брт2102',
              'бик2101', 'бик2102', 'бик2103', 'бик2104', 'бик2105', 'бик2106',
              'бик2107', 'бик2108', 'бик2109', 'бээ2101', 'бби2101', 'бэр2101')
    weeks = ('текущая неделя', 'следующая неделя')

    if day_input in days and group_input in groups and week_type in weeks:
        return True
    else:
        return False


async def week_check(week_type: str) -> str | bool:

    if whataweek.get_week() == False:
        print_error('Ошибка в чётности недели')
        return False

    if week_type == 'текущая неделя':
        return await whataweek.get_week()

    else:
        if await whataweek.get_week() == 'четная':
            return 'нечетная'

        else:
            return 'четная'  # Тут и тупой поймёт чо происходит


async def get_sheet(group: str, stream: str, temp_number: str) -> openpyxl.Workbook | bool:

    if not os.path.isdir("tables"):
        os.mkdir("tables")

    data = await recieve_time_table(group)  # Запрос на скачку таблицы

    try:
        path = glob.glob(f'tables/table_{stream}.xlsx')[0]
        wb_obj = openpyxl.load_workbook(path)
    except:
        print_error('Ошибка в получении таблицы')
        # Проверка вторая так как иногда ссылки меняют, и ест ьвероятность простого парса еррор сайта
        return False

    wb_obj.active = temp_number  # Задача листа таблицы
    sheet = wb_obj.active  # Выборка правильной таблицы

    return sheet


async def print_schedule(day_input: str, group_input: str, id: str, week_type: str) -> str | tuple | bool:

    if (('бвт' in group_input and int(group_input[-1]) < 5) or ('бфи' in group_input) or ('бст' in group_input and int(group_input[-1]) < 4)
        or ('бэи' in group_input) or ('биб' in group_input) or ('бмп' in group_input)
        or ('бап' in group_input) or ('бут' in group_input) or ('зрс' in group_input and int(group_input[-1]) == 1)
        or ('брт' in group_input) or ('бик' in group_input and int(group_input[-1]) < 4) or ('бээ' in group_input) or ('бби' in group_input)
            or ('бэр' in group_input)):
        group_list = 0
    elif (('бвт' in group_input and int(group_input[-1]) > 4) or ('бст' in group_input and int(group_input[-1]) > 3)
          or ('зрс' in group_input and int(group_input[-1]) == 2)
          or ('бик' in group_input and int(group_input[-1]) > 3 and int(group_input[-1]) < 7)):
        group_list = 1
    else:
        group_list = 2  # Выборка номера листа для каждой группы разный от условия

    if ((day_input == 'завтра' and datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) == 5)
            or (day_input == 'сегодня' and datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) == 6)):
        return 'Занятий нет'

    if check_right_input:

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

        match group_input[0:3]:

            case 'бвт':
                if day_input == 'вся неделя':
                    return await get_full_schedule_bvt(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_bvt(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)

            case 'бст':
                if day_input == 'вся неделя':
                    return await get_full_schedule_bst(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_bst(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)

            case 'бэи':
                if day_input == 'вся неделя':
                    return await get_full_schedule_bei(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_bei(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)

            case 'бфи':
                if day_input == 'вся неделя':
                    return await get_full_schedule_bfi(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_bfi(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)

            case 'биб':
                if day_input == 'вся неделя':
                    return await get_full_schedule_bib(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_bib(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)

            case 'бмп':
                if day_input == 'вся неделя':
                    return await get_full_schedule_bmp(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_bmp(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)

            case 'бап':
                if day_input == 'вся неделя':
                    return await get_full_schedule_bap(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_bap(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)

            case 'бут':
                if day_input == 'вся неделя':
                    return await get_full_schedule_but(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_but(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)

            case 'зрс':
                if day_input == 'вся неделя':
                    return await get_full_schedule_zrc(group_input, week_checked, schedule)
                else:
                    return await get_schedule_zrc(day_input, group_input, week_checked, schedule)

            case 'брт':
                if day_input == 'вся неделя':
                    return await get_full_schedule_brt(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_brt(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)

            case 'бик':
                if day_input == 'вся неделя':
                    return await get_full_schedule_bik(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_bik(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)

            case 'бээ':
                if day_input == 'вся неделя':
                    return await get_full_schedule_bee(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_bee(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)

            case 'бби':
                if day_input == 'вся неделя':
                    return await get_full_schedule_bbi(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_bbi(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)

            case 'бэр':
                if day_input == 'вся неделя':
                    return await get_full_schedule_ber(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_ber(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)
    else:
        print_error('Ошибка в сопоставлении ввода и потока')
        return False
