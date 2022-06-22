import json
from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadContainsFilter
from bot.logger import get_logger
from bot.utils import headman_request as hr
from bot.utils import EditHeadmanRequest
from bot.utils import post_request
from bot.keyboards import *
from bot.constants import RESTIP, RESTPORT
from bot.schedule import get_schedule_custom_headman

logger = get_logger(__name__)

edit_headman_router = DefaultRouter()

'''
*
Отвечает за редактор расписания для старост. Возможно попасть только из вне, только имея права старосты.
Эмулирует процесс выбора пары и ее редактирование/удаление + взаимодействие с аннотациями
ко всему дню недели.
*
'''


@simple_bot_message_handler(edit_headman_router, PayloadContainsFilter("edit_schedule_headman_parity_button"))
async def edit_schedule_parity(event: SimpleBotEvent) -> None:
    if hr.edit_headman_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["edit_schedule_headman_parity_button"] == 'back':
            hr.edit_headman_requests[event.from_id] = EditHeadmanRequest()
            await event.answer(message='Выберите опцию для редактирования расписания.\n\n Если у вас возникли какие-либо вопросы, воспользуйтесь \
кнопкой "Помощь" в главном меню.', keyboard=EDIT_SCHEDULE_KB.get_keyboard())
        else:
            if hr.edit_headman_requests[event.from_id].stream_group is None:
                hr.edit_headman_requests[event.from_id] = EditHeadmanRequest()
                await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
            else:
                hr.edit_headman_requests[event.from_id] = EditHeadmanRequest(
                    hr.edit_headman_requests[event.from_id].stream_group,
                    event.text.split()[0].lower()
                )
                await event.answer(message='Выберите день недели', keyboard=EDIT_SCHEDULE_HEADMAN_DAY_KB.get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {hr.edit_headman_requests[event.from_id]}')


@simple_bot_message_handler(edit_headman_router, PayloadContainsFilter("edit_schedule_headman_day_button"))
async def edit_schedule_day(event: SimpleBotEvent) -> None:
    if hr.edit_headman_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["edit_schedule_headman_day_button"] == 'back':
            hr.edit_headman_requests[event.from_id] = EditHeadmanRequest(
                hr.edit_headman_requests[event.from_id].stream_group
            )
            await event.answer(message='Выберите четность недели', keyboard=EDIT_SCHEDULE_HEADMAN_PARITY_KB.get_keyboard())
        else:
            if hr.edit_headman_requests[event.from_id].stream_group is None:
                hr.edit_headman_requests[event.from_id] = EditHeadmanRequest()
                await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
            else:
                hr.edit_headman_requests[event.from_id] = EditHeadmanRequest(
                    hr.edit_headman_requests[event.from_id].stream_group,
                    hr.edit_headman_requests[event.from_id].parity,
                    event.text.lower()
                )
                current_schedule = await get_schedule_custom_headman(
                    event.from_id,
                    hr.edit_headman_requests[event.from_id].stream_group,
                    hr.edit_headman_requests[event.from_id].day,
                    hr.edit_headman_requests[event.from_id].parity)
                await event.answer(message=f'Текущее расписание: \n\n {current_schedule}')
                await event.answer(message='Выберите пару, либо воспользуйтесь кнопкой "Сбросить все изменения" для сброса всех изменений', keyboard=EDIT_SCHEDULE_HEADMAN_PAIR_KB.get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {hr.edit_headman_requests[event.from_id]}')


@simple_bot_message_handler(edit_headman_router, PayloadContainsFilter("edit_schedule_headman_pair_button"))
async def edit_schedule_pair(event: SimpleBotEvent) -> None:
    if hr.edit_headman_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["edit_schedule_headman_pair_button"] == 'back':
            hr.edit_headman_requests[event.from_id] = EditHeadmanRequest(
                hr.edit_headman_requests[event.from_id].stream_group,
                hr.edit_headman_requests[event.from_id].parity
            )
            await event.answer(message='Выберите день недели', keyboard=EDIT_SCHEDULE_HEADMAN_DAY_KB.get_keyboard())
        else:
            if hr.edit_headman_requests[event.from_id].stream_group is None or hr.edit_headman_requests[event.from_id].parity is None:
                hr.edit_headman_requests[event.from_id] = EditHeadmanRequest()
                await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
            else:
                if event.payload['edit_schedule_headman_pair_button'] == 'reset_day':
                    # Сброс дня и в меню
                    response = await post_request(
                        url=f'http://{RESTIP}:{RESTPORT}/reset-schedule-headman/',
                        data={
                            'stream_group': hr.edit_headman_requests[event.from_id].stream_group,
                            'day': hr.edit_headman_requests[event.from_id].day,
                            'parity': hr.edit_headman_requests[event.from_id].parity
                        }
                    )
                    logger.info(response)
                    try:
                        json.loads(response)['ok']
                    except Exception:
                        logger.error(
                            'Ошибка при запросе к rest сервису на сброс всего дня.')
                        await event.answer(message='Ошибка при сбросе дня. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                    if json.loads(response)['ok'] != True:
                        logger.error(
                            'Ошибка при запросе к rest сервису на сброс всего дня.')
                        await event.answer(message='Ошибка при сбросе дня. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                    else:
                        current_schedule = await get_schedule_custom_headman(
                            event.from_id,
                            hr.edit_headman_requests[event.from_id].stream_group,
                            hr.edit_headman_requests[event.from_id].day,
                            hr.edit_headman_requests[event.from_id].parity)
                        await event.answer(message=f'Новое выводимое расписание: \n\n {current_schedule}')
                        await event.answer(message='День успешно сброшен.', keyboard=SCHEDULE_DAY_KB.get_keyboard())
                        hr.edit_headman_requests[event.from_id] = EditHeadmanRequest(
                        )
                elif event.payload['edit_schedule_headman_pair_button'] == 'whole_day':
                    hr.edit_headman_requests[event.from_id] = EditHeadmanRequest(
                        hr.edit_headman_requests[event.from_id].stream_group,
                        hr.edit_headman_requests[event.from_id].parity,
                        hr.edit_headman_requests[event.from_id].day,
                        0
                    )
                    await event.answer(message='Выберите действие с аннотацией на весь день', keyboard=EDIT_SCHEDULE_HEADMAN_MOVE_KB.get_keyboard())
                else:
                    hr.edit_headman_requests[event.from_id] = EditHeadmanRequest(
                        hr.edit_headman_requests[event.from_id].stream_group,
                        hr.edit_headman_requests[event.from_id].parity,
                        hr.edit_headman_requests[event.from_id].day,
                        int(event.text[0])
                    )
                    await event.answer(message='Выберите действие с выбранной парой', keyboard=EDIT_SCHEDULE_HEADMAN_MOVE_KB.get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {hr.edit_headman_requests[event.from_id]}')


@simple_bot_message_handler(edit_headman_router, PayloadContainsFilter("edit_schedule_headman_move_button"))
async def edit_schedule_move(event: SimpleBotEvent) -> None:
    if hr.edit_headman_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["edit_schedule_headman_move_button"] == 'back':
            hr.edit_headman_requests[event.from_id] = EditHeadmanRequest(
                hr.edit_headman_requests[event.from_id].stream_group,
                hr.edit_headman_requests[event.from_id].parity,
                hr.edit_headman_requests[event.from_id].day
            )
            await event.answer(message='Выберите пару, либо воспользуйтесь кнопкой "Сбросить все изменения" для сброса всех изменений', keyboard=EDIT_SCHEDULE_HEADMAN_PAIR_KB.get_keyboard())
        else:
            if hr.edit_headman_requests[event.from_id].stream_group is None or hr.edit_headman_requests[event.from_id].parity is None or hr.edit_headman_requests[event.from_id].pair_number is None:
                hr.edit_headman_requests[event.from_id] = EditHeadmanRequest()
                await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
            else:
                if event.payload['edit_schedule_headman_move_button'] == 'delete':
                    # Удалить пару и в меню
                    if hr.edit_headman_requests[event.from_id].pair_number != 0:
                        response = await post_request(
                            url=f'http://{RESTIP}:{RESTPORT}/remove-pair-headman/',
                            data={
                                'stream_group': hr.edit_headman_requests[event.from_id].stream_group,
                                'day': hr.edit_headman_requests[event.from_id].day,
                                'parity': hr.edit_headman_requests[event.from_id].parity,
                                'pair_number': hr.edit_headman_requests[event.from_id].pair_number
                            }
                        )
                        logger.info(response)
                        try:
                            json.loads(response)['ok']
                        except Exception:
                            logger.error(
                                'Ошибка при запросе к rest сервису на сброс всего дня.')
                            await event.answer(message='Ошибка при сбросе персонального дня. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                        if json.loads(response)['ok'] != True:
                            logger.error(
                                'Ошибка при запросе к rest сервису на удаление персональной пары.')
                            await event.answer(message='Ошибка при удалении персональной пары. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                        else:
                            await event.answer(message='Пара успешно удалена',
                                               keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                    else:
                        response = await post_request(
                            url=f'http://{RESTIP}:{RESTPORT}/remove-annotation-headman/',
                            data={
                                'stream_group': hr.edit_headman_requests[event.from_id].stream_group,
                                'day': hr.edit_headman_requests[event.from_id].day,
                                'parity': hr.edit_headman_requests[event.from_id].parity,
                            }
                        )
                        logger.info(response)
                        try:
                            json.loads(response)['ok']
                        except Exception:
                            logger.error(
                                'Ошибка при запросе к rest сервису на сброс всего дня.')
                            await event.answer(message='Ошибка при сбросе персонального дня. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                        if json.loads(response)['ok'] != True:
                            logger.error(
                                'Ошибка при запросе к rest сервису на удаление персональной аннотации.')
                            await event.answer(message='Ошибка при удалении персональной аннотации. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                        else:
                            await event.answer(message='Аннотация успешно удалена',
                                               keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                else:
                    hr.edit_headman_requests[event.from_id] = EditHeadmanRequest(
                        hr.edit_headman_requests[event.from_id].stream_group,
                        hr.edit_headman_requests[event.from_id].parity,
                        hr.edit_headman_requests[event.from_id].day,
                        hr.edit_headman_requests[event.from_id].pair_number,
                        writing_changes_or_annotation=True
                    )
                    if hr.edit_headman_requests[event.from_id].pair_number == 0:
                        await event.answer(message='Введите новую аннотацию')
                    else:
                        await event.answer(message='Введите изменения (время пары ставится автоматически)')
        logger.info(
            f'{event.from_id}: {event.text} - {hr.edit_headman_requests[event.from_id]}')
