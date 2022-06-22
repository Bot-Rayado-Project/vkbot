from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter
from bot.db import db_get_access_to_headman_edit, db_get_headman_group
from bot.logger import get_logger
from bot.keyboards import *
from bot.utils import headman_request as hr
from bot.utils import EditHeadmanRequest

logger = get_logger(__name__)

edit_router = DefaultRouter()


@simple_bot_message_handler(edit_router, PayloadFilter({"schedule_button": "edit"}))
async def edit_schedule(event: SimpleBotEvent) -> None:
    '''Обработчик кнопки "Редактировать расписание"'''
    await event.answer(message='Выберите опцию для редактирования расписания.\n\n Если у вас возникли какие-либо вопросы, воспользуйтесь \
кнопкой "Помощь" в главном меню.', keyboard=EDIT_SCHEDULE_KB.get_keyboard())


@simple_bot_message_handler(edit_router, PayloadFilter({"edit_schedule_button": "back"}))
async def edit_schedule_back(event: SimpleBotEvent) -> None:
    '''Обработчик кнопки "Назад" в поле видимости текущего ViewPort'а'''
    await event.answer(message='Выберите день недели, либо редактор расписания', keyboard=SCHEDULE_DAY_KB.get_keyboard())


@simple_bot_message_handler(edit_router, PayloadFilter({"edit_schedule_button": "headman"}))
async def edit_schedule_headman(event: SimpleBotEvent) -> None:
    '''Проверяет, является ли человек старостой или нет. В случае успеха отправляет в редактор edit_headman.py'''
    rights = await db_get_access_to_headman_edit(event.from_id)
    logger.info(rights)
    if rights == True:
        stream_group = await db_get_headman_group(event.from_id)
        hr.edit_headman_requests[event.from_id] = EditHeadmanRequest(
            stream_group
        )
        await event.answer(message='Доступ разрешен. Выберите неделю', keyboard=EDIT_SCHEDULE_HEADMAN_PARITY_KB.get_keyboard())
    else:
        await event.answer(message='Вас нет в списке старост какой-либо из групп. Если вы являетесь старостой или доверенным лицом для своей группы, \
напишите об этом @lamabot2000 либо @crymother и вам предоставят доступ к панели. \n\n Если вы хотите изменить расписание только для себя, а не для всей группы, \
вы можете воспользоваться кнопкой "Для себя", где внесенные изменения будут видны только вам.', keyboard=EDIT_SCHEDULE_KB.get_keyboard())


@simple_bot_message_handler(edit_router, PayloadFilter({"edit_schedule_button": "personal"}))
async def edit_schedule_personal(event: SimpleBotEvent) -> None:
    '''Отправляет в персональный редактор edit_personal.py'''
    await event.answer(message='Вы выбрали редактирование расписания для себя. Все вносимые изменения будете видеть только вы.\n\n Для получения помощи \
по использовании редактора, воспользуйтесь кнопкой "Помощь" в главном меню. Если вы являетесь старостой или доверенным лицом для своей группы, \
вы можете воспользоваться кнопкой "Для группы".', keyboard=EDIT_SCHEDULE_PERSONAL_FACULTY_KB.get_keyboard())
