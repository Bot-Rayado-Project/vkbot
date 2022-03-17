import openpyxl
import os
from datetime import datetime, timedelta
import schedule.whataweek as whataweek
from schedule.recieve import recieve_time_table
""" from recieve import recieve_time_table
import whataweek
import asyncio """


async def week_check(week_type):
    if week_type == 'текущая неделя':
        return await whataweek.get_week()
    else:
        if await whataweek.get_week() == 'четная':
            return 'нечетная'
        else:
            return 'четная'


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


async def get_sheet(group: str, user_id, temp_number) -> openpyxl.Workbook:
    try:
        if not os.path.isdir("tables"):
            os.mkdir("tables")
    except:
        return 'Ошибка в скачке таблицы #3'
    data = await recieve_time_table(group, user_id)
    if 'Ошибка' in data:
        return 'Ошибка в скачке таблицы #4'
    try:
        wb_obj = openpyxl.load_workbook('tables/table_{}.xlsx'.format(user_id))
    except:
        return 'Ошибка в скачке таблицы #2'
    match data:
        case "бвт", number:
            wb_obj.active = temp_number
        case "бфи", number:
            wb_obj.active = temp_number
        case "бст", number:
            wb_obj.active = temp_number
    sheet = wb_obj.active
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
        + 'День недели: ' + days[day_print].capitalize() + '\n' + 'Неделя: ' + (await week_check(week_type)).capitalize() + '\n' \
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


async def get_schedule(group_text, group_column, day_type, id, week_type, start_cell):

    if 'Ошибка' in await week_check(week_type):
        return await week_check(week_type)

    time = {
        1: '9:30 - 11:05\n',
        2: '11:20 - 12:55\n',
        3: '13:10 - 14:45\n',
        4: '15:25 - 17:00\n',
        5: '17:15 - 18:50\n'
    }
    groups = {
        'бвт2101': 0,
        'бвт2102': 0,
        'бвт2103': 0,
        'бвт2104': 0,
        'бвт2105': 1,
        'бвт2106': 1,
        'бвт2107': 1,
        'бвт2108': 1,
        'бфи2101': 0,
        'бфи2102': 0,
        'бст2101': 0,
        'бст2102': 0,
        'бст2103': 0,
        'бст2104': 1,
        'бст2105': 1,
        'бст2106': 1
    }
    days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
    days_num = {
        '0': start_cell,
        '1': start_cell + 11,
        '2': start_cell + 22,
        '3': start_cell + 33,
        '4': start_cell + 44,
        '5': start_cell + 55
    }
    day_time_utc = datetime.weekday(
        datetime.today().utcnow() + timedelta(hours=3))

    if day_type == 'завтра':
        if day_time_utc == 6:
            day = start_cell
            day_print = day_time_utc + 1
        else:
            try:
                day = days_num[str(day_time_utc + 1)]
            except KeyError:
                return 'Ошибка в выводе расписания #1'
            day_print = day_time_utc + 1
    else:
        if day_time_utc == 6:
            return 'занятий нет'
        else:
            try:
                day = days_num[str(day_time_utc)]
            except KeyError:
                return 'Ошибка в выводе расписания #1'
            day_print = day_time_utc
    schedule = await get_sheet(group_text, id, groups[group_text])
    if 'Ошибка' in schedule: return schedule
    try:
        schedule_output = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
            + 'День недели: ' + days[day_print].capitalize() + '\n' + 'Неделя: ' + (await week_check(week_type)).capitalize() + '\n' \
            + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    except KeyError:
        return 'Ошибка в выводе расписания #1'
    time_par = 1
    try:
        for i in range(day, day + 10, 2):

            try:
                if schedule[group_column + str(i)].value != None:
                    try:
                        schedule_output += str(time[time_par]) + '  ' \
                            + str(schedule[group_column + str(i)].value) + '\n\n' \
                            + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
                    except KeyError:
                        return 'Ошибка в выводе расписания #1'
            except:
                return 'Ошибка в считывании таблицы #1'
            else:
                schedule_output += 'Пары нет\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

            time_par += 1
    except:
        return 'Ошибка в выводе расписания #1'
    return schedule_output


'''async def get_full_schedule(group_text, week_column, const, id, week_type):

    full_schedule = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
        + 'Неделя: ' + (await week_check(week_type)).capitalize() + '\n' \
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


async def get_full_schedule(group_text, week_column, id, week_type, start_cell):

    full_schedule_tuple = ()
    full_schedule_list = []
    if 'Ошибка' in await week_check(week_type):
        return await week_check(week_type)
    full_schedule_list.append('⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n'
                              + 'Неделя: ' + (await week_check(week_type)).capitalize() + '\n'
                              + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n')
    groups = {
        'бвт2101': 0,
        'бвт2102': 0,
        'бвт2103': 0,
        'бвт2104': 0,
        'бвт2105': 1,
        'бвт2106': 1,
        'бвт2107': 1,
        'бвт2108': 1,
        'бфи2101': 0,
        'бфи2102': 0,
        'бст2101': 0,
        'бст2102': 0,
        'бст2103': 0,
        'бст2104': 1,
        'бст2105': 1,
        'бст2106': 1
    }
    try:
        schedule = await get_sheet(group_text, id, groups[group_text])
        if 'Ошибка' in schedule: return schedule
    except KeyError:
        return ('Ошибка в выводе расписания #1')
    subject = 0 if await week_check(week_type) == 'нечетная' else 1

    if group_text not in ('бвт2105', 'бвт2106', 'бвт2107', 'бвт2108'):
        column = 'A'
    else:
        column = 'B'

    for k in range(start_cell, 67, 11):
        try:
            full_schedule = str(
                schedule[column + str(k - subject)].value) + '\n\n'
        except:
            return ('Ошибка в считывании таблицы #1')

        for i in range(k, k + 10, 2):

            if schedule[week_column + str(i)].value != None:
                full_schedule += str(schedule[week_column + str(i)].value) + '\n'\
                    + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
            else:
                full_schedule += 'Пары нет\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

        full_schedule_list.append(full_schedule)

    full_schedule_tuple = tuple(full_schedule_list)

    return full_schedule_tuple


'''async def print_schedule(day_input, group_input, id, week_type): 

    week_checked = await week_check(week_type)

    const = 1 if week_checked == 'четная' else -1
    week_column = 'H' if week_checked == 'четная' else 'G'
    if day_input == 'вся неделя':
        return await get_full_schedule(group_input, week_column, const, id, week_type)
    else:
        return await get_schedule(group_input, week_column, const, day_input, id, week_type)'''


async def print_schedule(day_input, group_input, id, week_type):

    if 'Ошибка' in await week_check(week_type):
        return await week_check(week_type)

    weeks_bvt_01_04_bfi = {
        '1': 'D',
        '2': 'E',
        '3': 'F',
        '4': 'G'
    }
    weeks_bvt_05_08 = {
        '5': 'E',
        '6': 'F',
        '7': 'G',
        '8': 'H',
    }
    weeks_bst = {
        '1': 'D',
        '2': 'E',
        '3': 'F',
        '4': 'D',
        '5': 'E',
        '6': 'F',
    }
    week_type_2 = week_type
    groups = ('бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106',
    'бвт2107', 'бвт2108', 'бфи2101', 'бфи2102', 'бст2101', 'бст2102', 'бст2103',
    'бст2104', 'бст2105', 'бст2106')

    if day_input not in ('завтра', 'сегодня', 'вся неделя') or group_input not in groups or week_type not in ('следующая неделя', 'текущая неделя'):
        return 'Ошибка ввода #1'
    else:
        if day_input == 'завтра' and datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) == 6:
            week_type_2 = 'следующая неделя'
        elif day_input == 'завтра':
            week_type_2 = 'текущая неделя'
        start_cell = 2 if await week_check(week_type) == 'нечетная' else 3
        try:
            if group_input[1] == 'ф' or group_input[1] == 'в' and group_input[-1] not in ('5', '6', '7', '8'):
                group_column = weeks_bvt_01_04_bfi[group_input[-1]]
            else:
                if group_input[1] == 'в':
                    group_column = weeks_bvt_05_08[group_input[-1]]
                else:
                    group_column = weeks_bst[group_input[-1]] # То есть у нас номер колонки зависит от номера группы, в данном случае лист бст
        except IndexError:
            return 'Ошибка ввода #2' # В данном случае, при ошибке вернёт пользователю эту строку.
        
        if day_input == 'вся неделя': #В данном куске кода мы уже делаем отправку определённую фукнцию в зависимости от ввода данных
            return await get_full_schedule(group_input, group_column, id, week_type_2, start_cell)
        else:
            return await get_schedule(group_input, group_column, day_input, id, week_type_2, start_cell)

""" if __name__ == '__main__':
    async def main():
        s = await print_schedule('вся неделя', 'бвт2108', '1234142', 'следующая неделя')
        print(s)
asyncio.run(main()) """
