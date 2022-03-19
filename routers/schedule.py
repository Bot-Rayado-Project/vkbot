import schedule.sheethandler as sheethandler
import keyboards.schedule_kb as schedule_kb
import keyboards.menu_kb as menu_kb
from utils.sqlite_requests import database_handler, set_first, set_second, set_third

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, PayloadContainsFilter
from datetime import datetime, timedelta


schedule_router = DefaultRouter()


@simple_bot_message_handler(schedule_router, PayloadFilter({"button": "schedule"}))
@database_handler()
async def get_schedule(event: SimpleBotEvent) -> str:
    await event.answer(message='Выберите день.', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("dow_button"))
@database_handler(True)
async def get_day_of_week(event: SimpleBotEvent, fetch: dict) -> str:
    last_command = fetch[0][0].lower()  # Последняя команда
    if last_command == schedule_kb.DAYS_OF_WEEK_BUTTONS[2]:  # == вся неделя
        await event.answer(message='Выберите неделю.', keyboard=schedule_kb.CURRENT_OR_NEXT_WEEK_KB.get_keyboard())
    else:  # == сегодня | завтра
        await event.answer(message='Выберите поток.', keyboard=schedule_kb.STREAM_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("conw_button"))
@database_handler(True)
async def get_current_or_next_week(event: SimpleBotEvent, fetch: dict) -> str:
    await event.answer(message='Выберите поток.', keyboard=schedule_kb.STREAM_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("stream_button"))
@database_handler(True)
async def get_stream(event: SimpleBotEvent, fetch: dict) -> str:
    last_command = fetch[0][0].lower()  # Последняя команда
    if last_command == 'бфи':
        await event.answer(message='Выберите группу.', keyboard=schedule_kb.GROUP_BUTTONS_BFI_KB.get_keyboard())
    elif last_command == 'бвт':
        await event.answer(message='Выберите группу.', keyboard=schedule_kb.GROUP_BUTTONS_BVT_KB.get_keyboard())
    elif last_command == 'бст':
        await event.answer(message='Выберите группу.', keyboard=schedule_kb.GROUP_BUTTONS_BST_KB.get_keyboard())
    elif last_command == 'бэи':
        await event.answer(message='Выберите группу.', keyboard=schedule_kb.GROUP_BUTTONS_BEI_KB.get_keyboard())
    elif last_command == 'биб':
        await event.answer(message='Выберите группу.', keyboard=schedule_kb.GROUP_BUTTONS_BIB_KB.get_keyboard())
    elif last_command == 'бин':
        await event.answer(message='Выберите группу.', keyboard=schedule_kb.GROUP_BUTTONS_BIN_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("group_button"))
@database_handler(ret_cmd=True, ret_flag=True)
async def get_group(event: SimpleBotEvent, fetch: dict, flag: bool, btn: str) -> str:
    last_command = fetch[0][0].lower()  # Последняя команда # ГРУППА
    pre_penultimate_command = fetch[2][0].lower()  # Пред предпоследняя команда
    pre_pre_penultimate_command = fetch[3][0].lower()
    if flag == [(0,)]:
        if any(cmd.lower() in [pre_penultimate_command] for cmd in schedule_kb.CURRENT_OR_NEXT_WEEK_BUTTONS) and pre_pre_penultimate_command == schedule_kb.DAYS_OF_WEEK_BUTTONS[2]:
            schedule = await sheethandler.print_schedule('вся неделя', last_command, event.from_id, pre_penultimate_command)
            for i in range(len(schedule)):
                await event.answer(message=schedule[i], keyboard=menu_kb.START_KB.get_keyboard())
        elif any(cmd.lower() in [pre_penultimate_command] for cmd in schedule_kb.DAYS_OF_WEEK_BUTTONS):
            schedule = await sheethandler.print_schedule(pre_penultimate_command, last_command, event.from_id, 'текущая неделя')
            await event.answer(message=schedule, keyboard=menu_kb.START_KB.get_keyboard())
        else:
            await event.answer(message="Непредвиденная ошибка.", keyboard=menu_kb.START_KB.get_keyboard())
    else:
        if any(cmd.lower() in [pre_penultimate_command] for cmd in schedule_kb.CURRENT_OR_NEXT_WEEK_BUTTONS) and pre_pre_penultimate_command == schedule_kb.DAYS_OF_WEEK_BUTTONS[2]:
            result = pre_penultimate_command.split()[0] + ' ' + 'неделя' + ' ' + last_command
            if btn[0][0] == 'first_btn':
                set_first(result, event)
                await event.answer(message=f"Задан шаблон: {result}", keyboard=menu_kb.START_KB.get_keyboard())
            elif btn[0][0] == 'second_btn':
                set_second(result, event)
                await event.answer(message=f"Задан шаблон: {result}", keyboard=menu_kb.START_KB.get_keyboard())
            elif btn[0][0] == 'third_btn':
                set_third(result, event)
                await event.answer(message=f"Задан шаблон: {result}", keyboard=menu_kb.START_KB.get_keyboard())
            else:
                print("mistake")
        elif any(cmd.lower() in [pre_penultimate_command] for cmd in schedule_kb.DAYS_OF_WEEK_BUTTONS):
            result = pre_penultimate_command + ' ' + last_command
            if btn[0][0] == 'first_btn':
                set_first(result, event)
                await event.answer(message=f"Задан шаблон: {result}", keyboard=menu_kb.START_KB.get_keyboard())
            elif btn[0][0] == 'second_btn':
                set_second(result, event)
                await event.answer(message=f"Задан шаблон: {result}", keyboard=menu_kb.START_KB.get_keyboard())
            elif btn[0][0] == 'third_btn':
                set_third(result, event)
                await event.answer(message=f"Задан шаблон: {result}", keyboard=menu_kb.START_KB.get_keyboard())
            else:
                print("mistake")
        else:
            await event.answer(message="Непредвиденная ошибка.", keyboard=menu_kb.START_KB.get_keyboard())
