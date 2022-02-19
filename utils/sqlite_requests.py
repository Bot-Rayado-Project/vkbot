from utils.constants import C_SQLITE_ADD_COMMAND, C_SQLITE_SELLECT_ALL_COMMANDS
import entry

sqlite_connection, cursor = entry.set_up_connection_with_db()


async def sqlite_fetch(from_id: int, text: str, ret: bool = False) -> str:
    cursor.execute(C_SQLITE_ADD_COMMAND.format(from_id, text))
    sqlite_connection.commit()
    if ret:
        cursor.execute(C_SQLITE_SELLECT_ALL_COMMANDS.format(from_id))
        return cursor.fetchall()
    return
