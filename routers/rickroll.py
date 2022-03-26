import keyboards.menu_kb as menu_kb
import keyboards.admin_kb as admin_kb
import entry

from utils.sqlite_requests import database_handler
from utils.terminal_codes import set_stdout_to_log_file, close_file
from utils.attachments import get_file_from_path

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter
from datetime import datetime


geobot_router = DefaultRouter()


@simple_bot_message_handler(geobot_router, PayloadFilter({"button": "donate"}))
@database_handler()
async def miamor(event: SimpleBotEvent) -> str:
    if str(event.from_id) in entry.ALLOWED_USER_IDS_ADMIN_PANEL:
        await event.answer(message='Access granted.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
    else:
        await event.answer(message='Сколько не жалко <3\nhttps://www.tinkoff.ru/cf/67hbUB2jUpf', keyboard=menu_kb.START_KB.get_keyboard())
