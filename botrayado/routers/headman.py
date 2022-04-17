import botrayado.utils.constants as constants
import botrayado.keyboards.headman_kb as headman_kb
import botrayado.keyboards.schedule_kb as schedule_kb
import botrayado.keyboards.menu_kb as menu_kb
import botrayado.schedule.sheethandler as sheethandler

from botrayado.database.db import database_handler

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, PayloadContainsFilter

from botrayado.utils.logger import get_logger

logger = get_logger(__name__)

headman_router = DefaultRouter()


@simple_bot_message_handler(headman_router, PayloadFilter({"dow_button_c": "edit"}))
@database_handler()
async def help(event: SimpleBotEvent) -> str:
    if constants.headmans_ids.get(event.from_id) is not None:
        await event.answer(message='Выберите неделю', keyboard=headman_kb.CHOOSE_WEEK_KB.get_keyboard())
    else:
        await event.answer(message='Доступа нет. До свидания', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())


@simple_bot_message_handler(headman_router, PayloadContainsFilter("cwb_button"))
@database_handler()
async def help(event: SimpleBotEvent) -> str:
    constants.headman_requests[event.from_id] = constants.HeadmanRequest(event.text)  # Неделя
    await event.answer(message='Выберите день недели', keyboard=headman_kb.CHOOSE_DAY_OF_WEEK_KB.get_keyboard())


@simple_bot_message_handler(headman_router, PayloadContainsFilter("cdowb_button"))
@database_handler()
async def help(event: SimpleBotEvent) -> str:
    constants.headman_requests[event.from_id] = constants.HeadmanRequest(constants.headman_requests[event.from_id].week, event.text)  # День недели
    if constants.headman_requests[event.from_id].week.lower() == 'обе':
        schedule = ''
        schedule += await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                             constants.headman_requests[event.from_id].dayofweek.lower(),
                                                             True)
        schedule += await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                             constants.headman_requests[event.from_id].dayofweek.lower(),
                                                             False)
        await event.answer(message=f'Текущее расписание на выбранные дни: \n {schedule}', keyboard=headman_kb.CHOOSE_PAIR_KB.get_keyboard())
    else:
        even = True if constants.headman_requests[event.from_id].week.lower() == 'четная' else False
        schedule = await sheethandler.print_schedule_custom(constants.headmans_ids[event.from_id].lower(),
                                                            constants.headman_requests[event.from_id].dayofweek.lower(),
                                                            even)
        await event.answer(message=f'Текущее расписание на выбранный день: \n {schedule}', keyboard=headman_kb.CHOOSE_PAIR_KB.get_keyboard())
    await event.answer(message='Выберите пару для редактирования либо 6-ую кнопку для добавления общей аннотации ко дню', keyboard=headman_kb.CHOOSE_PAIR_KB.get_keyboard())


@ simple_bot_message_handler(headman_router, PayloadContainsFilter("cpb_button"))
@ database_handler()
async def help(event: SimpleBotEvent) -> str:
    constants.headman_requests[event.from_id] = constants.HeadmanRequest(constants.headman_requests[event.from_id].week,
                                                                         constants.headman_requests[event.from_id].dayofweek,
                                                                         event.text)  # Пара
    await event.answer(message='Выберите опцию - удалить пару или перезаписать.', keyboard=headman_kb.CHOOSE_MOVE_KB.get_keyboard())


@ simple_bot_message_handler(headman_router, PayloadContainsFilter("cmb_button"))
@ database_handler()
async def help(event: SimpleBotEvent) -> str:
    constants.headman_requests[event.from_id] = constants.HeadmanRequest(constants.headman_requests[event.from_id].week,
                                                                         constants.headman_requests[event.from_id].dayofweek,
                                                                         constants.headman_requests[event.from_id].pair,
                                                                         event.text)  # Действие
    logger.info(constants.headman_requests[event.from_id])
    if event.text.lower() == 'удалить':
        await event.answer(message='Пара успешно удалена', keyboard=menu_kb.START_KB.get_keyboard())
    else:
        await event.answer(message='Введите изменения')


@ simple_bot_message_handler(headman_router, PayloadFilter({"dow_button_c": "look"}))
@ database_handler()
async def help(event: SimpleBotEvent) -> str:
    await event.answer(message='Look', keyboard=menu_kb.START_KB.get_keyboard())
