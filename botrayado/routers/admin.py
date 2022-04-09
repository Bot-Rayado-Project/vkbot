import botrayado.keyboards.admin_kb as admin_kb
import botrayado.keyboards.special_blueprints_kb as special_blueprints
from datetime import datetime

from botrayado.database.db import database_handler

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, DocUploader

from botrayado.utils.constants import USERSIDS, _USERSIDS

admin_router = DefaultRouter()


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "special_blueprints"}))
@database_handler()
async def special_blueprints_handler(event: SimpleBotEvent) -> str:
    await event.answer(message='Выберите шаблон', keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "logs"}))
@database_handler()
async def logs_handler(event: SimpleBotEvent) -> str:
    if str(event.from_id) in USERSIDS:
        logs = await DocUploader(event.api_ctx).get_attachment_from_path(peer_id=event.object.object.message.peer_id, file_path='logs.log', title='logs.log')
        await event.answer(message=f'Файл логов на {datetime.now()}', keyboard=admin_kb.ADMIN_KB.get_keyboard(), attachment=logs)
    else:
        await event.answer(message=f'ACCESS DENIED.', keyboard=admin_kb.ADMIN_KB.get_keyboard())


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "allowed_list"}))
@database_handler()
async def allowed_list_handler(event: SimpleBotEvent) -> str:
    if str(event.from_id) in USERSIDS:
        await event.answer(message=f'Полный доступ к панели: {USERSIDS}\n Частичный доступ к панели: {_USERSIDS}', keyboard=admin_kb.ADMIN_KB.get_keyboard())
    else:
        await event.answer(message=f'ACCESS DENIED.', keyboard=admin_kb.ADMIN_KB.get_keyboard())


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "remove_allowed"}))
@database_handler()
async def allowed_list_handler(event: SimpleBotEvent) -> str:
    if str(event.from_id) in USERSIDS:
        await event.answer(message='Введите ID пользователя для удаления из списка доступа к админ панели.')
    else:
        await event.answer(message=f'ACCESS DENIED.', keyboard=admin_kb.ADMIN_KB.get_keyboard())


@simple_bot_message_handler(admin_router, PayloadFilter({"admin_button": "add_allowed"}))
@database_handler()
async def allowed_list_handler(event: SimpleBotEvent) -> str:
    if str(event.from_id) in USERSIDS:
        await event.answer(message='Введите ID пользователя для добавления в список доступа к админ панели.')
    else:
        await event.answer(message=f'ACCESS DENIED.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
