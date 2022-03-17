import keyboards.menu_kb as menu_kb
import geobot as geo

from utils.sqlite_requests import database_handler
from entry import settings

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, DocUploader
from datetime import datetime


geobot_router = DefaultRouter()


@simple_bot_message_handler(geobot_router, PayloadFilter({"button": "miamor"}))
@database_handler()
async def miamor(event: SimpleBotEvent) -> str:
    if str(event.from_id) in settings.GET_ALLOWED_USER_IDS():
        await event.answer(message='ACCESS GRANTED.', keyboard=menu_kb.START_KB.get_keyboard())
        await geo.write_gpx(0, 5)
        gpx = await DocUploader(event.api_ctx).get_attachment_from_path(peer_id=event.object.object.message.peer_id, file_path="geobot/test.gpx", title=f"Route {datetime.now()}")
        await event.answer(message='Карта:', keyboard=menu_kb.START_KB.get_keyboard(), attachment=gpx)
    else:
        await event.answer(message='MI AMOR LA VINO!!! CASILLERO DEL DIABLO!!!!', keyboard=menu_kb.START_KB.get_keyboard())
