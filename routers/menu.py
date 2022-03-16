from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler, TextFilter, PayloadFilter
from utils.sqlite_requests import database_handler
import keyboards.menu_kb


menu_router = DefaultRouter()


@simple_bot_message_handler(menu_router, TextFilter(["старт", "меню", "расписание"], PayloadFilter({"button": "menu"})))
@database_handler()
async def menu(event: SimpleBotEvent) -> str:
    await event.answer(message='Выберите команду из списка.', keyboard=keyboards.menu_kb.START_KB.get_keyboard())


@simple_bot_message_handler(menu_router, TextFilter(["привет", "добрый день", "здравствуй", "здравствуйте", "ку", "прив", "приффки", "дратути"]))
@database_handler()
async def hello(event: SimpleBotEvent) -> None:
    await event.answer(message='Здравствуйте', keyboard=keyboards.menu_kb.START_KB.get_keyboard())


@simple_bot_message_handler(menu_router, TextFilter(["пока", "до свидания", "бб", "прощай", "до связи"]))
@database_handler()
async def goodbye(event: SimpleBotEvent) -> None:
    await event.answer(message='До свидания', keyboard=keyboards.menu_kb.START_KB.get_keyboard())
