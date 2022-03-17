
import keyboards.menu_kb as menu_kb

from utils.sqlite_requests import database_handler

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent


idiots_router = DefaultRouter()


@simple_bot_message_handler(idiots_router)
@database_handler()
async def goodbye(event: SimpleBotEvent) -> None:
    await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.START_KB.get_keyboard())
