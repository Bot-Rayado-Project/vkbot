from bs4 import BeautifulSoup
import re
import aiohttp


async def aiohttp_fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_week() -> str:
    response = await aiohttp_fetch("http://week.kodan.ru/")
    soup = BeautifulSoup(response, 'lxml')
    return (((re.sub("^\s+|\n|\r|\s+$", '', str(soup.find_all("span", {"class": "week-type"}))).replace('[<span class="week-type">', '')).replace("</span>]", "")).replace('	', '')).lower()
