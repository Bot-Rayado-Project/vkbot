import keyboards.schedule_kb as schedule_kb
import keyboards.menu_kb as menu_kb
import schedule.sheethandler as sheethandler


from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, TextFilter

from utils.sqlite_requests import database_handler
from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, PayloadContainsFilter
from datetime import datetime, timedelta


aliases_router = DefaultRouter()


@simple_bot_message_handler(aliases_router, TextFilter("rayadotd"))
@database_handler()
async def rayadotd(event: SimpleBotEvent) -> None:
    answers: list = [await sheethandler.print_schedule("сегодня", "бвт2103", event.from_id, 'текущая неделя')]
    answers += [await sheethandler.print_schedule("сегодня", "бст2103", event.from_id, 'текущая неделя')]
    answers += [await sheethandler.print_schedule("сегодня", "бст2106", event.from_id, 'текущая неделя')]
    for i in range(len(answers)):
        await event.answer(message=answers[i], keyboard=menu_kb.START_KB.get_keyboard())


@simple_bot_message_handler(aliases_router, TextFilter("rayadotmr"))
@database_handler()
async def rayadotd(event: SimpleBotEvent) -> None:
    answers: list = [await sheethandler.print_schedule("завтра", "бвт2103", event.from_id, 'текущая неделя')]
    answers += [await sheethandler.print_schedule("завтра", "бст2103", event.from_id, 'текущая неделя')]
    answers += [await sheethandler.print_schedule("завтра", "бст2106", event.from_id, 'текущая неделя')]
    for i in range(len(answers)):
        await event.answer(message=answers[i], keyboard=menu_kb.START_KB.get_keyboard())
