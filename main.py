import vk_api
import sys
import config
import threading
import joke
import sheethandler
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from enum import Enum


listening_thread, controls_thread, command = None, None, None
listening_flag = "isRunning"
vk_session = vk_api.VkApi(token=config.Token)


class Commands(Enum):
    STOP = 0xA


def Instr(msg, event):
    ARGS = msg.split()[1::]
    CMD = msg.split()[0]
    if CMD == '!анекдот' and ARGS == []:
        sender(event.chat_id, joke.get_joke())
    else:
        sender(event.chat_id, 'Invalid argument.')


def sender(id, text):
    vk_session.method('messages.send', {
                      'chat_id': id, 'message': text, 'random_id': 0})


def main():
    global listening_thread, controls_thread, vk_session
    listening_thread = threading.Thread(target=listening, args=(vk_session,))
    controls_thread = threading.Thread(target=controls)
    controls_thread.start()
    listening_thread.start()


def listening(vk_session):
    global command, listening_flag
    longpoll = VkBotLongPoll(vk_session, config.group_id)
    for event in longpoll.listen():
        if command == Commands.STOP.name.lower():
            listening_flag = "isStopped"
            break
        if event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'][0] == "!":
            Instr(event.object.message['text'].lower(), event)


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
