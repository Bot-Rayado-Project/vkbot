import keyboards.menu_kb as menu_kb

from utils.sqlite_requests import database_handler

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter


geobot_router = DefaultRouter()


@simple_bot_message_handler(geobot_router, PayloadFilter({"button": "miamor"}))
@database_handler()
async def miamor(event: SimpleBotEvent) -> str:
    await event.answer(message='https://vk.cc/8U7VuC', keyboard=menu_kb.START_KB.get_keyboard())
