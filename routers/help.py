import keyboards.menu_kb as menu_kb

from utils.sqlite_requests import database_handler
from utils.attachments import get_photo_from_path

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter

help_router = DefaultRouter()


@simple_bot_message_handler(help_router, PayloadFilter({"button": "help"}))
@database_handler()
async def help(event: SimpleBotEvent) -> str:
    photo_monkey = await get_photo_from_path(event, "img/monkey.jpg")
    await event.answer(message='В случае ошибок или вопросов пишите: \n@lamabot2000\n@crymother\n \
    \nИспользование шаблонов:\n\nСоздаете шаблон, который будет выводить нужное вам расписание по одному клику. Шаблоны хранятся в кнопке "Шаблоны расписания".\n \
    \nРасписание:\n\nДля вывода нужного вам расписания надо нажимать кнопки в нужной вам последовательности.\n \
    \nКлавиатура:\n\nЕсли у вас не отображается клавиатура, нажмите на кнопку слева от вложения фотографий.', keyboard=menu_kb.START_KB.get_keyboard(), attachment=photo_monkey)
