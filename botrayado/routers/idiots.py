import botrayado.keyboards.menu_kb as menu_kb
import botrayado.keyboards.admin_kb as admin_kb
import botrayado.utils.constants as constants
import aiohttp

from botrayado.database.db import database_handler
from botrayado.utils.constants import _USERSIDS, USERSIDS, headmans_ids
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
async def idiots(event: SimpleBotEvent, fetch: list) -> None:
    if str(event.from_id) in USERSIDS or event.from_id in list(headmans_ids.keys()):

        last_command = fetch[1][0].lower()

        if last_command == 'дать доступ':

            _USERSIDS.append(str(event.text))
            await event.answer(message=f'Пользователь {event.text} добавлен в список.', keyboard=admin_kb.ADMIN_KB.get_keyboard())

        elif last_command == 'забрать доступ':

            _USERSIDS.remove(str(event.text))
            await event.answer(message=f'Пользователь {event.text} удален из списка.', keyboard=admin_kb.ADMIN_KB.get_keyboard())

        elif last_command == 'перезаписать(записать)':
            # Задание действия удалить или перезаписать(записать)
            constants.headman_requests[event.from_id] = constants.HeadmanRequest(
                week=constants.headman_requests[event.from_id].week,
                dayofweek=constants.headman_requests[event.from_id].dayofweek,
                pair=constants.headman_requests[event.from_id].pair,
                move=constants.headman_requests[event.from_id].move,
                changes=event.text,
                group=constants.headmans_ids.get(event.from_id)
            )

            # Если пара = 0, значит аннотация на весь день
            if constants.headman_requests[event.from_id].pair != 0:

                logger.info(constants.headman_requests[event.from_id])
                response = await post_request(
                    url=f'http://{RESTIP}:{RESTPORT}/change-schedule/',
                    data={
                        'week': constants.headman_requests[event.from_id].week,
                        'dayofweek': constants.headman_requests[event.from_id].dayofweek,
                        'group': constants.headman_requests[event.from_id].group,
                        'pair': constants.headman_requests[event.from_id].pair,
                        'changes': constants.headman_requests[event.from_id].changes
                    }
                )
                print(response)
                even = True if constants.headman_requests[event.from_id].week.lower() == 'четная' else False
                schedule = await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                                    constants.headman_requests[event.from_id].dayofweek.lower(),
                                                                    even)
                await event.answer(message=f'Успешно перезаписано', keyboard=menu_kb.START_KB.get_keyboard())
                await event.answer(message=f'Измененный день:\n {schedule}', keyboard=menu_kb.START_KB.get_keyboard())

            else:

                logger.info(constants.headman_requests[event.from_id])
                response = await post_request(
                    url=f'http://{RESTIP}:{RESTPORT}/add-annotation/',
                    data={
                        'week': constants.headman_requests[event.from_id].week,
                        'dayofweek': constants.headman_requests[event.from_id].dayofweek,
                        'group': constants.headman_requests[event.from_id].group,
                        'annotation': constants.headman_requests[event.from_id].changes
                    }
                )
                print(response)
                even = True if constants.headman_requests[event.from_id].week.lower() == 'четная' else False
                schedule = await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                                    constants.headman_requests[event.from_id].dayofweek.lower(),
                                                                    even)
                await event.answer(message=f'Успешно перезаписано', keyboard=menu_kb.START_KB.get_keyboard())
                await event.answer(message=f'Измененный день:\n {schedule}', keyboard=menu_kb.START_KB.get_keyboard())

        else:

            await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.START_KB.get_keyboard())

        constants.headman_requests[event.from_id] = constants.HeadmanRequest()

    else:

        await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.START_KB.get_keyboard())
