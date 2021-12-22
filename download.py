from bs4 import BeautifulSoup
import requests
import os
import shutil
import re

is_xls, is_downloaded = None, None


def download_sheet():
    global is_xls, is_downloaded
    url = 'https://mtuci.ru/time-table/'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    if os.path.exists("temp"):
        shutil.rmtree("temp")
        os.mkdir("temp")
    else:
        os.mkdir("temp")
    print('Entry point')
    for line in soup.find_all('span'):
        __line__ = (((str(line).replace(' ', '')).lower()).replace(
            '<span>', '')).replace('</span>', '')
        if 'расписаниезанятий' in __line__ and '09.03.01' in __line__ and '2курс' in __line__:
            print((str(line).replace('<span>', '')).replace('</span>', ''))
            if '.xlsx' in (str(line).replace('<span>', '')).replace('</span>', ''):
                file = open('temp/table_xlsx.xlsx', 'wb')
                is_xls = False
                print('XLSX')
            else:
                file = open('temp/table_xls.xls', 'wb')
                is_xls = True
                print('XLS')
            ufr = requests.get("https://mtuci.ru/time-table/files/{0}".format(re.sub(
                "^\s+|\n|\r|\s+$", '', (str(line).replace('<span>', '')).replace('</span>', ''))))
            file.write(ufr.content)
            file.close()
            is_downloaded = True
            print('FILE WRITTEN!')
            break


if __name__ == '__main__':
    download_sheet()
