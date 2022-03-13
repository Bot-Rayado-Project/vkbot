from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler, PayloadFilter, PayloadContainsFilter
from keyboards.schedule_kb import *
from keyboards.menu_kb import *
from utils.sqlite_requests import sqlite_fetch
import schedule.sheethandler as sheethandler
from datetime import datetime, timedelta


schedule_router = DefaultRouter()


@simple_bot_message_handler(schedule_router, PayloadFilter({"button": "schedule"}))
async def get_schedule(event: SimpleBotEvent) -> str:
    user = await event.get_user()
    sqlite_fetch(event, user)
    await event.answer(message='Выберите день.', keyboard=DAYS_OF_WEEK_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("dow_button"))
async def get_day_of_week(event: SimpleBotEvent) -> str:
    user = await event.get_user()
    fetch = sqlite_fetch(event, user, True)
    last_command = fetch[0][0].lower()  # Последняя команда
    if last_command == DAYS_OF_WEEK_BUTTONS[2]:  # == вся неделя
        await event.answer(message='Выберите неделю.', keyboard=CURRENT_OR_NEXT_WEEK_KB.get_keyboard())
    else:  # == сегодня | завтра
        await event.answer(message='Выберите поток.', keyboard=STREAM_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("conw_button"))
async def get_current_or_next_week(event: SimpleBotEvent) -> str:
    user = await event.get_user()
    fetch = sqlite_fetch(event, user, True)
    await event.answer(message='Выберите поток.', keyboard=STREAM_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("stream_button"))
async def get_stream(event: SimpleBotEvent) -> str:
    user = await event.get_user()
    fetch = sqlite_fetch(event, user, True)
    last_command = fetch[0][0].lower()  # Последняя команда
    if last_command == 'бфи':
        await event.answer(message='Выберите группу.', keyboard=GROUP_BUTTONS_BFI_KB.get_keyboard())
    elif last_command == 'бвт':
        await event.answer(message='Выберите группу.', keyboard=GROUP_BUTTONS_BVT_KB.get_keyboard())
    elif last_command == 'бст':
        await event.answer(message='Выберите группу.', keyboard=GROUP_BUTTONS_BST_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("group_button"))
async def get_group(event: SimpleBotEvent) -> str:
    user = await event.get_user()
    fetch = sqlite_fetch(event, user, True)
    last_command = fetch[0][0].lower()  # Последняя команда # ГРУППА
    pre_penultimate_command = fetch[2][0].lower()  # Пред предпоследняя команда
    pre_pre_penultimate_command = fetch[3][0].lower()
    if any(cmd.lower() in [pre_penultimate_command] for cmd in CURRENT_OR_NEXT_WEEK_BUTTONS) and pre_pre_penultimate_command == DAYS_OF_WEEK_BUTTONS[2]:
        schedule = await sheethandler.print_schedule('вся неделя', last_command, event.from_id, pre_penultimate_command)
        for i in range(len(schedule)):
            await event.answer(message=schedule[i], keyboard=START_KB.get_keyboard())
    elif any(cmd.lower() in [pre_penultimate_command] for cmd in DAYS_OF_WEEK_BUTTONS):
        if (pre_penultimate_command == 'сегодня' and datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) == 6) or (pre_penultimate_command == 'завтра' and datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) == 5):
            await event.answer(message=str(pre_penultimate_command + ' нет занятий.'), keyboard=START_KB.get_keyboard())
        else:
            if pre_penultimate_command == 'завтра' and datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) == 6:
                schedule = await sheethandler.print_schedule(pre_penultimate_command, last_command, event.from_id, 'следующая неделя')
            else:
                schedule = await sheethandler.print_schedule(pre_penultimate_command, last_command, event.from_id, 'текущая неделя')
            await event.answer(message=schedule, keyboard=START_KB.get_keyboard())
    else:
        await event.answer(message="Непредвиденная ошибка.", keyboard=START_KB.get_keyboard())
