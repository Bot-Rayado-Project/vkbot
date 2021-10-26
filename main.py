import vk_api
import sys
import config
import threading
import joke
import sheethandler
#from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from enum import Enum


listening_thread, controls_thread, command = None, None, None
listening_flag = "isRunning"
vk_session = vk_api.VkApi(token=config.Token)

""" def two_factor():
    code = input('Code? ')
    remember_device = True
    return code, remember_device """


class Commands(Enum):
    STOP = 0xA


def sender(id, text):
    vk_session.method('messages.send', {
                      'chat_id': id, 'message': text, 'random_id': 0})


def main():
    global listening_thread, controls_thread, vk_session
    listening_thread = threading.Thread(target=listening, args=(vk_session,))
    controls_thread = threading.Thread(target=controls)
    controls_thread.start()
    listening_thread.start()
    """ Login, Password = config.login, config.password
    vk_session = vk_api.VkApi(login=Login, password=Password,auth_handler=two_factor, app_id=2685278)
    try:
        vk_session.auth(token_only=True)
    except:
        print('Authorization failed.')
    print('Successfully logged in.') """


def listening(vk_session):
    global command, listening_flag
    longpoll = VkBotLongPoll(vk_session, config.group_id)
    for event in longpoll.listen():
        if command == Commands.STOP.name.lower():
            listening_flag = "isStopped"
            break
        if event.type == VkBotEventType.MESSAGE_NEW:
            msg = event.object.message['text'].lower()
            if msg == 'привет':
                sender(event.chat_id, "Hello")
                print(event.chat_id, event.client_info, event.object.items)
            if msg == 'анекдот':
                sender(event.chat_id, joke.get_joke())
                print(event.chat_id, event.client_info, event.object.items)
            if '!расписание' in msg:
                sender(event.chat_id, sheethandler.get_schedule(msg))
                print(event.chat_id, event.client_info, event.object.items)


def controls():
    global listening_thread, command, listening_flag
    print('Control utils are working.')
    while True:
        command = str(input()).lower()
        for commands in Commands:
            if command == commands.name.lower():
                print('Stop command detected. Waiting for event to exit...')
                while True:
                    if listening_flag == "isStopped":
                        controls_flag = "isStopped"
                        exiting(controls_flag)
                        break


def exiting(controls_flag):
    global listening_thread, controls_thread
    if listening_flag == 'isStopped':
        if controls_flag == 'isStopped':
            threading._shutdown()
            sys.exit()


if __name__ == '__main__':
    main()
