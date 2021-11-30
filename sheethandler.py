import download
import xlrd
import whataweek

global groups
groups_id = {'бфи2101': 3,
             'бфи2102': 4,
             'бвт2101': 5,
             'бвт2102': 6,
             'бвт2103': 7,
             'бвт2104': 8,
             'бвт2105': 9,
             'бвт2106': 10,
             'бвт2107': 11,
             'бвт2108': 12,
             'бст2101': 13,
             'бст2102': 14,
             'бст2103': 15,
             'бст2104': 16,
             'бст2105': 17,
             'бст2106': 18,
             }


def get_sheet():
    if not download.is_downloaded:
        download.download_sheet()
    if download.is_xls:
        wb = xlrd.open_workbook('temp/table_xls.xls', formatting_info=True)
    else:
        wb = xlrd.open_workbook('temp/table_xlsx.xlsx', formatting_info=True)
    sheet = wb.sheet_by_index(0)
    return sheet


def print_schedule(start, end):
    global groups_id, group
    schedule = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    schedule += time[k] + '\n'
    for i in range(start, end + 1):
        if str(sheet.cell_value(i, groups_id[group])) != '':
            schedule += str(sheet.cell_value(i, groups_id[group]) + '\n')
    if k == 4:
        schedule += '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    return schedule


def calculation(days_of_week, j):
    global groups_id, group
    coef = {0: 0,
            1: 4,
            2: 8,
            3: 12,
            4: 16
            }

    if (sheet.cell_value(days_of_week + coef[j], groups_id[group]) == '' and sheet.cell_value(days_of_week + coef[j] + 1, groups_id[group]) != '') or sheet.cell_value(days_of_week + coef[j], groups_id[group]) == 'дистанционно':
        start = days_of_week + coef[j]
        end = days_of_week + 3 + coef[j]
        return start, end
    else:
        if whataweek.get_week() == "четная":
            start = days_of_week + 2 + coef[j]
            end = days_of_week + 3 + coef[j]
        else:
            start = days_of_week + coef[j]
            end = days_of_week + 1 + coef[j]
        return start, end


def pred_print(day, i):

    start, end = calculation(day, i)
    return print_schedule(start, end)


def get_schedule(day_of_week, group_input):

    global sheet, time, k, stroka, groups, group
    group = group_input
    stroka = ''
    k = 0
    time = ['9-30', '11-20', '13-10', '15-25', '17-15']
    sheet = get_sheet()

    days = [11, 31, 51, 71, 91, 111]

    if day_of_week == 'понедельник':
        for i in range(5):
            stroka += pred_print(days[0], i)
            k += 1

    if day_of_week == 'вторник':
        for i in range(5):
            stroka += pred_print(days[1], i)
            k += 1

    if day_of_week == 'среда':
        for i in range(5):
            stroka += pred_print(days[2], i)
            k += 1

    if day_of_week == 'четверг':
        for i in range(5):
            stroka += pred_print(days[3], i)
            k += 1

    if day_of_week == 'пятница':
        for i in range(5):
            stroka += pred_print(days[4], i)
            k += 1

    if day_of_week == 'суббота':
        for i in range(5):
            stroka += pred_print(days[5], i)
            k += 1

    return stroka
