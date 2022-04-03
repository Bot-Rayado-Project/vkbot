import sys


file = None
INFO_CODE = "\033[38;5;255m[\033[38;5;40mINFO\033[38;5;255m]\033[0;0m     \033[38;5;254m{0}\033[0;0m"
WARNING_CODE = "\033[38;5;255m[\033[38;5;226mWARNING\033[38;5;255m]\033[0;0m  \033[38;5;254m{0}\033[0;0m"
ERROR_CODE = "\033[38;5;255m[\033[38;5;196mERROR\033[38;5;255m]\033[0;0m    \033[38;5;196m{0}\033[0;0m"
INFO_CODE_USER_MSG = "({0}) \033[38;5;80m{1} {2} \033[38;5;254m(ID: {3}): \033[38;5;80m{4}\033[0;0m"


def print_info(string: str) -> None:
    print(INFO_CODE.format(string))


def print_warning(string: str) -> None:
    print(WARNING_CODE.format(string))


def print_error(string: str) -> None:
    print(ERROR_CODE.format(string))


def set_stdout_to_log_file() -> None:
    global file
    file = open('info.log', 'w', encoding='UTF-8')
    sys.stdout = file


def close_file() -> None:
    global file
    file.close()
