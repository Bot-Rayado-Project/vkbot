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

SCHEDULE_FACULTY_BUTTONS: list = ['ИТ', 'КиИБ', 'РИТ', 'ЦЭиМК',
                                  'СиСС', 'Назад', 'Меню']
SCHEDULE_FACULTY_BUTTONS_PAYLOAD: list = [{'schedule_faculty_button': 'it'}, {'schedule_faculty_button': 'kiib'}, {'schedule_faculty_button': 'rit'},
                                          {'schedule_faculty_button': 'tseimk'}, {'schedule_faculty_button': 'siss'}, {'schedule_faculty_button': 'back'}, {'button': 'menu'}]
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
SCHEDULE_FACULTY_KB.add_text_button(text=SCHEDULE_FACULTY_BUTTONS[6],
                                    color=ButtonColor.PRIMARY,
                                    payload=SCHEDULE_FACULTY_BUTTONS_PAYLOAD[6])

'''
***
Создание клавиатур для четности
***
'''

SCHEDULE_PARITY_BUTTONS: list = ['Текущая неделя', 'Следующая неделя',
                                 'Назад', 'Меню']
SCHEDULE_PARITY_BUTTONS_PAYLOAD: list = [{'schedule_parity_button': 'current'}, {'schedule_parity_button': 'next'}, {'schedule_parity_button': 'back'},
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
SCHEDULE_PARITY_KB.add_text_button(text=SCHEDULE_PARITY_BUTTONS[3],
                                   color=ButtonColor.PRIMARY,
                                   payload=SCHEDULE_PARITY_BUTTONS_PAYLOAD[3])

'''
***
Создание клавиатур для потоков
***
'''

SCHEDULE_STREAM_IT_BUTTONS: list = ['БФИ', 'БВТ', 'БСТ', 'БЭИ',
                                    'Назад', 'Меню']
SCHEDULE_STREAM_IT_BUTTONS_PAYLOAD: list = [{'schedule_stream_button': 'bfi'}, {'schedule_stream_button': 'bvt'},
                                            {'schedule_stream_button': 'bst'}, {'schedule_stream_button': 'bei'}, {'schedule_stream_button': 'back'}, {'button': 'menu'}]
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
SCHEDULE_STREAM_IT_KB.add_text_button(text=SCHEDULE_STREAM_IT_BUTTONS[5],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_STREAM_IT_BUTTONS_PAYLOAD[5])

SCHEDULE_STREAM_KIIB_BUTTONS: list = ['БАП', 'БПМ', 'БУТ',
                                      'ЗРС', 'БИБ', 'Назад', 'Меню']
SCHEDULE_STREAM_KIIB_BUTTONS_PAYLOAD: list = [{'schedule_stream_button': 'bap'}, {'schedule_stream_button': 'bpm'}, {'schedule_stream_button': 'but'},
                                              {'schedule_stream_button': 'zrs'}, {'schedule_stream_button': 'bib'}, {'schedule_stream_button': 'back'}, {'button': 'menu'}]
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
SCHEDULE_STREAM_KIIB_KB.add_text_button(text=SCHEDULE_STREAM_KIIB_BUTTONS[6],
                                        color=ButtonColor.PRIMARY,
                                        payload=SCHEDULE_STREAM_KIIB_BUTTONS_PAYLOAD[6])

SCHEDULE_STREAM_RIT_BUTTONS: list = ['БРТ', 'БИК', 'Назад', 'Меню']
SCHEDULE_STREAM_RIT_BUTTONS_PAYLOAD: list = [{'schedule_stream_button': 'brt'}, {'schedule_stream_button': 'bik'},
                                             {'schedule_stream_button': 'back'}, {'button': 'menu'}]
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
SCHEDULE_STREAM_RIT_KB.add_text_button(text=SCHEDULE_STREAM_RIT_BUTTONS[3],
                                       color=ButtonColor.PRIMARY,
                                       payload=SCHEDULE_STREAM_RIT_BUTTONS_PAYLOAD[3])

SCHEDULE_STREAM_TSEIMK_BUTTONS: list = ['БЭЭ', 'БЭР', 'ББИ', 'Назад', 'Меню']
SCHEDULE_STREAM_TSEIMK_BUTTONS_PAYLOAD: list = [{'schedule_stream_button': 'bee'}, {'schedule_stream_button': 'ber'},
                                                {'schedule_stream_button': 'bbi'}, {'schedule_stream_button': 'back'}, {'button': 'menu'}]
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
SCHEDULE_STREAM_TSEIMK_KB.add_text_button(text=SCHEDULE_STREAM_TSEIMK_BUTTONS[4],
                                          color=ButtonColor.PRIMARY,
                                          payload=SCHEDULE_STREAM_TSEIMK_BUTTONS_PAYLOAD[4])

SCHEDULE_STREAM_SISS_BUTTONS: list = ['БИН', 'Назад', 'Меню']
SCHEDULE_STREAM_SISS_BUTTONS_PAYLOAD: list = [{'schedule_stream_button': 'bin'},
                                              {'schedule_stream_button': 'back'}, {'button': 'menu'}]
SCHEDULE_STREAM_SISS_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_STREAM_SISS_KB.add_text_button(text=SCHEDULE_STREAM_SISS_BUTTONS[0],
                                        color=ButtonColor.SECONDARY,
                                        payload=SCHEDULE_STREAM_SISS_BUTTONS_PAYLOAD[0])
SCHEDULE_STREAM_SISS_KB.add_row()
SCHEDULE_STREAM_SISS_KB.add_text_button(text=SCHEDULE_STREAM_SISS_BUTTONS[1],
                                        color=ButtonColor.PRIMARY,
                                        payload=SCHEDULE_STREAM_SISS_BUTTONS_PAYLOAD[1])
SCHEDULE_STREAM_SISS_KB.add_text_button(text=SCHEDULE_STREAM_SISS_BUTTONS[2],
                                        color=ButtonColor.PRIMARY,
                                        payload=SCHEDULE_STREAM_SISS_BUTTONS_PAYLOAD[2])

'''
***
Создание клавиатур для групп
***
'''

# ----- БФИ ----- #

SCHEDULE_GROUP_BFI_BUTTONS: list = ['БФИ2101', 'БФИ2102', 'Назад', 'Меню']
SCHEDULE_GROUP_BFI_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bfi2101'}, {'schedule_group_button': 'bfi2102'},
                                            {'schedule_group_button': 'back'}, {'button': 'menu'}]
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
SCHEDULE_GROUP_BFI_KB.add_text_button(text=SCHEDULE_GROUP_BFI_BUTTONS[3],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BFI_BUTTONS_PAYLOAD[3])

# ----- БВТ ----- #

SCHEDULE_GROUP_BVT_BUTTONS: list = ['БВТ2101', 'БВТ2102', 'БВТ2103',
                                    'БВТ2104', 'БВТ2105', 'Назад', 'Меню']
SCHEDULE_GROUP_BVT_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bvt2101'},
                                            {'schedule_group_button': 'bvt2102'},
                                            {'schedule_group_button': 'bvt2103'},
                                            {'schedule_group_button': 'bvt2104'},
                                            {'schedule_group_button': 'bvt2105'},
                                            {'schedule_group_button': 'back'},
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
SCHEDULE_GROUP_BVT_KB.add_row()
SCHEDULE_GROUP_BVT_KB.add_text_button(text=SCHEDULE_GROUP_BVT_BUTTONS[5],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BVT_BUTTONS_PAYLOAD[5])
SCHEDULE_GROUP_BVT_KB.add_text_button(text=SCHEDULE_GROUP_BVT_BUTTONS[6],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BVT_BUTTONS_PAYLOAD[6])

# ----- БСТ ----- #

SCHEDULE_GROUP_BST_BUTTONS: list = ['БСТ2101', 'БСТ2102', 'БСТ2103', 'БСТ2104', 'БСТ2105',
                                    'Назад', 'Меню']
SCHEDULE_GROUP_BST_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bst2101'},
                                            {'schedule_group_button': 'bst2102'},
                                            {'schedule_group_button': 'bst2103'},
                                            {'schedule_group_button': 'bst2104'},
                                            {'schedule_group_button': 'bst2105'},
                                            {'schedule_group_button': 'back'},
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
SCHEDULE_GROUP_BST_KB.add_row()
SCHEDULE_GROUP_BST_KB.add_text_button(text=SCHEDULE_GROUP_BST_BUTTONS[5],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BST_BUTTONS_PAYLOAD[5])
SCHEDULE_GROUP_BST_KB.add_text_button(text=SCHEDULE_GROUP_BST_BUTTONS[6],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BST_BUTTONS_PAYLOAD[6])

# ----- БЭИ ----- #

SCHEDULE_GROUP_BEI_BUTTONS: list = ['БЭИ2101', 'БЭИ2102', 'БЭИ2103',
                                    'Назад', 'Меню']
SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bei2101'},
                                            {'schedule_group_button': 'bei2102'},
                                            {'schedule_group_button': 'bei2103'},
                                            {'schedule_group_button': 'back'},
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
SCHEDULE_GROUP_BEI_KB.add_text_button(text=SCHEDULE_GROUP_BEI_BUTTONS[4],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BEI_BUTTONS_PAYLOAD[4])

# ----- БАП ----- #

SCHEDULE_GROUP_BAP_BUTTONS: list = ['БАП2101', 'Назад', 'Меню']
SCHEDULE_GROUP_BAP_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bap2101'},
                                            {'schedule_group_button': 'back'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BAP_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BAP_KB.add_text_button(text=SCHEDULE_GROUP_BAP_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BAP_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BAP_KB.add_row()
SCHEDULE_GROUP_BAP_KB.add_text_button(text=SCHEDULE_GROUP_BAP_BUTTONS[1],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BAP_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BAP_KB.add_text_button(text=SCHEDULE_GROUP_BAP_BUTTONS[2],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BAP_BUTTONS_PAYLOAD[2])

# ----- БПМ ----- #

SCHEDULE_GROUP_BPM_BUTTONS: list = ['БПМ2101', 'Назад', 'Меню']
SCHEDULE_GROUP_BPM_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bpm2101'},
                                            {'schedule_group_button': 'back'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BPM_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BPM_KB.add_text_button(text=SCHEDULE_GROUP_BPM_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BPM_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BPM_KB.add_row()
SCHEDULE_GROUP_BPM_KB.add_text_button(text=SCHEDULE_GROUP_BPM_BUTTONS[1],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BPM_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BPM_KB.add_text_button(text=SCHEDULE_GROUP_BPM_BUTTONS[2],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BPM_BUTTONS_PAYLOAD[2])

# ----- БУТ ----- #

SCHEDULE_GROUP_BUT_BUTTONS: list = ['БУТ2101', 'Назад', 'Меню']
SCHEDULE_GROUP_BUT_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'but2101'},
                                            {'schedule_group_button': 'back'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BUT_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BUT_KB.add_text_button(text=SCHEDULE_GROUP_BUT_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BUT_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BUT_KB.add_row()
SCHEDULE_GROUP_BUT_KB.add_text_button(text=SCHEDULE_GROUP_BUT_BUTTONS[1],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BUT_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BUT_KB.add_text_button(text=SCHEDULE_GROUP_BUT_BUTTONS[2],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BUT_BUTTONS_PAYLOAD[2])

# ----- ЗРС ----- #

SCHEDULE_GROUP_ZRS_BUTTONS: list = ['ЗРС2101', 'ЗРС2102', 'Назад', 'Меню']
SCHEDULE_GROUP_ZRS_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'zrs2101'},
                                            {'schedule_group_button': 'zrs2102'},
                                            {'schedule_group_button': 'back'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_ZRS_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_ZRS_KB.add_text_button(text=SCHEDULE_GROUP_ZRS_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_ZRS_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_ZRS_KB.add_text_button(text=SCHEDULE_GROUP_ZRS_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_ZRS_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_ZRS_KB.add_row()
SCHEDULE_GROUP_ZRS_KB.add_text_button(text=SCHEDULE_GROUP_ZRS_BUTTONS[2],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_ZRS_BUTTONS_PAYLOAD[2])
SCHEDULE_GROUP_ZRS_KB.add_text_button(text=SCHEDULE_GROUP_ZRS_BUTTONS[3],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_ZRS_BUTTONS_PAYLOAD[3])


# ----- БИБ ----- #

SCHEDULE_GROUP_BIB_BUTTONS: list = ['БИБ2101', 'БИБ2102', 'БИБ2103',
                                    'БИБ2104', 'Назад', 'Меню']
SCHEDULE_GROUP_BIB_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bib2101'},
                                            {'schedule_group_button': 'bib2102'},
                                            {'schedule_group_button': 'bib2103'},
                                            {'schedule_group_button': 'bib2104'},
                                            {'schedule_group_button': 'back'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BIB_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BIB_KB.add_text_button(text=SCHEDULE_GROUP_BIB_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIB_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BIB_KB.add_text_button(text=SCHEDULE_GROUP_BIB_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIB_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BIB_KB.add_text_button(text=SCHEDULE_GROUP_BIB_BUTTONS[2],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIB_BUTTONS_PAYLOAD[2])
SCHEDULE_GROUP_BIB_KB.add_row()
SCHEDULE_GROUP_BIB_KB.add_text_button(text=SCHEDULE_GROUP_BIB_BUTTONS[3],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIB_BUTTONS_PAYLOAD[3])
SCHEDULE_GROUP_BIB_KB.add_row()
SCHEDULE_GROUP_BIB_KB.add_text_button(text=SCHEDULE_GROUP_BIB_BUTTONS[4],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BIB_BUTTONS_PAYLOAD[4])
SCHEDULE_GROUP_BIB_KB.add_text_button(text=SCHEDULE_GROUP_BIB_BUTTONS[5],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BIB_BUTTONS_PAYLOAD[5])

# ----- БРТ ----- #

SCHEDULE_GROUP_BRT_BUTTONS: list = ['БРТ2101', 'БРТ2102', 'Назад', 'Меню']
SCHEDULE_GROUP_BRT_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'brt2101'},
                                            {'schedule_group_button': 'brt2102'},
                                            {'schedule_group_button': 'back'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BRT_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BRT_KB.add_text_button(text=SCHEDULE_GROUP_BRT_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BRT_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BRT_KB.add_text_button(text=SCHEDULE_GROUP_BRT_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BRT_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BRT_KB.add_row()
SCHEDULE_GROUP_BRT_KB.add_text_button(text=SCHEDULE_GROUP_BRT_BUTTONS[2],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BRT_BUTTONS_PAYLOAD[2])
SCHEDULE_GROUP_BRT_KB.add_text_button(text=SCHEDULE_GROUP_BRT_BUTTONS[3],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BRT_BUTTONS_PAYLOAD[3])

# ----- БИК ----- #

SCHEDULE_GROUP_BIK_BUTTONS: list = ['БИК2101', 'БИК2102', 'БИК2103', 'БИК2104', 'БИК2105',
                                    'БИК2106', 'БИК2107', 'БИК2108', 'БИК2109', 'Назад', 'Меню']
SCHEDULE_GROUP_BIK_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bik2101'},
                                            {'schedule_group_button': 'bik2102'},
                                            {'schedule_group_button': 'bik2103'},
                                            {'schedule_group_button': 'bik2104'},
                                            {'schedule_group_button': 'bik2105'},
                                            {'schedule_group_button': 'bik2106'},
                                            {'schedule_group_button': 'bik2107'},
                                            {'schedule_group_button': 'bik2108'},
                                            {'schedule_group_button': 'bik2109'},
                                            {'schedule_group_button': 'back'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BIK_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BIK_KB.add_text_button(text=SCHEDULE_GROUP_BIK_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIK_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BIK_KB.add_text_button(text=SCHEDULE_GROUP_BIK_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIK_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BIK_KB.add_text_button(text=SCHEDULE_GROUP_BIK_BUTTONS[2],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIK_BUTTONS_PAYLOAD[2])
SCHEDULE_GROUP_BIK_KB.add_row()
SCHEDULE_GROUP_BIK_KB.add_text_button(text=SCHEDULE_GROUP_BIK_BUTTONS[3],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIK_BUTTONS_PAYLOAD[3])
SCHEDULE_GROUP_BIK_KB.add_text_button(text=SCHEDULE_GROUP_BIK_BUTTONS[4],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIK_BUTTONS_PAYLOAD[4])
SCHEDULE_GROUP_BIK_KB.add_text_button(text=SCHEDULE_GROUP_BIK_BUTTONS[5],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIK_BUTTONS_PAYLOAD[5])
SCHEDULE_GROUP_BIK_KB.add_row()
SCHEDULE_GROUP_BIK_KB.add_text_button(text=SCHEDULE_GROUP_BIK_BUTTONS[6],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIK_BUTTONS_PAYLOAD[6])
SCHEDULE_GROUP_BIK_KB.add_text_button(text=SCHEDULE_GROUP_BIK_BUTTONS[7],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIK_BUTTONS_PAYLOAD[7])
SCHEDULE_GROUP_BIK_KB.add_text_button(text=SCHEDULE_GROUP_BIK_BUTTONS[8],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIK_BUTTONS_PAYLOAD[8])
SCHEDULE_GROUP_BIK_KB.add_row()
SCHEDULE_GROUP_BIK_KB.add_text_button(text=SCHEDULE_GROUP_BIK_BUTTONS[9],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BIK_BUTTONS_PAYLOAD[9])
SCHEDULE_GROUP_BIK_KB.add_text_button(text=SCHEDULE_GROUP_BIK_BUTTONS[10],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BIK_BUTTONS_PAYLOAD[10])

# ----- БЭЭ ----- #

SCHEDULE_GROUP_BEE_BUTTONS: list = ['БЭЭ2101', 'Назад', 'Меню']
SCHEDULE_GROUP_BEE_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bee2101'},
                                            {'schedule_group_button': 'back'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BEE_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BEE_KB.add_text_button(text=SCHEDULE_GROUP_BEE_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BEE_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BEE_KB.add_row()
SCHEDULE_GROUP_BEE_KB.add_text_button(text=SCHEDULE_GROUP_BEE_BUTTONS[1],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BEE_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BEE_KB.add_text_button(text=SCHEDULE_GROUP_BEE_BUTTONS[2],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BEE_BUTTONS_PAYLOAD[2])

# ----- БЭР ----- #

SCHEDULE_GROUP_BER_BUTTONS: list = ['БЭР2101', 'Назад', 'Меню']
SCHEDULE_GROUP_BER_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'ber2101'},
                                            {'schedule_group_button': 'back'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BER_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BER_KB.add_text_button(text=SCHEDULE_GROUP_BER_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BER_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BER_KB.add_row()
SCHEDULE_GROUP_BER_KB.add_text_button(text=SCHEDULE_GROUP_BER_BUTTONS[1],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BER_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BER_KB.add_text_button(text=SCHEDULE_GROUP_BER_BUTTONS[2],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BER_BUTTONS_PAYLOAD[2])

# ----- ББИ ----- #

SCHEDULE_GROUP_BBI_BUTTONS: list = ['ББИ2101', 'Назад', 'Меню']
SCHEDULE_GROUP_BBI_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bbi2101'},
                                            {'schedule_group_button': 'back'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BBI_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BBI_KB.add_text_button(text=SCHEDULE_GROUP_BBI_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BBI_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BBI_KB.add_row()
SCHEDULE_GROUP_BBI_KB.add_text_button(text=SCHEDULE_GROUP_BBI_BUTTONS[1],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BBI_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BBI_KB.add_text_button(text=SCHEDULE_GROUP_BBI_BUTTONS[2],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BBI_BUTTONS_PAYLOAD[2])

# ----- БИН ----- #

SCHEDULE_GROUP_BIN_BUTTONS: list = ['БИН2101', 'БИН2102', 'БИН2103', 'БИН2104', 'БИН2105',
                                    'БИН2106', 'БИН2107', 'БИН2108', 'БИН2109', 'БИН2110', 'Назад', 'Меню']
SCHEDULE_GROUP_BIN_BUTTONS_PAYLOAD: list = [{'schedule_group_button': 'bin2101'},
                                            {'schedule_group_button': 'bin2102'},
                                            {'schedule_group_button': 'bin2103'},
                                            {'schedule_group_button': 'bin2104'},
                                            {'schedule_group_button': 'bin2105'},
                                            {'schedule_group_button': 'bin2106'},
                                            {'schedule_group_button': 'bin2107'},
                                            {'schedule_group_button': 'bin2108'},
                                            {'schedule_group_button': 'bin2109'},
                                            {'schedule_group_button': 'bin2110'},
                                            {'schedule_group_button': 'back'},
                                            {'button': 'menu'}]
SCHEDULE_GROUP_BIN_KB: Keyboard = Keyboard(one_time=False)

SCHEDULE_GROUP_BIN_KB.add_text_button(text=SCHEDULE_GROUP_BIN_BUTTONS[0],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIN_BUTTONS_PAYLOAD[0])
SCHEDULE_GROUP_BIN_KB.add_text_button(text=SCHEDULE_GROUP_BIN_BUTTONS[1],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIN_BUTTONS_PAYLOAD[1])
SCHEDULE_GROUP_BIN_KB.add_text_button(text=SCHEDULE_GROUP_BIN_BUTTONS[2],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIN_BUTTONS_PAYLOAD[2])
SCHEDULE_GROUP_BIN_KB.add_row()
SCHEDULE_GROUP_BIN_KB.add_text_button(text=SCHEDULE_GROUP_BIN_BUTTONS[3],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIN_BUTTONS_PAYLOAD[3])
SCHEDULE_GROUP_BIN_KB.add_text_button(text=SCHEDULE_GROUP_BIN_BUTTONS[4],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIN_BUTTONS_PAYLOAD[4])
SCHEDULE_GROUP_BIN_KB.add_text_button(text=SCHEDULE_GROUP_BIN_BUTTONS[5],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIN_BUTTONS_PAYLOAD[5])
SCHEDULE_GROUP_BIN_KB.add_row()
SCHEDULE_GROUP_BIN_KB.add_text_button(text=SCHEDULE_GROUP_BIN_BUTTONS[6],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIN_BUTTONS_PAYLOAD[6])
SCHEDULE_GROUP_BIN_KB.add_text_button(text=SCHEDULE_GROUP_BIN_BUTTONS[7],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIN_BUTTONS_PAYLOAD[7])
SCHEDULE_GROUP_BIN_KB.add_text_button(text=SCHEDULE_GROUP_BIN_BUTTONS[8],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIN_BUTTONS_PAYLOAD[8])
SCHEDULE_GROUP_BIN_KB.add_row()
SCHEDULE_GROUP_BIN_KB.add_text_button(text=SCHEDULE_GROUP_BIN_BUTTONS[9],
                                      color=ButtonColor.SECONDARY,
                                      payload=SCHEDULE_GROUP_BIN_BUTTONS_PAYLOAD[9])
SCHEDULE_GROUP_BIN_KB.add_row()
SCHEDULE_GROUP_BIN_KB.add_text_button(text=SCHEDULE_GROUP_BIN_BUTTONS[10],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BIN_BUTTONS_PAYLOAD[10])
SCHEDULE_GROUP_BIN_KB.add_text_button(text=SCHEDULE_GROUP_BIN_BUTTONS[11],
                                      color=ButtonColor.PRIMARY,
                                      payload=SCHEDULE_GROUP_BIN_BUTTONS_PAYLOAD[11])


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
    'bei': SCHEDULE_GROUP_BEI_KB,
    'bap': SCHEDULE_GROUP_BAP_KB,
    'bpm': SCHEDULE_GROUP_BPM_KB,
    'but': SCHEDULE_GROUP_BUT_KB,
    'zrs': SCHEDULE_GROUP_ZRS_KB,
    'bib': SCHEDULE_GROUP_BIB_KB,
    'brt': SCHEDULE_GROUP_BRT_KB,
    'bik': SCHEDULE_GROUP_BIK_KB,
    'bee': SCHEDULE_GROUP_BEE_KB,
    'ber': SCHEDULE_GROUP_BER_KB,
    'bbi': SCHEDULE_GROUP_BBI_KB,
    'bin': SCHEDULE_GROUP_BIN_KB
}
