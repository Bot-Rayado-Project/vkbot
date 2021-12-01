from bs4 import BeautifulSoup
import requests


def get_week():
    url = 'https://whataweek.ru/'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    #return ((str(soup.find_all("div", {"class": "uppercase typo-h2"})).replace('[<div class="uppercase typo-h2">', '')).replace('</div>]', ''))
    return 'нечетная'