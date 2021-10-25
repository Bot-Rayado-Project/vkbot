from bs4 import BeautifulSoup
import requests
import random


def get_joke():
    url = 'https://baneks.ru/{}'.format(str(random.randint(1, 832+1)))
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    return ((str(soup.p).replace("<p>", "")).replace(
        "</p>", "")).replace("<br/>", "")
