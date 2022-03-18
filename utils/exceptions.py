import sys

from utils.terminal_codes import print_info


class SearchException(Exception):
    pass


def keyboard_interrupt(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        print_info("Keyboard interrupt has been detected.")
        print_info("Shutting down.")
        exit()
    else:
        sys.__excepthook__(exctype, value, traceback)
