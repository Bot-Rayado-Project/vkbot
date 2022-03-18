import sqlite3
import sys
import logging
from utils.exceptions import keyboard_interrupt
from vkwave.bots import SimpleLongPollBot
from utils.terminal_codes import print_info, print_error
from utils.settings import Settings

settings = Settings()


class InitializeComponent:
    def __init__(self, routers_list: list, token: str = None, group_id: str = None) -> None:
        '''Импортирует все нужное для запуска бота и инициализирует его класс в ручном либо автоматическом режиме.
        Для переход в ручной режим введите токены и id группы в поля token, group_id'''
        print_info("Waiting for application startup...")
        if token == None and group_id == None:
            print_info("Creating bot instance in automatic mode...")
            self.bot = SimpleLongPollBot(settings.GET_API_TOKEN(), settings.GET_GROUP_ID())
            for router in routers_list:
                self.bot.dispatcher.add_router(router)
        else:
            print_info("Creating bot instance in manual mode...")
            self.bot = SimpleLongPollBot(token, group_id)
            for router in routers_list:
                self.bot.dispatcher.add_router(router)
        # Установка обработчка прерывания с клавиатуры
        self.__set_keyboard_interrupt()
        # Установка логирования
        self.__set_logging()
        print_info("Application startup complete.")
        print_info("Started listening for messages...")

    def run(self) -> None:
        self.bot.run_forever()

    def __set_keyboard_interrupt(self) -> None:
        sys.excepthook = keyboard_interrupt

    def __set_logging(self) -> None:
        logging.basicConfig(filename="errors.log", level=logging.ERROR)


def set_up_connection_with_db(data_base_name: str) -> tuple | None:
    try:
        sqlite_connection: sqlite3.Connection = sqlite3.connect(data_base_name)
        print_info("Successfully connected to database.")
        return sqlite_connection, sqlite_connection.cursor()
    except sqlite3.Error:
        print_error("Database connection failure.")
        exit()
