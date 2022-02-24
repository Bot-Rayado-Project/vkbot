from vkwave.bots import Keyboard, ButtonColor

START_BUTTONS: list = ['расписание', 'анекдот', 'mi amor?', 'помощь']

# Создание экземпляров клавиатуры

START_KB: Keyboard = Keyboard(one_time=False)

for i in range(len(START_BUTTONS)):
    START_KB.add_text_button(
        START_BUTTONS[i].capitalize(), ButtonColor.SECONDARY)
    if i == 0:
        START_KB.add_row()
