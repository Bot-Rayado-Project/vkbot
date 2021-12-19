from vk_api import keyboard
import config
import vk_api
from typing import Optional, Union
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token=config.Token)
is_chosen = False


def sender(id, text, keyboard):
    vk_session.method('messages.send', {
        'user_id': id, 'message': text, 'random_id': 0, 'keyboard': keyboard.get_keyboard()})


def do_schedule_choose_group(event, keyboard):
    global is_chosen
    is_chosen = True
    sender(event.user_id, "Выберите группу.", keyboard)
