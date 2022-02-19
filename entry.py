from vkwave.bots import SimpleLongPollBot
from utils.constants import Settings
import sqlite3


def set_up_connection_with_db() -> tuple:  # Точка входа в программу
    '''Функция устанавливает соединение с БД, возвращает соединение и курсор'''
    try:
        sqlite_connection = sqlite3.connect('users.db')
        cursor = sqlite_connection.cursor()
        print("\nБаза данных успешно подключена к SQLite")
        return sqlite_connection, cursor
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQlite", error)
        exit()


def set_bot(API_TOKEN: str, GROUP_ID: str) -> SimpleLongPollBot:
    '''Создает экземпляр бота'''
    return SimpleLongPollBot(tokens=API_TOKEN, group_id=GROUP_ID)
