from datetime import datetime, timedelta
from bot.utils import get_parity, aiohttp_fetch
from bot.constants import DAYS_RU, DAYS_ENG, RESTIP, RESTPORT
from bot.db import db_get_priority_button
from bot.logger import get_logger
from transliterate import translit
import json
import traceback

logger = get_logger(__name__)


async def get_schedule_for_day(id: int, day: str, stream_group: str) -> str:
    '''Получает и собирает расписание на конкретный день'''
    day = day.lower()
    stream_group = stream_group.lower()
    day_time_utc = datetime.weekday(datetime.today().utcnow() +
                                    timedelta(hours=3))

    if day == 'завтра':
        day_time_utc += 1

    if day_time_utc == 6:
        return 'Занятий нет'

    if day_time_utc == 7:
        day_time_utc = 0

    else:
        pass
    parity = await get_parity()

    if parity == 'четная' and day == 'завтра' and day_time_utc == 0:
        parity = 'нечетная'

    elif parity == 'нечетная' and day == 'завтра' and day_time_utc == 0:
        parity = 'четная'

    else:
        pass

    _day = DAYS_ENG[day_time_utc]

    output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + stream_group.upper() + '\n' \
        + 'День недели: ' + DAYS_RU[day_time_utc].capitalize() + '\n' + 'Неделя: ' + parity.capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻\n'
    try:
        response = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?id={id}&stream_group={stream_group}&parity={parity}&day={_day}'))
    except Exception as e:
        logger.error(
            f"Ошибка в выводе расписания ({e}): {traceback.format_exc()}")
        return "Ошибка в получении расписания. Информация об ошибке направлена разработчикам"
    try:
        button = await db_get_priority_button(id)
    except Exception as e:
        logger.error(
            f"Ошибка в получении кнопки ({e}): {traceback.format_exc()}")
        return "Ошибка в получении кнопки приоритета. Информация об ошибке направлена разработчикам"

    if button == 'свое':
        if response["personal_schedule"][_day] == "":
            if response["headman_schedule"][_day] == "":
                output += response["shared_schedule"][_day]
                if response["personal_annotation"][_day] == "":
                    if response["headman_annotation"][_day] == "":
                        pass
                    else:
                        output += "\nАннотация от старосты:\n" + \
                            response["headman_annotation"][_day]
                else:
                    output += "\nАннотация от вас:\n" + \
                        response["personal_annotation"][_day]
            else:
                output = "Данный день изменен старостой: \n" + output
                output += response["headman_schedule"][_day]
                if response["personal_annotation"][_day] == "":
                    if response["headman_annotation"][_day] == "":
                        pass
                    else:
                        output += "\nАннотация от старосты:\n" + \
                            response["headman_annotation"][_day]
                else:
                    output += "\nАннотация от вас:\n" + \
                        response["personal_annotation"][_day]
        else:
            output = "Данный день изменен вами: \n" + output
            output += response["personal_schedule"][_day]
            if response["personal_annotation"][_day] == "":
                if response["headman_annotation"][_day] == "":
                    pass
                else:
                    output += "\nАннотация от старосты:\n" + \
                        response["headman_annotation"][_day]
            else:
                output += "\nАннотация от вас:\n" + \
                    response["personal_annotation"][_day]
    else:
        if response["headman_schedule"][_day] == "":
            if response["personal_schedule"][_day] == "":
                output += response["shared_schedule"][_day]
                if response["headman_annotation"][_day] == "":
                    if response["personal_annotation"][_day] == "":
                        pass
                    else:
                        output += "\nАннотация от вас:\n" + \
                            response["personal_annotation"][_day]
                else:
                    output += "\nАннотация от старосты:\n" + \
                        response["headman_annotation"][_day]
            else:
                output = "Данный день изменен вами: \n" + output
                output += response["personal_schedule"][_day]
                if response["headman_annotation"][_day] == "":
                    if response["personal_annotation"][_day] == "":
                        pass
                    else:
                        output += "\nАннотация от вас:\n" + \
                            response["personal_annotation"][_day]
                else:
                    output += "\nАннотация от старосты:\n" + \
                        response["headman_annotation"][_day]
        else:
            output = "Данный день изменен старостой: \n" + output
            output += response["headman_schedule"][_day]
            if response["headman_annotation"][_day] == "":
                if response["personal_annotation"][_day] == "":
                    pass
                else:
                    output += "\nАннотация от вас:\n" + \
                        response["personal_annotation"][_day]
            else:
                output += "\nАннотация от старосты:\n" + \
                    response["headman_annotation"][_day]
    return output


async def get_schedule_for_whole_week(id: int, week: str, stream_group: str) -> str:
    '''Получает и собирает расписание на всю неделю'''
    week = week.lower()
    stream_group = stream_group.lower()

    parity = await get_parity()
    if parity == 'четная':
        if week == 'следующая неделя':
            parity = 'нечетная'
        else:
            parity = 'четная'
    else:
        if week == 'следующая неделя':
            parity = 'четная'
        else:
            parity = 'нечетная'

    output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + stream_group.upper() + '\n' \
        + 'Неделя: ' + parity.capitalize() + '\n' + '⸻⸻⸻⸻⸻\n'

    try:
        response = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?id={id}&stream_group={stream_group}&parity={parity}'))
    except Exception as e:
        logger.error(
            f"Ошибка в выводе расписания ({e}): {traceback.format_exc()}")
        return "Ошибка в получении расписания. Информация об ошибке направлена разработчикам"
    try:
        button = await db_get_priority_button(id)
    except Exception as e:
        logger.error(
            f"Ошибка в получении кнопки ({e}): {traceback.format_exc()}")
        return "Ошибка в получении кнопки приоритета. Информация об ошибке направлена разработчикам"
    for i in range(6):
        if button == 'свое':
            if response["personal_schedule"][DAYS_ENG[i]] == "":
                if response["headman_schedule"][DAYS_ENG[i]] == "":
                    output += '\n' + \
                        DAYS_RU[i].capitalize() + '\n\n'
                    output += response["shared_schedule"][DAYS_ENG[i]]
                else:
                    output += '\n' + \
                        DAYS_RU[i].capitalize() + \
                        " - изменен старостой: \n\n"
                    output += response["headman_schedule"][DAYS_ENG[i]]
            else:
                output += '\n' + \
                    DAYS_RU[i].capitalize() + \
                    " - изменен вами: \n\n"
                output += response["personal_schedule"][DAYS_ENG[i]]
        else:
            if response["headman_schedule"][DAYS_ENG[i]] == "":
                if response["personal_schedule"][DAYS_ENG[i]] == "":
                    output += '\n' + \
                        DAYS_RU[i].capitalize() + '\n\n'
                    output += response["shared_schedule"][DAYS_ENG[i]]
                else:
                    output += '\n' + \
                        DAYS_RU[i].capitalize() + \
                        " - изменен вами: \n\n"
                    output += response["personal_schedule"][DAYS_ENG[i]]
            else:
                output += '\n' + \
                    DAYS_RU[i].capitalize() + \
                    " - изменен старостой: \n\n"
                output += response["headman_schedule"][DAYS_ENG[i]]

    return output


async def get_schedule_custom_headman(id: int, stream_group: str, day_of_week: str, parity: bool) -> str:
    try:
        output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + stream_group.upper() + '\n' \
            + 'День недели: ' + day_of_week.capitalize() + '\n' + 'Неделя: ' + parity.capitalize() + '\n' \
            + '⸻⸻⸻⸻⸻\n'
        day_of_week = translit(
            day_of_week, language_code='ru', reversed=True).replace("'", "")

        response = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?id={id}&stream_group={stream_group}&parity={parity}&day={day_of_week}'))

        if response['headman_schedule'][day_of_week] != "":
            output = "↤↤ Текущее расписание (Измененное вами) ↦↦ \n\n" + output + \
                response['headman_schedule'][day_of_week] + \
                "\nАннотация: " + (response['headman_annotation'][day_of_week]
                                   if response['headman_annotation'][day_of_week] != "" else 'Отсутствует') + '\n'
            output += "\n\n↤↤ Оригинальное расписание(Без изменений) ↦↦ \n\n" + \
                response['shared_schedule'][day_of_week]
        else:
            output += "Текущее расписание: \n\n" + \
                response['shared_schedule'][day_of_week]

        return output
    except Exception as e:
        logger.error(
            f"Error in sheethandler printing schedule ({e}): {traceback.format_exc()}")
        return "Ошибка в получении расписания. Информация об ошибке направлена разработчикам"


async def get_schedule_custom_personal(id: int, stream_group: str, day_of_week: str, parity: bool) -> str:
    try:
        output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + stream_group.upper() + '\n' \
            + 'День недели: ' + day_of_week.capitalize() + '\n' + 'Неделя: ' + parity.capitalize() + '\n' \
            + '⸻⸻⸻⸻⸻\n'
        day_of_week = translit(
            day_of_week, language_code='ru', reversed=True).replace("'", "")

        response = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?id={id}&stream_group={stream_group}&parity={parity}&day={day_of_week}'))

        if response['personal_schedule'][day_of_week] != "":
            output += "↤↤ Текущее расписание (Измененное вами) ↦↦ \n\n" + \
                response['personal_schedule'][day_of_week] + \
                "\nАннотация: " + (response['personal_annotation'][day_of_week]
                                   if response['personal_annotation'][day_of_week] != '' else 'Отсутствует.') + '\n'
            output += "\n\n↤↤ Оригинальное расписание(Без изменений) ↦↦ \n\n" + \
                response['shared_schedule'][day_of_week]
        else:
            output += "Текущее расписание: \n\n" + \
                response['shared_schedule'][day_of_week]

        return output
    except Exception as e:
        logger.error(
            f"Error in sheethandler printing schedule ({e}): {traceback.format_exc()}")
        return "Ошибка в получении расписания. Информация об ошибке направлена разработчикам"
