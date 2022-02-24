INFO_CODE = "\033[38;5;255m[\033[38;5;40mINFO\033[38;5;255m]\033[0;0m     \033[38;5;254m{0}\033[0;0m"
WARNING_CODE = "\033[38;5;255m[\033[38;5;226mWARNING\033[38;5;255m]\033[0;0m  \033[38;5;254m{0}\033[0;0m"
ERROR_CODE = "\033[38;5;255m[\033[38;5;196mERROR\033[38;5;255m]\033[0;0m    \033[38;5;196m{0}\033[0;0m"


def print_info(string: str) -> None:
    print(INFO_CODE.format(string))


def print_warning(string: str) -> None:
    print(WARNING_CODE.format(string))


def print_error(string: str) -> None:
    print(ERROR_CODE.format(string))
