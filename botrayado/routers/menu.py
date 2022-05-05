import botrayado.keyboards.menu_kb as menu_kb
import botrayado.utils.constants as constants

from botrayado.database.db import database_handler

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, TextFilter, PayloadFilter


menu_router = DefaultRouter()


@simple_bot_message_handler(menu_router, TextFilter(["старт", "начать"], PayloadFilter({"button": "menu"})))
@database_handler(is_menu=True)
async def menu(event: SimpleBotEvent, button: str) -> str:
    await event.answer(message='Добро пожаловать в Bot Rayado\n\nЕсли у вас не отобразилась клавиатура, нажмите на кнопку' +
                       'слева от кнопки выбора эмодзи\n\n Наши преимущества:\n\n - Есть шаблоны для быстрого получения расписания\n' +
                       ' - Всегда новое расписание, полученное с сайта\n - Все потоки 1 курса\n - Редактор расписания для себя и группы\n ' +
                       ' - Быстрая работа бота\n - Регулярные обновления', keyboard=menu_kb.create_menu_keyboard(button).get_keyboard())


@simple_bot_message_handler(menu_router, TextFilter(["меню", "расписание"], PayloadFilter({"button": "menu"})))
@database_handler(is_menu=True)
async def menu(event: SimpleBotEvent, button: str) -> str:
    await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.create_menu_keyboard(button).get_keyboard())


@simple_bot_message_handler(menu_router, PayloadFilter({"button": "priority"}))
@database_handler(is_menu=True, switch_button=True)
async def menu(event: SimpleBotEvent, button: str) -> str:
    if button == 'староста':
        await event.answer(message=f'Вы сменили приоритет вывода расписания на "{button}".\n\n \
Если при выводе расписания будут найдены изменения, сделанные старостой, то сначала отобразятся именно они. \
Далее если этих изменений найдено не будет, отобразятся ваши изменения. Если и их найденно не будет, отобразится стандартное \
расписание, которое видят все. Все вышесказанное аналогично относится и к аннотациям. \n\n \
Более подобную информацию о приоритете можно узнать в группе, либо нажав кнопку "Помощь".', keyboard=menu_kb.create_menu_keyboard(button).get_keyboard())
    else:
        await event.answer(message=f'Вы сменили приоритет вывода расписания на "{button}".\n\n \
Если при выводе расписания будут найдены изменения, сделанные вами, то сначала отобразятся именно они. \
Далее если этих изменений найдено не будет, отобразятся изменения старосты. Если и их найденно не будет, отобразится стандартное \
расписание, которое видят все. Все вышесказанное аналогично относится и к аннотациям. \n\n \
Более подобную информацию о приоритете можно узнать в группе, либо нажав кнопку "Помощь".', keyboard=menu_kb.create_menu_keyboard(button).get_keyboard())
