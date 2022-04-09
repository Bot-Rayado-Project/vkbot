import botrayado.keyboards.menu_kb as menu_kb
import aiohttp
from botrayado.database.db import database_handler

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter

joke_router = DefaultRouter()


async def aiohttp_fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


@simple_bot_message_handler(joke_router, PayloadFilter({"button": "joke"}))
@database_handler()
async def get_joke(event: SimpleBotEvent) -> str:
    msg = (await aiohttp_fetch(url='http://rzhunemogu.ru/RandJSON.aspx?CType=11'))[12:-2]
    await event.answer(message=msg, keyboard=menu_kb.START_KB.get_keyboard())
