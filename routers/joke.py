import keyboards.menu_kb as menu_kb

from utils.sqlite_requests import database_handler
from utils.aiohttp_requests import aiohttp_fetch

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter


joke_router = DefaultRouter()


@simple_bot_message_handler(joke_router, PayloadFilter({"button": "joke"}))
@database_handler()
async def get_joke(event: SimpleBotEvent) -> str:
    msg = (await aiohttp_fetch(url='http://rzhunemogu.ru/RandJSON.aspx?CType=11'))[12:-2]
    await event.answer(message=msg, keyboard=menu_kb.START_KB.get_keyboard())
