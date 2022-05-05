from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, DocUploader
from datetime import datetime
from botrayado.utils import *
from botrayado.keyboards import *
from botrayado.database import *
from botrayado.database.db import cursor

admin_router = DefaultRouter()


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "special_blueprints"}))
@database_handler()
async def special_blueprints_handler(event: SimpleBotEvent) -> str:
    await event.answer(message='Выберите шаблон', keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "logs"}))
@database_handler()
async def logs_handler(event: SimpleBotEvent) -> str:
    cursor.execute(
        f"SELECT full_admin_panel FROM accesses WHERE user_id={event.from_id}")
    fetch_admin = cursor.fetchall()
    if fetch_admin == []:
        is_admin = False
    else:
        is_admin = fetch_admin[0][0]
    if is_admin:
        logs = await DocUploader(event.api_ctx).get_attachment_from_path(peer_id=event.object.object.message.peer_id, file_path='logs.log', title='logs.log')
        await event.answer(message=f'Файл логов на {datetime.now()}', keyboard=admin_kb.ADMIN_KB.get_keyboard(), attachment=logs)
    else:
        await event.answer(message=f'ACCESS DENIED.', keyboard=admin_kb.ADMIN_KB.get_keyboard())


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "allowed_list"}))
@database_handler()
async def allowed_list_handler(event: SimpleBotEvent) -> str:
    pass


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "remove_allowed"}))
@database_handler()
async def allowed_list_handler(event: SimpleBotEvent) -> str:
    pass


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "add_allowed"}))
@database_handler()
async def allowed_list_handler(event: SimpleBotEvent) -> str:
    pass
