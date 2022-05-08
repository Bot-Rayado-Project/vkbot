from datetime import datetime, timedelta
from bot.utils import get_parity, aiohttp_fetch
from bot.constants import DAYS_RU, DAYS_ENG, RESTIP, RESTPORT
from bot.db import db_get_priority_button
import json


async def get_schedule_for_day(id: int, day: str, stream_group: str) -> str:
    '''Получает и собирает расписание на конкретный день'''
    day = day.lower()
    stream_group = stream_group.lower()
    day_time_utc = datetime.weekday(datetime.today().utcnow() +
                                    timedelta(hours=3))
    print(day_time_utc)

    if day == 'завтра':
        day_time_utc += 1
        print(day_time_utc)

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
    response = json.loads(await aiohttp_fetch(url=f'http://{RESTIP}:{RESTPORT}/schedule/?id={id}&stream_group={stream_group}&parity={parity}&day={_day}'))
    button = await db_get_priority_button(id)
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
