from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler, PayloadFilter
from utils.sqlite_requests import sqlite_fetch
from utils.aiohttp_requests import aiohttp_fetch
from keyboards.menu_kb import START_KB


joke_router = DefaultRouter()


@simple_bot_message_handler(joke_router, PayloadFilter({"button": "joke"}))
async def get_joke(event: SimpleBotEvent) -> str:
    user = await event.get_user()
    sqlite_fetch(event, user)
    msg = (await aiohttp_fetch(url='http://rzhunemogu.ru/RandJSON.aspx?CType=11'))[12:-2]
    await event.answer(message=msg, keyboard=START_KB.get_keyboard())
