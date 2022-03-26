from vkwave.bots import Keyboard, ButtonColor

ADMIN_BUTTONS: list = ['SP Шаблоны', 'Логи', 'ID с доступом', 'Забрать доступ', 'Дать доступ']
ADMIN_BUTTONS_PAYLOAD: list = [{"admin_button": "special_blueprints"}, {"admin_button": "logs"}, {"admin_button": "allowed_list"},
                               {"admin_button": "remove_allowed"}, {"admin_button": "add_allowed"}]
# Создание экземпляров клавиатуры

ADMIN_KB: Keyboard = Keyboard(one_time=False)

for i in range(1, len(ADMIN_BUTTONS) + 1):
    ADMIN_KB.add_text_button(text=ADMIN_BUTTONS[i - 1], color=ButtonColor.SECONDARY, payload=ADMIN_BUTTONS_PAYLOAD[i - 1])
    if i % 3 == 0:
        ADMIN_KB.add_row()
    if i == len(ADMIN_BUTTONS):
        ADMIN_KB.add_row()
        ADMIN_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
