from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, PayloadContainsFilter
from bot.logger import get_logger
from bot.schedule import get_schedule_for_day, get_schedule_for_whole_week
from bot.db import db_set_blueprints_buttons
from bot.keyboards import *
from bot.utils import BlueprintsRequest
import bot.utils.blueprints_request as br

logger = get_logger(__name__)

blueprints_router = DefaultRouter()


@simple_bot_message_handler(blueprints_router, PayloadFilter({"menu_button": "config"}))
async def blueprints(event: SimpleBotEvent) -> None:
    await event.answer(message='Выберите шаблон или создайте новый.', keyboard=(await create_blueprints_kb(event.from_id)).get_keyboard())


@simple_bot_message_handler(blueprints_router, PayloadContainsFilter('blueprints_button_cell'))
async def blueprints_cells(event: SimpleBotEvent) -> None:
    cell = event.text.lower()
    if cell == 'пустая ячейка':
        await event.answer(message='Ячейка пуста. Создайте шаблон с помощью кнопки "Создать шаблон".', keyboard=(await create_blueprints_kb(event.from_id)).get_keyboard())
    else:
        button = cell.split()
        if 'сн' in button or 'тн' in button:
            # Вся неделя, группа, тип недели
            schedule = await get_schedule_for_whole_week(event.from_id,
                                                         'следующая неделя' if 'сн' in button else 'текущая неделя',
                                                         button[1].lower())
            await event.answer(message=schedule, keyboard=(await create_blueprints_kb(event.from_id)).get_keyboard())
        else:
            # Сегодня БВТ2103 etc.
            schedule = await get_schedule_for_day(event.from_id,
                                                  button[0],
                                                  button[1])
            await event.answer(message=schedule, keyboard=(await create_blueprints_kb(event.from_id)).get_keyboard())


@simple_bot_message_handler(blueprints_router, PayloadFilter({"blueprints_button": "create_blueprint"}))
async def blueprint_create(event: SimpleBotEvent) -> None:
    br.user_blueprints_requests[event.from_id] = BlueprintsRequest()
    await event.answer(message='Выберите ячейку для (пере-)записи', keyboard=(await create_blueprints_choose_cell_choose_cell_kb(event.from_id)).get_keyboard())


@simple_bot_message_handler(blueprints_router, PayloadContainsFilter('blueprints_choose_cell_button_cell'))
async def blueprint_choose_cells(event: SimpleBotEvent) -> None:
    if br.user_blueprints_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["blueprints_choose_cell_button_cell"] == 'back':
            br.user_blueprints_requests[event.from_id] = BlueprintsRequest()
            await event.answer(message='Выберите шаблон', keyboard=(await create_blueprints_kb(event.from_id)).get_keyboard())
        else:
            br.user_blueprints_requests[event.from_id] = BlueprintsRequest(
                cell=event.payload['blueprints_choose_cell_button_cell']
            )
            await event.answer(message='Выберите день недели', keyboard=CREATE_SCHEDULE_BLUEPRINT_DAY_KB.get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {br.user_blueprints_requests[event.from_id]}')


@simple_bot_message_handler(blueprints_router, PayloadContainsFilter("create_schedule_blueprint_day_button"))
async def blueprints_create_day(event: SimpleBotEvent) -> None:
    if br.user_blueprints_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["create_schedule_blueprint_day_button"] == 'back':
            br.user_blueprints_requests[event.from_id] = BlueprintsRequest()
            await event.answer(message='Выберите день недели', keyboard=(await create_blueprints_choose_cell_choose_cell_kb(event.from_id)).get_keyboard())
        else:
            br.user_blueprints_requests[event.from_id] = BlueprintsRequest(
                event.text,
                cell=br.user_blueprints_requests[event.from_id].cell
            )
            if event.payload["create_schedule_blueprint_day_button"] == "today" or event.payload["create_schedule_blueprint_day_button"] == "tomorrow":
                await event.answer(message='Выберите факультет', keyboard=CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB.get_keyboard())
            else:
                await event.answer(message='Выберите четность недели', keyboard=CREATE_SCHEDULE_BLUEPRINT_PARITY_KB.get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {br.user_blueprints_requests[event.from_id]}')


@ simple_bot_message_handler(blueprints_router, PayloadContainsFilter("create_schedule_blueprint_parity_button"))
async def blueprints_create_parity(event: SimpleBotEvent) -> None:
    if br.user_blueprints_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["create_schedule_blueprint_parity_button"] == 'back':
            br.user_blueprints_requests[event.from_id] = BlueprintsRequest(
                cell=br.user_blueprints_requests[event.from_id].cell
            )
            await event.answer(message='Выберите день недели', keyboard=CREATE_SCHEDULE_BLUEPRINT_DAY_KB.get_keyboard())
        else:
            br.user_blueprints_requests[event.from_id] = BlueprintsRequest(
                br.user_blueprints_requests[event.from_id].day,
                event.text,
                cell=br.user_blueprints_requests[event.from_id].cell
            )
            await event.answer(message='Выберите факультет', keyboard=CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB.get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {br.user_blueprints_requests[event.from_id]}')


@ simple_bot_message_handler(blueprints_router, PayloadContainsFilter("create_schedule_blueprint_faculty_button"))
async def blueprints_create_faculty(event: SimpleBotEvent) -> None:
    if br.user_blueprints_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["create_schedule_blueprint_faculty_button"] == 'back':
            if br.user_blueprints_requests[event.from_id].day.lower() == 'вся неделя':
                br.user_blueprints_requests[event.from_id] = BlueprintsRequest(
                    br.user_blueprints_requests[event.from_id].day,
                    cell=br.user_blueprints_requests[event.from_id].cell
                )
                await event.answer(message='Выберите четность недели', keyboard=CREATE_SCHEDULE_BLUEPRINT_PARITY_KB.get_keyboard())
            else:
                br.user_blueprints_requests[event.from_id] = BlueprintsRequest(
                    cell=br.user_blueprints_requests[event.from_id].cell
                )
                await event.answer(message='Выберите день ячейку', keyboard=CREATE_SCHEDULE_BLUEPRINT_DAY_KB.get_keyboard())
        else:
            br.user_blueprints_requests[event.from_id] = BlueprintsRequest(
                br.user_blueprints_requests[event.from_id].day,
                br.user_blueprints_requests[event.from_id].parity,
                event.payload["create_schedule_blueprint_faculty_button"],
                cell=br.user_blueprints_requests[event.from_id].cell
            )
            await event.answer(message='Выберите поток', keyboard=CREATE_SCHEDULE_BLUEPRINT_FACULTY_MATCHING[event.payload["create_schedule_blueprint_faculty_button"]].get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {br.user_blueprints_requests[event.from_id]}')


@simple_bot_message_handler(blueprints_router, PayloadContainsFilter("create_schedule_blueprint_stream_button"))
async def blueprints_create_stream(event: SimpleBotEvent) -> None:
    if br.user_blueprints_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["create_schedule_blueprint_stream_button"] == 'back':
            if br.user_blueprints_requests[event.from_id].day is None or br.user_blueprints_requests[event.from_id].faculty is None:
                await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Отсуствует day или faculty в запросе. Откат в меню')
            elif br.user_blueprints_requests[event.from_id].day.lower() == 'вся неделя':
                if br.user_blueprints_requests[event.from_id].parity is None:
                    await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                    Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                    logger.info(
                        f'{event.from_id}: {event.text} - Отсуствует parity в запросе всей недели. Откат в меню')
                else:
                    br.user_blueprints_requests[event.from_id] = BlueprintsRequest(
                        br.user_blueprints_requests[event.from_id].day,
                        br.user_blueprints_requests[event.from_id].parity,
                        cell=br.user_blueprints_requests[event.from_id].cell
                    )
                    await event.answer(message='Выберите факультет', keyboard=CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB.get_keyboard())
            else:
                br.user_blueprints_requests[event.from_id] = BlueprintsRequest(
                    br.user_blueprints_requests[event.from_id].day,
                    cell=br.user_blueprints_requests[event.from_id].cell
                )
                await event.answer(message='Выберите факультет', keyboard=CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB.get_keyboard())
        else:
            await event.answer(message='Выберите группу', keyboard=CREATE_SCHEDULE_BLUEPRINT_STREAM_MATCHING[event.payload["create_schedule_blueprint_stream_button"]].get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {br.user_blueprints_requests[event.from_id]}')


@simple_bot_message_handler(blueprints_router, PayloadContainsFilter("create_schedule_blueprint_group_button"))
async def schedule_group(event: SimpleBotEvent) -> None:
    if br.user_blueprints_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["create_schedule_blueprint_group_button"] == 'back':
            if br.user_blueprints_requests[event.from_id].day is None or br.user_blueprints_requests[event.from_id].faculty is None:
                await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Отсуствует day или faculty в запросе. Откат в меню')
            elif br.user_blueprints_requests[event.from_id].day.lower() == 'вся неделя':
                if br.user_blueprints_requests[event.from_id].parity is None:
                    await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                    Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                    logger.info(
                        f'{event.from_id}: {event.text} - Отсуствует parity в запросе всей недели. Откат в меню')
                else:
                    br.user_blueprints_requests[event.from_id] = BlueprintsRequest(
                        br.user_blueprints_requests[event.from_id].day,
                        br.user_blueprints_requests[event.from_id].parity,
                        br.user_blueprints_requests[event.from_id].faculty,
                        cell=br.user_blueprints_requests[event.from_id].cell
                    )
                    await event.answer(message='Выберите поток', keyboard=CREATE_SCHEDULE_BLUEPRINT_FACULTY_MATCHING[br.user_blueprints_requests[event.from_id].faculty].get_keyboard())
            else:
                br.user_blueprints_requests[event.from_id] = BlueprintsRequest(
                    br.user_blueprints_requests[event.from_id].day,
                    None,
                    br.user_blueprints_requests[event.from_id].faculty,
                    cell=br.user_blueprints_requests[event.from_id].cell
                )
                await event.answer(message='Выберите поток', keyboard=CREATE_SCHEDULE_BLUEPRINT_FACULTY_MATCHING[br.user_blueprints_requests[event.from_id].faculty].get_keyboard())
        else:
            br.user_blueprints_requests[event.from_id] = BlueprintsRequest(
                br.user_blueprints_requests[event.from_id].day,
                br.user_blueprints_requests[event.from_id].parity,
                br.user_blueprints_requests[event.from_id].faculty,
                event.text,
                cell=br.user_blueprints_requests[event.from_id].cell
            )
            if br.user_blueprints_requests[event.from_id].parity is not None:
                blueprint = br.user_blueprints_requests[event.from_id].parity[0] + 'Н '
            else:
                blueprint = br.user_blueprints_requests[event.from_id].day + ' '
            blueprint += event.text
            res = await db_set_blueprints_buttons(event.from_id, blueprint, br.user_blueprints_requests[event.from_id].cell)
            if res == None:
                await event.answer(message='Ошибка в задании запроса. Повторите попытку позже', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Ошибка подключения к бд при задании шаблона')
            elif res == False:
                await event.answer(message='Данный шаблон уже задан', keyboard=(await create_blueprints_kb(event.from_id)).get_keyboard())
            else:
                await event.answer(message=f'Задан шаблон {blueprint}', keyboard=(await create_blueprints_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {br.user_blueprints_requests[event.from_id]}')
