from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, PayloadContainsFilter
from transliterate import translit
import botrayado.schedule.sheethandler as sheethandler
from botrayado.utils import *
from botrayado.keyboards import *
from botrayado.database import *
from botrayado.utils.constants import RESTIP, RESTPORT
import json
import aiohttp

logger = get_logger(__name__)

headman_router = DefaultRouter()


async def post_request(url: str, data: dict) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, json=data) as response:
            return await response.text()


async def get_request(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            return await response.text()


@simple_bot_message_handler(headman_router, PayloadContainsFilter("cwb_button"))
@database_handler()
async def choose_week(event: SimpleBotEvent) -> str:
    # Задание недели
    constants.headman_requests[event.from_id] = constants.HeadmanRequest(
        week=(event.text).split()[0],
        group=constants.headmans_ids.get(event.from_id)
    )

    await event.answer(message='Выберите день недели', keyboard=edit_kb.CHOOSE_DAY_OF_WEEK_KB.get_keyboard())


@simple_bot_message_handler(headman_router, PayloadContainsFilter("cdowb_button"))
@database_handler()
async def choose_day_of_week(event: SimpleBotEvent) -> str:
    # Задание дня недели
    constants.headman_requests[event.from_id] = constants.HeadmanRequest(
        week=constants.headman_requests[event.from_id].week,
        dayofweek=translit(event.text, language_code='ru',
                           reversed=True).replace("'", "").lower(),
        group=constants.headmans_ids.get(event.from_id)
    )

    if constants.headman_requests[event.from_id].week.lower() == 'обе':
        schedule = await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                            constants.headman_requests[event.from_id].dayofweek.lower(
        ),
            True)
        schedule += await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                             constants.headman_requests[event.from_id].dayofweek.lower(
        ),
            False)
        await event.answer(message=f'Текущее расписание на выбранные дни: \n {schedule}', keyboard=edit_kb.CHOOSE_PAIR_KB.get_keyboard())
    else:
        even = True if constants.headman_requests[event.from_id].week.lower(
        ) == 'четная' else False
        schedule = await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                            constants.headman_requests[event.from_id].dayofweek.lower(
        ),
            even)
        await event.answer(message=f'Текущее расписание на выбранный день: \n {schedule}', keyboard=edit_kb.CHOOSE_PAIR_KB.get_keyboard())

    await event.answer(message='Выберите пару для редактирования либо 6-ую кнопку для добавления общей аннотации ко дню', keyboard=edit_kb.CHOOSE_PAIR_KB.get_keyboard())


@simple_bot_message_handler(headman_router, PayloadFilter({'cpb_button': 'resetall'}))
@database_handler()
async def resetday(event: SimpleBotEvent) -> str:
    # Сброс дня
    constants.headman_requests[event.from_id] = constants.HeadmanRequest(
        week=constants.headman_requests[event.from_id].week,
        dayofweek=constants.headman_requests[event.from_id].dayofweek,
        pair=-1,
        group=constants.headmans_ids.get(event.from_id)
    )

    even = True if constants.headman_requests[event.from_id].week.lower(
    ) == 'четная' else False
    response = json.loads(await get_request(
        f'http://{RESTIP}:{RESTPORT}/annotation/?group={constants.headman_requests[event.from_id].group}&day={constants.headman_requests[event.from_id].dayofweek}&even={even}'
    ))
    annotation = response['annotation']
    if annotation == 'No annotation found':
        await event.answer(message='Аннотации на текущий день нет')
    else:
        await event.answer(message=f'Предыдущая аннотация (до сброса): {annotation}')
        response = await post_request(
            url=f'http://{RESTIP}:{RESTPORT}/remove-annotation/',
            data={
                'week': constants.headman_requests[event.from_id].week,
                'dayofweek': constants.headman_requests[event.from_id].dayofweek,
                'group': constants.headman_requests[event.from_id].group,
            }
        )
    if constants.headman_requests[event.from_id].week.lower() == 'обе':
        schedule = await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                            constants.headman_requests[event.from_id].dayofweek.lower(
        ),
            True)
        schedule += await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                             constants.headman_requests[event.from_id].dayofweek.lower(
        ),
            False)
        await event.answer(message=f'Предыдущее расписание на выбранные дни (до сброса): \n {schedule}', keyboard=menu_kb.START_KB.get_keyboard())
        response = await post_request(
            url=f'http://{RESTIP}:{RESTPORT}/reset-schedule/',
            data={
                'week': "Нечетная",
                'dayofweek': constants.headman_requests[event.from_id].dayofweek,
                'group': constants.headman_requests[event.from_id].group,
            }
        )
        response = await post_request(
            url=f'http://{RESTIP}:{RESTPORT}/reset-schedule/',
            data={
                'week': "Четная",
                'dayofweek': constants.headman_requests[event.from_id].dayofweek,
                'group': constants.headman_requests[event.from_id].group,
            }
        )
        schedule = await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                            constants.headman_requests[event.from_id].dayofweek.lower(
        ),
            True)
        schedule += await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                             constants.headman_requests[event.from_id].dayofweek.lower(
        ),
            False)
        await event.answer(message=f'День успешно сброшен. Текущее расписание (после сброса): {schedule}', keyboard=menu_kb.START_KB.get_keyboard())
    else:
        even = True if constants.headman_requests[event.from_id].week.lower(
        ) == 'четная' else False
        schedule = await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                            constants.headman_requests[event.from_id].dayofweek.lower(
        ),
            even)
        await event.answer(message=f'Предыдущее расписание на выбранный день (до сброса): \n {schedule}', keyboard=menu_kb.START_KB.get_keyboard())
        response = await post_request(
            url=f'http://{RESTIP}:{RESTPORT}/reset-schedule/',
            data={
                'week': constants.headman_requests[event.from_id].week,
                'dayofweek': constants.headman_requests[event.from_id].dayofweek,
                'group': constants.headman_requests[event.from_id].group,
            }
        )
        schedule = await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                            constants.headman_requests[event.from_id].dayofweek.lower(
        ),
            even)
        await event.answer(message=f'День успешно сброшен. Текущее расписание (после сброса): {schedule}', keyboard=menu_kb.START_KB.get_keyboard())


@simple_bot_message_handler(headman_router, PayloadFilter({'cpb_button': 'forall'}))
@database_handler()
async def choose_pair_forall(event: SimpleBotEvent) -> str:
    # Задание аннотации для всего дня
    constants.headman_requests[event.from_id] = constants.HeadmanRequest(
        week=constants.headman_requests[event.from_id].week,
        dayofweek=constants.headman_requests[event.from_id].dayofweek,
        pair=0,
        group=constants.headmans_ids.get(event.from_id)
    )

    even = True if constants.headman_requests[event.from_id].week.lower(
    ) == 'четная' else False
    response = json.loads(await get_request(
        f'http://{RESTIP}:{RESTPORT}/annotation/?group={constants.headman_requests[event.from_id].group}&day={constants.headman_requests[event.from_id].dayofweek}&even={even}'
    ))
    annotation = response['annotation']
    if annotation == 'No annotation found':
        await event.answer(message='Аннотации на текущий день нет')
    else:
        await event.answer(message=f'Текущая аннотация: {annotation}')
    await event.answer(message='Выберите опцию - удалить аннотацию или перезаписать(записать).', keyboard=edit_kb.CHOOSE_MOVE_KB.get_keyboard())


@ simple_bot_message_handler(headman_router, PayloadContainsFilter("cpb_button"))
@ database_handler()
async def choose_pair(event: SimpleBotEvent) -> str:
    # Задание выбранной пары
    constants.headman_requests[event.from_id] = constants.HeadmanRequest(
        week=constants.headman_requests[event.from_id].week,
        dayofweek=constants.headman_requests[event.from_id].dayofweek,
        pair=int(event.text[0]),
        group=constants.headmans_ids.get(event.from_id)
    )

    if constants.headman_requests[event.from_id].week.lower() == 'обе':
        schedule = (await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                             constants.headman_requests[event.from_id].dayofweek.lower(
        ),
            True)).split('⸻⸻⸻⸻⸻\n')[constants.headman_requests[event.from_id].pair + 1]
        schedule += (await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                              constants.headman_requests[event.from_id].dayofweek.lower(
        ),
            False)).split('⸻⸻⸻⸻⸻\n')[constants.headman_requests[event.from_id].pair + 1]
        await event.answer(message=f'Выбранные пары: \n {schedule}', keyboard=edit_kb.CHOOSE_PAIR_KB.get_keyboard())
    else:
        even = True if constants.headman_requests[event.from_id].week.lower(
        ) == 'четная' else False
        schedule = (await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                             constants.headman_requests[event.from_id].dayofweek.lower(
        ),
            even)).split('⸻⸻⸻⸻⸻\n')[constants.headman_requests[event.from_id].pair + 1]
        await event.answer(message=f'Выбранная пара: \n {schedule}', keyboard=edit_kb.CHOOSE_PAIR_KB.get_keyboard())

    await event.answer(message='Выберите опцию - удалить пару или перезаписать.', keyboard=edit_kb.CHOOSE_MOVE_KB.get_keyboard())


@ simple_bot_message_handler(headman_router, PayloadContainsFilter("cmb_button"))
@ database_handler()
async def choose_move(event: SimpleBotEvent) -> str:
    # Задание действия удалить или перезаписать(записать)
    constants.headman_requests[event.from_id] = constants.HeadmanRequest(
        week=constants.headman_requests[event.from_id].week,
        dayofweek=constants.headman_requests[event.from_id].dayofweek,
        pair=constants.headman_requests[event.from_id].pair,
        move=event.text,
        group=constants.headmans_ids.get(event.from_id)
    )

    even = True if constants.headman_requests[event.from_id].week.lower(
    ) == 'четная' else False

    # Если пара = 0, значит аннотация на весь день
    if constants.headman_requests[event.from_id].pair != 0:
        if event.text.lower() == 'удалить':
            logger.info(constants.headman_requests[event.from_id])
            response = await post_request(
                url=f'http://{RESTIP}:{RESTPORT}/remove-pair/',
                data={
                    'week': constants.headman_requests[event.from_id].week,
                    'dayofweek': constants.headman_requests[event.from_id].dayofweek,
                    'group': constants.headman_requests[event.from_id].group,
                    'pair': constants.headman_requests[event.from_id].pair
                }
            )
            print(response)
            schedule = await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                                constants.headman_requests[event.from_id].dayofweek.lower(
            ),
                even)
            await event.answer(message='Пара успешно удалена', keyboard=menu_kb.START_KB.get_keyboard())
            await event.answer(message=f'Измененный день:\n {schedule}', keyboard=menu_kb.START_KB.get_keyboard())
        else:
            await event.answer(message='Введите изменения')
    else:
        if event.text.lower() == 'удалить':
            logger.info(constants.headman_requests[event.from_id])
            response = await post_request(
                url=f'http://{RESTIP}:{RESTPORT}/remove-annotation/',
                data={
                    'week': constants.headman_requests[event.from_id].week,
                    'dayofweek': constants.headman_requests[event.from_id].dayofweek,
                    'group': constants.headman_requests[event.from_id].group,
                }
            )
            await event.answer(message='Аннотация успешно удалена', keyboard=menu_kb.START_KB.get_keyboard())
            print(response)
        else:
            await event.answer(message='Введите изменения')
