from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter
from bot.keyboards import create_menu_kb
from bot.db import db_change_priority_button


priority_router = DefaultRouter()


@simple_bot_message_handler(priority_router, PayloadFilter({"menu_button": "priority"}))
async def change_priority(event: SimpleBotEvent) -> None:
    new_button = await db_change_priority_button(event.from_id)
    old_button = 'староста' if new_button == 'свое' else 'свое'
    await event.answer(message=f'Вы сменили приоритет на {old_button}', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
