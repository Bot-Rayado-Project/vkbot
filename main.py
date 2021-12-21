import vk_api
import sys
import config
import threading
from commands import *
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import asyncio


listening_thread, controls_thread, command = None, None, None
listening_flag = "isRunning"
request = []
vk_session = vk_api.VkApi(token=config.Token)


async def InitializeComponent():

    global keyboardStart, keyboardChooseGroup, keyboardChooseDayOfWeek, start, groups, daysofweek, commands
    # Создание экземпляров клавиатуры

    keyboardStart: VkKeyboard = VkKeyboard()
    keyboardChooseGroup: VkKeyboard = VkKeyboard()
    keyboardChooseDayOfWeek: VkKeyboard = VkKeyboard()

    # Названия кнопок
    start: list = ['Расписание', 'Анекдот', 'Рулетка', 'Помощь']
    groups: list = ['бфи2101', 'бфи2102', 'бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106',
                    'бвт2107', 'бвт2108', 'бст2101', 'бст2102', 'бст2103', 'бст2104', 'бст2105', 'бст2106']
    daysofweek: list = ['понедельник', 'вторник',
                        'среда', 'четверг', 'пятница', 'суббота']
    # Создание и заполнение списка команд
    commands_labels: list = ['привет', 'меню', 'начать',
                             'начало', 'анекдот', 'помощь', 'рулетка', 'расписание']
    commands_functions: list = [[do_start, keyboardStart], [do_start, keyboardStart], [do_start, keyboardStart], [do_start, keyboardStart], [
        do_joke, keyboardStart], [do_help, keyboardStart], [do_roulette, keyboardStart], [do_schedule_choose_group, keyboardChooseGroup]]
    for i in range(len(groups)):
        commands_labels += [groups[i]]
        commands_functions += [[do_schedule_choose_day_of_week,
                                keyboardChooseDayOfWeek]]
    for i in range(len(daysofweek)):
        commands_labels += [daysofweek[i]]
        commands_functions += [[do_schedule_get_schedule,
                                keyboardStart]]
    commands: dict = dict(zip(commands_labels, commands_functions))

    # Генерация кнопок
    for i in range(len(start)):
        keyboardStart.add_button(start[i], VkKeyboardColor.SECONDARY)
        if i == 0:
            keyboardStart.add_line()
    for i in range(1, len(groups)+1):
        keyboardChooseGroup.add_button(
            groups[i-1].upper(), VkKeyboardColor.SECONDARY)
        if i % 3 == 0:
            keyboardChooseGroup.add_line()
        if i == len(groups):
            keyboardChooseGroup.add_line()
            keyboardChooseGroup.add_button('Меню', VkKeyboardColor.PRIMARY)
    for i in range(1, len(daysofweek)+1):
        keyboardChooseDayOfWeek.add_button(
            daysofweek[i-1].capitalize(), VkKeyboardColor.SECONDARY)
        if i % 3 == 0:
            keyboardChooseDayOfWeek.add_line()
        if i == len(daysofweek):
            keyboardChooseDayOfWeek.add_button('Меню', VkKeyboardColor.PRIMARY)


def dispatch(msg, event):
    global keyboardStart, keyboardChooseGroup, keyboardChooseDayOfWeek, groups, daysofweek, request
    if 'msg' in list(commands.keys()):
        commands[msg](event, keyboard_type)
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


async def main():
    Initialize_task = asyncio.create_task(InitializeComponent())
    listening_thread.start()
    global listening_thread, controls_thread, vk_session
    listening_thread = threading.Thread(target=listening, args=(vk_session,))


async def listening(vk_session):
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.to_me and event.type == VkEventType.MESSAGE_NEW:
            print(event.user_id)
            dispatch(event.text.lower(), event)


if __name__ == '__main__':
    asyncio.run(main())
