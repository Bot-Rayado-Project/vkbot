from vkwave.bots import Keyboard, ButtonColor
from bot.db import db_get_priority_button, db_get_blueprints_buttons
from bot.utils import schedule_request as sr
from bot.utils import ScheduleRequest
from bot.utils import personal_request as pr
from bot.utils import EditPersonalRequest
from bot.utils import headman_request as hr
from bot.utils import EditHeadmanRequest
from bot.utils import blueprints_request as br
from bot.utils import BlueprintsRequest


async def create_blueprints_kb(user_id: int) -> Keyboard:
    '''Генерирует клавиатуру шаблонов и устанавливает реквесты пользователя на стандарт'''
    hr.edit_headman_requests[user_id] = EditHeadmanRequest()
    sr.user_schedule_requests[user_id] = ScheduleRequest()
    pr.edit_personal_requests[user_id] = EditPersonalRequest(user_id)
    br.user_blueprints_requests[user_id] = BlueprintsRequest()

    await db_get_priority_button(user_id)

    first_button, second_button, third_button = await db_get_blueprints_buttons(user_id)

    BLUEPRINTS_BUTTONS: list = [first_button, second_button, third_button,
                                'Создать шаблон', 'Меню']
    BLUEPRINTS_BUTTONS_PAYLOAD: list = [{"blueprints_button_cell": "first_button"}, {"blueprints_button_cell": "second_button"}, {"blueprints_button_cell": "third_button"},
                                        {"blueprints_button": "create_blueprint"}, {"button": "menu"}]
    BLUEPRINTS_KB: Keyboard = Keyboard(one_time=False)

    BLUEPRINTS_KB.add_text_button(text=BLUEPRINTS_BUTTONS[0],
                                  color=ButtonColor.SECONDARY,
                                  payload=BLUEPRINTS_BUTTONS_PAYLOAD[0])
    BLUEPRINTS_KB.add_text_button(text=BLUEPRINTS_BUTTONS[1],
                                  color=ButtonColor.SECONDARY,
                                  payload=BLUEPRINTS_BUTTONS_PAYLOAD[1])
    BLUEPRINTS_KB.add_text_button(text=BLUEPRINTS_BUTTONS[2],
                                  color=ButtonColor.SECONDARY,
                                  payload=BLUEPRINTS_BUTTONS_PAYLOAD[2])
    BLUEPRINTS_KB.add_row()
    BLUEPRINTS_KB.add_text_button(text=BLUEPRINTS_BUTTONS[3],
                                  color=ButtonColor.SECONDARY,
                                  payload=BLUEPRINTS_BUTTONS_PAYLOAD[3])
    BLUEPRINTS_KB.add_row()
    BLUEPRINTS_KB.add_text_button(text=BLUEPRINTS_BUTTONS[4],
                                  color=ButtonColor.PRIMARY,
                                  payload=BLUEPRINTS_BUTTONS_PAYLOAD[4])

    return BLUEPRINTS_KB


'''
***
Создание клавиатур для выбора ячейки
***
'''


async def create_blueprints_choose_cell_choose_cell_kb(user_id: int) -> Keyboard:
    '''Генерирует клавиатуру шаблонов и устанавливает реквесты пользователя на стандарт'''

    await db_get_priority_button(user_id)

    first_button, second_button, third_button = await db_get_blueprints_buttons(user_id)

    BLUEPRINTS_CHOOSE_CELL_BUTTONS: list = [first_button, second_button, third_button,
                                            'Назад', 'Меню']
    BLUEPRINTS_CHOOSE_CELL_BUTTONS_PAYLOAD: list = [{"blueprints_choose_cell_button_cell": "first_button"},
                                                    {"blueprints_choose_cell_button_cell": "second_button"},
                                                    {"blueprints_choose_cell_button_cell": "third_button"},
                                                    {"blueprints_choose_cell_button": "back"}, {"button": "menu"}]
    BLUEPRINTS_CHOOSE_CELL_KB: Keyboard = Keyboard(one_time=False)

    BLUEPRINTS_CHOOSE_CELL_KB.add_text_button(text=BLUEPRINTS_CHOOSE_CELL_BUTTONS[0],
                                              color=ButtonColor.SECONDARY,
                                              payload=BLUEPRINTS_CHOOSE_CELL_BUTTONS_PAYLOAD[0])
    BLUEPRINTS_CHOOSE_CELL_KB.add_text_button(text=BLUEPRINTS_CHOOSE_CELL_BUTTONS[1],
                                              color=ButtonColor.SECONDARY,
                                              payload=BLUEPRINTS_CHOOSE_CELL_BUTTONS_PAYLOAD[1])
    BLUEPRINTS_CHOOSE_CELL_KB.add_text_button(text=BLUEPRINTS_CHOOSE_CELL_BUTTONS[2],
                                              color=ButtonColor.SECONDARY,
                                              payload=BLUEPRINTS_CHOOSE_CELL_BUTTONS_PAYLOAD[2])
    BLUEPRINTS_CHOOSE_CELL_KB.add_row()
    BLUEPRINTS_CHOOSE_CELL_KB.add_text_button(text=BLUEPRINTS_CHOOSE_CELL_BUTTONS[3],
                                              color=ButtonColor.PRIMARY,
                                              payload=BLUEPRINTS_CHOOSE_CELL_BUTTONS_PAYLOAD[3])
    BLUEPRINTS_CHOOSE_CELL_KB.add_text_button(text=BLUEPRINTS_CHOOSE_CELL_BUTTONS[4],
                                              color=ButtonColor.PRIMARY,
                                              payload=BLUEPRINTS_CHOOSE_CELL_BUTTONS_PAYLOAD[4])

    return BLUEPRINTS_CHOOSE_CELL_KB

'''
***
Создание клавиатур для выбора дня
***
'''

CREATE_SCHEDULE_BLUEPRINT_DAY_BUTTONS: list = [
    'Сегодня', 'Завтра', 'Вся неделя', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_DAY_BUTTONS_PAYLOAD: list = [{"create_schedule_blueprint_day_button": "today"}, {"create_schedule_blueprint_day_button": "tomorrow"},
                                                       {"create_schedule_blueprint_day_button": "whole_week"},
                                                       {"create_schedule_blueprint_day_button": "back"}, {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_DAY_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_DAY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_DAY_BUTTONS[0],
                                                 color=ButtonColor.SECONDARY,
                                                 payload=CREATE_SCHEDULE_BLUEPRINT_DAY_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_DAY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_DAY_BUTTONS[1],
                                                 color=ButtonColor.SECONDARY,
                                                 payload=CREATE_SCHEDULE_BLUEPRINT_DAY_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_DAY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_DAY_BUTTONS[2],
                                                 color=ButtonColor.SECONDARY,
                                                 payload=CREATE_SCHEDULE_BLUEPRINT_DAY_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_DAY_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_DAY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_DAY_BUTTONS[3],
                                                 color=ButtonColor.PRIMARY,
                                                 payload=CREATE_SCHEDULE_BLUEPRINT_DAY_BUTTONS_PAYLOAD[3])
CREATE_SCHEDULE_BLUEPRINT_DAY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_DAY_BUTTONS[4],
                                                 color=ButtonColor.PRIMARY,
                                                 payload=CREATE_SCHEDULE_BLUEPRINT_DAY_BUTTONS_PAYLOAD[4])

'''
***
Создание клавиатур для факультетов
***
'''

CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS: list = ['ИТ', 'КиИБ', 'РИТ', 'ЦЭиМК',
                                                   'СиСС', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_faculty_button': 'it'}, {'create_schedule_blueprint_faculty_button': 'kiib'}, {'create_schedule_blueprint_faculty_button': 'rit'},
                                                           {'create_schedule_blueprint_faculty_button': 'tseimk'}, {'create_schedule_blueprint_faculty_button': 'siss'}, {'create_schedule_blueprint_faculty_button': 'back'}, {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS[0],
                                                     color=ButtonColor.SECONDARY,
                                                     payload=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS[1],
                                                     color=ButtonColor.SECONDARY,
                                                     payload=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS[2],
                                                     color=ButtonColor.SECONDARY,
                                                     payload=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS[3],
                                                     color=ButtonColor.SECONDARY,
                                                     payload=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS_PAYLOAD[3])
CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS[4],
                                                     color=ButtonColor.SECONDARY,
                                                     payload=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS_PAYLOAD[4])
CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS[5],
                                                     color=ButtonColor.PRIMARY,
                                                     payload=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS_PAYLOAD[5])
CREATE_SCHEDULE_BLUEPRINT_FACULTY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS[6],
                                                     color=ButtonColor.PRIMARY,
                                                     payload=CREATE_SCHEDULE_BLUEPRINT_FACULTY_BUTTONS_PAYLOAD[6])

'''
***
Создание клавиатур для четности
***
'''

CREATE_SCHEDULE_BLUEPRINT_PARITY_BUTTONS: list = ['Текущая неделя', 'Следующая неделя',
                                                  'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_PARITY_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_parity_button': 'current'}, {'create_schedule_blueprint_parity_button': 'next'}, {'create_schedule_blueprint_parity_button': 'back'},
                                                          {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_PARITY_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_PARITY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_PARITY_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=CREATE_SCHEDULE_BLUEPRINT_PARITY_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_PARITY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_PARITY_BUTTONS[1],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=CREATE_SCHEDULE_BLUEPRINT_PARITY_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_PARITY_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_PARITY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_PARITY_BUTTONS[2],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=CREATE_SCHEDULE_BLUEPRINT_PARITY_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_PARITY_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_PARITY_BUTTONS[3],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=CREATE_SCHEDULE_BLUEPRINT_PARITY_BUTTONS_PAYLOAD[3])

'''
***
Создание клавиатур для потоков
***
'''

CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS: list = ['БФИ', 'БВТ', 'БСТ', 'БЭИ',
                                                     'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_stream_button': 'bfi'}, {'create_schedule_blueprint_stream_button': 'bvt'},
                                                             {'create_schedule_blueprint_stream_button': 'bst'}, {'create_schedule_blueprint_stream_button': 'bei'}, {'create_schedule_blueprint_stream_button': 'back'}, {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS[1],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS[2],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS[3],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS_PAYLOAD[3])
CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS[4],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS_PAYLOAD[4])
CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS[5],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_BUTTONS_PAYLOAD[5])

CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS: list = ['БАП', 'БПМ', 'БУТ',
                                                       'ЗРС', 'БИБ', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_stream_button': 'bap'}, {'create_schedule_blueprint_stream_button': 'bpm'}, {'create_schedule_blueprint_stream_button': 'but'},
                                                               {'create_schedule_blueprint_stream_button': 'zrs'}, {'create_schedule_blueprint_stream_button': 'bib'}, {'create_schedule_blueprint_stream_button': 'back'}, {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS[0],
                                                         color=ButtonColor.SECONDARY,
                                                         payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS[1],
                                                         color=ButtonColor.SECONDARY,
                                                         payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS[2],
                                                         color=ButtonColor.SECONDARY,
                                                         payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS[3],
                                                         color=ButtonColor.SECONDARY,
                                                         payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS_PAYLOAD[3])
CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS[4],
                                                         color=ButtonColor.SECONDARY,
                                                         payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS_PAYLOAD[4])
CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS[5],
                                                         color=ButtonColor.PRIMARY,
                                                         payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS_PAYLOAD[5])
CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS[6],
                                                         color=ButtonColor.PRIMARY,
                                                         payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_BUTTONS_PAYLOAD[6])

CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_BUTTONS: list = [
    'БРТ', 'БИК', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_stream_button': 'brt'}, {'create_schedule_blueprint_stream_button': 'bik'},
                                                              {'create_schedule_blueprint_stream_button': 'back'}, {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_BUTTONS[0],
                                                        color=ButtonColor.SECONDARY,
                                                        payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_BUTTONS[1],
                                                        color=ButtonColor.SECONDARY,
                                                        payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_BUTTONS[2],
                                                        color=ButtonColor.PRIMARY,
                                                        payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_BUTTONS[3],
                                                        color=ButtonColor.PRIMARY,
                                                        payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_BUTTONS_PAYLOAD[3])

CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_BUTTONS: list = [
    'БЭЭ', 'БЭР', 'ББИ', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_stream_button': 'bee'}, {'create_schedule_blueprint_stream_button': 'ber'},
                                                                 {'create_schedule_blueprint_stream_button': 'bbi'}, {'create_schedule_blueprint_stream_button': 'back'}, {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_BUTTONS[0],
                                                           color=ButtonColor.SECONDARY,
                                                           payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_BUTTONS[1],
                                                           color=ButtonColor.SECONDARY,
                                                           payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_BUTTONS[2],
                                                           color=ButtonColor.SECONDARY,
                                                           payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_BUTTONS[3],
                                                           color=ButtonColor.PRIMARY,
                                                           payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_BUTTONS_PAYLOAD[3])
CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_BUTTONS[4],
                                                           color=ButtonColor.PRIMARY,
                                                           payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_BUTTONS_PAYLOAD[4])

CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_BUTTONS: list = ['БИН', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_stream_button': 'bin'},
                                                               {'create_schedule_blueprint_stream_button': 'back'}, {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_BUTTONS[0],
                                                         color=ButtonColor.SECONDARY,
                                                         payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_BUTTONS[1],
                                                         color=ButtonColor.PRIMARY,
                                                         payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_BUTTONS[2],
                                                         color=ButtonColor.PRIMARY,
                                                         payload=CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_BUTTONS_PAYLOAD[2])

'''
***
Создание клавиатур для групп
***
'''

# ----- БФИ ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_BUTTONS: list = [
    'БФИ2101', 'БФИ2102', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'bfi2101'}, {'create_schedule_blueprint_group_button': 'bfi2102'},
                                                             {'create_schedule_blueprint_group_button': 'back'}, {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_BUTTONS[1],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_BUTTONS[2],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_BUTTONS[3],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_BUTTONS_PAYLOAD[3])

# ----- БВТ ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS: list = ['БВТ2101', 'БВТ2102', 'БВТ2103', 'БВТ2104', 'БВТ2105',
                                                     'БВТ2106', 'БВТ2107', 'БВТ2108', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'bvt2101'},
                                                             {'create_schedule_blueprint_group_button': 'bvt2102'},
                                                             {'create_schedule_blueprint_group_button': 'bvt2103'},
                                                             {'create_schedule_blueprint_group_button': 'bvt2104'},
                                                             {'create_schedule_blueprint_group_button': 'bvt2105'},
                                                             {'create_schedule_blueprint_group_button': 'bvt2106'},
                                                             {'create_schedule_blueprint_group_button': 'bvt2107'},
                                                             {'create_schedule_blueprint_group_button': 'bvt2108'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS[1],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS[2],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS[3],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS_PAYLOAD[3])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS[4],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS_PAYLOAD[4])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS[5],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS_PAYLOAD[5])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS[6],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS_PAYLOAD[6])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS[7],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS_PAYLOAD[7])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS[8],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS_PAYLOAD[8])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS[9],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_BUTTONS_PAYLOAD[9])

# ----- БСТ ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS: list = ['БСТ2101', 'БСТ2102', 'БСТ2103', 'БСТ2104', 'БСТ2105',
                                                     'БСТ2106', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'bst2101'},
                                                             {'create_schedule_blueprint_group_button': 'bst2102'},
                                                             {'create_schedule_blueprint_group_button': 'bst2103'},
                                                             {'create_schedule_blueprint_group_button': 'bst2104'},
                                                             {'create_schedule_blueprint_group_button': 'bst2105'},
                                                             {'create_schedule_blueprint_group_button': 'bst2106'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS[1],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS[2],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS[3],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS_PAYLOAD[3])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS[4],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS_PAYLOAD[4])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS[5],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS_PAYLOAD[5])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS[6],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS_PAYLOAD[6])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS[7],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_BUTTONS_PAYLOAD[7])

# ----- БЭИ ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_BUTTONS: list = ['БЭИ2101', 'БЭИ2102', 'БЭИ2103',
                                                     'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'bei2101'},
                                                             {'create_schedule_blueprint_group_button': 'bei2102'},
                                                             {'create_schedule_blueprint_group_button': 'bei2103'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_BUTTONS[1],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_BUTTONS[2],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_BUTTONS[3],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_BUTTONS_PAYLOAD[3])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_BUTTONS[4],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_BUTTONS_PAYLOAD[4])

# ----- БАП ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_BUTTONS: list = [
    'БАП2101', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'bap2101'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_BUTTONS[1],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_BUTTONS[2],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_BUTTONS_PAYLOAD[2])

# ----- БПМ ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_BUTTONS: list = [
    'БПМ2101', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'bpm2101'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_BUTTONS[1],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_BUTTONS[2],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_BUTTONS_PAYLOAD[2])

# ----- БУТ ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_BUTTONS: list = [
    'БУТ2101', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'but2101'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_BUTTONS[1],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_BUTTONS[2],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_BUTTONS_PAYLOAD[2])

# ----- ЗРС ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_BUTTONS: list = [
    'ЗРС2101', 'ЗРС2102', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'zrs2101'},
                                                             {'create_schedule_blueprint_group_button': 'zrs2102'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_BUTTONS[1],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_BUTTONS[2],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_BUTTONS[3],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_BUTTONS_PAYLOAD[3])


# ----- БИБ ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS: list = ['БИБ2101', 'БИБ2102', 'БИБ2103',
                                                     'БИБ2104', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'bib2101'},
                                                             {'create_schedule_blueprint_group_button': 'bib2102'},
                                                             {'create_schedule_blueprint_group_button': 'bib2103'},
                                                             {'create_schedule_blueprint_group_button': 'bib2104'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS[1],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS[2],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS[3],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS_PAYLOAD[3])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS[4],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS_PAYLOAD[4])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS[5],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_BUTTONS_PAYLOAD[5])

# ----- БРТ ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_BUTTONS: list = [
    'БРТ2101', 'БРТ2102', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'brt2101'},
                                                             {'create_schedule_blueprint_group_button': 'brt2102'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_BUTTONS[1],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_BUTTONS[2],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_BUTTONS[3],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_BUTTONS_PAYLOAD[3])

# ----- БИК ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS: list = ['БИК2101', 'БИК2102', 'БИК2103', 'БИК2104', 'БИК2105',
                                                     'БИК2106', 'БИК2107', 'БИК2108', 'БИК2109', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'bik2101'},
                                                             {'create_schedule_blueprint_group_button': 'bik2102'},
                                                             {'create_schedule_blueprint_group_button': 'bik2103'},
                                                             {'create_schedule_blueprint_group_button': 'bik2104'},
                                                             {'create_schedule_blueprint_group_button': 'bik2105'},
                                                             {'create_schedule_blueprint_group_button': 'bik2106'},
                                                             {'create_schedule_blueprint_group_button': 'bik2107'},
                                                             {'create_schedule_blueprint_group_button': 'bik2108'},
                                                             {'create_schedule_blueprint_group_button': 'bik2109'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS[1],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS[2],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS[3],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS_PAYLOAD[3])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS[4],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS_PAYLOAD[4])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS[5],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS_PAYLOAD[5])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS[6],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS_PAYLOAD[6])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS[7],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS_PAYLOAD[7])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS[8],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS_PAYLOAD[8])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS[9],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS_PAYLOAD[9])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS[10],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_BUTTONS_PAYLOAD[10])

# ----- БЭЭ ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_BUTTONS: list = [
    'БЭЭ2101', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'bee2101'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_BUTTONS[1],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_BUTTONS[2],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_BUTTONS_PAYLOAD[2])

# ----- БЭР ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_BUTTONS: list = [
    'БЭР2101', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'ber2101'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_BUTTONS[1],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_BUTTONS[2],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_BUTTONS_PAYLOAD[2])

# ----- ББИ ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_BUTTONS: list = [
    'ББИ2101', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'bbi2101'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_BUTTONS[1],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_BUTTONS[2],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_BUTTONS_PAYLOAD[2])

# ----- БИН ----- #

CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS: list = ['БИН2101', 'БИН2102', 'БИН2103', 'БИН2104', 'БИН2105',
                                                     'БИН2106', 'БИН2107', 'БИН2108', 'БИН2109', 'БИН2110', 'Назад', 'Меню']
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS_PAYLOAD: list = [{'create_schedule_blueprint_group_button': 'bin2101'},
                                                             {'create_schedule_blueprint_group_button': 'bin2102'},
                                                             {'create_schedule_blueprint_group_button': 'bin2103'},
                                                             {'create_schedule_blueprint_group_button': 'bin2104'},
                                                             {'create_schedule_blueprint_group_button': 'bin2105'},
                                                             {'create_schedule_blueprint_group_button': 'bin2106'},
                                                             {'create_schedule_blueprint_group_button': 'bin2107'},
                                                             {'create_schedule_blueprint_group_button': 'bin2108'},
                                                             {'create_schedule_blueprint_group_button': 'bin2109'},
                                                             {'create_schedule_blueprint_group_button': 'bin2110'},
                                                             {'create_schedule_blueprint_group_button': 'back'},
                                                             {'button': 'menu'}]
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB: Keyboard = Keyboard(one_time=False)

CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS[0],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS_PAYLOAD[0])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS[1],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS_PAYLOAD[1])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS[2],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS_PAYLOAD[2])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS[3],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS_PAYLOAD[3])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS[4],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS_PAYLOAD[4])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS[5],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS_PAYLOAD[5])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS[6],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS_PAYLOAD[6])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS[7],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS_PAYLOAD[7])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS[8],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS_PAYLOAD[8])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS[9],
                                                       color=ButtonColor.SECONDARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS_PAYLOAD[9])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_row()
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS[10],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS_PAYLOAD[10])
CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB.add_text_button(text=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS[11],
                                                       color=ButtonColor.PRIMARY,
                                                       payload=CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_BUTTONS_PAYLOAD[11])

# Словарь совпадения клавиатуры по факультету

CREATE_SCHEDULE_BLUEPRINT_FACULTY_MATCHING = {
    'it': CREATE_SCHEDULE_BLUEPRINT_STREAM_IT_KB,
    'kiib': CREATE_SCHEDULE_BLUEPRINT_STREAM_KIIB_KB,
    'rit': CREATE_SCHEDULE_BLUEPRINT_STREAM_RIT_KB,
    'tseimk': CREATE_SCHEDULE_BLUEPRINT_STREAM_TSEIMK_KB,
    'siss': CREATE_SCHEDULE_BLUEPRINT_STREAM_SISS_KB
}

# Словарь совпадения клавиатуры по потоку

CREATE_SCHEDULE_BLUEPRINT_STREAM_MATCHING = {
    'bfi': CREATE_SCHEDULE_BLUEPRINT_GROUP_BFI_KB,
    'bvt': CREATE_SCHEDULE_BLUEPRINT_GROUP_BVT_KB,
    'bst': CREATE_SCHEDULE_BLUEPRINT_GROUP_BST_KB,
    'bei': CREATE_SCHEDULE_BLUEPRINT_GROUP_BEI_KB,
    'bap': CREATE_SCHEDULE_BLUEPRINT_GROUP_BAP_KB,
    'bpm': CREATE_SCHEDULE_BLUEPRINT_GROUP_BPM_KB,
    'but': CREATE_SCHEDULE_BLUEPRINT_GROUP_BUT_KB,
    'zrs': CREATE_SCHEDULE_BLUEPRINT_GROUP_ZRS_KB,
    'bib': CREATE_SCHEDULE_BLUEPRINT_GROUP_BIB_KB,
    'brt': CREATE_SCHEDULE_BLUEPRINT_GROUP_BRT_KB,
    'bik': CREATE_SCHEDULE_BLUEPRINT_GROUP_BIK_KB,
    'bee': CREATE_SCHEDULE_BLUEPRINT_GROUP_BEE_KB,
    'ber': CREATE_SCHEDULE_BLUEPRINT_GROUP_BER_KB,
    'bbi': CREATE_SCHEDULE_BLUEPRINT_GROUP_BBI_KB,
    'bin': CREATE_SCHEDULE_BLUEPRINT_GROUP_BIN_KB
}
