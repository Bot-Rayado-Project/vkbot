import download
import xlrd
import whataweek

global groups, columns
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
    schedule = [] #str(sheet.cell_value(i, groups_id[group]))
    schedule.append(time[k])
    for i in range(start, end + 1):
        temp = str(sheet.cell_value(i, groups_id[group]))
        if temp != '':
            if 'дистанционно' in temp or 'Дистанционно' in temp:
                schedule.append(temp[len(temp) - 12 : len(temp)])
            else:
                schedule.append(temp)
    if schedule[len(schedule) - 1] == 'Физическая культура и спорт  на 16, 17 нед.':
        temp = schedule[len(schedule) - 1]
        schedule.pop(len(schedule) - 1)
        schedule[len(schedule) - 2] += '\n' + temp
    if len(schedule) == 4:
        temp = schedule[1] + ' ' + schedule[2]
        temp_dist = schedule[3]
        schedule.pop(1)
        schedule.pop(1)
        schedule.pop(1)
        schedule += temp + temp_dist
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

def table_ui(stroka1):
    global stroka
    
    print_group = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group.upper() + '\n' \
    + 'День недели: ' + day.capitalize() + '\n' + 'Неделя: ' + whataweek.get_week().capitalize() + '\n' \
    + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

    for i in range(len(stroka)):
        print_group += '\n' + 'Пара №' + str(i + 1) + ' (' + str(stroka[i][0]) + ')' + '\n'
        if len(stroka[i]) > 2:
            if 'ФИЗИЧЕСКАЯ' in stroka[i][1]:
                print_group += stroka[i][1][1:len(stroka[i][1])] + '\n'
            else:
                print_group += stroka[i][1] + '\n'
            print_group += 'Кабинет: ' + stroka[i][2] + '\n' + '\n'
        else:
            print_group += 'Пары нет' + '\n' + '\n'
    print_group += '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    return print_group


def get_schedule(day_of_week, group_input):

    global sheet, time, k, stroka, groups, group, day
    group = group_input
    day = day_of_week
    stroka = []
    k = 0
    time = ['09-30', '11-20', '13-10', '15-25', '17-15']
    sheet = get_sheet()

    days = [11, 31, 51, 71, 91, 111]

    if day_of_week == 'понедельник':
        for i in range(5):
            stroka.append(pred_print(days[0], i))
            k += 1

    if day_of_week == 'вторник':
        for i in range(5):
            stroka.append(pred_print(days[1], i))
            k += 1

    if day_of_week == 'среда':
        for i in range(5):
            stroka.append(pred_print(days[2], i))
            k += 1

    if day_of_week == 'четверг':
        for i in range(5):
            stroka.append(pred_print(days[3], i))
            k += 1

    if day_of_week == 'пятница':
        for i in range(5):
            stroka.append(pred_print(days[4], i))
            k += 1

    if day_of_week == 'суббота':
        for i in range(5):
            stroka.append(pred_print(days[5], i))
            k += 1
    return table_ui(stroka)