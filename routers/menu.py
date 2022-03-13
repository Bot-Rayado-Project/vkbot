from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler, TextFilter, PayloadFilter
from utils.sqlite_requests import sqlite_fetch
from keyboards.menu_kb import START_KB


menu_router = DefaultRouter()


@simple_bot_message_handler(menu_router, TextFilter(["привет", "начать", "начало", "старт", "меню", "расписание"], PayloadFilter({"button": "menu"})))
async def greet(event: SimpleBotEvent) -> str:
    user = await event.get_user()
    sqlite_fetch(event, user)
    await event.answer(message='Выберите команду из списка.', keyboard=START_KB.get_keyboard())
