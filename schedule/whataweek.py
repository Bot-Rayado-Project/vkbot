from bs4 import BeautifulSoup
from utils.aiohttp_requests import aiohttp_fetch
import re


async def get_week() -> str:
    response = await aiohttp_fetch("http://week.kodan.ru/")
    soup = BeautifulSoup(response, 'lxml')
    return (((re.sub("^\s+|\n|\r|\s+$", '', str(soup.find_all("span", {"class": "week-type"}))).replace('[<span class="week-type">', '')).replace("</span>]", "")).replace('	', '')).lower()
