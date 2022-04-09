import botrayado.keyboards.menu_kb as menu_kb

from botrayado.database.db import database_handler

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, TextFilter, PhotoUploader

help_router = DefaultRouter()


@simple_bot_message_handler(help_router, TextFilter("помощь"), PayloadFilter({"button": "help"}))
@database_handler()
async def help(event: SimpleBotEvent) -> str:
    photo_monkey = await PhotoUploader(event.api_ctx).get_attachment_from_path(peer_id=event.object.object.message.peer_id, file_path='botrayado/img/monkey.jpg')
    await event.answer(message='В случае ошибок или вопросов пишите: \n@lamabot2000\n@crymother\n \
    \nИспользование шаблонов:\n\nСоздаете шаблон, который будет выводить нужное вам расписание по одному клику. Шаблоны хранятся в кнопке "Шаблоны расписания".\n \
    \nРасписание:\n\nДля вывода нужного вам расписания надо нажимать кнопки в нужной вам последовательности.\n \
    \nКлавиатура:\n\nЕсли у вас не отображается клавиатура, нажмите на кнопку слева от выбора эмодзи.', keyboard=menu_kb.START_KB.get_keyboard(), attachment=photo_monkey)
