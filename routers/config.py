import keyboards.config_kb as config_kb
import schedule.sheethandler as sheethandler
import keyboards.schedule_kb as schedule_kb

from utils.sqlite_requests import database_handler

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, PayloadContainsFilter

config_router = DefaultRouter()


@simple_bot_message_handler(config_router, PayloadFilter({"button": "config"}))
@database_handler(ret_cfg=True)
async def config_start(event: SimpleBotEvent, buttons: list[tuple]) -> None:
    CONFIG_KB = config_kb.create_config_keyboard(buttons)
    await event.answer(message='Выберите шаблон или создайте новый.', keyboard=CONFIG_KB.get_keyboard())


@simple_bot_message_handler(config_router, PayloadContainsFilter("cell"))
@database_handler(ret_cfg=True)
async def cells_handler(event: SimpleBotEvent, buttons: list[tuple]) -> None:
    CONFIG_KB = config_kb.create_config_keyboard(buttons)
    matching: dict = {"first_btn": 0, "second_btn": 1, "third_btn": 2}
    cell = buttons[0][0].split(', ')[matching[event.payload["cell"]]]
    if cell == 'Пустая ячейка':
        await event.answer(message='Ячейка пуста. Создайте шаблон с помощью кнопки "Создать шаблон".', keyboard=CONFIG_KB.get_keyboard())
    else:
        button = cell.lower().split()
        if 'сн' in button or 'тн' in button:
            schedule = await sheethandler.print_schedule('вся неделя', button[1].lower(), event.from_id, 'следующая неделя' if 'сн' in button else 'текущая неделя')  # Вся неделя, группа, тип недели
            for _schedule in schedule:
                await event.answer(message=_schedule, keyboard=CONFIG_KB.get_keyboard())
        else:
            schedule = await sheethandler.print_schedule(button[0].lower(), button[1].lower(), event.from_id, 'текущая неделя')  # Сегодня БВТ2103 etc.
            await event.answer(message=schedule, keyboard=CONFIG_KB.get_keyboard())


@simple_bot_message_handler(config_router, PayloadFilter({"button": "create_blueprint"}))
@database_handler(ret_cfg=True)
async def create_blueprint_start(event: SimpleBotEvent, buttons: list[tuple]) -> None:
    CONFIG_KB = config_kb.create_config_keyboard(buttons, True)
    await event.answer(message='Выберите ячейку для (пере-)записи.', keyboard=CONFIG_KB.get_keyboard())


@simple_bot_message_handler(config_router, PayloadContainsFilter("choose_cell"))
@database_handler(write_flag=True)
async def choose_cells_handler(event: SimpleBotEvent) -> None:
    await event.answer(message='Выберите последовательность шаблона.', keyboard=schedule_kb.DAYS_OF_WEEK_KB.get_keyboard())
