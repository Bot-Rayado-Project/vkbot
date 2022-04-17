import botrayado.keyboards.menu_kb as menu_kb
import botrayado.keyboards.admin_kb as admin_kb
import botrayado.utils.constants as constants

from botrayado.database.db import database_handler
from botrayado.utils.constants import _USERSIDS, USERSIDS, headmans_ids
from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent


idiots_router = DefaultRouter()


@simple_bot_message_handler(idiots_router)
@database_handler(ret_cmd=True, is_menu=True)
async def idiots(event: SimpleBotEvent, fetch: list) -> None:
    if str(event.from_id) in USERSIDS or event.from_id in list(headmans_ids.keys()):
        last_command = fetch[1][0].lower()
        if last_command == 'дать доступ':
            _USERSIDS.append(str(event.text))
            await event.answer(message=f'Пользователь {event.text} добавлен в список.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
        elif last_command == 'забрать доступ':
            _USERSIDS.remove(str(event.text))
            await event.answer(message=f'Пользователь {event.text} удален из списка.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
        elif last_command == 'перезаписать':
            await event.answer(message=f'Успешно перезаписано', keyboard=admin_kb.ADMIN_KB.get_keyboard())
            constants.headman_requests[event.from_id] = constants.HeadmanRequest()
    else:
        await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.START_KB.get_keyboard())
