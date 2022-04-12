from vkwave.bots import Keyboard, ButtonColor

SPECIAL_BLUEPRINTS_BUTTONS: list = ['rayadotd', 'rayadotmr', 'fuckmaryamtd', 'fuckmaryamtmr', 'ваня']
SPECIAL_BLUEPRINTS_BUTTONS_PAYLOAD: list = [{"special_blueprint_button": "rayadotd"}, {"special_blueprint_button": "rayadotmr"},
                                            {"special_blueprint_button": "fuckmaryamtd"}, {"special_blueprint_button": "fuckmaryamtmr"},
                                            {"special_blueprint_button": "vanya"}]
# Создание экземпляров клавиатуры

SPECIAL_BLUEPRINTS_KB: Keyboard = Keyboard(one_time=False)

for i in range(1, len(SPECIAL_BLUEPRINTS_BUTTONS) + 1):
    SPECIAL_BLUEPRINTS_KB.add_text_button(text=SPECIAL_BLUEPRINTS_BUTTONS[i - 1], color=ButtonColor.SECONDARY, payload=SPECIAL_BLUEPRINTS_BUTTONS_PAYLOAD[i - 1])
    if i % 3 == 0:
        SPECIAL_BLUEPRINTS_KB.add_row()
    if i == len(SPECIAL_BLUEPRINTS_BUTTONS):
        SPECIAL_BLUEPRINTS_KB.add_row()
        SPECIAL_BLUEPRINTS_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
