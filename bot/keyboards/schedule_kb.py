from vkwave.bots import Keyboard, ButtonColor

'''
***
Создание клавиатур для стартовой кнопки Расписание
***
'''

SCHEDULE_DAY_BUTTONS: list = ['Сегодня', 'Завтра', 'Вся неделя',
                              'Редактировать расписание', 'Меню']
SCHEDULE_DAY_BUTTONS_PAYLOAD: list = [{"schedule_day_button": "today"}, {"schedule_day_button": "tomorrow"},
                                      {"schedule_day_button": "whole_week"}, {"schedule_button": "edit"}, {'button': 'menu'}]
SCHEDULE_DAY_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_DAY_KB.add_text_button(text=SCHEDULE_DAY_BUTTONS[0],
                                color=ButtonColor.SECONDARY,
                                payload=SCHEDULE_DAY_BUTTONS_PAYLOAD[0])
SCHEDULE_DAY_KB.add_text_button(text=SCHEDULE_DAY_BUTTONS[1],
                                color=ButtonColor.SECONDARY,
                                payload=SCHEDULE_DAY_BUTTONS_PAYLOAD[1])
SCHEDULE_DAY_KB.add_text_button(text=SCHEDULE_DAY_BUTTONS[2],
                                color=ButtonColor.SECONDARY,
                                payload=SCHEDULE_DAY_BUTTONS_PAYLOAD[2])
SCHEDULE_DAY_KB.add_row()
SCHEDULE_DAY_KB.add_text_button(text=SCHEDULE_DAY_BUTTONS[3],
                                color=ButtonColor.SECONDARY,
                                payload=SCHEDULE_DAY_BUTTONS_PAYLOAD[3])
SCHEDULE_DAY_KB.add_row()
SCHEDULE_DAY_KB.add_text_button(text=SCHEDULE_DAY_BUTTONS[4],
                                color=ButtonColor.PRIMARY,
                                payload=SCHEDULE_DAY_BUTTONS_PAYLOAD[4])

'''
***
Создание клавиатур для факультетов
***
'''

SCHEDULE_FACULTY_BUTTONS: list = ['ИТ', 'КиИБ', 'РИТ', 'ЦЭиМК', 'СиСС', 'Меню']
SCHEDULE_FACULTY_BUTTONS_PAYLOAD: list = [{'schedule_faculty_button': 'it'}, {'schedule_faculty_button': 'kiib'}, {'schedule_faculty_button': 'rit'},
                                          {'schedule_faculty_button': 'tseimk'}, {'schedule_faculty_button': 'siss'}, {'button': 'menu'}]
SCHEDULE_FACULTY_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_FACULTY_KB.add_text_button(text=SCHEDULE_FACULTY_BUTTONS[0],
                                    color=ButtonColor.SECONDARY,
                                    payload=SCHEDULE_FACULTY_BUTTONS_PAYLOAD[0])
SCHEDULE_FACULTY_KB.add_text_button(text=SCHEDULE_FACULTY_BUTTONS[1],
                                    color=ButtonColor.SECONDARY,
                                    payload=SCHEDULE_FACULTY_BUTTONS_PAYLOAD[1])
SCHEDULE_FACULTY_KB.add_text_button(text=SCHEDULE_FACULTY_BUTTONS[2],
                                    color=ButtonColor.SECONDARY,
                                    payload=SCHEDULE_FACULTY_BUTTONS_PAYLOAD[2])
SCHEDULE_FACULTY_KB.add_row()
SCHEDULE_FACULTY_KB.add_text_button(text=SCHEDULE_FACULTY_BUTTONS[3],
                                    color=ButtonColor.SECONDARY,
                                    payload=SCHEDULE_FACULTY_BUTTONS_PAYLOAD[3])
SCHEDULE_FACULTY_KB.add_text_button(text=SCHEDULE_FACULTY_BUTTONS[4],
                                    color=ButtonColor.SECONDARY,
                                    payload=SCHEDULE_FACULTY_BUTTONS_PAYLOAD[4])
SCHEDULE_FACULTY_KB.add_row()
SCHEDULE_FACULTY_KB.add_text_button(text=SCHEDULE_FACULTY_BUTTONS[5],
                                    color=ButtonColor.PRIMARY,
                                    payload=SCHEDULE_FACULTY_BUTTONS_PAYLOAD[5])

'''
***
Создание клавиатур для четности
***
'''

SCHEDULE_PARITY_BUTTONS: list = ['Четная', 'Нечетная', 'Меню']
SCHEDULE_PARITY_BUTTONS_PAYLOAD: list = [{'schedule_parity_button': 'even'}, {'schedule_parity_button': 'odd'},
                                         {'button': 'menu'}]
SCHEDULE_PARITY_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_PARITY_KB.add_text_button(text=SCHEDULE_PARITY_BUTTONS[0],
                                   color=ButtonColor.SECONDARY,
                                   payload=SCHEDULE_PARITY_BUTTONS_PAYLOAD[0])
SCHEDULE_PARITY_KB.add_text_button(text=SCHEDULE_PARITY_BUTTONS[1],
                                   color=ButtonColor.SECONDARY,
                                   payload=SCHEDULE_PARITY_BUTTONS_PAYLOAD[1])
SCHEDULE_PARITY_KB.add_row()
SCHEDULE_PARITY_KB.add_text_button(text=SCHEDULE_PARITY_BUTTONS[2],
                                   color=ButtonColor.PRIMARY,
                                   payload=SCHEDULE_PARITY_BUTTONS_PAYLOAD[2])

'''
***
Создание клавиатур для потоков
***
'''

SCHEDULE_STREAM_IT_BUTTONS: list = ['БФИ', 'БВТ', 'БСТ', 'БЭИ', 'Меню']
SCHEDULE_STREAM_IT_BUTTONS_PAYLOAD: list = [{'schedule_stream_button': 'bfi'}, {'schedule_stream_button': 'bvt'},
                                            {'schedule_stream_button': 'bst'}, {'schedule_stream_button': 'bei'}, {'button': 'menu'}]
SCHEDULE_STREAM_IT_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_STREAM_IT_KB.add_text_button(text=SCHEDULE_STREAM_IT_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_STREAM_IT_BUTTONS_PAYLOAD[0])
SCHEDULE_STREAM_IT_KB.add_text_button(text=SCHEDULE_STREAM_IT_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_STREAM_IT_BUTTONS_PAYLOAD[1])
SCHEDULE_STREAM_IT_KB.add_text_button(text=SCHEDULE_STREAM_IT_BUTTONS[2],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_STREAM_IT_BUTTONS_PAYLOAD[2])
SCHEDULE_STREAM_IT_KB.add_text_button(text=SCHEDULE_STREAM_IT_BUTTONS[3],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_STREAM_IT_BUTTONS_PAYLOAD[3])
SCHEDULE_STREAM_IT_KB.add_row()
SCHEDULE_STREAM_IT_KB.add_text_button(text=SCHEDULE_STREAM_IT_BUTTONS[4],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_STREAM_IT_BUTTONS_PAYLOAD[4])

SCHEDULE_STREAM_KIIB_BUTTONS: list = ['БАП', 'БПМ', 'БУТ',
                                      'ЗРС', 'БИБ', 'Меню']
SCHEDULE_STREAM_KIIB_BUTTONS_PAYLOAD: list = [{'schedule_stream_button': 'bap'}, {'schedule_stream_button': 'bpm'}, {'schedule_stream_button': 'but'},
                                              {'schedule_stream_button': 'zrs'}, {'schedule_stream_button': 'bib'}, {'button': 'menu'}]
SCHEDULE_STREAM_KIIB_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_STREAM_KIIB_KB.add_text_button(text=SCHEDULE_STREAM_KIIB_BUTTONS[0],
                                        color=ButtonColor.SECONDARY,
                                        payload=SCHEDULE_STREAM_KIIB_BUTTONS_PAYLOAD[0])
SCHEDULE_STREAM_KIIB_KB.add_text_button(text=SCHEDULE_STREAM_KIIB_BUTTONS[1],
                                        color=ButtonColor.SECONDARY,
                                        payload=SCHEDULE_STREAM_KIIB_BUTTONS_PAYLOAD[1])
SCHEDULE_STREAM_KIIB_KB.add_text_button(text=SCHEDULE_STREAM_KIIB_BUTTONS[2],
                                        color=ButtonColor.SECONDARY,
                                        payload=SCHEDULE_STREAM_KIIB_BUTTONS_PAYLOAD[2])
SCHEDULE_STREAM_KIIB_KB.add_row()
SCHEDULE_STREAM_KIIB_KB.add_text_button(text=SCHEDULE_STREAM_KIIB_BUTTONS[3],
                                        color=ButtonColor.SECONDARY,
                                        payload=SCHEDULE_STREAM_KIIB_BUTTONS_PAYLOAD[3])
SCHEDULE_STREAM_KIIB_KB.add_text_button(text=SCHEDULE_STREAM_KIIB_BUTTONS[4],
                                        color=ButtonColor.SECONDARY,
                                        payload=SCHEDULE_STREAM_KIIB_BUTTONS_PAYLOAD[4])
SCHEDULE_STREAM_KIIB_KB.add_row()
SCHEDULE_STREAM_KIIB_KB.add_text_button(text=SCHEDULE_STREAM_KIIB_BUTTONS[5],
                                        color=ButtonColor.PRIMARY,
                                        payload=SCHEDULE_STREAM_KIIB_BUTTONS_PAYLOAD[5])

SCHEDULE_STREAM_RIT_BUTTONS: list = ['БРТ', 'БИК', 'Меню']
SCHEDULE_STREAM_RIT_BUTTONS_PAYLOAD: list = [{'schedule_stream_button': 'brt'}, {'schedule_stream_button': 'bik'},
                                             {'button': 'menu'}]
SCHEDULE_STREAM_RIT_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_STREAM_RIT_KB.add_text_button(text=SCHEDULE_STREAM_RIT_BUTTONS[0],
                                       color=ButtonColor.SECONDARY,
                                       payload=SCHEDULE_STREAM_RIT_BUTTONS_PAYLOAD[0])
SCHEDULE_STREAM_RIT_KB.add_text_button(text=SCHEDULE_STREAM_RIT_BUTTONS[1],
                                       color=ButtonColor.SECONDARY,
                                       payload=SCHEDULE_STREAM_RIT_BUTTONS_PAYLOAD[1])
SCHEDULE_STREAM_RIT_KB.add_row()
SCHEDULE_STREAM_RIT_KB.add_text_button(text=SCHEDULE_STREAM_RIT_BUTTONS[2],
                                       color=ButtonColor.PRIMARY,
                                       payload=SCHEDULE_STREAM_RIT_BUTTONS_PAYLOAD[2])

SCHEDULE_STREAM_TSEIMK_BUTTONS: list = ['БЭЭ', 'БЭР', 'ББИ', 'Меню']
SCHEDULE_STREAM_TSEIMK_BUTTONS_PAYLOAD: list = [{'schedule_stream_button': 'bee'}, {'schedule_stream_button': 'ber'},
                                                {'schedule_stream_button': 'bbi'}, {'button': 'menu'}]
SCHEDULE_STREAM_TSEIMK_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_STREAM_TSEIMK_KB.add_text_button(text=SCHEDULE_STREAM_TSEIMK_BUTTONS[0],
                                          color=ButtonColor.SECONDARY,
                                          payload=SCHEDULE_STREAM_TSEIMK_BUTTONS_PAYLOAD[0])
SCHEDULE_STREAM_TSEIMK_KB.add_text_button(text=SCHEDULE_STREAM_TSEIMK_BUTTONS[1],
                                          color=ButtonColor.SECONDARY,
                                          payload=SCHEDULE_STREAM_TSEIMK_BUTTONS_PAYLOAD[1])
SCHEDULE_STREAM_TSEIMK_KB.add_text_button(text=SCHEDULE_STREAM_TSEIMK_BUTTONS[2],
                                          color=ButtonColor.SECONDARY,
                                          payload=SCHEDULE_STREAM_TSEIMK_BUTTONS_PAYLOAD[2])
SCHEDULE_STREAM_TSEIMK_KB.add_row()
SCHEDULE_STREAM_TSEIMK_KB.add_text_button(text=SCHEDULE_STREAM_TSEIMK_BUTTONS[3],
                                          color=ButtonColor.PRIMARY,
                                          payload=SCHEDULE_STREAM_TSEIMK_BUTTONS_PAYLOAD[3])

SCHEDULE_STREAM_SISS_BUTTONS: list = ['БИН', 'Меню']
SCHEDULE_STREAM_SISS_BUTTONS_PAYLOAD: list = [{'schedule_stream_button': 'bin'},
                                              {'button': 'menu'}]
SCHEDULE_STREAM_SISS_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_STREAM_SISS_KB.add_text_button(text=SCHEDULE_STREAM_SISS_BUTTONS[0],
                                        color=ButtonColor.SECONDARY,
                                        payload=SCHEDULE_STREAM_SISS_BUTTONS_PAYLOAD[0])
SCHEDULE_STREAM_SISS_KB.add_row()
SCHEDULE_STREAM_SISS_KB.add_text_button(text=SCHEDULE_STREAM_SISS_BUTTONS[1],
                                        color=ButtonColor.PRIMARY,
                                        payload=SCHEDULE_STREAM_SISS_BUTTONS_PAYLOAD[1])

'''
***
Создание клавиатур для групп
***
'''

# ----- БФИ ----- #

SCHEDULE_GROUP_BFI_BUTTONS: list = ['БФИ2101', 'БФИ2102', 'Меню']
SCHEDULE_GROUP_BFI_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bfi2101'}, {'schedule_group_button': 'bfi2102'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BFI_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BFI_KB.add_text_button(text=SCHEDULE_GROUP_BFI_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BFI_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BFI_KB.add_text_button(text=SCHEDULE_GROUP_BFI_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BFI_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BFI_KB.add_row()
SCHEDULE_GROUP_BFI_KB.add_text_button(text=SCHEDULE_GROUP_BFI_BUTTONS[2],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BFI_BUTTONS_PAYLOAD[2])

# ----- БВТ ----- #

SCHEDULE_GROUP_BVT_BUTTONS: list = ['БВТ2101', 'БВТ2102', 'БВТ2103', 'БВТ2104', 'БВТ2105',
                                    'БВТ2106', 'БВТ2107', 'БВТ2108', 'Меню']
SCHEDULE_GROUP_BVT_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bvt2101'},
                                            {'schedule_group_button': 'bvt2102'},
                                            {'schedule_group_button': 'bvt2103'},
                                            {'schedule_group_button': 'bvt2104'},
                                            {'schedule_group_button': 'bvt2105'},
                                            {'schedule_group_button': 'bvt2106'},
                                            {'schedule_group_button': 'bvt2107'},
                                            {'schedule_group_button': 'bvt2108'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BVT_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BVT_KB.add_text_button(text=SCHEDULE_GROUP_BVT_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BVT_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BVT_KB.add_text_button(text=SCHEDULE_GROUP_BVT_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BVT_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BVT_KB.add_text_button(text=SCHEDULE_GROUP_BVT_BUTTONS[2],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BVT_BUTTONS_PAYLOAD[2])
SCHEDULE_GROUP_BVT_KB.add_row()
SCHEDULE_GROUP_BVT_KB.add_text_button(text=SCHEDULE_GROUP_BVT_BUTTONS[3],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BVT_BUTTONS_PAYLOAD[3])
SCHEDULE_GROUP_BVT_KB.add_text_button(text=SCHEDULE_GROUP_BVT_BUTTONS[4],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BVT_BUTTONS_PAYLOAD[4])
SCHEDULE_GROUP_BVT_KB.add_text_button(text=SCHEDULE_GROUP_BVT_BUTTONS[5],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BVT_BUTTONS_PAYLOAD[5])
SCHEDULE_GROUP_BVT_KB.add_row()
SCHEDULE_GROUP_BVT_KB.add_text_button(text=SCHEDULE_GROUP_BVT_BUTTONS[6],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BVT_BUTTONS_PAYLOAD[6])
SCHEDULE_GROUP_BVT_KB.add_text_button(text=SCHEDULE_GROUP_BVT_BUTTONS[7],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BVT_BUTTONS_PAYLOAD[7])
SCHEDULE_GROUP_BVT_KB.add_row()
SCHEDULE_GROUP_BVT_KB.add_text_button(text=SCHEDULE_GROUP_BVT_BUTTONS[8],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BVT_BUTTONS_PAYLOAD[8])

# ----- БСТ ----- #

SCHEDULE_GROUP_BST_BUTTONS: list = ['БСТ2101', 'БСТ2102', 'БСТ2103', 'БСТ2104', 'БСТ2105',
                                    'БСТ2106', 'Меню']
SCHEDULE_GROUP_BST_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bst2101'},
                                            {'schedule_group_button': 'bst2102'},
                                            {'schedule_group_button': 'bst2103'},
                                            {'schedule_group_button': 'bst2104'},
                                            {'schedule_group_button': 'bst2105'},
                                            {'schedule_group_button': 'bst2106'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BST_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BST_KB.add_text_button(text=SCHEDULE_GROUP_BST_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BST_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BST_KB.add_text_button(text=SCHEDULE_GROUP_BST_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BST_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BST_KB.add_text_button(text=SCHEDULE_GROUP_BST_BUTTONS[2],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BST_BUTTONS_PAYLOAD[2])
SCHEDULE_GROUP_BST_KB.add_row()
SCHEDULE_GROUP_BST_KB.add_text_button(text=SCHEDULE_GROUP_BST_BUTTONS[3],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BST_BUTTONS_PAYLOAD[3])
SCHEDULE_GROUP_BST_KB.add_text_button(text=SCHEDULE_GROUP_BST_BUTTONS[4],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BST_BUTTONS_PAYLOAD[4])
SCHEDULE_GROUP_BST_KB.add_text_button(text=SCHEDULE_GROUP_BST_BUTTONS[5],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BST_BUTTONS_PAYLOAD[5])
SCHEDULE_GROUP_BST_KB.add_row()
SCHEDULE_GROUP_BST_KB.add_text_button(text=SCHEDULE_GROUP_BST_BUTTONS[6],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BST_BUTTONS_PAYLOAD[6])

# ----- БЭИ ----- #

SCHEDULE_GROUP_BEI_BUTTONS: list = ['БЭИ2101', 'БЭИ2102', 'БЭИ2103', 'Меню']
SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bei2101'},
                                            {'schedule_group_button': 'bei2102'},
                                            {'schedule_group_button': 'bei2103'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BEI_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[2],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[2])
SCHEDULE_GROUP_BEI_KB.add_row()
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[3],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[3])

# ----- БАП ----- #

SCHEDULE_GROUP_BAP_BUTTONS: list = ['БАП2101', 'Меню']
SCHEDULE_GROUP_BAP_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bap2101'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BAP_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BAP_KB.add_text_button(text=SCHEDULE_GROUP_BAP_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BAP_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BAP_KB.add_row()
SCHEDULE_GROUP_BAP_KB.add_text_button(text=SCHEDULE_GROUP_BAP_BUTTONS[1],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BAP_BUTTONS_PAYLOAD[1])

# ----- БЭИ ----- #

SCHEDULE_GROUP_BEI_BUTTONS: list = ['БЭИ2101', 'БЭИ2102', 'БЭИ2103', 'Меню']
SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bei2101'},
                                            {'schedule_group_button': 'bei2102'},
                                            {'schedule_group_button': 'bei2103'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BEI_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[2],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[2])
SCHEDULE_GROUP_BEI_KB.add_row()
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[3],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[3])

# ----- БЭИ ----- #

SCHEDULE_GROUP_BEI_BUTTONS: list = ['БЭИ2101', 'БЭИ2102', 'БЭИ2103', 'Меню']
SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bei2101'},
                                            {'schedule_group_button': 'bei2102'},
                                            {'schedule_group_button': 'bei2103'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BEI_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[2],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[2])
SCHEDULE_GROUP_BEI_KB.add_row()
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[3],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[3])

# ----- БЭИ ----- #

SCHEDULE_GROUP_BEI_BUTTONS: list = ['БЭИ2101', 'БЭИ2102', 'БЭИ2103', 'Меню']
SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bei2101'},
                                            {'schedule_group_button': 'bei2102'},
                                            {'schedule_group_button': 'bei2103'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BEI_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[2],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[2])
SCHEDULE_GROUP_BEI_KB.add_row()
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[3],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[3])

# ----- БЭИ ----- #

SCHEDULE_GROUP_BEI_BUTTONS: list = ['БЭИ2101', 'БЭИ2102', 'БЭИ2103', 'Меню']
SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bei2101'},
                                            {'schedule_group_button': 'bei2102'},
                                            {'schedule_group_button': 'bei2103'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BEI_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[2],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[2])
SCHEDULE_GROUP_BEI_KB.add_row()
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[3],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[3])

SCHEDULE_FACULTY_MATCHING = {
    'it': SCHEDULE_STREAM_IT_KB,
    'kiib': SCHEDULE_STREAM_KIIB_KB,
    'rit': SCHEDULE_STREAM_RIT_KB,
    'tseimk': SCHEDULE_STREAM_TSEIMK_KB,
    'siss': SCHEDULE_STREAM_SISS_KB
}

SCHEDULE_STREAM_MATCHING = {
    'bfi': SCHEDULE_GROUP_BFI_KB,
    'bvt': SCHEDULE_GROUP_BVT_KB,
    'bst': SCHEDULE_GROUP_BST_KB,
    'bei': SCHEDULE_GROUP_BEI_KB
}
