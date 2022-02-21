from vkwave.bots import SimpleLongPollBot
import sqlite3


def InitializeComponent(vars: tuple) -> SimpleLongPollBot:
    '''Функция выводит локальные переменные при певой загрузке и в случае успеха возвращает экземпляр бота'''
    match vars:
        case [*allowed_user_ids], [*api_tokens], group_id, ["dev"] | ["rel"] as state:
            print("ALLOWED_USER_IDS: ", *allowed_user_ids)
            print("API_TOKEN: ", *[token[:6] for token in api_tokens])
            print("GROUP_ID: ", *group_id)
            print("STATE: ", *state)
            print("\nEnvironmental Variables successfully loaded.")
            return SimpleLongPollBot(api_tokens, group_id)
        case _:
            print('Wrong argument.')
            exit()


def set_up_connection_with_db() -> tuple:  # Точка входа в программу
    '''Функция устанавливает соединение с БД, возвращает соединение и курсор'''
    try:
        sqlite_connection: sqlite3.Connection = sqlite3.connect('users.db')
        cursor: sqlite3.Cursor = sqlite_connection.cursor()
        print("\nSQLite Data base successfully connected.\n")
        return sqlite_connection, cursor
    except sqlite3.Error as error:
        print("Error connecting to data base", error)
        exit()
