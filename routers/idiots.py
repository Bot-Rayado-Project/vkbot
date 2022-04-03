import keyboards.menu_kb as menu_kb
import keyboards.admin_kb as admin_kb
import utils.settings as sett

from utils.sqlite_requests import database_handler

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent


idiots_router = DefaultRouter()


@simple_bot_message_handler(idiots_router)
@database_handler(ret_cmd=True, is_menu=True)
async def goodbye(event: SimpleBotEvent, fetch: list) -> None:
    try:
        last_command = fetch[1][0].lower()
    except:
        await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.START_KB.get_keyboard())
        pass
    if last_command == 'дать доступ':
        try:
            print(sett.ALLOWED_USER_IDS_ADMIN_PANEL)
            print(sett.ALLOWED_USER_IDS_START)
            sett.ALLOWED_USER_IDS_ADMIN_PANEL += [str(event.text)]
            print(sett.ALLOWED_USER_IDS_ADMIN_PANEL)
            print(sett.ALLOWED_USER_IDS_START)
            await event.answer(message=f'Пользователь {event.text} добавлен в список.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
        except ValueError:
            await event.answer(message=f'Ошибка добавления {event.text} в список {sett.ALLOWED_USER_IDS_ADMIN_PANEL}.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
        except AttributeError:
            await event.answer(message=f'Критическая ошибка. Список - не список.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
    elif last_command == 'забрать доступ':
        try:
            sett.ALLOWED_USER_IDS_ADMIN_PANEL.remove(str(event.text))
            await event.answer(message=f'Пользователь {event.text} удален из списка.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
        except ValueError:
            await event.answer(message=f'Ошибка удаления {event.text} из списка {sett.ALLOWED_USER_IDS_ADMIN_PANEL}. Значения нет.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
        except AttributeError:
            await event.answer(message=f'Критическая ошибка. Список - не список.', keyboard=admin_kb.ADMIN_KB.get_keyboard())
    else:
        await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.START_KB.get_keyboard())
