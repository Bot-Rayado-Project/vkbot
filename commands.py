import config
import vk_api
import joke
import sheethandler
import russian_roulette

vk_session = vk_api.VkApi(token=config.Token)


def sender(id, text):
    vk_session.method('messages.send', {
                      'user_id': id, 'message': text, 'random_id': 0})


def wrong_arguments_error(request):
    sender(request[0].user_id, "Неверные аргументы.")


def too_much_arguments_error(request):
    sender(request[0].user_id, "Слишком много аргументов.")


def do_roulette(request):
    sender(request[0].user_id, russian_roulette.roulette())


def do_get_joke(request):
    sender(request[0].user_id, joke.get_joke())


def do_get_schedule(request):
    sender(request[0].user_id, sheethandler.get_schedule(
        request[1], request[2]))


def do_get_help(request):
    sender(request[0].user_id, "@crymother @lamabot2000")
