from vkwave.bots import Keyboard, ButtonColor

CHOOSE_HEADMAN_OR_PERSONAL_BUTTONS: list = ['для группы', 'для себя']
CHOOSE_HEADMAN_OR_PERSONAL_PAYLOAD: list = [{'chp': 'headman'},
                                            {'chp': 'personal'}]
# Создание экземпляров клавиатуры

CHOOSE_HEADMAN_OR_PERSONAL_KB: Keyboard = Keyboard(one_time=False)

for i in range(len(CHOOSE_HEADMAN_OR_PERSONAL_BUTTONS)):
    CHOOSE_HEADMAN_OR_PERSONAL_KB.add_text_button(text=CHOOSE_HEADMAN_OR_PERSONAL_BUTTONS[i].capitalize(
    ), color=ButtonColor.SECONDARY, payload=CHOOSE_HEADMAN_OR_PERSONAL_PAYLOAD[i])
    if i == 1:
        CHOOSE_HEADMAN_OR_PERSONAL_KB.add_row()
        CHOOSE_HEADMAN_OR_PERSONAL_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})
