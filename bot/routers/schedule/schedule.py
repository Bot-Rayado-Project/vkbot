from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, PayloadContainsFilter
from bot.utils import schedule_request as sr
from bot.utils import ScheduleRequest
from bot.logger import get_logger
from bot.keyboards import *

logger = get_logger(__name__)

schedule_router = DefaultRouter()


@simple_bot_message_handler(schedule_router, PayloadFilter({"menu_button": "schedule"}))
async def schedule(event: SimpleBotEvent) -> None:
    sr.user_schedule_requests[event.from_id] = ScheduleRequest()
    await event.answer(message='Выберите день недели, либо редактор расписания', keyboard=SCHEDULE_DAY_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("schedule_day_button"))
async def schedule_day(event: SimpleBotEvent) -> None:
    if sr.user_schedule_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        sr.user_schedule_requests[event.from_id] = ScheduleRequest(event.text)
        if event.payload["schedule_day_button"] == "today" or event.payload["schedule_day_button"] == "tomorrow":
            await event.answer(message='Выберите факультет', keyboard=SCHEDULE_FACULTY_KB.get_keyboard())
        else:
            await event.answer(message='Выберите четность недели', keyboard=SCHEDULE_PARITY_KB.get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {sr.user_schedule_requests[event.from_id]}')


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("schedule_parity_button"))
async def schedule_parity(event: SimpleBotEvent) -> None:
    if sr.user_schedule_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["schedule_parity_button"] == 'back':
            sr.user_schedule_requests[event.from_id] = ScheduleRequest()
            await event.answer(message='Выберите день недели, либо редактор расписания', keyboard=SCHEDULE_DAY_KB.get_keyboard())
        else:
            sr.user_schedule_requests[event.from_id] = ScheduleRequest(
                sr.user_schedule_requests[event.from_id].day, event.text
            )
            await event.answer(message='Выберите факультет', keyboard=SCHEDULE_FACULTY_KB.get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {sr.user_schedule_requests[event.from_id]}')


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("schedule_faculty_button"))
async def schedule_faculty(event: SimpleBotEvent) -> None:
    if sr.user_schedule_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["schedule_faculty_button"] == 'back':
            if sr.user_schedule_requests[event.from_id].day.lower() == 'вся неделя':
                sr.user_schedule_requests[event.from_id] = ScheduleRequest(
                    sr.user_schedule_requests[event.from_id].day
                )
                await event.answer(message='Выберите четность недели', keyboard=SCHEDULE_PARITY_KB.get_keyboard())
            else:
                sr.user_schedule_requests[event.from_id] = ScheduleRequest()
                await event.answer(message='Выберите день недели, либо редактор расписания', keyboard=SCHEDULE_DAY_KB.get_keyboard())
        else:
            sr.user_schedule_requests[event.from_id] = ScheduleRequest(
                sr.user_schedule_requests[event.from_id].day,
                None,
                event.payload["schedule_faculty_button"]
            )
            await event.answer(message='Выберите поток', keyboard=SCHEDULE_FACULTY_MATCHING[event.payload["schedule_faculty_button"]].get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {sr.user_schedule_requests[event.from_id]}')


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("schedule_stream_button"))
async def schedule_stream(event: SimpleBotEvent) -> None:
    if sr.user_schedule_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["schedule_stream_button"] == 'back':
            if sr.user_schedule_requests[event.from_id].day is None or sr.user_schedule_requests[event.from_id].faculty is None:
                await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Отсуствует day или faculty в запросе. Откат в меню')
            elif sr.user_schedule_requests[event.from_id].day.lower() == 'вся неделя':
                if sr.user_schedule_requests[event.from_id].parity.lower() == None:
                    await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                    Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                    logger.info(
                        f'{event.from_id}: {event.text} - Отсуствует parity в запросе всей недели. Откат в меню')
                else:
                    sr.user_schedule_requests[event.from_id] = ScheduleRequest(
                        sr.user_schedule_requests[event.from_id].day,
                        sr.user_schedule_requests[event.from_id].parity
                    )
                    await event.answer(message='Выберите факультет', keyboard=SCHEDULE_FACULTY_KB.get_keyboard())
            else:
                sr.user_schedule_requests[event.from_id] = ScheduleRequest(
                    sr.user_schedule_requests[event.from_id].day
                )
                await event.answer(message='Выберите факультет', keyboard=SCHEDULE_FACULTY_KB.get_keyboard())
        else:
            await event.answer(message='Выберите группу', keyboard=SCHEDULE_STREAM_MATCHING[event.payload["schedule_stream_button"]].get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {sr.user_schedule_requests[event.from_id]}')


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("schedule_group_button"))
async def schedule_group(event: SimpleBotEvent) -> None:
    if sr.user_schedule_requests.get(event.from_id) == None:
        await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
        Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - Ошибка в отображении новой клавиатуры. Перемещение в меню')
    else:
        if event.payload["schedule_group_button"] == 'back':
            if sr.user_schedule_requests[event.from_id].day is None or sr.user_schedule_requests[event.from_id].faculty is None:
                await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                logger.info(
                    f'{event.from_id}: {event.text} - Отсуствует day или faculty в запросе. Откат в меню')
            elif sr.user_schedule_requests[event.from_id].day.lower() == 'вся неделя':
                if sr.user_schedule_requests[event.from_id].parity.lower() == None:
                    await event.answer(message='Запрашиваемая вами клавиатура изменилась в связи с обновлением. \
                    Во избежание ошибок повторите свой запрос', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                    logger.info(
                        f'{event.from_id}: {event.text} - Отсуствует parity в запросе всей недели. Откат в меню')
                else:
                    sr.user_schedule_requests[event.from_id] = ScheduleRequest(
                        sr.user_schedule_requests[event.from_id].day,
                        sr.user_schedule_requests[event.from_id].parity,
                        sr.user_schedule_requests[event.from_id].faculty
                    )
                    await event.answer(message='Выберите поток', keyboard=SCHEDULE_FACULTY_MATCHING[sr.user_schedule_requests[event.from_id].faculty].get_keyboard())
            else:
                sr.user_schedule_requests[event.from_id] = ScheduleRequest(
                    sr.user_schedule_requests[event.from_id].day,
                    None,
                    sr.user_schedule_requests[event.from_id].faculty
                )
                await event.answer(message='Выберите поток', keyboard=SCHEDULE_FACULTY_MATCHING[sr.user_schedule_requests[event.from_id].faculty].get_keyboard())
        else:
            sr.user_schedule_requests[event.from_id] = ScheduleRequest(
                sr.user_schedule_requests[event.from_id].day,
                sr.user_schedule_requests[event.from_id].parity,
                sr.user_schedule_requests[event.from_id].faculty,
                event.text
            )
            await event.answer(message='Расписание: ', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
        logger.info(
            f'{event.from_id}: {event.text} - {sr.user_schedule_requests[event.from_id]}')
