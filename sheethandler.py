import download
import xlrd


def get_schedule():
    if not download.is_downloaded:
        download.download_sheet()
    schedule = "===============================================\n"
    if download.is_xls:
        wb = xlrd.open_workbook('table_xls.xls', formatting_info=True)
    else:
        wb = xlrd.open_workbook('table_xlsx.xlsx', formatting_info=True)
    sheet = wb.sheet_by_index(0)
    sheetdict = {}
    k = 0
    for i in range(11, 30+1):
        if sheet.cell_value(i, 7) == "":
            if k == 0:
                schedule += "===============================================\n"
            k += 1
        else:
            schedule += str(sheet.cell_value(i, 7)+"\n")
            k = 0
    return schedule
