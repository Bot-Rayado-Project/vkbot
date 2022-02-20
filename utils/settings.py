import os
from types import NoneType


class Settings():
    def __init__(self) -> None:
        try:
            self.__ALLOWED_USER_IDS = os.getenv('ALLOWED_USER_IDS').split()
            self.__API_TOKEN = os.getenv('API_TOKEN').split()
            self.__GROUP_ID = os.getenv('GROUP_ID').split()
            self.__STATE = os.getenv('STATE').split()
        except:
            print("Empty variable error.\n")
            print("ALLOWED_USER_IDS: ", os.getenv('ALLOWED_USER_IDS'))
            print("API_TOKEN: ", os.getenv('API_TOKEN'))
            print("GROUP_ID: ", os.getenv('GROUP_ID'))
            print("STATE: ", os.getenv('STATE'))

    def GET_ALLOWED_USER_IDS(self) -> list:
        return self.__ALLOWED_USER_IDS

    def GET_API_TOKEN(self) -> str:
        return self.__API_TOKEN

    def GET_GROUP_ID(self) -> str:
        return self.__GROUP_ID

    def GET_STATE(self) -> str:
        return self.__STATE

    def GET_ALL_VARIABLES(self) -> tuple:
        '''Возвращает кортеж из всех переменных окружения. ALLOWED_USER_IDS, API_TOKEN, GROUP_ID, STATE'''
        return self.__ALLOWED_USER_IDS, self.__API_TOKEN, self.__GROUP_ID, self.__STATE

    def SET_ALLOWED_USER_IDS(self, value) -> None:
        self.__ALLOWED_USER_IDS = value

    def SET_API_TOKEN(self, value) -> None:
        self.__API_TOKEN = value

    def SET_GROUP_ID(self, value) -> None:
        self.__GROUP_ID = value

    def SET_STATE(self, value) -> None:
        self.__STATE = value


settings = Settings()
