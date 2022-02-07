from bs4 import BeautifulSoup
import requests
import os
import shutil
import re


def download_sheet():
    link = "https://mtuci.ru/upload/iblock/f9c/1-kurs-_IT_09.03.01-Informatika-i-vychislitelnaya-tekhnika.xlsx"
    file = open('table.xlsx', 'wb')
    file.write(requests.get(link).content)


if __name__ == '__main__':
    download_sheet()
