import botrayado.keyboards.menu_kb as menu_kb
import botrayado.keyboards.admin_kb as admin_kb

from botrayado.database.db import database_handler
from botrayado.utils.constants import _USERSIDS
from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent


idiots_router = DefaultRouter()


@simple_bot_message_handler(idiots_router)
@database_handler(ret_cmd=True, is_menu=True)
async def goodbye(event: SimpleBotEvent, fetch: list) -> None:
    try:
        last_command = fetch[1][0].lower()
    except Exception:
        await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.START_KB.get_keyboard())
        pass
    if last_command == 'дать доступ':
        _USERSIDS.append(str(event.text))
        await event.answer(message=f'Пользователь {event.text} добавлен в список.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
    elif last_command == 'забрать доступ':
        _USERSIDS.remove(str(event.text))
        await event.answer(message=f'Пользователь {event.text} удален из списка.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
    else:
        await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.START_KB.get_keyboard())
