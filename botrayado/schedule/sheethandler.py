from botrayado.schedule.whataweek import get_week
from transliterate import translit
from datetime import datetime, timedelta
from botrayado.utils.constants import DAYS_ENG, DAYS_RU, RESTIP, RESTPORT
import json
import aiohttp


async def aiohttp_fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def print_schedule(day_type: str, group: str) -> str:

    day_time_utc = datetime.weekday(datetime.today().utcnow() + timedelta(hours=3))

    if day_type == 'завтра':
        day_time_utc += 1
    if day_time_utc == 6:
        return 'Занятий нет'

    week_checked = await get_week()
    even = True if week_checked == 'четная' else False
    output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + group.upper() + '\n' \
        + 'День недели: ' + DAYS_RU[day_time_utc].capitalize() + '\n' + 'Неделя: ' + week_checked.capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻\n'
    group = translit(group, language_code='ru', reversed=True)

    if day_type == 'завтра':
        if day_time_utc == 7:
            day_of_week = DAYS_ENG[0]
        else:
            day_of_week = DAYS_ENG[day_time_utc]
    else:
        day_of_week = DAYS_ENG[day_time_utc]

    responce = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?group={group}&even={even}&day={day_of_week}'))
    output += responce['schedule']

    return output


async def print_full_schedule(day_type: str, group: str) -> str:

    week_checked = await get_week()
    if week_checked == 'четная':
        if day_type == 'следующая неделя':
            even = False
        else:
            even = True
    else:
        if day_type == 'следующая неделя':
            even = True
        else:
            even = False

    output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + group.upper() + '\n' \
        + 'Неделя: ' + week_checked.capitalize() + '\n' + '⸻⸻⸻⸻⸻\n'
    group = translit(group, language_code='ru', reversed=True)

    responce = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?group={group}&even={even}'))
    for i in range(6):
        output += '\n' + DAYS_RU[i].capitalize() + '\n\n'
        output += responce['schedule'][i]['schedule']

    return output
