import botrayado.keyboards.menu_kb as menu_kb

from botrayado.database.db import database_handler

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, TextFilter, PhotoUploader

help_router = DefaultRouter()


@simple_bot_message_handler(help_router, TextFilter("помощь"), PayloadFilter({"button": "help"}))
@database_handler(ret_btn=True)
async def help(event: SimpleBotEvent, button: str) -> str:
    photo_monkey = await PhotoUploader(event.api_ctx).get_attachment_from_path(peer_id=event.object.object.message.peer_id, file_path='botrayado/img/monkey.jpg')
    await event.answer(message='В случае ошибок или вопросов пишите: \n@lamabot2000\n@crymother\n \
    \nИспользование шаблонов:\n\nСоздаете шаблон, который будет выводить нужное вам расписание по одному клику. Шаблоны хранятся в кнопке "Шаблоны расписания".\n \
    \nРасписание:\n\nДля вывода нужного вам расписания надо нажимать кнопки в нужной вам последовательности.\n \
    \nКлавиатура:\n\nЕсли у вас не отображается клавиатура, нажмите на кнопку слева от выбора эмодзи.\n \
    \nРедактор расписания:\n\nВ боте имеется редактор расписания. Вы можете изменить расписание как для себя, так и для всей группы, при наличии доступа. \
    При редактировании для себя, изменения будут видны только вам. Если же вы являетесь старостой, или доверенным лицом группы, у вас будет доступ \
    для редактирования расписания так, что изменения будут видны всем. В главном меню имеется кнопка приоритета вывода. \
    Если на один и тот же день расписание изменено как вами, так и старостой, то вывод будет зависить от выбранного вами приоритета. \
    \n\nПри использовании редактора, вы можете удалить либо изменить пару, а также добавить личную заметку к данному дню. \
    Если вам что-то не понравилось или вы случайно сделали ошибку, вы можете сбросить все внесенные изменения на этот день.', keyboard=menu_kb.create_menu_keyboard(button).get_keyboard(), attachment=photo_monkey)
