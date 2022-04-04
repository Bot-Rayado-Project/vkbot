import sys
import logging
from utils.exceptions import keyboard_interrupt
from vkwave.bots import SimpleLongPollBot
from utils.terminal_codes import print_info, print_warning, set_stdout_to_log_file
import utils.terminal_codes as term
from utils.settings import settings


class InitializeComponent:
    def __init__(self, routers_list: list, token: str = None, group_id: str = None) -> None:
        '''Импортирует все нужное для запуска бота и инициализирует его класс в ручном либо автоматическом режиме.
        Для переход в ручной режим введите токены и id группы в поля token, group_id'''
        print_info("Waiting for application startup...")
        if settings.GET_STATE() == ['DEBUG']:
            print_warning("Debug state detected. Stdout is set to terminal. Proceed with caution.")
        else:
            term.INFO_CODE = "[INFO]    {0}"
            term.WARNING_CODE = "[WARNING]  {0}"
            term.ERROR_CODE = "[ERROR]    {0}"
            term.INFO_CODE_USER_MSG = "({0}) {1} {2} (ID: {3}): {4}"
            set_stdout_to_log_file()
            pass
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
