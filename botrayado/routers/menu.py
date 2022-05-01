import botrayado.keyboards.menu_kb as menu_kb
import botrayado.utils.constants as constants

from botrayado.database.db import database_handler
from botrayado.utils.constants import headmans_ids

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, TextFilter, PayloadFilter


menu_router = DefaultRouter()


@simple_bot_message_handler(menu_router, TextFilter(["старт", "начать"], PayloadFilter({"button": "menu"})))
@database_handler(is_menu=True)
async def menu(event: SimpleBotEvent, button: str) -> str:
    await event.answer(message='Добро пожаловать в Bot Rayado\n\nЕсли у вас не отобразилась клавиатура, нажмите на кнопку' +
                       'слева от кнопки выбора эмодзи\n\n Наши преимущества:\n\n - Есть шаблоны для быстрого получения расписания\n' +
                       ' - Всегда новое расписание, полученное с сайта\n - Все потоки 1 курса\n - Быстрая работа бота\n - Регулярные обновления', keyboard=menu_kb.create_menu_keyboard(button).get_keyboard())


@simple_bot_message_handler(menu_router, TextFilter(["меню", "расписание"], PayloadFilter({"button": "menu"})))
@database_handler(is_menu=True)
async def menu(event: SimpleBotEvent, button: str) -> str:
    await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.create_menu_keyboard(button).get_keyboard())


@simple_bot_message_handler(menu_router, PayloadFilter({"button": "priority"}))
@database_handler(is_menu=True, switch_button=True)
async def menu(event: SimpleBotEvent, button: str) -> str:
    await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.create_menu_keyboard(button).get_keyboard())
