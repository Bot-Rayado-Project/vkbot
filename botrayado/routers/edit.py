import json
from transliterate import translit
import botrayado.utils.constants as constants
import botrayado.keyboards.edit_kb as edit_kb
import botrayado.keyboards.schedule_kb as schedule_kb
import botrayado.keyboards.menu_kb as menu_kb
import botrayado.schedule.sheethandler as sheethandler
import aiohttp

from botrayado.database.db import database_handler

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, PayloadContainsFilter

from botrayado.utils.logger import get_logger

logger = get_logger(__name__)

edit_router = DefaultRouter()


@simple_bot_message_handler(edit_router, PayloadFilter({'chp': 'headman'}))
@database_handler()
async def edit_headman(event: SimpleBotEvent) -> str:
    if constants.headmans_ids.get(event.from_id) is not None:
        await event.answer(message='Выберите неделю', keyboard=edit_kb.CHOOSE_WEEK_KB.get_keyboard())
    else:
        await event.answer(message='Вас нет в списке старост какой-либо из групп. Если вы являетесь старостой или доверенным лицом для своей группы, \
напишите об этом @lamabot2000 либо @crymother и вам предоставят доступ к панели. Если вы хотите изменить расписание только для себя, а не для всей группы, \
вы можете воспользоваться кнопкой "Для себя", где внесенные изменения будут видны только вам.', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())


@simple_bot_message_handler(edit_router, PayloadFilter({'chp': 'personal'}))
@database_handler()
async def edit_headman(event: SimpleBotEvent) -> str:
    await event.answer(message='Вы выбрали редактирование расписания для себя. Все вносимые изменения будете видеть только вы. Для получения помощи \
по использовании редактора, воспользуйтесь кнопкой "Помощь" в главном меню. Если вы являетесь старостой или доверенным лицом для своей группы, \
вы можете воспользоваться кнопкой "Для группы".', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
