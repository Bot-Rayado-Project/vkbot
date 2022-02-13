import openpyxl
import whataweek
from pathlib import Path
from recieve import recieve_time_table
import asyncio
import re


async def get_sheet(group: str) -> openpyxl.Workbook:
    data = await recieve_time_table(group)
    wb_obj = openpyxl.load_workbook(Path('table.xlsx'))
    match data:
        case "бвт", number:
            wb_obj.active = group_number
        case "бфи", number:
            wb_obj.active = group_number - 8
        case "бст", number:
            wb_obj.active = group_number - 10
    sheet = wb_obj.active
    print(group_number, group, wb_obj.active, sheet)
    return sheet

async def week_check():

    if week_type == 'текущая неделя':
        week = await whataweek.get_week()
    else:
        if await whataweek.get_week() == 'четная':
            week = 'нечетная'
        else:
            week = 'четная'
    return week
    
async def get_schedule(group: str) -> str:
    global schedule_output,schedule

    schedule = await get_sheet(group)
    schedule_output = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
        + 'День недели: ' + day_text.capitalize() + '\n' + 'Неделя: ' + (await week_check()).capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    
    for i in range(day_number, day_number + 5):

        if schedule[week_column + str(i)].value != None:
            schedule_output += str(time[i - day_number + 1]) + '  ' \
                + str(schedule[week_column + str(i)].value) + '\n\n' \
                + 'Преподаватель: ' + str(schedule[chr(ord(week_column) + 1) + str(i)].value)+ '\n'\
                + 'Вид занятия: ' + supplements[str(schedule[chr(ord(week_column) + 2) + str(i)].value)] + '\n' \
                + 'Форма проведения: ' + supplements[str(schedule[chr(ord(week_column) + 3) + str(i)].value)] + '\n' \
                + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
        else:
            schedule_output += 'Пары нет\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    return schedule_output


async def print_schedule(day_of_week, group_input, week_type_input):  # тоже пиздец
    global day_number, day_text, week_column, groups, group_text, \
    group_number, time, week_type, supplements

    week_type = week_type_input
    days_of_week = {
        'понедельник': 14,
        'вторник': 20,
        'среда': 26,
        'четверг': 32,
        'пятница': 38,
        'суббота': 44,
    }
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
    time = {
        1: '9-30',
        2: '11-20',
        3: '13-10',
        4: '15-25',
        5: '17-15'
    }
    supplements = {
        'лек': 'лекция',
        'лаб': 'лабораторная',
        'пр' : 'практика',
        'дист': 'дистанционно'

    }
    day_text = day_of_week
    day_number = days_of_week[day_of_week]

    week_checked = await week_check()
    week_column = 'H' if week_checked=='четная' else 'G'

    group_number = groups[group_input]
    group_text = group_input

    return await get_schedule(group_input)