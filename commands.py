import config
import vk_api
import joke
import sheethandler
import russian_roulette
import main
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token=config.Token)


def sender(id, text, keyboard):
    vk_session.method('messages.send', {
        'user_id': id, 'message': text, 'random_id': 0, 'keyboard': keyboard.get_keyboard()})


def wrong_arguments_error(request, request_sec):
    sender(request[0].user_id, "Неверные аргументы.")


def too_much_arguments_error(request, request_sec):
    sender(request[0].user_id, "Слишком много аргументов.")


def do_roulette(request, request_sec):
    sender(request[0].user_id, russian_roulette.roulette(), request[1])


def do_get_joke(request, request_sec):
    sender(request[0].user_id, joke.get_joke(), request[1])


def do_choose_group(request, request_sec):
    sender(request_sec[0].user_id, "Выберите группу.", request_sec[1])


def do_get_schedule(event, request, keyboard):
    sender(event.user_id, sheethandler.get_schedule(
        request[1], request[0]), keyboard)


def do_get_help(request, request_sec):
    sender(request[0].user_id,
           "Иван - vk.com/crymother\nАлександр - vk.com/lamabot2000", request[1])


def choose_group(event, keyboard):
    sender(event.user_id, "Выберите группу.", keyboard)


def choose_dayofweek(event, keyboard):
    sender(event.user_id, "Выберите день недели.", keyboard)
