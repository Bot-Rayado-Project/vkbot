import openpyxl
import os
from datetime import datetime, timedelta
import schedule.whataweek as whataweek
#import whataweek
from schedule.recieve import recieve_time_table
#from recieve import recieve_time_table
import asyncio


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
    if not os.path.isdir("tables"):
        os.mkdir("tables")
    data = await recieve_time_table(group, user_id)
    wb_obj = openpyxl.load_workbook('tables/table_{}.xlsx'.format(user_id))
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


async def get_schedule(group_text, group_column, day_type, id, week_type):

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
        '0': 2,
        '1': 13,
        '2': 24,
        '3': 35,
        '4': 46,
        '5': 57
    }
    day_time_utc = datetime.weekday(datetime.today().utcnow() + timedelta(hours=3))

    if day_type == 'завтра':
        if day_time_utc == 6:
            day = 2
            day_print = day_time_utc + 1
        else:
            day = days_num[str(day_time_utc + 1)]
            day_print = day_time_utc + 1
    else:
        if day_time_utc == 6:
            return 'занятий нет'
        else:
            day = days_num[str(day_time_utc)]
            day_print = day_time_utc
    schedule = await get_sheet(group_text, id, groups[group_text])
    schedule_output = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
        + 'День недели: ' + days[day_print].capitalize() + '\n' + 'Неделя: ' + (await week_check(week_type)).capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    time_par = 1
    for i in range(day, day + 10, 2):

        if schedule[group_column + str(i)].value != None:
            schedule_output += str(time[time_par]) + '  ' \
                + str(schedule[group_column + str(i)].value) + '\n\n' \
                + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
        else:
            schedule_output += 'Пары нет\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

        time_par += 1
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


async def get_full_schedule(group_text, week_column, id, week_type):

    full_schedule_tuple = ()
    full_schedule_list = []
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
    schedule = await get_sheet(group_text, id, groups[group_text])

    for k in range(2, 67, 11):

        full_schedule = str(schedule['A' + str(k)].value) + '\n\n'

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

    week_checked = await week_check(week_type)

    weeks_bvt_bfi = {
        '1': 'D',
        '2': 'E',
        '3': 'F',
        '4': 'G',
        '5': 'D',
        '6': 'E',
        '7': 'F',
        '8': 'G',
    }
    weeks_bst = {
        '1': 'D',
        '2': 'E',
        '3': 'F',
        '4': 'D',
        '5': 'E',
        '6': 'F',
    }
    if group_input[1] == 'ф' or group_input[1] == 'в':
        group_column = weeks_bvt_bfi[group_input[-1]]
    else:
        group_column = weeks_bst[group_input[-1]]

    if day_input == 'вся неделя':
        return await get_full_schedule(group_input, group_column, id, week_type)
    else:
        return await get_schedule(group_input, group_column, day_input, id, week_type)

#if __name__ == '__main__':
#    async def main():
#        s = await print_schedule('завтра', 'бфи2102', '1234142', 'следующая неделя')
#        print(s)
#
#asyncio.run(main())
