import botrayado.keyboards.menu_kb as menu_kb
import botrayado.keyboards.admin_kb as admin_kb

from botrayado.database.db import database_handler
from botrayado.utils.constants import _USERSIDS

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter

donate_router = DefaultRouter()


@simple_bot_message_handler(donate_router, PayloadFilter({"button": "donate"}))
@database_handler()
async def donate(event: SimpleBotEvent) -> str:
    if str(event.from_id) in _USERSIDS:
        await event.answer(message='Access granted.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
    else:
        await event.answer(message='Благодарим всех за поддержку\nhttps://www.tinkoff.ru/cf/67hbUB2jUpf', keyboard=menu_kb.START_KB.get_keyboard())
