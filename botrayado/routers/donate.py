from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter
from botrayado.utils import *
from botrayado.keyboards import *
from botrayado.database import *
from botrayado.database.db import *

donate_router = DefaultRouter()


@simple_bot_message_handler(donate_router, PayloadFilter({"button": "donate"}))
@database_handler(ret_btn=True)
async def donate(event: SimpleBotEvent, button: str) -> str:
    cursor.execute(
        f"SELECT semi_admin_panel FROM accesses WHERE user_id={event.from_id}")
    fetch_admin = cursor.fetchall()
    if fetch_admin == []:
        is_admin = False
    else:
        is_admin = fetch_admin[0][0]
    if is_admin:
        await event.answer(message='Access granted.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
    else:
        await event.answer(message='Благодарим всех за поддержку\nhttps://www.tinkoff.ru/cf/67hbUB2jUpf', keyboard=menu_kb.create_menu_keyboard(button).get_keyboard())
