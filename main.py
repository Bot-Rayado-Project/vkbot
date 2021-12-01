import vk_api
import sys
import config
import threading
import sheethandler
from commands import *
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


listening_thread, controls_thread, command = None, None, None
listening_flag = "isRunning"
vk_session = vk_api.VkApi(token=config.Token)

keyboardStart = VkKeyboard()
keyboardChooseGroup = VkKeyboard()
keyboardChooseDayOfWeek = VkKeyboard()
groups = ['бфи2101', 'бфи2102', 'бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106',
          'бвт2107', 'бвт2108', 'бст2101', 'бст2102', 'бст2103', 'бст2104', 'бст2105', 'бст2106']
daysofweek = ['понедельник', 'вторник',
              'среда', 'четверг', 'пятница', 'суббота']
request = []
keyboardStart.add_button('Расписание', VkKeyboardColor.SECONDARY)
keyboardStart.add_line()
keyboardStart.add_button('Анекдот', VkKeyboardColor.SECONDARY)
keyboardStart.add_button('Рулетка', VkKeyboardColor.SECONDARY)
keyboardStart.add_button('Помощь', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_button('БФИ2101', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_button('БФИ2102', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_button('БВТ2101', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_line()
keyboardChooseGroup.add_button('БВТ2102', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_button('БВТ2103', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_button('БВТ2104', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_line()
keyboardChooseGroup.add_button('БВТ2105', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_button('БВТ2106', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_button('БВТ2107', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_line()
keyboardChooseGroup.add_button('БВТ2108', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_button('БСТ2101', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_button('БСТ2102', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_line()
keyboardChooseGroup.add_button('БСТ2103', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_button('БСТ2104', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_button('БСТ2105', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_line()
keyboardChooseGroup.add_button('БСТ2106', VkKeyboardColor.SECONDARY)
keyboardChooseGroup.add_line()
keyboardChooseGroup.add_button('Меню', VkKeyboardColor.PRIMARY)
keyboardChooseDayOfWeek.add_button('Понедельник', VkKeyboardColor.SECONDARY)
keyboardChooseDayOfWeek.add_button('Вторник', VkKeyboardColor.SECONDARY)
keyboardChooseDayOfWeek.add_button('Среда', VkKeyboardColor.SECONDARY)
keyboardChooseDayOfWeek.add_line()
keyboardChooseDayOfWeek.add_button('Четверг', VkKeyboardColor.SECONDARY)
keyboardChooseDayOfWeek.add_button('Пятница', VkKeyboardColor.SECONDARY)
keyboardChooseDayOfWeek.add_button('Суббота', VkKeyboardColor.SECONDARY)
keyboardChooseDayOfWeek.add_line()
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
