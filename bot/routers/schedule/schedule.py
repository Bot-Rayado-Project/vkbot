from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, PayloadContainsFilter
from bot.keyboards import *


schedule_router = DefaultRouter()


@simple_bot_message_handler(schedule_router, PayloadFilter({"menu_button": "schedule"}))
async def schedule(event: SimpleBotEvent) -> None:
    await event.answer(message='Выберите день недели, либо редактор расписания', keyboard=SCHEDULE_DAY_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("schedule_day_button"))
async def schedule_day(event: SimpleBotEvent) -> None:
    if event.payload["schedule_day_button"] == "today" or event.payload["schedule_day_button"] == "tomorrow":
        await event.answer(message='Выберите факультет', keyboard=SCHEDULE_FACULTY_KB.get_keyboard())
    else:
        await event.answer(message='Выберите четность недели', keyboard=SCHEDULE_PARITY_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("schedule_parity_button"))
async def schedule_faculty(event: SimpleBotEvent) -> None:
    await event.answer(message='Выберите факультет', keyboard=SCHEDULE_FACULTY_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("schedule_faculty_button"))
async def schedule_faculty(event: SimpleBotEvent) -> None:
    await event.answer(message='Выберите поток', keyboard=SCHEDULE_FACULTY_MATCHING[event.payload["schedule_faculty_button"]].get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("schedule_faculty_button"))
async def schedule_stream(event: SimpleBotEvent) -> None:
    await event.answer(message='Выберите поток', keyboard=SCHEDULE_FACULTY_MATCHING[event.payload["schedule_faculty_button"]].get_keyboard())
