import keyboards.menu_kb as menu_kb

from utils.sqlite_requests import database_handler
from utils.terminal_codes import set_stdout_to_log_file, close_file
from utils.attachments import get_file_from_path
from entry import settings

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter
from datetime import datetime


geobot_router = DefaultRouter()


@simple_bot_message_handler(geobot_router, PayloadFilter({"button": "donate"}))
@database_handler()
async def miamor(event: SimpleBotEvent) -> str:
    if str(event.from_id) in settings.GET_ALLOWED_USER_IDS():
        close_file()
        log_file = await get_file_from_path(event, f"{datetime.now()}.log", "info.log")
        await event.answer(message=f'Файл логов на {datetime.now()}', keyboard=menu_kb.START_KB.get_keyboard(), attachment=log_file)
        set_stdout_to_log_file()
    else:
        await event.answer(message='Сколько не жалко <3\nhttps://www.tinkoff.ru/cf/67hbUB2jUpf', keyboard=menu_kb.START_KB.get_keyboard())
