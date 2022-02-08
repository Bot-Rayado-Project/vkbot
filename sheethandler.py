import download
import openpyxl
from pathlib import Path
import glob
import whataweek

def get_sheet():
    download.download_sheet()
    sheet_file = Path('table.xlsx')
    wb_obj = openpyxl.load_workbook(sheet_file)
    wb_obj.active = group_number
    sheet = wb_obj.active
    return sheet


def print_schedule():
    schedule = get_sheet()
    global schedule_2
    schedule_2 =  '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
        + 'День недели: ' + day_text.capitalize() + '\n' + 'Неделя: ' + whataweek.get_week().capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    for i in range(day_number, day_number+ 5):
        if schedule[nedelya + str(i)].value != None:
            schedule_2 += str(schedule[nedelya + str(i)].value) + '\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
        else:
            schedule_2 += 'Пары нет\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    return schedule_2

def get_schedule(day_of_week, group_input):
    global day_number, day_text, nedelya, groups,group_text,group_number
    days_of_week = {
        'понедельник': 14,
        'вторник': 20,
        'среда': 26,
        'четверг': 32,
        'пятница': 38,
        'суббота': 44,
    }
    groups = {
        'бвт2101' : 0,
        'бвт2102' : 1,
        'бвт2103' : 2,
        'бвт2104' : 3,
        'бвт2105' : 4,
        'бвт2106' : 5,
        'бвт2107' : 6,
        'бвт2108' : 7
    }
    day_text = day_of_week
    day_number = days_of_week[day_of_week]
    if whataweek.get_week() == "четная":
        nedelya = 'H'
    else:
        nedelya = 'G'

    group_number = groups[group_input]
    group_text = group_input
    return print_schedule()