import re
import config
import vk_api
import joke
import sheethandler

vk_session = vk_api.VkApi(token=config.Token)


def sender(id, text):
    vk_session.method('messages.send', {
                      'chat_id': id, 'message': text, 'random_id': 0})


def do_get_joke(request):
    sender(request[0].chat_id, joke.get_joke())


def do_get_schedule(request):
    sender(request[0].chat_id, sheethandler.get_schedule(request[1]))


def do_get_help(request):
    sender(request[0].chat_id, "@crymother @lamabot2000")
