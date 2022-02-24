import sqlite3
import sys
import logging
import shutil
from vkwave.bots import SimpleLongPollBot
from utils.terminal_codes import print_info, print_error
from utils.settings import Settings

settings = Settings()


def set_up_connection_with_db(data_base_name: str) -> tuple | None:
    try:
        sqlite_connection: sqlite3.Connection = sqlite3.connect(data_base_name)
        print_info("Successfully connected to database.")
        return sqlite_connection, sqlite_connection.cursor()
    except sqlite3.Error as error:
        print_error("Database connection failure.")
        exit()


def my_except_hook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        print_info("Keyboard interrupt has been detected.")
        print_info("Shutting down.")
        exit()
    else:
        sys.__excepthook__(exctype, value, traceback)


def InitializeComponent() -> SimpleLongPollBot:
    ALLOWED_USER_IDS, API_TOKEN, GROUP_ID = settings.GET_ALL_VARIABLES()
    # Установка логирования
    logging.basicConfig(filename="logs.log", level=logging.ERROR)
    # Установка обработчика ошибок
    sys.excepthook = my_except_hook
    return SimpleLongPollBot(API_TOKEN, GROUP_ID)
