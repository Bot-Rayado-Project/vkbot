import vk_api
import sys
import config
import threading
from commands import *
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


listening_thread, controls_thread, command = None, None, None
listening_flag = "isRunning"
request = []
vk_session = vk_api.VkApi(token=config.Token)


def InitializeComponent():

    global keyboardStart, keyboardChooseGroup, keyboardChooseDayOfWeek, start, groups, daysofweek
    # Создание экземпляров клавиатуры

    keyboardStart = VkKeyboard()
    keyboardChooseGroup = VkKeyboard()
    keyboardChooseDayOfWeek = VkKeyboard()

    # Названия кнопок
    start = ['Расписание', 'Анекдот', 'Рулетка', 'Помощь']
    groups = ['бфи2101', 'бфи2102', 'бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106',
              'бвт2107', 'бвт2108', 'бст2101', 'бст2102', 'бст2103', 'бст2104', 'бст2105', 'бст2106']
    daysofweek = ['понедельник', 'вторник',
                  'среда', 'четверг', 'пятница', 'суббота']

    # Добавление кнопок
    for i in range(len(start)):
        keyboardStart.add_button(start[i], VkKeyboardColor.SECONDARY)
        if i == 0:
            keyboardStart.add_line()
    for i in range(1, len(groups)+1):
        keyboardChooseGroup.add_button(
            groups[i-1].upper(), VkKeyboardColor.SECONDARY)
        if i % 3 == 0:
            keyboardChooseGroup.add_line()
        elif i == len(groups):
            keyboardChooseGroup.add_line()
            keyboardChooseGroup.add_button('Меню', VkKeyboardColor.PRIMARY)
    for i in range(1, len(daysofweek)+1):
        keyboardChooseGroup.add_button(
            daysofweek[i-1].capitalize(), VkKeyboardColor.SECONDARY)
        if i % 3 == 0:
            keyboardChooseGroup.add_line()
        elif i == len(daysofweek):
            keyboardChooseGroup.add_line()
            keyboardChooseDayOfWeek.add_button('Меню', VkKeyboardColor.PRIMARY)


def dispatch(msg, event):
    global keyboardStart, keyboardChooseGroup, keyboardChooseDayOfWeek, groups, daysofweek, request
    if msg == "начать" or msg == "меню":
        sender(event.user_id, 'Выберите команду.', keyboardStart)
        request = []
    if msg == "анекдот":
        sender(event.user_id, joke.get_joke(), keyboardStart)
    if msg == "рулетка":
        sender(event.user_id, russian_roulette.roulette(), keyboardStart)
    if msg == "помощь":
        sender(event.user_id,
               "Иван - vk.com/crymother\nАлександр - vk.com/lamabot2000", keyboardStart)
    if msg == "расписание":
        choose_group(event, keyboardChooseGroup)
    if msg in groups:
        request += [msg]
        choose_dayofweek(event, keyboardChooseDayOfWeek)
    if msg in daysofweek:
        request += [msg]
        do_get_schedule(event, request, keyboardStart)
        request = []


def main():
    InitializeComponent()
    global listening_thread, controls_thread, vk_session
    listening_thread = threading.Thread(target=listening, args=(vk_session,))
    controls_thread = threading.Thread(target=controls)
    controls_thread.start()
    listening_thread.start()


def listening(vk_session):
    global command, listening_flag
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.to_me:
            if command == 'stop':
                listening_flag = "isStopped"
                break
            if event.type == VkEventType.MESSAGE_NEW:
                dispatch(event.text.lower(), event)


def controls():
    global listening_thread, command, listening_flag
    print('Control utils are working.')
    while True:
        command = str(input()).lower()
        if command == 'stop':
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
