from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter
import botrayado.routers.edit_headman as edit_headman
from botrayado.utils import *
from botrayado.keyboards import *
from botrayado.database import *
from botrayado.database.db import cursor

logger = get_logger(__name__)

edit_router = DefaultRouter()


@simple_bot_message_handler(edit_router, PayloadFilter({"dow_button_c": "edit"}))
@database_handler()
async def edit_schedule(event: SimpleBotEvent) -> None:
    await event.answer(message='Выберите опцию для редактирования расписания.\n\n Если у вас возникли какие-либо вопросы, воспользуйтесь \
кнопкой "Помощь" в главном меню.', keyboard=edit_kb.CHOOSE_HEADMAN_OR_PERSONAL_KB.get_keyboard())


@simple_bot_message_handler(edit_router, PayloadFilter({'chp': 'headman'}))
@database_handler()
async def edit_schedule_headman(event: SimpleBotEvent) -> None:
    cursor.execute(
        f"SELECT headman_panel FROM accesses WHERE user_id={event.from_id}")
    haedman_panel = cursor.fetchall()
    if haedman_panel != []:
        is_headman = haedman_panel[0][0]
        if is_headman:
            cursor.execute(
                f"SELECT stream_group FROM accesses WHERE user_id={event.from_id}")
            group = cursor.fetchall()
            if group != []:
                _group = group[0][0]
    else:
        is_headman = False

    if is_headman:
        edit_headman.edit_headman_requests[event.from_id] = edit_headman.EditHeadmanRequest(
            _group)
        await event.answer(message='Доступ разрешен. Выберите неделю', keyboard=edit_headman_kb.CHOOSE_WEEK_HEADMAN_KB.get_keyboard())
    else:
        await event.answer(message='Вас нет в списке старост какой-либо из групп. Если вы являетесь старостой или доверенным лицом для своей группы, \
напишите об этом @lamabot2000 либо @crymother и вам предоставят доступ к панели. \n\n Если вы хотите изменить расписание только для себя, а не для всей группы, \
вы можете воспользоваться кнопкой "Для себя", где внесенные изменения будут видны только вам.', keyboard=edit_kb.CHOOSE_HEADMAN_OR_PERSONAL_KB.get_keyboard())


@simple_bot_message_handler(edit_router, PayloadFilter({'chp': 'personal'}))
@database_handler()
async def edit_schedule_personal(event: SimpleBotEvent) -> None:
    await event.answer(message='Вы выбрали редактирование расписания для себя. Все вносимые изменения будете видеть только вы.\n\n Для получения помощи \
по использовании редактора, воспользуйтесь кнопкой "Помощь" в главном меню. Если вы являетесь старостой или доверенным лицом для своей группы, \
вы можете воспользоваться кнопкой "Для группы".', keyboard=edit_personal_kb.FACULTIES_BUTTONS_KB.get_keyboard())
