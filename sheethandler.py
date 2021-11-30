import download
import xlrd
import whataweek
from enum import Enum


def get_schedule(cmd):
    if not download.is_downloaded:
        download.download_sheet()
    schedule = "===============================================\n"
    start, end = None, None
    if download.is_xls:
        wb = xlrd.open_workbook('table_xls.xls', formatting_info=True)
    else:
        wb = xlrd.open_workbook('table_xlsx.xlsx', formatting_info=True)
    sheet = wb.sheet_by_index(0)
    k = 0
    # Понедельник, вторник, среда, четверг, пятница, суббота
    if get_week() == "четная":

        days = [[11, 30], [31, 50], [51, 70], [71, 90], [91, 110], [111, 130]]

        if "понедельник" in cmd:
            start = days[0][0]
            end = days[0][1]
        elif "вторник" in cmd:
            start = days[1][0]
            end = days[1][1]
        elif "среда" in cmd:
            start = days[2][0]
            end = days[2][1]
        elif "четверг" in cmd:
            start = days[3][0]
            end = days[3][1]
        elif "пятница" in cmd:
            start = days[4][0]
            end = days[4][1]
        elif "субоота" in cmd:
            start = days[5][0]
            end = days[5][1]
        print(cmd, start, end)
        if start != None and end != None:
            for i in range(start, end+1):
                if sheet.cell_value(i, 7) == "":
                    if k == 0:
                        schedule += "===============================================\n"
                    k += 1
                else:
                    schedule += str(sheet.cell_value(i, 7)+"\n")
                    k = 0
            return schedule
