from vkwave.bots import SimpleLongPollBot
from utils.settings import settings
import sqlite3


def get_env_vars() -> None:
    '''Функция выводит локальные переменные при певой загрузке'''
    vars = tuple(settings.GET_ALLOWED_USER_IDS(), settings.GET_API_TOKEN(
    ), settings.GET_GROUP_ID(), settings.GET_STATE())


def set_up_connection_with_db() -> tuple:  # Точка входа в программу
    '''Функция устанавливает соединение с БД, возвращает соединение и курсор'''
    try:
        sqlite_connection: sqlite3.Connection = sqlite3.connect('users.db')
        cursor: sqlite3.Cursor = sqlite_connection.cursor()
        print("\nБаза данных успешно подключена к SQLite\n")
        return sqlite_connection, cursor
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQlite", error)
        exit()


def set_bot(API_TOKEN: str, GROUP_ID: str) -> SimpleLongPollBot:
    '''Создает экземпляр бота'''
    return SimpleLongPollBot(tokens=API_TOKEN, group_id=GROUP_ID)
