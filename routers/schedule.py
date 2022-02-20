from email import message
from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler, TextFilter
from utils.keyboards import *
from utils.sqlite_requests import sqlite_fetch
import schedule.sheethandler as sheethandler
from datetime import datetime


schedule_router = DefaultRouter()


@simple_bot_message_handler(schedule_router, TextFilter("расписание"))
async def get_schedule(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if fetch[0][0].lower() not in COMMANDS:
        await event.answer(message='Выберите день', keyboard=DAYS_OF_WEEK_KB.get_keyboard())
    else:
        await event.answer(message='Выберите правильную команду.', keyboard=START_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, TextFilter(DAYS_OF_WEEK_BUTTONS))
async def get_day_of_week(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if all((any(cmd.lower() in [fetch[0][0].lower()] for cmd in DAYS_OF_WEEK_BUTTONS), fetch[1][0].lower() == 'расписание')):
        await event.answer(message='Выберите поток', keyboard=POTOK_KB.get_keyboard())
    else:
        await event.answer(message='Неверно выбран поток', keyboard=START_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, TextFilter(POTOK_BUTTONS[0]))
async def get_group(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if all((any(cmd.lower() in [fetch[0][0].lower()] for cmd in POTOK_BUTTONS), any(cmd.lower() in [fetch[1][0].lower()] for cmd in DAYS_OF_WEEK_BUTTONS), fetch[2][0].lower() == 'расписание')):
        await event.answer(message='Выберите группу', keyboard=GROUP_BUTTONS_BFI_KB.get_keyboard())
    else:
        await event.answer(message='Неверно выбрана что то.', keyboard=START_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, TextFilter(POTOK_BUTTONS[1]))
async def get_group(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if all((any(cmd.lower() in [fetch[0][0].lower()] for cmd in POTOK_BUTTONS), any(cmd.lower() in [fetch[1][0].lower()] for cmd in DAYS_OF_WEEK_BUTTONS), fetch[2][0].lower() == 'расписание')):
        await event.answer(message='Выберите группу', keyboard=GROUP_BUTTONS_BVT_KB.get_keyboard())
    else:
        await event.answer(message='Неверно выбрана что то.', keyboard=START_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, TextFilter(POTOK_BUTTONS[2]))
async def get_group(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if all((any(cmd.lower() in [fetch[0][0].lower()] for cmd in POTOK_BUTTONS), any(cmd.lower() in [fetch[1][0].lower()] for cmd in DAYS_OF_WEEK_BUTTONS), fetch[2][0].lower() == 'расписание')):
        await event.answer(message='Выберите группу', keyboard=GROUP_BUTTONS_BST_KB.get_keyboard())
    else:
        await event.answer(message='Неверно выбрана что то.', keyboard=START_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, TextFilter(GROUP_BUTTONS))
async def get_week(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if (fetch[2][0].lower() == 'сегодня' and datetime.weekday(datetime.today()) == 6) or (fetch[2][0].lower() == 'завтра' and datetime.weekday(datetime.today()) == 5):
        await event.answer(message=str(fetch[2][0].capitalize() + ' нет занятий.'), keyboard=START_KB.get_keyboard())
    else:
        if fetch[2][0].lower() == 'завтра' and datetime.weekday(datetime.today()) == 6:
            schedule = await sheethandler.print_schedule(fetch[2][0].lower(), fetch[0][0].lower(), event.from_id, 'следующая неделя')
        else:
            schedule = await sheethandler.print_schedule(fetch[2][0].lower(), fetch[0][0].lower(), event.from_id, 'текущая неделя')
        if fetch[2][0].lower() == 'вся неделя':
            for i in range(len(schedule)):
                await event.answer(message=schedule[i], keyboard=START_KB.get_keyboard())
        else:
            await event.answer(message=schedule, keyboard=START_KB.get_keyboard())
