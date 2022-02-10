from bs4 import BeautifulSoup
import requests
import os
import shutil
import re


def download_sheet(group_number):
    link = "https://mtuci.ru/time-table/"
    r = requests.get(link)
    code_timetable = r.text
    if group_number >= 0 and group_number <= 7:
        a = code_timetable.find('09.03.01')
        link_2 = 'https://mtuci.ru/' + code_timetable[a - 29: a + 52]
    if group_number >= 8 and group_number <= 9:
        a = code_timetable.find('02.03.02')
        link_2 = 'https://mtuci.ru/' + code_timetable[a - 29: a + 71]
    if group_number >= 10 and group_number <= 15:
        a = code_timetable.find('09.03.02')
        link_2 = 'https://mtuci.ru/' + code_timetable[a - 29: a + 51]
    file = open('table.xlsx', 'wb')
    file.write(requests.get(link_2).content)
