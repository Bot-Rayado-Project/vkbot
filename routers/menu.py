import keyboards.menu_kb as menu_kb

from utils.sqlite_requests import database_handler

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, TextFilter, PayloadFilter


menu_router = DefaultRouter()


@simple_bot_message_handler(menu_router, TextFilter(["старт", "начать"], PayloadFilter({"button": "menu"})))
@database_handler(is_menu=True)
async def menu(event: SimpleBotEvent) -> str:
    await event.answer(message='Добро пожаловать в Bot Rayado\n\nЕсли у вас не отобразилась клавиатура, нажмите на кнопку \
                       слева от кнопки выбора эмодзи\n\n Наши преимущества:\n\n - Есть шаблоны для быстрого получения расписания\n \
                        - Всегда новое расписание, полученное с сайта\n \
                       - Большое количество потоков\n - Быстрая работа бота\n - Регулярные обновления', keyboard=menu_kb.START_KB.get_keyboard())


@simple_bot_message_handler(menu_router, TextFilter(["меню", "расписание", ], PayloadFilter({"button": "menu"})))
@database_handler(is_menu=True)
async def menu(event: SimpleBotEvent) -> str:
    await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.START_KB.get_keyboard())


@simple_bot_message_handler(menu_router, TextFilter(["привет", "добрый день", "здравствуй", "здравствуйте", "ку", "прив", "приффки", "дратути"]))
@database_handler()
async def hello(event: SimpleBotEvent) -> None:
    await event.answer(message='Здравствуйте', keyboard=menu_kb.START_KB.get_keyboard())


@simple_bot_message_handler(menu_router, TextFilter(["пока", "до свидания", "бб", "прощай", "до связи"]))
@database_handler()
async def goodbye(event: SimpleBotEvent) -> None:
    await event.answer(message='До свидания', keyboard=menu_kb.START_KB.get_keyboard())
