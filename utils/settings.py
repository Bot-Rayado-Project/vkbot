import os


class Settings():
    def __init__(self) -> None:
        self.__ALLOWED_USER_IDS = os.getenv('ALLOWED_USER_IDS')
        self.__API_TOKEN = os.getenv('API_TOKEN')
        self.__GROUP_ID = os.getenv('GROUP_ID')
        self.__STATE = os.getenv('STATE')

    def GET_ALLOWED_USER_IDS(self) -> list:
        return self.__ALLOWED_USER_IDS

    def GET_API_TOKEN(self) -> str:
        return self.__API_TOKEN

    def GET_GROUP_ID(self) -> str:
        return self.__GROUP_ID

    def GET_STATE(self) -> str:
        return self.__STATE

    def SET_ALLOWED_USER_IDS(self, value) -> None:
        self.__ALLOWED_USER_IDS = value

    def SET_API_TOKEN(self, value) -> None:
        self.__API_TOKEN = value

    def SET_GROUP_ID(self, value) -> None:
        self.__GROUP_ID = value

    def SET_STATE(self, value) -> None:
        self.__STATE = value


settings = Settings()
