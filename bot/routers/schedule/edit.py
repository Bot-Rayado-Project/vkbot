from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter
from bot.db import db_get_access_to_headman_edit
from bot.logger import get_logger
from bot.keyboards import *

logger = get_logger(__name__)

edit_router = DefaultRouter()


@simple_bot_message_handler(edit_router, PayloadFilter({"schedule_button": "edit"}))
async def edit_schedule(event: SimpleBotEvent) -> None:
    await event.answer(message='Выберите опцию для редактирования расписания.\n\n Если у вас возникли какие-либо вопросы, воспользуйтесь \
кнопкой "Помощь" в главном меню.', keyboard=EDIT_SCHEDULE_KB.get_keyboard())


@simple_bot_message_handler(edit_router, PayloadFilter({"edit_schedule_button": "back"}))
async def edit_schedule_back(event: SimpleBotEvent) -> None:
    await event.answer(message='Выберите день недели, либо редактор расписания', keyboard=SCHEDULE_DAY_KB.get_keyboard())


@simple_bot_message_handler(edit_router, PayloadFilter({"edit_schedule_button": "headman"}))
async def edit_schedule_headman(event: SimpleBotEvent) -> None:
    rights = await db_get_access_to_headman_edit(event.from_id)
    logger.info(rights)
    if rights == True:
        await event.answer(message='Доступ разрешен. Выберите неделю')
    else:
        await event.answer(message='Вас нет в списке старост какой-либо из групп. Если вы являетесь старостой или доверенным лицом для своей группы, \
напишите об этом @lamabot2000 либо @crymother и вам предоставят доступ к панели. \n\n Если вы хотите изменить расписание только для себя, а не для всей группы, \
вы можете воспользоваться кнопкой "Для себя", где внесенные изменения будут видны только вам.', keyboard=EDIT_SCHEDULE_KB.get_keyboard())


@simple_bot_message_handler(edit_router, PayloadFilter({"edit_schedule_button": "personal"}))
async def edit_schedule_personal(event: SimpleBotEvent) -> None:
    await event.answer(message='Вы выбрали редактирование расписания для себя. Все вносимые изменения будете видеть только вы.\n\n Для получения помощи \
по использовании редактора, воспользуйтесь кнопкой "Помощь" в главном меню. Если вы являетесь старостой или доверенным лицом для своей группы, \
вы можете воспользоваться кнопкой "Для группы".', keyboard=EDIT_SCHEDULE_PERSONAL_FACULTY_KB.get_keyboard())
