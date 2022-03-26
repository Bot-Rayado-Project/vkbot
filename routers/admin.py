import keyboards.menu_kb as menu_kb
import keyboards.admin_kb as admin_kb
import keyboards.special_blueprints_kb as special_blueprints
import entry

from utils.sqlite_requests import database_handler
from utils.terminal_codes import set_stdout_to_log_file, close_file
from utils.attachments import get_file_from_path

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter
from datetime import datetime


admin_router = DefaultRouter()


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "special_blueprints"}))
@database_handler()
async def special_blueprints_handler(event: SimpleBotEvent) -> str:
    await event.answer(message='Выберите шаблон', keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "logs"}))
@database_handler()
async def logs_handler(event: SimpleBotEvent) -> str:
    if str(event.from_id) in entry.ALLOWED_USER_IDS_START:
        close_file()
        log_file = await get_file_from_path(event, f"{datetime.now()}.log", "info.log")
        await event.answer(message=f'Файл логов на {datetime.now()}', keyboard=menu_kb.START_KB.get_keyboard(), attachment=log_file)
        set_stdout_to_log_file()
    else:
        await event.answer(message='ACCESS DENIED.', keyboard=admin_kb.ADMIN_KB.get_keyboard())


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "allowed_list"}))
@database_handler()
async def allowed_list_handler(event: SimpleBotEvent) -> str:
    if str(event.from_id) in entry.ALLOWED_USER_IDS_START:
        await event.answer(message=f'Список людей с доступом к админ панели: {entry.ALLOWED_USER_IDS_ADMIN_PANEL}', keyboard=admin_kb.ADMIN_KB.get_keyboard())
    else:
        await event.answer(message=f'ACCESS DENIED.', keyboard=admin_kb.ADMIN_KB.get_keyboard())


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "remove_allowed"}))
@database_handler()
async def allowed_list_handler(event: SimpleBotEvent) -> str:
    print(str(event.from_id))
    print(entry.ALLOWED_USER_IDS_START)
    print(entry.ALLOWED_USER_IDS_ADMIN_PANEL)
    if str(event.from_id) in entry.ALLOWED_USER_IDS_START:
        await event.answer(message='Введите ID пользователя для удаления из списка доступа к админ панели.')
    else:
        await event.answer(message=f'ACCESS DENIED.', keyboard=admin_kb.ADMIN_KB.get_keyboard())


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "add_allowed"}))
@database_handler()
async def allowed_list_handler(event: SimpleBotEvent) -> str:
    if str(event.from_id) in entry.ALLOWED_USER_IDS_START:
        await event.answer(message='Введите ID пользователя для добавления в список доступа к админ панели.')
    else:
        await event.answer(message=f'ACCESS DENIED.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
