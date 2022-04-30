import json
from transliterate import translit
import botrayado.utils.constants as constants
import botrayado.keyboards.edit_kb as edit_kb
import botrayado.keyboards.lookheadman_kb as lookheadman_kb
import botrayado.keyboards.menu_kb as menu_kb
import botrayado.schedule.sheethandler as sheethandler
import aiohttp

from botrayado.database.db import database_handler
from botrayado.utils.constants import DAYS_ENG, DAYS_RU, RESTIP, RESTPORT

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, PayloadContainsFilter

from botrayado.utils.logger import get_logger

logger = get_logger(__name__)

lookheadman_router = DefaultRouter()


async def post_request(url: str, data: dict) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, json=data) as response:
            return await response.text()


async def get_request(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            return await response.text()


@simple_bot_message_handler(lookheadman_router, PayloadFilter({"dow_button_c": "look"}))
@database_handler()
async def choose_faculty_to_look(event: SimpleBotEvent) -> str:
    await event.answer(message='Выберите факультет.', keyboard=lookheadman_kb.FACULTIES_BUTTONS_KB.get_keyboard())


@simple_bot_message_handler(lookheadman_router, PayloadContainsFilter("faculty_button_h"))
@database_handler()
async def get_faculty(event: SimpleBotEvent) -> str:
    await event.answer(message='Выберите поток.', keyboard=lookheadman_kb.KB_STREAMS[event.payload['faculty_button_h']]())


@simple_bot_message_handler(lookheadman_router, PayloadContainsFilter("stream_button_h"))
@database_handler()
async def get_stream(event: SimpleBotEvent) -> str:
    await event.answer(message='Выберите группу.', keyboard=lookheadman_kb.KB[event.text.lower()]())


@simple_bot_message_handler(lookheadman_router, PayloadContainsFilter("group_button_h"))
@database_handler()
async def get_group(event: SimpleBotEvent) -> str:
    answer = ''
    for day in DAYS_ENG:
        for even in True, False:
            response = json.loads(await get_request(
                f'http://{RESTIP}:{RESTPORT}/annotation/?group={event.payload["group_button_h"]}&day={day}&even={even}'
            ))
            annotation = response['annotation']
            print(annotation)
            _week = 'четная' if even else 'нечетная'
            if annotation != 'No annotation found':
                answer += '⸻⸻⸻⸻⸻\n' + f'День: {DAYS_RU[DAYS_ENG.index(day)]}\n Неделя: {_week}\n {annotation}\n'
    print(answer)
    if answer != '':
        await event.answer(message=answer, keyboard=menu_kb.START_KB.get_keyboard())
    else:
        await event.answer(message='Аннотаций для вашей группы нет', keyboard=menu_kb.START_KB.get_keyboard())
