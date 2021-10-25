from bs4 import BeautifulSoup
import requests

is_xsl, is_downloaded = None, None


def download_sheet():
    global is_xls, is_downloaded
    url = 'https://mtuci.ru/time-table/'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    for link in soup.find_all('a'):
        if "ф-т ИТ -  02.03.02, 09.03.01, 09.03.02 - 1, 2 курс - семестр 1,3 " in str(link.get('href')):
            print(link.get('href')[6:])
            if ".xlsx" in str(link.get('href')):
                file = open('table_xlsx.xlsx', 'wb')
                is_xls = False
            elif ".xls" in str(link.get('href')):
                file = open('table_xls.xls', 'wb')
                is_xls = True
            ufr = requests.get(
                "https://mtuci.ru/time-table/files/{}".format(link.get('href')[6:]))
            file.write(ufr.content)
            file.close()
            is_downloaded = True
            break
