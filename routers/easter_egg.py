from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler, TextFilter, PhotoUploader
from utils.sqlite_requests import sqlite_fetch
from utils.constants import START_KB


easter_egg_router = DefaultRouter()


@simple_bot_message_handler(easter_egg_router, TextFilter("дима"))
async def easteregg(event: SimpleBotEvent) -> str:
    await sqlite_fetch(event.from_id, event.text)
    gif = await PhotoUploader(event.api_ctx).get_attachment_from_link(peer_id=event.object.object.message.peer_id, link="https://memes.co.in/memes/update/uploads/2021/12/InShot_20211209_222013681-1024x1024.jpg")
    await event.answer(message='?', keyboard=START_KB.get_keyboard(), attachment=gif)
