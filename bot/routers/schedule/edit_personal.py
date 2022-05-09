import json
from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadContainsFilter
from bot.logger import get_logger
from bot.utils import personal_request as pr
from bot.utils import EditPersonalRequest
from bot.utils import post_request
from bot.keyboards import *
from bot.constants import RESTIP, RESTPORT

logger = get_logger(__name__)

edit_personal_router = DefaultRouter()


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("edit_schedule_personal_faculty_button"))
async def edit_schedule_faculty(event: SimpleBotEvent) -> None:
    if pr.edit_personal_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["edit_schedule_personal_faculty_button"] == 'back':
            await event.answer(message='Выберите опцию для редактирования расписания.\n\n Если у вас возникли какие-либо вопросы, воспользуйтесь \
        кнопкой "Помощь" в главном меню.', keyboard=EDIT_SCHEDULE_KB.get_keyboard())
            pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                event.from_id
            )
        else:
            pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                event.from_id,
                event.payload["edit_schedule_personal_faculty_button"].lower()
            )
            await event.answer(message='Выберите поток', keyboard=EDIT_SCHEDULE_PERSONAL_FACULTY_MATCHING[event.payload["edit_schedule_personal_faculty_button"]].get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {pr.edit_personal_requests[event.from_id]}')


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("edit_schedule_personal_stream_button"))
async def edit_schedule_stream(event: SimpleBotEvent) -> None:
    if pr.edit_personal_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["edit_schedule_personal_stream_button"] == 'back':
            await event.answer(message='Выберите факультет', keyboard=EDIT_SCHEDULE_KB.get_keyboard())
            pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                event.from_id
            )
        else:
            pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                event.from_id,
                pr.edit_personal_requests[event.from_id].faculty,
                event.payload["edit_schedule_personal_stream_button"].lower()
            )
            await event.answer(message='Выберите группу', keyboard=EDIT_SCHEDULE_PERSONAL_STREAM_MATCHING[event.payload["edit_schedule_personal_stream_button"]].get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {pr.edit_personal_requests[event.from_id]}')


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("edit_schedule_personal_group_button"))
async def edit_schedule_group(event: SimpleBotEvent) -> None:
    if pr.edit_personal_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["edit_schedule_personal_group_button"] == 'back':
            pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                event.from_id,
                pr.edit_personal_requests[event.from_id].faculty
            )
            await event.answer(message='Выберите поток', keyboard=EDIT_SCHEDULE_PERSONAL_FACULTY_MATCHING[pr.edit_personal_requests[event.from_id].faculty].get_keyboard())
        else:
            if pr.edit_personal_requests[event.from_id].faculty is None:
                pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                    event.from_id
                )
                await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Отсуствует faculty в персональном редакторе. Откат в меню')
            else:
                pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                    event.from_id,
                    pr.edit_personal_requests[event.from_id].faculty,
                    pr.edit_personal_requests[event.from_id].stream,
                    event.text.lower()
                )
                await event.answer(message='Выберите четность недели', keyboard=EDIT_SCHEDULE_PERSONAL_PARITY_KB.get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {pr.edit_personal_requests[event.from_id]}')


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("edit_schedule_personal_parity_button"))
async def edit_schedule_parity(event: SimpleBotEvent) -> None:
    if pr.edit_personal_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["edit_schedule_personal_parity_button"] == 'back':
            pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                event.from_id,
                pr.edit_personal_requests[event.from_id].faculty,
                pr.edit_personal_requests[event.from_id].stream
            )
            await event.answer(message='Выберите группу', keyboard=EDIT_SCHEDULE_PERSONAL_STREAM_MATCHING[pr.edit_personal_requests[event.from_id].stream].get_keyboard())
        else:
            if pr.edit_personal_requests[event.from_id].faculty is None or pr.edit_personal_requests[event.from_id].stream is None:
                pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                    event.from_id
                )
                await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Отсуствует faculty или stream в персональном редакторе. Откат в меню')
            else:
                pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                    event.from_id,
                    pr.edit_personal_requests[event.from_id].faculty,
                    pr.edit_personal_requests[event.from_id].stream,
                    pr.edit_personal_requests[event.from_id].stream_group,
                    event.text.split()[0].lower()
                )
                await event.answer(message='Выберите день недели', keyboard=EDIT_SCHEDULE_PERSONAL_DAY_KB.get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {pr.edit_personal_requests[event.from_id]}')


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("edit_schedule_personal_day_button"))
async def edit_schedule_day(event: SimpleBotEvent) -> None:
    if pr.edit_personal_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["edit_schedule_personal_day_button"] == 'back':
            pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                event.from_id,
                pr.edit_personal_requests[event.from_id].faculty,
                pr.edit_personal_requests[event.from_id].stream,
                pr.edit_personal_requests[event.from_id].stream_group
            )
            await event.answer(message='Выберите четность недели', keyboard=EDIT_SCHEDULE_PERSONAL_PARITY_KB.get_keyboard())
        else:
            if pr.edit_personal_requests[event.from_id].faculty is None or pr.edit_personal_requests[event.from_id].stream is None or pr.edit_personal_requests[event.from_id].stream_group is None:
                pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                    event.from_id
                )
                await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Отсуствует faculty или stream или stream_group в персональном редакторе. Откат в меню')
            else:
                pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                    event.from_id,
                    pr.edit_personal_requests[event.from_id].faculty,
                    pr.edit_personal_requests[event.from_id].stream,
                    pr.edit_personal_requests[event.from_id].stream_group,
                    pr.edit_personal_requests[event.from_id].parity,
                    event.text.lower()
                )
                await event.answer(message='Выберите пару, либо воспользуйтесь кнопкой "Сбросить все изменения" для сброса всех изменений', keyboard=EDIT_SCHEDULE_PERSONAL_PAIR_KB.get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {pr.edit_personal_requests[event.from_id]}')


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("edit_schedule_personal_pair_button"))
async def edit_schedule_pair(event: SimpleBotEvent) -> None:
    if pr.edit_personal_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["edit_schedule_personal_pair_button"] == 'back':
            pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                event.from_id,
                pr.edit_personal_requests[event.from_id].faculty,
                pr.edit_personal_requests[event.from_id].stream,
                pr.edit_personal_requests[event.from_id].stream_group,
                pr.edit_personal_requests[event.from_id].parity
            )
            await event.answer(message='Выберите день недели', keyboard=EDIT_SCHEDULE_PERSONAL_DAY_KB.get_keyboard())
        else:
            if pr.edit_personal_requests[event.from_id].faculty is None or pr.edit_personal_requests[event.from_id].stream is None or pr.edit_personal_requests[event.from_id].stream_group is None or pr.edit_personal_requests[event.from_id].parity is None:
                pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                    event.from_id
                )
                await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Отсуствует faculty или stream или stream_group или parity в персональном редакторе. Откат в меню')
            else:
                if event.payload['edit_schedule_personal_pair_button'] == 'reset_day':
                    # Сброс дня и в меню
                    response = await post_request(
                        url=f'http://{RESTIP}:{RESTPORT}/reset-schedule-personal/',
                        data={
                            'stream_group': pr.edit_personal_requests[event.from_id].stream_group,
                            'day': pr.edit_personal_requests[event.from_id].day,
                            'parity': pr.edit_personal_requests[event.from_id].parity,
                            'id': event.from_id
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
                            'Ошибка при запросе к rest сервису на сброс всего дня.')
                        await event.answer(message='Ошибка при сбросе персонального дня. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                    else:
                        # current_schedule = await print_schedule(event.from_id, event.text.lower(), edit_personal_requests[event.from_id].stream_group)
                        # await event.answer(message=f'Новое выводимое расписание: \n\n {current_schedule}')
                        await event.answer(message='День успешно сброшен.', keyboard=SCHEDULE_DAY_KB.get_keyboard())
                        pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                            event.from_id
                        )
                elif event.payload['edit_schedule_personal_pair_button'] == 'whole_day':
                    pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                        event.from_id,
                        pr.edit_personal_requests[event.from_id].faculty,
                        pr.edit_personal_requests[event.from_id].stream,
                        pr.edit_personal_requests[event.from_id].stream_group,
                        pr.edit_personal_requests[event.from_id].parity,
                        pr.edit_personal_requests[event.from_id].day,
                        0
                    )
                    await event.answer(message='Выберите действие с аннотацией на весь день', keyboard=EDIT_SCHEDULE_PERSONAL_MOVE_KB.get_keyboard())
                else:
                    pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                        event.from_id,
                        pr.edit_personal_requests[event.from_id].faculty,
                        pr.edit_personal_requests[event.from_id].stream,
                        pr.edit_personal_requests[event.from_id].stream_group,
                        pr.edit_personal_requests[event.from_id].parity,
                        pr.edit_personal_requests[event.from_id].day,
                        int(event.text[0])
                    )
                    await event.answer(message='Выберите действие с выбранной парой', keyboard=EDIT_SCHEDULE_PERSONAL_MOVE_KB.get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {pr.edit_personal_requests[event.from_id]}')


@simple_bot_message_handler(edit_personal_router, PayloadContainsFilter("edit_schedule_personal_move_button"))
async def edit_schedule_move(event: SimpleBotEvent) -> None:
    if pr.edit_personal_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["edit_schedule_personal_move_button"] == 'back':
            pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                event.from_id,
                pr.edit_personal_requests[event.from_id].faculty,
                pr.edit_personal_requests[event.from_id].stream,
                pr.edit_personal_requests[event.from_id].stream_group,
                pr.edit_personal_requests[event.from_id].parity,
                pr.edit_personal_requests[event.from_id].day
            )
            await event.answer(message='Выберите пару, либо воспользуйтесь кнопкой "Сбросить все изменения" для сброса всех изменений', keyboard=EDIT_SCHEDULE_PERSONAL_PAIR_KB.get_keyboard())
        else:
            if pr.edit_personal_requests[event.from_id].faculty is None or pr.edit_personal_requests[event.from_id].stream is None or pr.edit_personal_requests[event.from_id].stream_group is None or pr.edit_personal_requests[event.from_id].parity is None or pr.edit_personal_requests[event.from_id].pair_number is None:
                pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                    event.from_id
                )
                await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Отсуствует faculty или stream или stream_group или parity или pair_number в персональном редакторе. Откат в меню')
            else:
                if event.payload['edit_schedule_personal_move_button'] == 'delete':
                    # Удалить пару и в меню
                    if pr.edit_personal_requests[event.from_id].pair_number != 0:
                        response = await post_request(
                            url=f'http://{RESTIP}:{RESTPORT}/remove-pair-personal/',
                            data={
                                'stream_group': pr.edit_personal_requests[event.from_id].stream_group,
                                'day': pr.edit_personal_requests[event.from_id].day,
                                'parity': pr.edit_personal_requests[event.from_id].parity,
                                'id': event.from_id,
                                'pair_number': pr.edit_personal_requests[event.from_id].pair_number
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
                            url=f'http://{RESTIP}:{RESTPORT}/remove-annotation-personal/',
                            data={
                                'stream_group': pr.edit_personal_requests[event.from_id].stream_group,
                                'day': pr.edit_personal_requests[event.from_id].day,
                                'parity': pr.edit_personal_requests[event.from_id].parity,
                                'id': event.from_id
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
                    pr.edit_personal_requests[event.from_id] = EditPersonalRequest(
                        event.from_id,
                        pr.edit_personal_requests[event.from_id].faculty,
                        pr.edit_personal_requests[event.from_id].stream,
                        pr.edit_personal_requests[event.from_id].stream_group,
                        pr.edit_personal_requests[event.from_id].parity,
                        pr.edit_personal_requests[event.from_id].day,
                        pr.edit_personal_requests[event.from_id].pair_number,
                        writing_changes_or_annotation=True
                    )
                    if pr.edit_personal_requests[event.from_id].pair_number == 0:
                        await event.answer(message='Введите новую аннотацию')
                    else:
                        await event.answer(message='Введите изменения (время пары ставится автоматически)')
        logger.info(
            f'{event.from_id}: {event.text} - {pr.edit_personal_requests[event.from_id]}')
