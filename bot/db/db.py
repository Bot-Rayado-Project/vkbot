from bot.constants import DBHOST, DBNAME, DBPASSWORD, DBUSER
from bot.logger import get_logger
import asyncpg
import asyncio
import traceback
import typing

logger = get_logger(__name__)


async def connect_create_if_not_exists(user, database):
    try:
        conn = await asyncpg.connect(user=user, database=database)
    except asyncpg.InvalidCatalogNameError:
        # Database does not exist, create it.
        sys_conn = await asyncpg.connect(
            database='',
            user='postgres'
        )
        await sys_conn.execute(
            f'CREATE DATABASE "{database}" OWNER "{user}"'
        )
        await sys_conn.close()

        # Connect to the newly created database.
        conn = await asyncpg.connect(user=user, database=database)

    return conn


async def db_connect(user: str, password: str, name: str, host: str) -> asyncpg.Connection | None:
    '''Выполняет подключение к базе данных. В случае ошибки подключение выполняет еще одну попытку. Всего попыток 5.
    В случае последней неудачи возвращает None, иначе - asyncpg.Connection'''
    tries = 5
    while True:
        try:
            connection = await asyncpg.connect(user=user, password=password, database=name, host=host)
            if tries != 5:
                logger.info(
                    f'Successfully connected to database {name} to host {host} with user {user}')
            return connection
        except asyncpg.InvalidCatalogNameError as i:
            logger.info("Database does not exist, create it.")
            sys_conn = await asyncpg.connect(
                database='template1',
                user='postgres',
                host=host,
                password=password
            )
            await sys_conn.execute(
                f'CREATE DATABASE "{name}" OWNER "{user}"'
            )
            await sys_conn.close()
            connection: asyncpg.Connection = await asyncpg.connect(user=user, password=password, database=name, host=host)
            logger.info("Seeding database...")
            commands = ["CREATE TABLE IF NOT EXISTS users(user_id integer NOT NULL,date timestamp NOT NULL,command text NOT NULL);",
                        "CREATE TABLE IF NOT EXISTS menu_buttons_table(user_id INT NOT NULL, button TEXT NOT NULL);",
                        "CREATE TABLE IF NOT EXISTS config(user_id integer NOT NULL,keyboard_buttons text NOT NULL,is_writing boolean NOT NULL,button_to_write text NOT NULL);",
                        "CREATE TABLE IF NOT EXISTS accesses(user_id integer NOT NULL,full_admin_panel BOOLEAN NOT NULL, semi_admin_panel BOOLEAN NOT NULL,headman_panel BOOLEAN NOT NULL,stream_group TEXT);",
                        "INSERT INTO accesses VALUES(255632502, False, False, True, 'бвт2101');",
                        "INSERT INTO accesses VALUES(228506651, False, False, True, 'бвт2102');",
                        "INSERT INTO accesses VALUES(355129349, False, False, True, 'бвт2103');",
                        "INSERT INTO accesses VALUES(116008591, False, False, True, 'бвт2104');",
                        "INSERT INTO accesses VALUES(237079184, False, False, True, 'бвт2105');",
                        "INSERT INTO accesses VALUES(210481885, True, True, True, 'бвт2103');",
                        "INSERT INTO accesses VALUES(162956112, True, True, True, 'бвт2103');",
                        "INSERT INTO accesses VALUES(213304238, False, True, False, NULL);",
                        "INSERT INTO accesses VALUES(528860991, False, True, False, NULL);",
                        "INSERT INTO accesses VALUES(278233695, False, True, False, NULL);"
                        ]
            for comd in commands:
                logger.info("Executing: " + comd)
                await connection.execute(comd)
            return connection
        except Exception as e:
            tries -= 1
            logger.info(
                f"Error connecting to database ({e}). Tries left: {tries}")
            await asyncio.sleep(0.33)
            if tries == 0:
                logger.error(
                    f"Error connecting to database: {traceback.format_exc()}")
                return None


async def db_connect_env_variables() -> asyncpg.Connection | None:
    '''Выполняет подключение к БД, с использованием переменных окружения'''
    connection = await db_connect(DBUSER, DBPASSWORD, DBNAME, DBHOST)
    return connection


async def db_close(connection: asyncpg.Connection) -> None:
    '''Закрывает подключение с БД'''
    try:
        await connection.close()
    except Exception as e:
        logger.error(
            f"Error closing database connection ({e}): {traceback.format_exc()}")
        await asyncio.sleep(0.33)


async def db_get_priority_button(user_id: int, connection: typing.Optional[asyncpg.Connection] = None) -> str:
    '''Забирает кнопку приоритета из меню. Если записи в бд нет, то запsисывает на старосту'''
    connection = connection or await db_connect_env_variables()
    if connection is None:
        logger.error('Connection is None')
        return 'староста'
    database_responce = await connection.fetchrow(f'SELECT button FROM menu_buttons_table WHERE user_id={user_id};')
    if database_responce is None:
        await connection.fetch(f"INSERT INTO menu_buttons_table VALUES({user_id}, 'староста');")
        await db_close(connection)
        return 'староста'
    await db_close(connection)
    return dict(database_responce)['button']


async def db_change_priority_button(user_id: int, connection: typing.Optional[asyncpg.Connection] = None) -> str:
    '''Меняет кнопку приоритета из меню на противоположную'''
    connection = connection or await db_connect_env_variables()
    button = await db_get_priority_button(user_id)
    if button == 'староста':
        await connection.fetch(f"UPDATE menu_buttons_table SET button='свое' where user_id={user_id};")
    else:
        await connection.fetch(f"UPDATE menu_buttons_table SET button='староста' where user_id={user_id};")
    await db_close(connection)
    return button


async def db_get_access_to_headman_edit(user_id: int, connection: typing.Optional[asyncpg.Connection] = None) -> str:
    '''Забирает права старосты у человека'''
    connection = connection or await db_connect_env_variables()
    if connection is None:
        logger.error('Connection is None')
        return False
    database_responce = await connection.fetchrow(f'SELECT headman_panel FROM accesses WHERE user_id={user_id};')
    if database_responce is None:
        await db_close(connection)
        return False
    await db_close(connection)
    return dict(database_responce)['headman_panel']


async def db_get_headman_group(user_id: int, connection: typing.Optional[asyncpg.Connection] = None) -> str:
    '''Забирает права старосты у человека'''
    connection = connection or await db_connect_env_variables()
    if connection is None:
        logger.error('Connection is None')
        return ''
    database_responce = await connection.fetchrow(f'SELECT stream_group FROM accesses WHERE user_id={user_id};')
    if database_responce is None:
        await db_close(connection)
        return ''
    await db_close(connection)
    return dict(database_responce)['stream_group']


async def db_get_blueprints_buttons(user_id: int, connection: typing.Optional[asyncpg.Connection] = None) -> tuple:
    '''Забирает кнопки шаблонов у человека'''
    connection = connection or await db_connect_env_variables()
    if connection is None:
        logger.error('Connection is None')
        return ('Пустая ячейка', 'Пустая ячейка', 'Пустая ячейка')
    database_responce = await connection.fetchrow(f'SELECT keyboard_buttons FROM config WHERE user_id={user_id};')
    if database_responce is None:
        logger.info(f'{user_id} - отсутствуют шаблоны.')
        await connection.fetch(f"INSERT INTO config VALUES({user_id}, 'Пустая ячейка, Пустая ячейка, Пустая ячейка', False, 'first_btn');")
        await db_close(connection)
        return ('Пустая ячейка', 'Пустая ячейка', 'Пустая ячейка')
    await db_close(connection)
    buttons = dict(database_responce)['keyboard_buttons'].split(', ')
    logger.info(f'{user_id} - {tuple(buttons)}')
    return tuple(buttons)


async def db_set_blueprints_buttons(user_id: int, blueprint: str, button: str, connection: typing.Optional[asyncpg.Connection] = None) -> bool | None:
    '''Ставит кнопки шаблонов у человека'''
    connection = connection or await db_connect_env_variables()
    if connection is None:
        logger.error('Connection is None')
        return None
    database_responce = await connection.fetchrow(f'SELECT keyboard_buttons FROM config WHERE user_id={user_id};')
    if database_responce is None:
        logger.info(f'{user_id} - отсутствуют шаблоны.')
        await connection.fetch(f"INSERT INTO config VALUES({user_id}, 'Пустая ячейка, Пустая ячейка, Пустая ячейка', False, 'first_btn');")
    database_responce = await connection.fetchrow(f'SELECT keyboard_buttons FROM config WHERE user_id={user_id};')
    buttons = dict(database_responce)['keyboard_buttons'].split(', ')
    if blueprint == buttons[0] or blueprint == buttons[1] or blueprint == buttons[2]:
        return False
    if button == 'first_button':
        buttons[0] = blueprint
    elif button == 'second_button':
        buttons[1] = blueprint
    else:
        buttons[2] = blueprint
    _buttons = buttons[0] + ', ' + buttons[1] + ', ' + buttons[2]
    logger.info(f'{user_id} - {tuple(buttons)} - {_buttons}')
    await connection.fetch(f"UPDATE config SET keyboard_buttons='{_buttons}' where user_id={user_id};")
    await db_close(connection)
    return True
