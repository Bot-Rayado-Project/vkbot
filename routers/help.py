import keyboards.menu_kb as menu_kb

from utils.sqlite_requests import database_handler
from utils.attachments import get_photo_from_path

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter

help_router = DefaultRouter()


@simple_bot_message_handler(help_router, PayloadFilter({"button": "help"}))
@database_handler()
async def help(event: SimpleBotEvent) -> str:
    photo_lamabot, photo_crymother = await get_photo_from_path(event, "img/sasha.jpg", "img/ivan.jpg")
    await event.answer(message='Помощи нет и не будет. \n@lamabot2000\n@crymother', keyboard=menu_kb.START_KB.get_keyboard(), attachment=[photo_lamabot, photo_crymother])
