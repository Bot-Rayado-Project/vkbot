import traceback
from botrayado.schedule.whataweek import get_week
from transliterate import translit
from botrayado.utils.logger import get_logger
from botrayado.database.db import sqlite_connection, cursor
from datetime import datetime, timedelta
from botrayado.utils.constants import DAYS_ENG, DAYS_RU, RESTIP, RESTPORT
import json
import aiohttp

logger = get_logger(__name__)


async def aiohttp_fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def print_schedule(id: int, day_type: str, stream_group: str) -> str:
    try:
        day_time_utc = datetime.weekday(
            datetime.today().utcnow() + timedelta(hours=3))
        if day_type == 'завтра':
            day_time_utc += 1
        if day_time_utc == 6:
            return 'Занятий нет'
        if day_time_utc == 7:
            day_time_utc = 0

        week_checked = await get_week()
        even = True if week_checked == 'четная' else False
        if week_checked == 'четная' and day_type == 'завтра' and day_time_utc == 0:
            even = False
            week_checked = 'нечетная'
        elif week_checked == 'нечетная' and day_type == 'завтра' and day_time_utc == 0:
            even = True
            week_checked = 'четная'
        parity = 'четная' if even else 'нечетная'
        output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + stream_group.upper() + '\n' \
            + 'День недели: ' + DAYS_RU[day_time_utc].capitalize() + '\n' + 'Неделя: ' + week_checked.capitalize() + '\n' \
            + '⸻⸻⸻⸻⸻\n'

        day_of_week = DAYS_ENG[day_time_utc] if day_type == 'завтра' else DAYS_ENG[day_time_utc]

        response = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?id={id}&stream_group={stream_group}&parity={parity}&day={day_of_week}'))
        cursor.execute(
            f'SELECT button FROM menu_buttons_table WHERE user_id={id};')
        btn = cursor.fetchall()[0][0]
        if btn == 'свое':
            if response["personal_schedule"][day_of_week] == "":
                if response["headman_schedule"][day_of_week] == "":
                    output += response["shared_schedule"][day_of_week]
                    if response["personal_annotation"][day_of_week] == "":
                        if response["headman_annotation"][day_of_week] == "":
                            pass
                        else:
                            output += "\nАннотация от старосты:\n" + \
                                response["headman_annotation"][day_of_week]
                    else:
                        output += "\nАннотация от вас:\n" + \
                            response["personal_annotation"][day_of_week]
                else:
                    output = "Данный день изменен старостой: \n" + output
                    output += response["headman_schedule"][day_of_week]
                    if response["personal_annotation"][day_of_week] == "":
                        if response["headman_annotation"][day_of_week] == "":
                            pass
                        else:
                            output += "\nАннотация от старосты:\n" + \
                                response["headman_annotation"][day_of_week]
                    else:
                        output += "\nАннотация от вас:\n" + \
                            response["personal_annotation"][day_of_week]
            else:
                output = "Данный день изменен вами: \n" + output
                output += response["personal_schedule"][day_of_week]
                if response["personal_annotation"][day_of_week] == "":
                    if response["headman_annotation"][day_of_week] == "":
                        pass
                    else:
                        output += "\nАннотация от старосты:\n" + \
                            response["headman_annotation"][day_of_week]
                else:
                    output += "\nАннотация от вас:\n" + \
                        response["personal_annotation"][day_of_week]
        else:
            if response["headman_schedule"][day_of_week] == "":
                if response["personal_schedule"][day_of_week] == "":
                    output += response["shared_schedule"][day_of_week]
                    if response["headman_annotation"][day_of_week] == "":
                        if response["personal_annotation"][day_of_week] == "":
                            pass
                        else:
                            output += "\nАннотация от вас:\n" + \
                                response["personal_annotation"][day_of_week]
                    else:
                        output += "\nАннотация от старосты:\n" + \
                            response["headman_annotation"][day_of_week]
                else:
                    output = "Данный день изменен вами: \n" + output
                    output += response["personal_schedule"][day_of_week]
                    if response["headman_annotation"][day_of_week] == "":
                        if response["personal_annotation"][day_of_week] == "":
                            pass
                        else:
                            output += "\nАннотация от вас:\n" + \
                                response["personal_annotation"][day_of_week]
                    else:
                        output += "\nАннотация от старосты:\n" + \
                            response["headman_annotation"][day_of_week]
            else:
                output = "Данный день изменен старостой: \n" + output
                output += response["headman_schedule"][day_of_week]
                if response["headman_annotation"][day_of_week] == "":
                    if response["personal_annotation"][day_of_week] == "":
                        pass
                    else:
                        output += "\nАннотация от вас:\n" + \
                            response["personal_annotation"][day_of_week]
                else:
                    output += "\nАннотация от старосты:\n" + \
                        response["headman_annotation"][day_of_week]

        return output
    except Exception as e:
        logger.error(
            f"Error in sheethandler printing schedule ({e}): {traceback.format_exc()}")
        return "Ошибка в получении расписания. Информация об ошибке направлена разработчикам"


async def print_full_schedule(id: int, day_type: str, stream_group: str) -> str:
    try:
        week_checked = await get_week()
        if week_checked == 'четная':
            if day_type == 'следующая неделя':
                even = False
                week_checked = 'нечетная'
            else:
                even = True
                week_checked = 'четная'
        else:
            if day_type == 'следующая неделя':
                week_checked = 'четная'
                even = True
            else:
                even = False
                week_checked = 'нечетная'
        parity = 'четная' if even else 'нечетная'

        output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + stream_group.upper() + '\n' \
            + 'Неделя: ' + week_checked.capitalize() + '\n' + '⸻⸻⸻⸻⸻\n'

        response = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?id={id}&stream_group={stream_group}&parity={parity}'))
        for i in range(6):
            output += '\n' + DAYS_RU[i].capitalize() + '\n\n'
            output += response['shared_schedule'][DAYS_ENG[i]]

        return output
    except Exception as e:
        logger.error(
            f"Error in sheethandler printing full schedule ({e}): {traceback.format_exc()}")
        return "Ошибка в получении расписания. Информация об ошибке направлена разработчикам"


async def print_schedule_custom(group: str, day_of_week: str, even: bool) -> str:
    try:
        week_checked = 'четная' if even else 'нечетная'
        output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + group.upper() + '\n' \
            + 'День недели: ' + day_of_week.capitalize() + '\n' + 'Неделя: ' + week_checked.capitalize() + '\n' \
            + '⸻⸻⸻⸻⸻\n'
        group = translit(group, language_code='ru', reversed=True)
        day_of_week = translit(
            day_of_week, language_code='ru', reversed=True).replace("'", "")

        responce = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?group={group}&even={even}&day={day_of_week}'))
        output += responce['schedule']
        if responce['annotation'] == 'No annotation found':
            pass
        else:
            output += 'Аннотация на текущий день: \n' + responce['annotation']

        return output
    except Exception as e:
        logger.error(
            f"Error in sheethandler printing schedule ({e}): {traceback.format_exc()}")
        return "Ошибка в получении расписания. Информация об ошибке направлена разработчикам"
