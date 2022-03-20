from utils.constants import *
from utils.terminal_codes import print_info
from datetime import datetime
from vkwave.bots import SimpleBotEvent
import entry
import typing

sqlite_connection, cursor = entry.set_up_connection_with_db("users.db")


def database_handler(ret_cmd: bool = False, ret_cfg: bool = False, ret_flag: bool = False, write_flag: bool = False, is_menu: bool = False):
    def decorator(func: typing.Callable[..., typing.Any]):
        async def wrapper(event: SimpleBotEvent) -> str:
            try:
                user = await event.get_user()
                print_info(f"({datetime.today().strftime('%H:%M:%S')}) \033[38;5;80m{user.first_name} {user.last_name} \033[38;5;254m(ID: {event.from_id}): \033[38;5;80m{event.text}\033[0;0m")
                cursor.execute(C_SQLITE_ADD_COMMAND.format(event.from_id, event.text))
                sqlite_connection.commit()
                if is_menu:
                    cursor.execute(C_SQLITE_SELECT_CONFIG_KEYBOARD_BUTTONS.format(event.from_id))
                    btn = cursor.fetchall()
                    if btn == []:
                        cursor.execute(C_SQLITE_FIRST_ADD_CONFIG_BUTTONS.format(event.from_id))
                        sqlite_connection.commit()
                        return await func(event)
                    else:
                        cursor.execute(C_SQLITE_SET_IS_WRITING_FALSE.format(event.from_id))
                        sqlite_connection.commit()
                        return await func(event)
                if write_flag:
                    cursor.execute(C_SQLITE_SET_IS_WRITING_TRUE.format(event.from_id))
                    sqlite_connection.commit()
                    cursor.execute(C_SQLITE_SET_BUTTON_TO_WRITE.format(event.payload["choose_cell"], event.from_id))
                    return await func(event)
                elif ret_cfg:
                    cursor.execute(C_SQLITE_SELECT_CONFIG_KEYBOARD_BUTTONS.format(event.from_id))
                    btn = cursor.fetchall()
                    if btn == []:
                        cursor.execute(C_SQLITE_FIRST_ADD_CONFIG_BUTTONS.format(event.from_id))
                        sqlite_connection.commit()
                        return await func(event, btn)  # Вернет кнопки клавы с пустыми ячейками
                    else:
                        cursor.execute(C_SQLITE_SELECT_CONFIG_KEYBOARD_BUTTONS.format(event.from_id))
                        return await func(event, cursor.fetchall())  # Вернет кнопки клавы с чем то уже имеющимся
                elif ret_cmd and ret_flag:
                    cursor.execute(C_SQLITE_SELLECT_ALL_COMMANDS.format(event.from_id))
                    cmd = cursor.fetchall()
                    cursor.execute(C_SQLITE_GET_IS_WRITING.format(event.from_id))
                    flag = cursor.fetchall()
                    cursor.execute(C_SQLITE_GET_BUTTON_TO_WRITE.format(event.from_id))
                    btn = cursor.fetchall()
                    return await func(event, cmd, flag, btn)
                elif ret_cmd:
                    cursor.execute(C_SQLITE_SELLECT_ALL_COMMANDS.format(event.from_id))
                    return await func(event, cursor.fetchall())
                else:
                    return await func(event)
            except:
                pass
        return wrapper
    return decorator


def set_first(cmd, event):
    cursor.execute(C_SQLITE_SELECT_CONFIG_KEYBOARD_BUTTONS.format(event.from_id))
    btn = cursor.fetchall()[0][0].split(', ')
    cursor.execute(C_SQLITE_UPDATE_CONFIG_BUTTONS.format(cmd, btn[1], btn[2], event.from_id))
    cursor.execute(C_SQLITE_SET_IS_WRITING_FALSE.format(event.from_id))
    sqlite_connection.commit()


def set_second(cmd, event):
    cursor.execute(C_SQLITE_SELECT_CONFIG_KEYBOARD_BUTTONS.format(event.from_id))
    btn = cursor.fetchall()[0][0].split(', ')
    cursor.execute(C_SQLITE_UPDATE_CONFIG_BUTTONS.format(btn[0], cmd, btn[2], event.from_id))
    cursor.execute(C_SQLITE_SET_IS_WRITING_FALSE.format(event.from_id))
    sqlite_connection.commit()


def set_third(cmd, event):
    cursor.execute(C_SQLITE_SELECT_CONFIG_KEYBOARD_BUTTONS.format(event.from_id))
    btn = cursor.fetchall()[0][0].split(', ')
    cursor.execute(C_SQLITE_UPDATE_CONFIG_BUTTONS.format(btn[0], btn[1], cmd, event.from_id))
    cursor.execute(C_SQLITE_SET_IS_WRITING_FALSE.format(event.from_id))
    sqlite_connection.commit()
