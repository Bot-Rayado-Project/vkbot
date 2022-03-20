import sqlite3
import sys
import logging
import requests
from bs4 import BeautifulSoup
from utils.exceptions import keyboard_interrupt
from vkwave.bots import SimpleLongPollBot
from vkwave.bots.storage.storages import Storage
from vkwave.bots.storage.types import Key
from utils.terminal_codes import print_info, print_error
from utils.settings import Settings
import re
import asyncio
from typing import NamedTuple

settings = Settings()
storage = Storage()
default_keys = {}


class GroupInfo(NamedTuple):
    stream: str
    group: str


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
        # Установка стандартных ключей
        get_default_keys()
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


def get_default_keys():
    global default_keys
    responce = requests.get("https://mtuci.ru/time-table/")
    soup = BeautifulSoup(responce.text, 'lxml')
    STREAM_ID: dict = {'бвт': '09.03.01', 'бст': '09.03.02', 'бфи': '02.03.02', 'биб': '10.03.01', 'бэи': '09.03.03', 'бин': '11.03.02'}
    for link in soup.find_all('a'):
        _link = link.get('href')
        try:
            if _link.startswith('/upload/') and ("IT" in _link or "KiIB" in _link or 'SiSS' in _link) and "1-kurs" in _link:
                if STREAM_ID["бвт"] in _link:
                    default_keys["бвт"] = _link[15:18]
                elif STREAM_ID["бст"] in _link:
                    default_keys["бст"] = _link[15:18]
                elif STREAM_ID["бфи"] in _link:
                    default_keys["бфи"] = _link[15:18]
                elif STREAM_ID["биб"] in _link:
                    default_keys["биб"] = _link[15:18]
                elif STREAM_ID["бэи"] in _link:
                    default_keys["бэи"] = _link[15:18]
                elif STREAM_ID["бин"] in _link:
                    default_keys["бин"] = _link[15:18]
                else:
                    pass
        except AttributeError:
            pass
        except KeyError:
            print_error("Ошибка задания стартовых ключей ключей.")
            return None
