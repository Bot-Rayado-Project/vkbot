import keyboards.menu_kb as menu_kb

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, TextFilter

from utils.sqlite_requests import database_handler
from utils.attachments import get_photo_from_link


easter_egg_router = DefaultRouter()


@simple_bot_message_handler(easter_egg_router, TextFilter("дима"))
@database_handler()
async def easteregg(event: SimpleBotEvent) -> None:
    photo = get_photo_from_link(event, "https://memes.co.in/memes/update/uploads/2021/12/InShot_20211209_222013681-1024x1024.jpg")
    await event.answer(message='?', keyboard=menu_kb.START_KB.get_keyboard(), attachment=photo)
