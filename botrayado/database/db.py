from botrayado.utils.constants import *
from vkwave.bots import SimpleBotEvent
from botrayado.utils.logger import get_logger
from botrayado.utils.constants import VOLUMENAME
import typing
import sqlite3

logger = get_logger(__name__)


def set_up_connection_with_db(data_base_name: str) -> tuple | None:
    try:
        sqlite_connection: sqlite3.Connection = sqlite3.connect(data_base_name)
        logger.info("Successfully connected to database.")
        return sqlite_connection, sqlite_connection.cursor()
    except sqlite3.Error:
        logger.error("Database connection failure.")
        exit()


if DEBUG is not None:
    sqlite_connection, cursor = set_up_connection_with_db(
        "botrayado/database/db/users.db")
else:
    sqlite_connection, cursor = set_up_connection_with_db(
        f"/var/lib/docker/volumes/{VOLUMENAME}/_data/users.db")

'''cursor.execute(
    'CREATE TABLE IF NOT EXISTS menu_buttons_table(user_id INT NOT NULL, button TEXT NOT NULL);')
sqlite_connection.commit()
cursor.execute('SELECT * FROM menu_buttons_table;')
'''


def database_handler(ret_cmd: bool = False, ret_cfg: bool = False, ret_flag: bool = False, write_flag: bool = False, is_menu: bool = False, switch_button: bool = False, ret_btn: bool = False):
    '''это'''
    def decorator(func: typing.Callable[..., typing.Any]):
        '''просто'''
        async def wrapper(event: SimpleBotEvent) -> str:
            '''пиздец'''
            user = await event.get_user()
            logger.info(
                f'{user.first_name} {user.last_name} ({event.from_id}): {event.text}')
            cursor.execute(C_SQLITE_ADD_COMMAND.format(
                event.from_id, event.text))
            sqlite_connection.commit()
            if is_menu:
                cursor.execute(
                    f'SELECT button FROM menu_buttons_table WHERE user_id={event.from_id};')
                btn = cursor.fetchall()
                if btn == []:
                    cursor.execute(
                        f'INSERT INTO menu_buttons_table VALUES({event.from_id}, "староста");')
                    sqlite_connection.commit()
                else:
                    print(btn)
                    print(btn[0][0])
                    if switch_button:
                        if btn[0][0] == "староста":
                            cursor.execute(
                                'UPDATE menu_buttons_table SET button="свое";')
                            sqlite_connection.commit()
                        else:
                            cursor.execute(
                                'UPDATE menu_buttons_table SET button="староста";')
                            sqlite_connection.commit()
                cursor.execute(
                    C_SQLITE_SELECT_CONFIG_KEYBOARD_BUTTONS.format(event.from_id))
                btn = cursor.fetchall()
                if btn == []:
                    cursor.execute(
                        C_SQLITE_FIRST_ADD_CONFIG_BUTTONS.format(event.from_id))
                    sqlite_connection.commit()
                    if ret_cmd:
                        cursor.execute(
                            f'SELECT button FROM menu_buttons_table WHERE user_id={event.from_id};')
                        btn1 = cursor.fetchall()
                        cursor.execute(
                            C_SQLITE_SELLECT_ALL_COMMANDS.format(event.from_id))
                        return await func(event, cursor.fetchall(), btn1[0][0])
                    else:
                        cursor.execute(
                            f'SELECT button FROM menu_buttons_table WHERE user_id={event.from_id};')
                        btn = cursor.fetchall()
                        return await func(event, btn[0][0])
                else:
                    cursor.execute(
                        C_SQLITE_SET_IS_WRITING_FALSE.format(event.from_id))
                    sqlite_connection.commit()
                    if ret_cmd:
                        cursor.execute(
                            f'SELECT button FROM menu_buttons_table WHERE user_id={event.from_id};')
                        btn1 = cursor.fetchall()
                        cursor.execute(
                            C_SQLITE_SELLECT_ALL_COMMANDS.format(event.from_id))
                        return await func(event, cursor.fetchall(), btn1[0][0])
                    else:
                        cursor.execute(
                            f'SELECT button FROM menu_buttons_table WHERE user_id={event.from_id};')
                        btn = cursor.fetchall()
                        return await func(event, btn[0][0])
            if write_flag:
                cursor.execute(
                    C_SQLITE_SET_IS_WRITING_TRUE.format(event.from_id))
                sqlite_connection.commit()
                cursor.execute(C_SQLITE_SET_BUTTON_TO_WRITE.format(
                    event.payload["choose_cell"], event.from_id))
                return await func(event)
            elif ret_cfg:
                cursor.execute(
                    C_SQLITE_SELECT_CONFIG_KEYBOARD_BUTTONS.format(event.from_id))
                btn = cursor.fetchall()
                if btn == []:
                    cursor.execute(
                        C_SQLITE_FIRST_ADD_CONFIG_BUTTONS.format(event.from_id))
                    sqlite_connection.commit()
                    # Вернет кнопки клавы с пустыми ячейками
                    return await func(event, btn)
                else:
                    cursor.execute(
                        C_SQLITE_SELECT_CONFIG_KEYBOARD_BUTTONS.format(event.from_id))
                    # Вернет кнопки клавы с чем то уже имеющимся
                    return await func(event, cursor.fetchall())
            elif ret_cmd and ret_flag and ret_btn:
                cursor.execute(
                    C_SQLITE_SELLECT_ALL_COMMANDS.format(event.from_id))
                cmd = cursor.fetchall()
                cursor.execute(C_SQLITE_GET_IS_WRITING.format(event.from_id))
                flag = cursor.fetchall()
                cursor.execute(
                    C_SQLITE_GET_BUTTON_TO_WRITE.format(event.from_id))
                btn = cursor.fetchall()
                cursor.execute(
                    f'SELECT button FROM menu_buttons_table WHERE user_id={event.from_id};')
                btn1 = cursor.fetchall()
                return await func(event, cmd, flag, btn, btn1[0][0])
            elif ret_cmd:
                cursor.execute(
                    C_SQLITE_SELLECT_ALL_COMMANDS.format(event.from_id))
                return await func(event, cursor.fetchall())
            elif ret_btn:
                cursor.execute(
                    f'SELECT button FROM menu_buttons_table WHERE user_id={event.from_id};')
                btn1 = cursor.fetchall()
                return await func(event, btn1[0][0])
            else:
                return await func(event)
        return wrapper
    return decorator


def set_button_blueprint(sc_btn: str, cmd: str, event: SimpleBotEvent) -> bool:
    '''Устанавливает шаблон на кнопку в конце алгоритма. Возвращает True в случае если шаблон уже существует,
    False в случае успеха - шаблона нет.'''
    cursor.execute(
        C_SQLITE_SELECT_CONFIG_KEYBOARD_BUTTONS.format(event.from_id))
    btn = cursor.fetchall()[0][0].split(', ')
    if cmd not in btn:
        if sc_btn == 'first_btn':
            cursor.execute(C_SQLITE_UPDATE_CONFIG_BUTTONS.format(
                cmd, btn[1], btn[2], event.from_id))
        elif sc_btn == 'second_btn':
            cursor.execute(C_SQLITE_UPDATE_CONFIG_BUTTONS.format(
                btn[0], cmd, btn[2], event.from_id))
        elif sc_btn == 'third_btn':
            cursor.execute(C_SQLITE_UPDATE_CONFIG_BUTTONS.format(
                btn[0], btn[1], cmd, event.from_id))
        cursor.execute(C_SQLITE_SET_IS_WRITING_FALSE.format(event.from_id))
        sqlite_connection.commit()
        return False
    else:
        cursor.execute(C_SQLITE_SET_IS_WRITING_FALSE.format(event.from_id))
        sqlite_connection.commit()
        return True
