from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler, TextFilter, PhotoUploader
from utils.sqlite_requests import sqlite_fetch
from keyboards.menu_kb import START_KB


help_router = DefaultRouter()


@simple_bot_message_handler(help_router, TextFilter("помощь"))
async def help(event: SimpleBotEvent) -> str:
    await sqlite_fetch(event)
    photo_lamabot = await PhotoUploader(event.api_ctx).get_attachment_from_link(peer_id=event.object.object.message.peer_id, link="https://sun9-83.userapi.com/impg/bVoWiYTwRgQ4ThlsaJNHMUKh_-nGIZM9IOID0Q/LVt87ogMi4g.jpg?size=591x556&quality=95&sign=30bf84a7dae605fb9ed4050a4c0e93dc&type=album")
    photo_crymother = await PhotoUploader(event.api_ctx).get_attachment_from_link(peer_id=event.object.object.message.peer_id, link="https://sun9-63.userapi.com/impg/BpR7pnTl6CWAw0ud7ph8Qy1eZoWl0aD4qlJpgg/YLkSB-8Tib8.jpg?size=595x560&quality=95&sign=ecf377f818c46e7c8cf634fab5957d02&type=album")
    await event.answer(message='Помощи нет и не будет. \n@lamabot2000\n@crymother', keyboard=START_KB.get_keyboard(), attachment=[photo_lamabot, photo_crymother])
