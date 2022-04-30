from vkwave.bots import Keyboard, ButtonColor
CHOOSE_HEADMAN_OR_PERSONAL_BUTTONS: list = ['для группы', 'для себя']
CHOOSE_HEADMAN_OR_PERSONAL_PAYLOAD: list = [{'chp': 'headman'}, {'chp': 'personal'}]
# Создание экземпляров клавиатуры

CHOOSE_HEADMAN_OR_PERSONAL_KB: Keyboard = Keyboard(one_time=False)

for i in range(len(CHOOSE_HEADMAN_OR_PERSONAL_BUTTONS)):
    CHOOSE_HEADMAN_OR_PERSONAL_KB.add_text_button(text=CHOOSE_HEADMAN_OR_PERSONAL_BUTTONS[i].capitalize(), color=ButtonColor.SECONDARY, payload=CHOOSE_HEADMAN_OR_PERSONAL_PAYLOAD[i])
    if i == 1:
        CHOOSE_HEADMAN_OR_PERSONAL_KB.add_row()
        CHOOSE_HEADMAN_OR_PERSONAL_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})


CHOOSE_WEEK_BUTTONS: list = ['четная неделя', 'нечетная неделя']
CHOOSE_WEEK_BUTTONS_PAYLOAD: list = [{"cwb_button": "even"}, {"cwb_button": "odd"}]
# Создание экземпляров клавиатуры

CHOOSE_WEEK_KB: Keyboard = Keyboard(one_time=False)

for i in range(len(CHOOSE_WEEK_BUTTONS)):
    CHOOSE_WEEK_KB.add_text_button(text=CHOOSE_WEEK_BUTTONS[i].capitalize(), color=ButtonColor.SECONDARY, payload=CHOOSE_WEEK_BUTTONS_PAYLOAD[i])
    if i == 1:
        CHOOSE_WEEK_KB.add_row()
        CHOOSE_WEEK_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})

CHOOSE_DAY_OF_WEEK_BUTTONS: list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
CHOOSE_DAY_OF_WEEK_BUTTONS_PAYLOAD: list = [{"cdowb_button": "ponedelnik"}, {"cdowb_button": "vtornik"}, {"cdowb_button": "sreda"}, {"cdowb_button": "chetverg"}, {"cdowb_button": "pjatnitsa"}, {"cdowb_button": "subbota"}]
# Создание экземпляров клавиатуры

CHOOSE_DAY_OF_WEEK_KB: Keyboard = Keyboard(one_time=False)

for i in range(len(CHOOSE_DAY_OF_WEEK_BUTTONS)):
    CHOOSE_DAY_OF_WEEK_KB.add_text_button(text=CHOOSE_DAY_OF_WEEK_BUTTONS[i].capitalize(), color=ButtonColor.SECONDARY, payload=CHOOSE_DAY_OF_WEEK_BUTTONS_PAYLOAD[i])
    if i == 2:
        CHOOSE_DAY_OF_WEEK_KB.add_row()
    if i == len(CHOOSE_DAY_OF_WEEK_BUTTONS) - 1:
        CHOOSE_DAY_OF_WEEK_KB.add_row()
        CHOOSE_DAY_OF_WEEK_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})


CHOOSE_PAIR_BUTTONS: list = ['1 пара', '2 пара', '3 пара', '4 пара', '5 пара', 'общ. аннотация', 'сбросить все изменения']
CHOOSE_PAIR_BUTTONS_PAYLOAD: list = [{"cpb_button": "first"}, {"cpb_button": "second"}, {"cpb_button": "third"}, {"cpb_button": "fourth"}, {"cpb_button": "fifth"}, {"cpb_button": "forall"}, {"cpb_button": "resetall"}]
# Создание экземпляров клавиатуры

CHOOSE_PAIR_KB: Keyboard = Keyboard(one_time=False)

for i in range(len(CHOOSE_PAIR_BUTTONS)):
    CHOOSE_PAIR_KB.add_text_button(text=CHOOSE_PAIR_BUTTONS[i].capitalize(), color=ButtonColor.SECONDARY, payload=CHOOSE_PAIR_BUTTONS_PAYLOAD[i])
    if i == 2:
        CHOOSE_PAIR_KB.add_row()
    if i == 5:
        CHOOSE_PAIR_KB.add_row()
        CHOOSE_PAIR_KB.add_text_button(text=CHOOSE_PAIR_BUTTONS[i + 1].capitalize(), color=ButtonColor.NEGATIVE, payload=CHOOSE_PAIR_BUTTONS_PAYLOAD[i + 1])
        CHOOSE_PAIR_KB.add_row()
        CHOOSE_PAIR_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})
        break

CHOOSE_MOVE_BUTTONS: list = ['перезаписать(Записать)', 'удалить']
CHOOSE_MOVE_BUTTONS_PAYLOAD: list = [{"cmb_button": "rewrite"}, {"cmb_button": "remove"}]
# Создание экземпляров клавиатуры

CHOOSE_MOVE_KB: Keyboard = Keyboard(one_time=True)

for i in range(len(CHOOSE_MOVE_BUTTONS)):
    CHOOSE_MOVE_KB.add_text_button(text=CHOOSE_MOVE_BUTTONS[i].capitalize(), color=ButtonColor.SECONDARY, payload=CHOOSE_MOVE_BUTTONS_PAYLOAD[i])
    if i == 2:
        CHOOSE_MOVE_KB.add_row()
    if i == len(CHOOSE_MOVE_BUTTONS) - 1:
        CHOOSE_MOVE_KB.add_row()
        CHOOSE_MOVE_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})
