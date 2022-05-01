from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, TextFilter
from botrayado.keyboards import *
from botrayado.database import *

aliases_router = DefaultRouter()


@simple_bot_message_handler(aliases_router, PayloadFilter({"special_blueprint_button": "rayadotd"}), TextFilter('rayadotd'))
@database_handler()
async def rayadotd(event: SimpleBotEvent) -> None:
    await event.answer(message=await sheethandler.print_schedule(event.from_id, "сегодня", "бвт2103"), keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule(event.from_id, "сегодня", "бст2103"), keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule(event.from_id, "сегодня", "бст2106"), keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())


@simple_bot_message_handler(aliases_router, PayloadFilter({"special_blueprint_button": "rayadotmr"}), TextFilter('rayadotmr'))
@database_handler()
async def rayadotmr(event: SimpleBotEvent) -> None:
    await event.answer(message=await sheethandler.print_schedule(event.from_id, "завтра", "бвт2103"), keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule(event.from_id, "завтра", "бст2103"), keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule(event.from_id, "завтра", "бст2106"), keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())


@simple_bot_message_handler(aliases_router, PayloadFilter({"special_blueprint_button": "fuckmaryamtd"}), TextFilter('fuckmaryamtd'))
@database_handler()
async def fuckmaryamtd(event: SimpleBotEvent) -> None:
    await event.answer(message=await sheethandler.print_schedule(event.from_id, "сегодня", "бст2103"), keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule(event.from_id, "сегодня", "брт2101"), keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule(event.from_id, "сегодня", "бин2102"), keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())


@simple_bot_message_handler(aliases_router, PayloadFilter({"special_blueprint_button": "fuckmaryamtmr"}), TextFilter('fuckmaryamtmr'))
@database_handler()
async def fuckmaryamtmr(event: SimpleBotEvent) -> None:
    await event.answer(message=await sheethandler.print_schedule(event.from_id, "завтра", "бст2103"), keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule(event.from_id, "завтра", "брт2101"), keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule(event.from_id, "завтра", "бин2102"), keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())


@simple_bot_message_handler(aliases_router, PayloadFilter({"special_blueprint_button": "vanya"}), TextFilter('ваня'))
@database_handler()
async def vanya(event: SimpleBotEvent) -> None:
    schedule = await sheethandler.print_full_schedule("следующая неделя", "бвт2103")
    await event.answer(message=schedule, keyboard=special_blueprints.SPECIAL_BLUEPRINTS_KB.get_keyboard())
