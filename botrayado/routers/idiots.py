from botrayado.keyboards import *
import botrayado.utils.constants as constants
import botrayado.routers.edit_personal as edit_personal
import botrayado.routers.edit_headman as edit_headman
import aiohttp
import json

from botrayado.database.db import database_handler
from botrayado.database.db import cursor
from botrayado.utils.constants import RESTIP, RESTPORT
from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent
from botrayado.utils.logger import get_logger
import botrayado.schedule.sheethandler as sheethandler


logger = get_logger(__name__)

idiots_router = DefaultRouter()


async def post_request(url: str, data: dict) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, json=data) as response:
            return await response.text()


@simple_bot_message_handler(idiots_router)
@database_handler(ret_cmd=True, is_menu=True)
async def idiots(event: SimpleBotEvent, fetch: list, button: str) -> None:
    try:
        last_command = fetch[1][0].lower()
    except:
        await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.create_menu_keyboard(button).get_keyboard())
    logger.info(last_command)
    cursor.execute(
        f"SELECT full_admin_panel FROM accesses WHERE user_id={event.from_id}")
    fetch_admin = cursor.fetchall()
    if fetch_admin == []:
        is_admin = False
    else:
        is_admin = fetch_admin[0][0]
    logger.info(fetch_admin)
    logger.info(is_admin)
    if last_command == 'дать доступ' and is_admin == True:

        await event.answer(message=f'Пользователь {event.text} добавлен в список.', keyboard=admin_kb.ADMIN_KB.get_keyboard())

    elif last_command == 'забрать доступ' and is_admin == True:

        await event.answer(message=f'Пользователь {event.text} удален из списка.', keyboard=admin_kb.ADMIN_KB.get_keyboard())

    elif last_command == 'перезаписать(записать)':
        cursor.execute(
            f"SELECT stream_group FROM accesses WHERE user_id={event.from_id}")
        group = cursor.fetchall()

        if constants.currently_editing[event.from_id] == True:

            if edit_personal.edit_personal_requests[event.from_id].pair_number != 0:
                response = await post_request(
                    url=f'http://{RESTIP}:{RESTPORT}/change-schedule-personal/',
                    data={
                        'stream_group': edit_personal.edit_personal_requests[event.from_id].stream_group,
                        'day': edit_personal.edit_personal_requests[event.from_id].day,
                        'parity': edit_personal.edit_personal_requests[event.from_id].parity,
                        'pair_number': edit_personal.edit_personal_requests[event.from_id].pair_number,
                        'changes': event.text,
                        'id': event.from_id,
                    }
                )
                if json.loads(response)['ok'] != True:
                    logger.error(
                        'Ошибка при запросе к rest сервису на изменение персональной пары.')
                    await event.answer(message='Ошибка при изменении персональной пары. Информация об ошибке направлена разработчикам', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
                await event.answer(message='Пара успешно изменена', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
            else:
                response = await post_request(
                    url=f'http://{RESTIP}:{RESTPORT}/add-annotation-personal/',
                    data={
                        'stream_group': edit_personal.edit_personal_requests[event.from_id].stream_group,
                        'day': edit_personal.edit_personal_requests[event.from_id].day,
                        'parity': edit_personal.edit_personal_requests[event.from_id].parity,
                        'id': event.from_id,
                        'annotation': event.text
                    }
                )
                if json.loads(response)['ok'] != True:
                    logger.error(
                        'Ошибка при запросе к rest сервису на изменение персональной аннотации.')
                    await event.answer(message='Ошибка при изменении персональной аннотации. Информация об ошибке направлена разработчикам', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
                await event.answer(message='Аннотация успешно изменена', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
            edit_personal.edit_personal_requests[event.from_id] = edit_personal.EditPersonalRequest(
                event.from_id)

        else:

            if edit_headman.edit_headman_requests[event.from_id].pair_number != 0:
                response = await post_request(
                    url=f'http://{RESTIP}:{RESTPORT}/change-schedule-headman/',
                    data={
                        'stream_group': edit_headman.edit_headman_requests[event.from_id].stream_group,
                        'day': edit_headman.edit_headman_requests[event.from_id].day,
                        'parity': edit_headman.edit_headman_requests[event.from_id].parity,
                        'pair_number': edit_headman.edit_headman_requests[event.from_id].pair_number,
                        'changes': event.text
                    }
                )
                if json.loads(response)['ok'] != True:
                    logger.error(
                        'Ошибка при запросе к rest сервису на изменение старосты пары.')
                    await event.answer(message='Ошибка при изменении старосты пары. Информация об ошибке направлена разработчикам', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
                await event.answer(message='Пара успешно изменена', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
            else:
                response = await post_request(
                    url=f'http://{RESTIP}:{RESTPORT}/add-annotation-headman/',
                    data={
                        'stream_group': edit_headman.edit_headman_requests[event.from_id].stream_group,
                        'day': edit_headman.edit_headman_requests[event.from_id].day,
                        'parity': edit_headman.edit_headman_requests[event.from_id].parity,
                        'annotation': event.text
                    }
                )
                if json.loads(response)['ok'] != True:
                    logger.error(
                        'Ошибка при запросе к rest сервису на изменение старосты аннотации.')
                    await event.answer(message='Ошибка при изменении старосты аннотации. Информация об ошибке направлена разработчикам', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
                await event.answer(message='Аннотация успешно изменена', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
            if group != []:
                edit_headman.edit_headman_requests[event.from_id] = edit_headman.EditHeadmanRequest(
                    group[0][0])

    else:

        await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.create_menu_keyboard(button).get_keyboard())
