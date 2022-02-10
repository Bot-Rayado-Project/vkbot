import fake_useragent
from bs4 import BeautifulSoup
import requests

link = "https://lms.mtuci.ru/lms/login/index.php"
session = requests.Session()
user = fake_useragent.UserAgent().random

header = {
    'user-agent': user
}

request = session.get(link, headers=header)
soup = BeautifulSoup(request.text, 'lxml')
login_token = soup.findAll('input', {'name': "logintoken"})[0]['value']
math_link = "https://lms.mtuci.ru/lms/mod/bigbluebuttonbn/view.php?id=50036"

data = {
    'anchor': '',
    'logintoken': login_token,
    'username': '1bvt21115',
    'password': 'Rest0re1',
    'rememberusername': 1
}

responce = session.post(link, data=data, headers=header)
with open('file.txt', 'w', encoding='UTF-8  ') as file:
    file.write(str(BeautifulSoup(session.get(math_link).text, 'lxml')))
