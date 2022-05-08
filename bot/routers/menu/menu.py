from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, TextFilter, PayloadFilter
from bot.keyboards import create_menu_kb


menu_router = DefaultRouter()


@simple_bot_message_handler(menu_router, PayloadFilter({"button": "menu"}))
async def menu(event: SimpleBotEvent) -> None:
    await event.answer(message='Выберите необходимую вам кнопку на клавиатуре', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())


@simple_bot_message_handler(menu_router, TextFilter(("старт", "start", "/start", "начало")))
async def menu(event: SimpleBotEvent) -> None:
    await event.answer(message='Добро пожаловать в Bot Rayado\n\nЕсли у вас не отобразилась клавиатура, нажмите на кнопку' +
                       'слева от кнопки выбора эмодзи\n\n Наши преимущества:\n\n - Есть шаблоны для быстрого получения расписания\n' +
                       ' - Всегда новое расписание, полученное с сайта\n - Все потоки 1 курса\n - Редактор расписания для себя и группы\n ' +
                       ' - Быстрая работа бота\n - Регулярные обновления', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())


@simple_bot_message_handler(menu_router)
async def menu(event: SimpleBotEvent) -> None:
    await event.answer(message='Выберите необходимую вам кнопку на клавиатуре', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
