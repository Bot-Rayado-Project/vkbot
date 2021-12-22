from bs4 import BeautifulSoup
import requests
import re


def get_week():
    url = 'http://week.kodan.ru/'
    responce = requests.get(url)
    responce.encoding = 'utf-8'
    soup = BeautifulSoup(responce.text, 'lxml')
    return (((re.sub("^\s+|\n|\r|\s+$", '', str(soup.find_all("span", {"class": "week-type"}))).replace('[<span class="week-type">', '')).replace("</span>]", "")).replace('	', '')).lower()
