from utils.constants import C_SQLITE_ADD_COMMAND, C_SQLITE_SELLECT_ALL_COMMANDS
from utils.terminal_codes import print_info
from datetime import datetime
from vkwave.bots import SimpleBotEvent
import entry

sqlite_connection, cursor = entry.set_up_connection_with_db("users.db")


async def sqlite_fetch(event: SimpleBotEvent, ret: bool = False) -> str:
    user = await event.get_user()
    print_info(
        f"({datetime.today().strftime('%H:%M:%S')}) \033[38;5;80m{user.first_name} {user.last_name} \033[38;5;254m(ID: {event.from_id}): \033[38;5;80m{event.text}\033[0;0m"
    )
    cursor.execute(C_SQLITE_ADD_COMMAND.format(event.from_id, event.text))
    sqlite_connection.commit()
    if ret:
        cursor.execute(C_SQLITE_SELLECT_ALL_COMMANDS.format(event.from_id))
        return cursor.fetchall()
    return
