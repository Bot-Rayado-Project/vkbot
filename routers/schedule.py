from utils.attachments import get_file_from_path
import schedule.sheethandler as sheethandler
import keyboards.schedule_kb as schedule_kb
import keyboards.menu_kb as menu_kb
from utils.terminal_codes import print_error, print_info
from utils.sqlite_requests import database_handler, set_button_blueprint

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, PayloadContainsFilter
from datetime import datetime, timedelta


schedule_router = DefaultRouter()


@simple_bot_message_handler(schedule_router, PayloadFilter({"button": "schedule"}))
@database_handler(is_menu=True)
async def get_schedule(event: SimpleBotEvent) -> str:
    await event.answer(message='Выберите день.', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("dow_button"))
@database_handler(True)
async def get_day_of_week(event: SimpleBotEvent, fetch: dict) -> str:
    last_command = fetch[0][0].lower()  # Последняя команда
    if last_command == schedule_kb.DAYS_OF_WEEK_BUTTONS[2]:  # == вся неделя
        await event.answer(message='Выберите неделю.', keyboard=schedule_kb.CURRENT_OR_NEXT_WEEK_KB.get_keyboard())
    else:  # == сегодня | завтра
        await event.answer(message='Выберите факультет.', keyboard=schedule_kb.FACULTIES_BUTTONS_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("faculty_button"))
@database_handler(True)
async def get_faculty(event: SimpleBotEvent, fetch: dict) -> str:
    last_command = fetch[0][0].lower()
    await event.answer(message='Выберите поток.', keyboard=schedule_kb.KB_STREAMS[event.payload['faculty_button']]())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("conw_button"))
@database_handler(True)
async def get_current_or_next_week(event: SimpleBotEvent, fetch: dict) -> str:
    last_command = fetch[0][0].lower()
    await event.answer(message='Выберите факультет.', keyboard=schedule_kb.FACULTIES_BUTTONS_KB.get_keyboard())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("stream_button"))
@database_handler(True)
async def get_stream(event: SimpleBotEvent, fetch: dict) -> str:
    last_command = fetch[0][0].lower()
    await event.answer(message='Выберите группу.', keyboard=schedule_kb.KB[last_command]())


@simple_bot_message_handler(schedule_router, PayloadContainsFilter("group_button"))
@database_handler(ret_cmd=True, ret_flag=True)
async def get_group(event: SimpleBotEvent, fetch: dict, flag: bool, btn: str) -> str:
    last_command = fetch[0][0].lower()  # Последняя команда # ГРУППА
    pre_penultimate_command = fetch[3][0].lower()  # Пред предпоследняя команда
    pre_pre_penultimate_command = fetch[4][0].lower()  # Пред пред предпоследняя команда
    start_time = datetime.now()
    if flag == [(0,)]:
        if any(cmd.lower() in [pre_penultimate_command] for cmd in schedule_kb.CURRENT_OR_NEXT_WEEK_BUTTONS) and pre_pre_penultimate_command == schedule_kb.DAYS_OF_WEEK_BUTTONS[2]:
            print_info('Вся неделя')
            schedule = await sheethandler.print_schedule('вся неделя', last_command, event.from_id, pre_penultimate_command)
            if schedule == False:
                table_file = await get_file_from_path(event, f"Расписание {last_command[0:3]}.xlsx", f"tables/table_{(last_command.lower())[0:3]}.xlsx")
                await event.answer(message=f'Ошибка в получении расписания. Возможно изменился формат таблицы, посмотрите расписание вручную. Информация об ошибке передана разработчкам', keyboard=menu_kb.START_KB.get_keyboard(), attachment=table_file)
                print_error('Критическая ошибка в получении расписания. Проверить таблицу.')
            else:
                for i in range(len(schedule)):
                    await event.answer(message=schedule[i], keyboard=menu_kb.START_KB.get_keyboard())
        elif any(cmd.lower() in [pre_penultimate_command] for cmd in schedule_kb.DAYS_OF_WEEK_BUTTONS):
            print_info('Сегодня/завтра')
            schedule = await sheethandler.print_schedule(pre_penultimate_command, last_command, event.from_id, 'текущая неделя')
            if schedule == False:
                table_file = await get_file_from_path(event, f"Расписание {last_command[0:3]}.xlsx", f"tables/table_{(last_command.lower())[0:3]}.xlsx")
                await event.answer(message=f'Ошибка в получении расписания. Возможно изменился формат таблицы, посмотрите расписание вручную. Информация об ошибке передана разработчкам', keyboard=menu_kb.START_KB.get_keyboard(), attachment=table_file)
                print_error('Критическая ошибка в получении расписания. Проверить таблицу.')
            else:
                await event.answer(message=schedule, keyboard=menu_kb.START_KB.get_keyboard())
        else:
            await event.answer(message="Непредвиденная ошибка. Не нажимайте на 2 разные кнопки в одной категории. Повторите свой запрос.", keyboard=menu_kb.START_KB.get_keyboard())
            print_error('Непредвиденная ошибка в выводе расписания. Предположительно было нажато 2 разные кнопки в одной категории.')
        print_info(f"Общее время вывода расписания: {datetime.now() - start_time}")
    else:
        if any(cmd.lower() in [pre_penultimate_command] for cmd in schedule_kb.CURRENT_OR_NEXT_WEEK_BUTTONS) and pre_pre_penultimate_command == schedule_kb.DAYS_OF_WEEK_BUTTONS[2]:
            result = pre_penultimate_command.split()[0][0].upper() + 'Н' + ' ' + last_command.upper()  # ТН БВТ2103 либо СН БВТ2103 (текущая неделя | следующая неделя, группа)
        elif any(cmd.lower() in [pre_penultimate_command] for cmd in schedule_kb.DAYS_OF_WEEK_BUTTONS):
            result = pre_penultimate_command.capitalize() + ' ' + last_command.upper()  # Сегодня БВТ2103 (сегодня | завтра, группа)
        else:
            await event.answer(message="Непредвиденная ошибка.", keyboard=menu_kb.START_KB.get_keyboard())
        already_exists = set_button_blueprint(btn[0][0], result, event)
        await event.answer(message=f"Задан шаблон: {result}", keyboard=menu_kb.START_KB.get_keyboard()) if not already_exists else await event.answer(message="Данный шаблон уже существует в {} ячейке.".format({'first_btn': 1, 'second_btn': 2, 'third_btn': 3}[btn[0][0]]), keyboard=menu_kb.START_KB.get_keyboard())
