from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter, TextFilter
from bot.keyboards import create_menu_kb

donate_router = DefaultRouter()


@simple_bot_message_handler(donate_router, PayloadFilter({"menu_button": "donate"}))
async def donate(event: SimpleBotEvent) -> None:
    '''Обработчик кнопки "Поддержать" по пейлоаду'''
    await event.answer(message='Благодарим всех за поддержку!\nhttps://www.tinkoff.ru/cf/67hbUB2jUpf', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())


@simple_bot_message_handler(donate_router, TextFilter("поддержать"))
async def donate(event: SimpleBotEvent) -> None:
    '''Обработчик кнопки "Поддержать" по тексту'''
    await event.answer(message='Благодарим всех за поддержку!\nhttps://www.tinkoff.ru/cf/67hbUB2jUpf', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
