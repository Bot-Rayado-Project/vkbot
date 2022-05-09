from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, TextFilter
from bot.keyboards import create_menu_kb
from bot.utils import aiohttp_fetch

joke_router = DefaultRouter()


@simple_bot_message_handler(joke_router, PayloadFilter({"menu_button": "joke"}))
async def joke(event: SimpleBotEvent) -> None:
    response = (await aiohttp_fetch(url='http://rzhunemogu.ru/RandJSON.aspx?CType=11'))[12:-2]
    await event.answer(message=response, keyboard=(await create_menu_kb(event.from_id)).get_keyboard())


@ simple_bot_message_handler(joke_router, TextFilter("анекдот"))
async def joke(event: SimpleBotEvent) -> None:
    response = (await aiohttp_fetch(url='http://rzhunemogu.ru/RandJSON.aspx?CType=11'))[12:-2]
    await event.answer(message=response, keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
