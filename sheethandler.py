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
    if whataweek.get_week() == "четная":

        days = [[11, 30], [31, 50], [51, 70], [71, 90], [91, 110], [111, 130]]

        if "понедельник" in cmd:
            for i in range(days[0][0], days[0][0] + 4):
                if sheet.cell_value(i, 7) == '':
                    start = days[0][0]
                    end = days[0][0] + 4
                    break
            else:
                start = days[0][0] + 2
                end = days[0][0] + 3
            for i in range(start, end + 1):
                if sheet.cell_value(i, 7) == "":
                    if k == 0:
                        schedule += "===============================================\n"
                    k += 1
                else:
                    schedule += str(sheet.cell_value(i, 7)+"\n")
                    k = 0
            schedule += "===============================================\n"
            return schedule
