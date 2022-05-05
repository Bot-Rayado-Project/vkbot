from vkwave.bots import Keyboard, ButtonColor

CHOOSE_WEEK_HEADMAN_BUTTONS: list = ['четная неделя', 'нечетная неделя']
CHOOSE_WEEK_HEADMAN_PAYLOAD: list = [{"cwh_button": "even"},
                                     {"cwh_button": "odd"}]
# Создание экземпляров клавиатуры

CHOOSE_WEEK_HEADMAN_KB: Keyboard = Keyboard(one_time=False)

for i in range(len(CHOOSE_WEEK_HEADMAN_BUTTONS)):
    CHOOSE_WEEK_HEADMAN_KB.add_text_button(text=CHOOSE_WEEK_HEADMAN_BUTTONS[i].capitalize(
    ), color=ButtonColor.SECONDARY, payload=CHOOSE_WEEK_HEADMAN_PAYLOAD[i])
    if i == 1:
        CHOOSE_WEEK_HEADMAN_KB.add_row()
        CHOOSE_WEEK_HEADMAN_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})

CHOOSE_DAY_OF_WEEK_HEADMAN_BUTTONS: list = [
    'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
CHOOSE_DAY_OF_WEEK_HEADMAN_PAYLOAD: list = [{"cdowh_button": "ponedelnik"}, {"cdowh_button": "vtornik"}, {
    "cdowh_button": "sreda"}, {"cdowh_button": "chetverg"}, {"cdowh_button": "pjatnitsa"}, {"cdowh_button": "subbota"}]
# Создание экземпляров клавиатуры

CHOOSE_DAY_OF_WEEK_HEADMAN_KB: Keyboard = Keyboard(one_time=False)

for i in range(len(CHOOSE_DAY_OF_WEEK_HEADMAN_BUTTONS)):
    CHOOSE_DAY_OF_WEEK_HEADMAN_KB.add_text_button(text=CHOOSE_DAY_OF_WEEK_HEADMAN_BUTTONS[i].capitalize(
    ), color=ButtonColor.SECONDARY, payload=CHOOSE_DAY_OF_WEEK_HEADMAN_PAYLOAD[i])
    if i == 2:
        CHOOSE_DAY_OF_WEEK_HEADMAN_KB.add_row()
    if i == len(CHOOSE_DAY_OF_WEEK_HEADMAN_BUTTONS) - 1:
        CHOOSE_DAY_OF_WEEK_HEADMAN_KB.add_row()
        CHOOSE_DAY_OF_WEEK_HEADMAN_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})


CHOOSE_PAIR_HEADMAN_BUTTONS: list = ['1 пара', '2 пара', '3 пара',
                                     '4 пара', '5 пара', 'общ. аннотация', 'сбросить все изменения']
CHOOSE_PAIR_HEADMAN_PAYLOAD: list = [{"cph_button": "first"}, {"cph_button": "second"}, {"cph_button": "third"}, {
    "cph_button": "fourth"}, {"cph_button": "fifth"}, {"cph_button": "forall"}, {"cph_button": "resetall"}]
# Создание экземпляров клавиатуры

CHOOSE_PAIR_HEADMAN_KB: Keyboard = Keyboard(one_time=False)

for i in range(len(CHOOSE_PAIR_HEADMAN_BUTTONS)):
    CHOOSE_PAIR_HEADMAN_KB.add_text_button(text=CHOOSE_PAIR_HEADMAN_BUTTONS[i].capitalize(
    ), color=ButtonColor.SECONDARY, payload=CHOOSE_PAIR_HEADMAN_PAYLOAD[i])
    if i == 2:
        CHOOSE_PAIR_HEADMAN_KB.add_row()
    if i == 5:
        CHOOSE_PAIR_HEADMAN_KB.add_row()
        CHOOSE_PAIR_HEADMAN_KB.add_text_button(text=CHOOSE_PAIR_HEADMAN_BUTTONS[i + 1].capitalize(
        ), color=ButtonColor.NEGATIVE, payload=CHOOSE_PAIR_HEADMAN_PAYLOAD[i + 1])
        CHOOSE_PAIR_HEADMAN_KB.add_row()
        CHOOSE_PAIR_HEADMAN_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})
        break

CHOOSE_MOVE_HEADMAN_BUTTONS: list = ['перезаписать(Записать)', 'удалить']
CHOOSE_MOVE_HEADMAN_PAYLOAD: list = [
    {"cmh_button": "rewrite"}, {"cmh_button": "remove"}]
# Создание экземпляров клавиатуры

CHOOSE_MOVE_HEADMAN_KB: Keyboard = Keyboard(one_time=True)

for i in range(len(CHOOSE_MOVE_HEADMAN_BUTTONS)):
    CHOOSE_MOVE_HEADMAN_KB.add_text_button(text=CHOOSE_MOVE_HEADMAN_BUTTONS[i].capitalize(
    ), color=ButtonColor.SECONDARY, payload=CHOOSE_MOVE_HEADMAN_PAYLOAD[i])
    if i == 2:
        CHOOSE_MOVE_HEADMAN_KB.add_row()
    if i == len(CHOOSE_MOVE_HEADMAN_BUTTONS) - 1:
        CHOOSE_MOVE_HEADMAN_KB.add_row()
        CHOOSE_MOVE_HEADMAN_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})
