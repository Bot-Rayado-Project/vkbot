from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler, TextFilter
from utils.keyboards import *
from utils.sqlite_requests import sqlite_fetch
import schedule.sheethandler as sheethandler


schedule_router = DefaultRouter()


@simple_bot_message_handler(schedule_router, TextFilter("расписание"))
async def get_schedule(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if fetch[0][0].lower() not in COMMANDS:
        await event.answer(message='Выберите день недели.', keyboard=DAYS_OF_WEEK_KB.get_keyboard())
    else:
        await event.answer(message='Выберите правильную команду.', keyboard=START_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, TextFilter(DAYS_OF_WEEK_BUTTONS))
async def get_day_of_week(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if all((any(cmd.lower() in [fetch[0][0].lower()] for cmd in DAYS_OF_WEEK_BUTTONS), fetch[1][0].lower() == 'расписание')):
        await event.answer(message='Выберите группу.', keyboard=GROUPS_KB.get_keyboard())
    else:
        await event.answer(message='Неверно выбрана группа.', keyboard=START_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, TextFilter(GROUPS_BUTTONS))
async def get_group(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if all((any(cmd.lower() in [fetch[0][0].lower()] for cmd in GROUPS_BUTTONS), any(cmd.lower() in [fetch[1][0].lower()] for cmd in DAYS_OF_WEEK_BUTTONS), fetch[2][0].lower() == 'расписание')):
        await event.answer(message='Выберите неделю.', keyboard=CURRENT_OR_NEXT_WEEK_KB.get_keyboard())
    else:
        await event.answer(message='Неверно выбрана что то.', keyboard=START_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, TextFilter(CURRENT_OR_NEXT_WEEK_BUTTONS))
async def get_week(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if all((any(cmd.lower() in [fetch[0][0].lower()] for cmd in CURRENT_OR_NEXT_WEEK_BUTTONS), any(cmd.lower() in [fetch[1][0].lower()] for cmd in GROUPS_BUTTONS), any(cmd.lower() in [fetch[2][0].lower()] for cmd in DAYS_OF_WEEK_BUTTONS), fetch[3][0].lower() == 'расписание')):
        schedule = await sheethandler.print_schedule(fetch[2][0].lower(), fetch[1][0].lower(), fetch[0][0].lower(), event.from_id)
        if fetch[2][0].lower() == 'вся неделя':
            for i in range(len(schedule)):
                await event.answer(message=schedule[i], keyboard=START_KB.get_keyboard())
        else:
            await event.answer(message=schedule, keyboard=START_KB.get_keyboard())
