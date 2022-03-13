from vkwave.bots import Keyboard, ButtonColor

START_BUTTONS: list = ['расписание', 'анекдот', 'mi amor?', 'помощь']
START_BUTTONS_PAYLOAD: list = [{"button": "schedule"}, {"button": "joke"}, {"button": "miamor"}, {"button": "help"}]

# Создание экземпляров клавиатуры

START_KB: Keyboard = Keyboard(one_time=False)

for i in range(len(START_BUTTONS)):
    START_KB.add_text_button(text=START_BUTTONS[i].capitalize(), color=ButtonColor.SECONDARY, payload=START_BUTTONS_PAYLOAD[i])
    if i == 0:
        START_KB.add_row()
