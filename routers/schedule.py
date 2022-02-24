from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler, TextFilter
from keyboards.schedule_kb import *
from keyboards.menu_kb import *
from utils.sqlite_requests import sqlite_fetch
import schedule.sheethandler as sheethandler
from datetime import datetime


schedule_router = DefaultRouter()


@simple_bot_message_handler(schedule_router, TextFilter("расписание"))
async def get_schedule(event: SimpleBotEvent) -> str:
    fetch = sqlite_fetch(event.from_id, event.text, True)
    await event.answer(message='Выберите день.', keyboard=DAYS_OF_WEEK_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, TextFilter(DAYS_OF_WEEK_BUTTONS))
async def get_day_of_week(event: SimpleBotEvent) -> str:
    fetch = sqlite_fetch(event.from_id, event.text, True)
    last_command = fetch[0][0].lower()  # Последняя команда
    penultimate_command = fetch[1][0].lower()  # Предпоследняя команда
    if penultimate_command == 'расписание':
        if last_command == DAYS_OF_WEEK_BUTTONS[2]:  # == вся неделя
            await event.answer(message='Выберите неделю.', keyboard=CURRENT_OR_NEXT_WEEK_KB.get_keyboard())
        else:  # == сегодня | завтра
            await event.answer(message='Выберите поток.', keyboard=STREAM_KB.get_keyboard())
    else:
        await event.answer(message='Неверно выбран день.', keyboard=START_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, TextFilter(CURRENT_OR_NEXT_WEEK_BUTTONS))
async def get_current_or_next_week(event: SimpleBotEvent) -> str:
    fetch = sqlite_fetch(event.from_id, event.text, True)
    penultimate_command = fetch[1][0].lower()  # Предпоследняя команда
    pre_penultimate_command = fetch[2][0].lower()  # Пред предпоследняя команда
    if pre_penultimate_command == 'расписание' and any(cmd.lower() in [penultimate_command] for cmd in DAYS_OF_WEEK_BUTTONS):
        await event.answer(message='Выберите поток.', keyboard=STREAM_KB.get_keyboard())
    else:
        await event.answer(message='Неверно выбран поток.', keyboard=START_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, TextFilter(STREAM_BUTTONS))
async def get_stream(event: SimpleBotEvent) -> str:
    fetch = sqlite_fetch(event.from_id, event.text, True)
    last_command = fetch[0][0].lower()  # Последняя команда
    penultimate_command = fetch[1][0].lower()  # Предпоследняя команда
    pre_penultimate_command = fetch[2][0].lower()  # Пред предпоследняя команда
    if any(cmd.lower() in [penultimate_command] for cmd in CURRENT_OR_NEXT_WEEK_BUTTONS):
        pre_pre_penultimate_command = fetch[3][0].lower()
        if pre_pre_penultimate_command == 'расписание' and any(cmd.lower() in [pre_penultimate_command] for cmd in DAYS_OF_WEEK_BUTTONS):
            if last_command == 'бфи':
                await event.answer(message='Выберите группу.', keyboard=GROUP_BUTTONS_BFI_KB.get_keyboard())
            elif last_command == 'бвт':
                await event.answer(message='Выберите группу.', keyboard=GROUP_BUTTONS_BVT_KB.get_keyboard())
            elif last_command == 'бст':
                await event.answer(message='Выберите группу.', keyboard=GROUP_BUTTONS_BST_KB.get_keyboard())
    elif pre_penultimate_command == 'расписание' and any(cmd.lower() in [penultimate_command] for cmd in DAYS_OF_WEEK_BUTTONS) and penultimate_command != DAYS_OF_WEEK_BUTTONS[2]:
        if last_command == 'бфи':
            await event.answer(message='Выберите группу.', keyboard=GROUP_BUTTONS_BFI_KB.get_keyboard())
        elif last_command == 'бвт':
            await event.answer(message='Выберите группу.', keyboard=GROUP_BUTTONS_BVT_KB.get_keyboard())
        elif last_command == 'бст':
            await event.answer(message='Выберите группу.', keyboard=GROUP_BUTTONS_BST_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, TextFilter(GROUP_BUTTONS))
async def get_group(event: SimpleBotEvent) -> str:
    fetch = sqlite_fetch(event.from_id, event.text, True)
    last_command = fetch[0][0].lower()  # Последняя команда # ГРУППА
    penultimate_command = fetch[1][0].lower()  # Предпоследняя команда
    pre_penultimate_command = fetch[2][0].lower()  # Пред предпоследняя команда
    if any(cmd.lower() in [penultimate_command] for cmd in STREAM_BUTTONS):
        # Пре пре пре пре последняя команда
        pre_pre_penultimate_command = fetch[3][0].lower()
        if any(cmd.lower() in [pre_penultimate_command] for cmd in CURRENT_OR_NEXT_WEEK_BUTTONS) and pre_pre_penultimate_command == DAYS_OF_WEEK_BUTTONS[2]:
            schedule = await sheethandler.print_schedule('вся неделя', last_command, event.from_id, pre_penultimate_command)
            for i in range(len(schedule)):
                await event.answer(message=schedule[i], keyboard=START_KB.get_keyboard())
        elif any(cmd.lower() in [pre_penultimate_command] for cmd in DAYS_OF_WEEK_BUTTONS):
            if (pre_penultimate_command == 'сегодня' and datetime.weekday(datetime.today()) == 6) or (pre_penultimate_command == 'завтра' and datetime.weekday(datetime.today()) == 5):
                await event.answer(message=str(pre_penultimate_command + ' нет занятий.'), keyboard=START_KB.get_keyboard())
            else:
                if pre_penultimate_command == 'завтра' and datetime.weekday(datetime.today()) == 6:
                    schedule = await sheethandler.print_schedule(pre_penultimate_command, last_command, event.from_id, 'следующая неделя')
                else:
                    schedule = await sheethandler.print_schedule(pre_penultimate_command, last_command, event.from_id, 'текущая неделя')
                await event.answer(message=schedule, keyboard=START_KB.get_keyboard())
        else:
            await event.answer(message="Непредвиденная ошибка.", keyboard=START_KB.get_keyboard())
