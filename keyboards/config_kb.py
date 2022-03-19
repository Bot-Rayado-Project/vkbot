from vkwave.bots import Keyboard, ButtonColor


def create_config_keyboard(buttons: list[tuple], cells_only: bool = False) -> Keyboard:
    CONFIG_BUTTONS: list = buttons[0][0].split(', ') + ["создать шаблон"] if not cells_only else buttons[0][0].split(', ')
    CONFIG_BUTTONS_PAYLOAD: list = [{"cell": "first_btn"}, {"cell": "second_btn"}, {"cell": "third_btn"}, {"button": "create_blueprint"}
                                    ] if not cells_only else [{"choose_cell": "first_btn"}, {"choose_cell": "second_btn"}, {"choose_cell": "third_btn"}]
    # Создание экземпляров клавиатуры

    CONFIG_KB: Keyboard = Keyboard(one_time=False)

    for i in range(len(CONFIG_BUTTONS)):
        CONFIG_KB.add_text_button(text=CONFIG_BUTTONS[i].capitalize(), color=ButtonColor.SECONDARY, payload=CONFIG_BUTTONS_PAYLOAD[i])
        if i == 2 and not cells_only:
            CONFIG_KB.add_row()
        elif i == 3 or (i == 2 and cells_only):
            CONFIG_KB.add_row()
            CONFIG_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
    return CONFIG_KB
