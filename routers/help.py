from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler, PayloadFilter, PhotoUploader
from utils.sqlite_requests import sqlite_fetch
from keyboards.menu_kb import START_KB


help_router = DefaultRouter()


@simple_bot_message_handler(help_router, PayloadFilter({"button": "help"}))
async def help(event: SimpleBotEvent) -> str:
    user = await event.get_user()
    sqlite_fetch(event, user)
    photo_lamabot = await PhotoUploader(event.api_ctx).get_attachment_from_path(peer_id=event.object.object.message.peer_id, file_path="img/sasha.jpg")
    photo_crymother = await PhotoUploader(event.api_ctx).get_attachment_from_path(peer_id=event.object.object.message.peer_id, file_path="img/ivan.jpg")
    await event.answer(message='Помощи нет и не будет. \n@lamabot2000\n@crymother', keyboard=START_KB.get_keyboard(), attachment=[photo_lamabot, photo_crymother])
