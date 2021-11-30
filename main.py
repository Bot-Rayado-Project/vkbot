import vk_api
import sys
import config
import threading
from commands import *
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from enum import Enum


listening_thread, controls_thread, command = None, None, None
listening_flag = "isRunning"
vk_session = vk_api.VkApi(token=config.Token)


class Commands(Enum):
    STOP = 0xA


def dispatch(msg, event):
    args = msg.split(' ')[1::]
    cmd = msg.split(' ')[0]
    Commands = {
        '!анекдот': [0, '', do_get_joke],
        '!расписание': [2, ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота'], ['бфи2101', 'бфи2102', 'бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106', 'бвт2107', 'бвт2108', 'бcт2101', 'бcт2102', 'бcт2103', 'бcт2104', 'бcт2105', 'бcт2106'], do_get_schedule],
        '!помощь': [0, '', do_get_help]
    }
    request = [event]
    if len(args) != Commands[cmd][0]:
        too_much_arguments_error(request)
    else:
        for i in range(len(args)):
            if args[i] in Commands[cmd][i+1]:
                request += [args[i]]
            else:
                wrong_arguments_error(request)
                break
        Commands[cmd][-1](request)


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
            dispatch(event.object.message['text'].lower(), event)


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
