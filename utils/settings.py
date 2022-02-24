import os
from utils.terminal_codes import print_info, print_error, print_warning


class Settings():
    def __init__(self) -> None:
        print_info("Importing environment variables")
        error = False
        counter = 0
        try:
            self.__ALLOWED_USER_IDS = os.getenv('ALLOWED_USER_IDS').split()
            print_info("ALLOWED_USER_IDS: " +
                       ", ".join(self.__ALLOWED_USER_IDS))
        except:
            print_error("ALLOWED_USER_IDS is not given.")
            counter += 1
            error = True
        try:
            self.__API_TOKEN = os.getenv('API_TOKEN').split()
            if len(self.__API_TOKEN) == 1:
                print_warning(
                    "Only 1 API_TOKEN is given. For better performance use 3 or more.")
            self.__API_TOKEN_OUTPUT = []
            for i in self.__API_TOKEN:
                self.__API_TOKEN_OUTPUT += [i[:8]+"..."]
            print_info("API_TOKENS: " +
                       ", ".join(self.__API_TOKEN_OUTPUT))
        except:
            print_error("API_TOKENS is not given.")
            counter += 1
            error = True
        try:
            self.__GROUP_ID = os.getenv('GROUP_ID').split()
            print_info("GROUP_ID: " +
                       ", ".join(self.__GROUP_ID))
        except:
            print_error("GROUP_ID is not given.")
            counter += 1
            error = True
        if error:
            print_error(f"Import error. {counter} arguments are not given.")
            exit()
        else:
            print_info("Import complete.")

    def GET_ALLOWED_USER_IDS(self) -> list:
        return self.__ALLOWED_USER_IDS

    def GET_API_TOKEN(self) -> str:
        return self.__API_TOKEN

    def GET_GROUP_ID(self) -> str:
        return self.__GROUP_ID

    def GET_ALL_VARIABLES(self) -> tuple:
        return self.__ALLOWED_USER_IDS, self.__API_TOKEN, self.__GROUP_ID

    def SET_ALLOWED_USER_IDS(self, value) -> None:
        self.__ALLOWED_USER_IDS = value

    def SET_API_TOKEN(self, value) -> None:
        self.__API_TOKEN = value

    def SET_GROUP_ID(self, value) -> None:
        self.__GROUP_ID = value
