from typing import NamedTuple
import aiohttp
import json
from transliterate import translit
from botrayado.utils.constants import RESTIP, RESTPORT
import botrayado.utils.constants as constants
from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, PayloadContainsFilter
from botrayado.utils import *
from botrayado.keyboards import *
from botrayado.database import *
from botrayado.schedule.sheethandler import *

logger = get_logger(__name__)

edit_headman_router = DefaultRouter()


async def post_request(url: str, data: dict) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, json=data) as response:
            return await response.text()


async def get_request(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            return await response.text()

edit_headman_requests: dict = {}


class EditHeadmanRequest(NamedTuple):
    stream_group: str
    parity: str = None
    day: str = None
    pair_number: int = None
    changes: int = None
    annotation: str = None


@simple_bot_message_handler(edit_headman_router, PayloadContainsFilter("cwh_button"))
@database_handler()
async def choose_week(event: SimpleBotEvent) -> str:
    constants.currently_editing[event.from_id] = False
    edit_headman_requests[event.from_id] = EditHeadmanRequest(
        edit_headman_requests[event.from_id].stream_group,
        event.text.lower().split()[0]
    )
    await event.answer(message='Выберите день недели',
                       keyboard=edit_headman_kb.CHOOSE_DAY_OF_WEEK_HEADMAN_KB.get_keyboard())


@simple_bot_message_handler(edit_headman_router, PayloadContainsFilter("cdowh_button"))
@database_handler()
async def choose_day_of_week(event: SimpleBotEvent) -> str:
    constants.currently_editing[event.from_id] = False
    edit_headman_requests[event.from_id] = EditHeadmanRequest(
        edit_headman_requests[event.from_id].stream_group,
        edit_headman_requests[event.from_id].parity,
        event.text.lower()
    )
    current_schedule = await print_schedule_custom_headman(event.from_id, edit_headman_requests[event.from_id].stream_group, edit_headman_requests[event.from_id].day, edit_headman_requests[event.from_id].parity)
    await event.answer(message=current_schedule)
    logger.info(edit_headman_requests[event.from_id])
    await event.answer(message='Выберите пару, либо воспользуйтесь кнопкой "Сбросить все изменения" для сброса всех изменений',
                       keyboard=edit_headman_kb.CHOOSE_PAIR_HEADMAN_KB.get_keyboard())


@simple_bot_message_handler(edit_headman_router, PayloadContainsFilter("cph_button"))
@database_handler()
async def choose_pair_number(event: SimpleBotEvent) -> str:
    constants.currently_editing[event.from_id] = False
    if event.text.lower() == 'сбросить все изменения':
        response = await post_request(
            url=f'http://{RESTIP}:{RESTPORT}/reset-schedule-headman/',
            data={
                'stream_group': edit_headman_requests[event.from_id].stream_group,
                'day': edit_headman_requests[event.from_id].day,
                'parity': edit_headman_requests[event.from_id].parity
            }
        )
        if json.loads(response)['ok'] != True:
            logger.error(
                'Ошибка при запросе к rest сервису на сброс всего дня староста.')
            await event.answer(message='Ошибка при сбросе дня старосты. Информация об ошибке направлена разработчикам', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
        edit_headman_requests[event.from_id] = EditHeadmanRequest(
            event.from_id
        )
        await event.answer(message='День успешно сброшен.', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())

    elif event.text.lower() == 'общ. аннотация':
        edit_headman_requests[event.from_id] = EditHeadmanRequest(
            edit_headman_requests[event.from_id].stream_group,
            edit_headman_requests[event.from_id].parity,
            edit_headman_requests[event.from_id].day,
            0
        )
        logger.info(edit_headman_requests[event.from_id])
        await event.answer(message='Выберите опцию - удалить аннотацию или перезаписать(записать).',
                           keyboard=edit_headman_kb.CHOOSE_MOVE_HEADMAN_KB.get_keyboard())

    else:
        edit_headman_requests[event.from_id] = EditHeadmanRequest(
            edit_headman_requests[event.from_id].stream_group,
            edit_headman_requests[event.from_id].parity,
            edit_headman_requests[event.from_id].day,
            int(event.text.lower().split()[0])
        )
        logger.info(edit_headman_requests[event.from_id])
        await event.answer(message='Выберите действие с выбранной парой',
                           keyboard=edit_headman_kb.CHOOSE_MOVE_HEADMAN_KB.get_keyboard())


@simple_bot_message_handler(edit_headman_router, PayloadContainsFilter("cmh_button"))
@database_handler()
async def choose_pair_number(event: SimpleBotEvent) -> str:
    constants.currently_editing[event.from_id] = False
    logger.info(edit_headman_requests[event.from_id])
    if event.text.lower() == 'удалить':
        if edit_headman_requests[event.from_id].pair_number != 0:
            response = await post_request(
                url=f'http://{RESTIP}:{RESTPORT}/remove-pair-headman/',
                data={
                    'stream_group': edit_headman_requests[event.from_id].stream_group,
                    'day': edit_headman_requests[event.from_id].day,
                    'parity': edit_headman_requests[event.from_id].parity,
                    'pair_number': edit_headman_requests[event.from_id].pair_number
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
                url=f'http://{RESTIP}:{RESTPORT}/remove-annotation-headman/',
                data={
                    'stream_group': edit_headman_requests[event.from_id].stream_group,
                    'day': edit_headman_requests[event.from_id].day,
                    'parity': edit_headman_requests[event.from_id].parity
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
