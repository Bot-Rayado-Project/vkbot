from vkwave.bots import Keyboard, ButtonColor


# Создание экземпляров клавиатуры


def create_menu_keyboard(priority):
    START_BUTTONS: list = ['расписание',
                           'шаблоны расписания', 'анекдот', 'донат', 'помощь', 'приоритет расписания: {0}']
    START_BUTTONS_PAYLOAD: list = [{"button": "schedule"}, {"button": "config"}, {
        "button": "joke"}, {"button": "donate"}, {"button": "help"}, {"button": "priority"}]
    START_KB: Keyboard = Keyboard(one_time=False)

    for i in range(len(START_BUTTONS)):
        if i != 5:
            START_KB.add_text_button(text=START_BUTTONS[i].capitalize(
            ), color=ButtonColor.SECONDARY, payload=START_BUTTONS_PAYLOAD[i])
        if i == 1:
            START_KB.add_row()
        if i == 5:
            START_KB.add_row()
            START_KB.add_text_button(text=START_BUTTONS[i].format(priority).capitalize(
            ), color=ButtonColor.SECONDARY, payload=START_BUTTONS_PAYLOAD[i])
    return START_KB
