from typing import NamedTuple
import aiohttp
import json
from botrayado.utils.constants import RESTIP, RESTPORT
import botrayado.utils.constants as constants
from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadContainsFilter
from botrayado.schedule.sheethandler import *
from botrayado.utils import *
from botrayado.keyboards import *
from botrayado.database import *

logger = get_logger(__name__)

edit_personal_router = DefaultRouter()


async def post_request(url: str, data: dict) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, json=data) as response:
            return await response.text()


async def get_request(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            return await response.text()

edit_personal_requests: dict = {}


class EditPersonalRequest(NamedTuple):
    id: int
    stream_group: str = None
    parity: str = None
    day: str = None
    pair_number: int = None
    changes: int = None
    annotation: str = None


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("faculty_button_p"))
@database_handler()
async def get_faculty(event: SimpleBotEvent) -> str:
    constants.currently_editing[event.from_id] = True
    edit_personal_requests[event.from_id] = EditPersonalRequest(
        event.from_id
    )
    await event.answer(message='Выберите поток',
                       keyboard=edit_personal_kb.KB_STREAMS[event.payload['faculty_button_p']]())


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("stream_button_p"))
@database_handler()
async def get_stream(event: SimpleBotEvent) -> str:
    constants.currently_editing[event.from_id] = True
    await event.answer(message='Выберите группу',
                       keyboard=edit_personal_kb.KB[event.text.lower()]())


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("group_button_p"))
@database_handler()
async def get_group(event: SimpleBotEvent) -> str:
    constants.currently_editing[event.from_id] = True
    edit_personal_requests[event.from_id] = EditPersonalRequest(
        event.from_id,
        event.text.lower()
    )
    await event.answer(message='Выберите неделю',
                       keyboard=edit_personal_kb.CHOOSE_WEEK_PERSONAL_KB.get_keyboard())


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("cwp_button"))
@database_handler()
async def choose_week(event: SimpleBotEvent) -> str:
    constants.currently_editing[event.from_id] = True
    edit_personal_requests[event.from_id] = EditPersonalRequest(
        event.from_id,
        edit_personal_requests[event.from_id].stream_group,
        event.text.lower().split()[0]
    )
    await event.answer(message='Выберите день недели',
                       keyboard=edit_personal_kb.CHOOSE_DAY_OF_WEEK_PERSONAL_KB.get_keyboard())


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("cdowp_button"))
@database_handler()
async def choose_day_of_week(event: SimpleBotEvent) -> str:
    constants.currently_editing[event.from_id] = True
    edit_personal_requests[event.from_id] = EditPersonalRequest(
        event.from_id,
        edit_personal_requests[event.from_id].stream_group,
        edit_personal_requests[event.from_id].parity,
        event.text.lower()
    )
    logger.info(edit_personal_requests[event.from_id])
    current_schedule = await print_schedule_custom_personal(event.from_id, edit_personal_requests[event.from_id].stream_group, edit_personal_requests[event.from_id].day, edit_personal_requests[event.from_id].parity)
    await event.answer(message=current_schedule)
    await event.answer(message='Выберите пару, либо воспользуйтесь кнопкой "Сбросить все изменения" для сброса всех изменений',
                       keyboard=edit_personal_kb.CHOOSE_PAIR_PERSONAL_KB.get_keyboard())


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("cpp_button"))
@database_handler()
async def choose_pair_number(event: SimpleBotEvent) -> str:
    constants.currently_editing[event.from_id] = True
    if event.text.lower() == 'сбросить все изменения':
        response = await post_request(
            url=f'http://{RESTIP}:{RESTPORT}/reset-schedule-personal/',
            data={
                'stream_group': edit_personal_requests[event.from_id].stream_group,
                'day': edit_personal_requests[event.from_id].day,
                'parity': edit_personal_requests[event.from_id].parity,
                'id': event.from_id
            }
        )
        if json.loads(response)['ok'] != True:
            logger.error(
                'Ошибка при запросе к rest сервису на сброс всего дня.')
            await event.answer(message='Ошибка при сбросе персонального дня. Информация об ошибке направлена разработчикам', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
        edit_personal_requests[event.from_id] = EditPersonalRequest(
            event.from_id
        )
        current_schedule = await print_schedule(event.from_id, event.text.lower(), edit_personal_requests[event.from_id].stream_group)
        await event.answer(message=f'Новое выводимое расписание: \n\n {current_schedule}')
        await event.answer(message='День успешно сброшен.', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())

    elif event.text.lower() == 'общ. аннотация':
        edit_personal_requests[event.from_id] = EditPersonalRequest(
            event.from_id,
            edit_personal_requests[event.from_id].stream_group,
            edit_personal_requests[event.from_id].parity,
            edit_personal_requests[event.from_id].day,
            0
        )
        logger.info(edit_personal_requests[event.from_id])
        await event.answer(message='Выберите опцию - удалить аннотацию или перезаписать(записать).',
                           keyboard=edit_personal_kb.CHOOSE_MOVE_PERSONAL_KB.get_keyboard())

    else:
        edit_personal_requests[event.from_id] = EditPersonalRequest(
            event.from_id,
            edit_personal_requests[event.from_id].stream_group,
            edit_personal_requests[event.from_id].parity,
            edit_personal_requests[event.from_id].day,
            int(event.text.lower().split()[0])
        )
        logger.info(edit_personal_requests[event.from_id])
        await event.answer(message='Выберите действие с выбранной парой',
                           keyboard=edit_personal_kb.CHOOSE_MOVE_PERSONAL_KB.get_keyboard())


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("cmp_button"))
@database_handler()
async def choose_pair_number(event: SimpleBotEvent) -> str:
    constants.currently_editing[event.from_id] = True
    logger.info(edit_personal_requests[event.from_id])
    if event.text.lower() == 'удалить':
        if edit_personal_requests[event.from_id].pair_number != 0:
            response = await post_request(
                url=f'http://{RESTIP}:{RESTPORT}/remove-pair-personal/',
                data={
                    'stream_group': edit_personal_requests[event.from_id].stream_group,
                    'day': edit_personal_requests[event.from_id].day,
                    'parity': edit_personal_requests[event.from_id].parity,
                    'id': event.from_id,
                    'pair_number': edit_personal_requests[event.from_id].pair_number
                }
            )
            if json.loads(response)['ok'] != True:
                logger.error(
                    'Ошибка при запросе к rest сервису на удаление персональной пары.')
                await event.answer(message='Ошибка при удалении персональной пары. Информация об ошибке направлена разработчикам', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
            await event.answer(message='Пара успешно удалена',
                               keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
        else:
            response = await post_request(
                url=f'http://{RESTIP}:{RESTPORT}/remove-annotation-personal/',
                data={
                    'stream_group': edit_personal_requests[event.from_id].stream_group,
                    'day': edit_personal_requests[event.from_id].day,
                    'parity': edit_personal_requests[event.from_id].parity,
                    'id': event.from_id
                }
            )
            if json.loads(response)['ok'] != True:
                logger.error(
                    'Ошибка при запросе к rest сервису на удаление персональной аннотации.')
                await event.answer(message='Ошибка при удалении персональной аннотации. Информация об ошибке направлена разработчикам', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
            await event.answer(message='Аннотация успешно удалена',
                               keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
    else:
        await event.answer(message='Введите изменения')
