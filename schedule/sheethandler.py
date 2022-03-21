from datetime import datetime, timedelta
import openpyxl
import os
import glob


import schedule.whataweek as whataweek
from schedule.recieve import recieve_time_table
from utils.constants_schedule import week_columns_groups
from schedule.streams.bvt import get_full_schedule_bvt, get_schedule_bvt
from schedule.streams.bst import get_full_schedule_bst, get_schedule_bst
from schedule.streams.bei import get_full_schedule_bei, get_schedule_bei
from schedule.streams.bfi import get_full_schedule_bfi, get_schedule_bfi
from schedule.streams.bib import get_full_schedule_bib, get_schedule_bib
from schedule.streams.bin import get_full_schedule_bin, get_schedule_bin


async def check_right_input(day_input: str, group_input: str, week_type: str) -> bool:

    days = ('сегодня', 'завтра', 'вся неделя')
    groups = ('бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106',
              'бвт2107', 'бвт2108', 'бфи2101', 'бфи2102', 'бст2101', 'бст2102',
              'бст2103', 'бст2104', 'бст2105', 'бст2106', 'бэи2101', 'бэи2102',
              'бэи2103', 'биб2101', 'биб2102', 'биб2103', 'биб2104', 'бин2101',
              'бин2102', 'бин2103', 'бин2104', 'бин2105', 'бин2106', 'бин2107',
              'бин2108', 'бин2109', 'бин2110')
    weeks = ('текущая неделя', 'следующая неделя')

    if day_input in days and group_input in groups and week_type in weeks:
        return True
    else:
        return False


async def week_check(week_type: str) -> str:

    if week_type == 'текущая неделя':
        return await whataweek.get_week()

    else:
        if await whataweek.get_week() == 'четная':
            return 'нечетная'

        else:
            return 'четная'  # Тут и тупой поймёт чо происходит


'''async def get_sheet(group: str, user_id, temp_number) -> openpyxl.Workbook:
    if not os.path.isdir("tables"):
        os.mkdir("tables")
    data = await recieve_time_table(group, user_id)
    wb_obj = openpyxl.load_workbook('tables/table_{}.xlsx'.format(user_id))
    match data:
        case "бвт", number:
            wb_obj.active = temp_number
        case "бфи", number:
            wb_obj.active = temp_number - 8
        case "бст", number:
            wb_obj.active = temp_number - 10
    sheet = wb_obj.active
    return sheet'''


async def get_sheet(group: str, user_id: str, temp_number: str) -> openpyxl.Workbook:
    try:
        if not os.path.isdir("tables"):
            os.mkdir("tables")
    except:
        # Тут происходит обработки ошибки с папкой tables, вдруг её нет или не создаётся
        return 'Ошибка в скачке таблицы #3'

    data = await recieve_time_table(group, user_id)  # Запрос на скачку таблицы

    # if 'Ошибка' in data:
    #    return 'Ошибка в скачке таблицы #4'  # Проверка, что скачалось без ошибки

    try:
        path = glob.glob('tables/table_{0}_*.xlsx'.format(user_id))[0]
        wb_obj = openpyxl.load_workbook(path)
    except:
        # Проверка вторая так как иногда ссылки меняют, и ест ьвероятность простого парса еррор сайта
        return 'Ошибка в скачке таблицы #2'

    wb_obj.active = temp_number  # Задача листа таблицы
    sheet = wb_obj.active  # Выборка правильной таблицы

    return sheet

'''async def get_schedule(group_text, week_column, const, day_type, id, week_type):

    time = {
        1: '9:30 - 11:05\n',
        2: '11:20 - 12:55\n',
        3: '13:10 - 14:45\n',
        4: '15:25 - 17:00\n',
        5: '17:15 - 18:50\n'
    }
    supplements = {
        'лек': 'лекция',
        'лаб': 'лабораторная',
        'пр': 'практика',
        'дист': 'дистанционно',
        'очно': 'очно'}
    groups = {
        'бвт2101': 0,
        'бвт2102': 1,
        'бвт2103': 2,
        'бвт2104': 3,
        'бвт2105': 4,
        'бвт2106': 5,
        'бвт2107': 6,
        'бвт2108': 7,
        'бфи2101': 8,
        'бфи2102': 9,
        'бст2101': 10,
        'бст2102': 11,
        'бст2103': 12,
        'бст2104': 13,
        'бст2105': 14,
        'бст2106': 15
    }
    days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
    if day_type == 'завтра':
        if datetime.weekday(datetime.today()) == 6:
            day = 14
            day_print = 0
        else:
            day = datetime.weekday(datetime.today()) * 6 + 14 + 6
            day_print = datetime.weekday(datetime.today()) + 1
    else:
        day = datetime.weekday(datetime.today()) * 6 + 14
        day_print = datetime.weekday(datetime.today())
    schedule = await get_sheet(group_text, id, groups[group_text])
    schedule_output = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
        + 'День недели: ' + days[day_print].capitalize() + '\n' + 'Неделя: ' + (week_checked).capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

    for i in range(day, day + 5):

        if schedule[week_column + str(i)].value != None:
            schedule_output += str(time[i - day + 1]) + '  ' \
                + str(schedule[week_column + str(i)].value) + '\n\n' \
                + 'Преподаватель: ' + str(schedule[chr(ord(week_column) + 1 * const) + str(i)].value) + '\n'\
                + 'Вид занятия: ' + str(supplements[str(schedule[chr(ord(week_column) + 2 * const) + str(i)].value)]) + '\n' \
                + 'Форма проведения: ' + str(supplements[str(schedule[chr(ord(week_column) + 3 * const) + str(i)].value)]) + '\n' \
                + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
        else:
            schedule_output += 'Пары нет\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    return schedule_output'''


'''async def get_full_schedule(group_text, week_column, const, id, week_type):

    full_schedule = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
        + 'Неделя: ' + (week_checked).capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    full_schedule_tuple = ()
    full_schedule_list = []
    groups = {
        'бвт2101': 0,
        'бвт2102': 1,
        'бвт2103': 2,
        'бвт2104': 3,
        'бвт2105': 4,
        'бвт2106': 5,
        'бвт2107': 6,
        'бвт2108': 7,
        'бфи2101': 8,
        'бфи2102': 9,
        'бст2101': 10,
        'бст2102': 11,
        'бст2103': 12,
        'бст2104': 13,
        'бст2105': 14,
        'бст2106': 15
    }
    schedule = await get_sheet(group_text, id, groups[group_text])

    for k in range(14, 49, 6):

        current_day_column = 0
        full_schedule = str(
            schedule['A' + str(k - 1)].value) + '\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

        for i in range(k + current_day_column, k + current_day_column + 5):

            if schedule[week_column + str(i)].value != None:
                full_schedule += str(current_day_column + 1) + '. ' \
                    + str(schedule[week_column + str(i)].value) + '(' + str(str(schedule[chr(ord(week_column) + 3 * const) + str(i)].value)) \
                    + ' ' + str(str(schedule[chr(ord(week_column) + 2 * const) + str(i)].value)) + ')' + '\n'\
                    + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
            else:
                full_schedule += str(current_day_column + 1) + \
                    '. ' + 'Пары нет\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

            current_day_column += 1

        full_schedule_list.append(full_schedule)

    full_schedule_tuple = tuple(full_schedule_list)

    return full_schedule_tuple'''


'''async def print_schedule(day_input, group_input, id, week_type): 

    week_checked = week_checked

    const = 1 if week_checked == 'четная' else -1
    week_column = 'H' if week_checked == 'четная' else 'G'
    if day_input == 'вся неделя':
        return await get_full_schedule(group_input, week_column, const, id, week_type)
    else:
        return await get_schedule(group_input, week_column, const, day_input, id, week_type)'''


async def print_schedule(day_input: str, group_input: str, id: str, week_type: str) -> str | tuple:


    if (('бвт' in group_input and int(group_input[-1]) < 5) or ('бфи' in group_input) or ('бст' in group_input and int(group_input[-1]) < 4) 
    or ('бэи' in group_input) or ('биб' in group_input) or ('бин' in group_input and int(group_input[-1]) < 5)):
        group_list = 0
    elif (('бвт' in group_input and int(group_input[-1]) > 4) or ('бст' in group_input and int(group_input[-1]) > 3) 
    or ('бин' in group_input and int(group_input[-1]) > 4 and int(group_input[-1]) < 8)):
        group_list = 1
    else:
        group_list = 2 # Выборка номера листа для каждой группы разный от условия

    if ((day_input == 'завтра' and datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) == 5)
            or (day_input == 'сегодня' and datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) == 6)):
        return 'Занятий нет'

    if check_right_input:

        if (day_input == 'завтра' and datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) == 6):
            week_checked = await week_check('следуюящая неделя')

        else:
            week_checked = await week_check(week_type)

        try:
            schedule = await get_sheet(group_input, id, group_list)
        except:
            return 'Ошибка в таблице, sheethandler.py'

        if 'Ошибка' in week_checked:
            return week_checked  # Проверка ошибки в чётности недели
        if 'Ошибка' in schedule:
            return schedule  # Проверка ошибки в скачке расписания

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

            case 'бин':
                if day_input == 'вся неделя':
                    return await get_full_schedule_bin(group_input, week_checked, schedule, week_columns_groups[group_input])
                else:
                    return await get_schedule_bin(day_input, group_input, week_columns_groups[group_input], week_checked, schedule)
    else:
        return 'Ошибка ввода'