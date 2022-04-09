import botrayado.keyboards.admin_kb as admin_kb
import botrayado.schedule.sheethandler as sheethandler

from botrayado.database.db import database_handler
from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter


aliases_router = DefaultRouter()


@simple_bot_message_handler(aliases_router, PayloadFilter({"special_blueprint_button": "rayadotd"}))
@database_handler()
async def rayadotd(event: SimpleBotEvent) -> None:
    await event.answer(message=await sheethandler.print_schedule("сегодня", "бвт2103"), keyboard=admin_kb.ADMIN_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule("сегодня", "бст2103"), keyboard=admin_kb.ADMIN_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule("сегодня", "бст2106"), keyboard=admin_kb.ADMIN_KB.get_keyboard())


@simple_bot_message_handler(aliases_router, PayloadFilter({"special_blueprint_button": "rayadotmr"}))
@database_handler()
async def rayadotmr(event: SimpleBotEvent) -> None:
    await event.answer(message=await sheethandler.print_schedule("завтра", "бвт2103"), keyboard=admin_kb.ADMIN_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule("завтра", "бст2103"), keyboard=admin_kb.ADMIN_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule("завтра", "бст2106"), keyboard=admin_kb.ADMIN_KB.get_keyboard())


@simple_bot_message_handler(aliases_router, PayloadFilter({"special_blueprint_button": "fuckmaryamtd"}))
@database_handler()
async def fuckmaryamtd(event: SimpleBotEvent) -> None:
    await event.answer(message=await sheethandler.print_schedule("сегодня", "бст2103"), keyboard=admin_kb.ADMIN_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule("сегодня", "брт2101"), keyboard=admin_kb.ADMIN_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule("сегодня", "бин2102"), keyboard=admin_kb.ADMIN_KB.get_keyboard())


@simple_bot_message_handler(aliases_router, PayloadFilter({"special_blueprint_button": "fuckmaryamtmr"}))
@database_handler()
async def fuckmaryamtmr(event: SimpleBotEvent) -> None:
    await event.answer(message=await sheethandler.print_schedule("завтра", "бст2103"), keyboard=admin_kb.ADMIN_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule("завтра", "брт2101"), keyboard=admin_kb.ADMIN_KB.get_keyboard())
    await event.answer(message=await sheethandler.print_schedule("завтра", "бин2102"), keyboard=admin_kb.ADMIN_KB.get_keyboard())


@simple_bot_message_handler(aliases_router, PayloadFilter({"special_blueprint_button": "vanya"}))
@database_handler()
async def vanya(event: SimpleBotEvent) -> None:
    schedule = await sheethandler.print_full_schedule("следующая неделя", "бвт2103")
    await event.answer(message=schedule, keyboard=admin_kb.ADMIN_KB.get_keyboard())
