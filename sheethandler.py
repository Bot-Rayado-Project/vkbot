import openpyxl
from pathlib import Path
import whataweek
import download

def get_sheet():
    download.download_sheet(group_number)
    sheet_file = Path('table.xlsx')
    wb_obj = openpyxl.load_workbook(sheet_file)
    if 'бвт' in group_text:
        wb_obj.active = group_number
    if 'бфи' in group_text:
        wb_obj.active = group_number - 8
    if 'бст' in group_text:
        wb_obj.active = group_number - 10
    sheet = wb_obj.active
    return sheet


def print_schedule():
    schedule = get_sheet()
    global schedule_2
    schedule_2 =  '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
        + 'День недели: ' + day_text.capitalize() + '\n' + 'Неделя: ' + whataweek.get_week().capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    for i in range(day_number, day_number+ 5):
        dobavka, dobavka_2 = '', ''

        if str(schedule[format_pari + str(i)].value) == 'лек':
            dobavka = 'ция'
        else:
            if str(schedule[format_pari + str(i)].value) == 'лаб':
                dobavka = 'ораторная'
            else:
                dobavka = 'актика'
        if str(schedule[kab + str(i)].value) == 'дист':
            dobavka_2 = 'ант'
        if schedule[nedelya + str(i)].value != None:
            schedule_2 += str(time[i - day_number + 1]) + '\n' \
            + str(schedule[nedelya + str(i)].value) + '\n'\
            + str(schedule[format_pari  + str(i)].value) + dobavka + '\n' \
            + str(schedule[kab + str(i)].value) + dobavka_2 + '\n' \
            + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
        else:
            schedule_2 += 'Пары нет\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    return schedule_2

def get_schedule(day_of_week, group_input):
    global day_number, day_text, nedelya, groups,group_text,group_number, kab, format_pari,time
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
        'бвт2108' : 7,
        'бфи2101' : 8,
        'бфи2102' : 9,
        'бст2101' : 10,
        'бст2102' : 11,
        'бст2103' : 12,
        'бст2104' : 13,
        'бст2105' : 14,
        'бст2106' : 15
    }
    time = {
        1 : '9-30',
        2 : '11-20',
        3 : '13-10',
        4 : '15-25',
        5 : '17-15'
    }
    day_text = day_of_week
    day_number = days_of_week[day_of_week]
    if whataweek.get_week() == "четная":
        nedelya = 'H'
        kab = 'K'
        format_pari = 'J'
    else:
        nedelya = 'G'
        kab = 'D'
        format_pari = 'E'

    group_number = groups[group_input]
    group_text = group_input
    return print_schedule()