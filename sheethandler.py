import download
import xlrd
import whataweek

isDownloaded = False


def get_sheet():
    global isDownloaded
    if not download.is_downloaded:
        download.download_sheet()
    if download.is_xls:
        wb = xlrd.open_workbook('temp/table_xls.xls', formatting_info=True)
    else:
        wb = xlrd.open_workbook('temp/table_xlsx.xlsx', formatting_info=True)
    sheet = wb.sheet_by_index(0)
    isDownloaded = True
    return sheet


def print_schedule(start, end):
    schedule = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    schedule += time[k] + '\n'
    for i in range(start, end + 1):
        if str(sheet.cell_value(i, 7)) != '':
            schedule += str(sheet.cell_value(i, 7) + '\n')
    if k == 4:
        schedule += '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    return schedule


def calculation(days_of_week, j):

    coef = {0: 0,
            1: 4,
            2: 8,
            3: 12,
            4: 16
            }

    if sheet.cell_value(days_of_week + coef[j], 7) == '' and sheet.cell_value(days_of_week + coef[j] + 1, 7) != '':
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


def get_schedule(day_of_week):

    global sheet, time, k, stroka
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
