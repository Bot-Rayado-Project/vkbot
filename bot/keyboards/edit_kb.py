from vkwave.bots import Keyboard, ButtonColor

'''
***
Создание клавиатур для стартовой кнопки Редактирование
***
'''

EDIT_SCHEDULE_BUTTONS: list = ['Для группы', 'Для себя', 'Назад', 'Меню']
EDIT_SCHEDULE_BUTTONS_PAYLOAD: list = [{"edit_schedule_button": "headman"}, {"edit_schedule_button": "personal"},
                                       {"edit_schedule_button": "back"}, {'button': 'menu'}]
EDIT_SCHEDULE_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_KB.add_text_button(text=EDIT_SCHEDULE_BUTTONS[0],
                                 color=ButtonColor.SECONDARY,
                                 payload=EDIT_SCHEDULE_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_KB.add_text_button(text=EDIT_SCHEDULE_BUTTONS[1],
                                 color=ButtonColor.SECONDARY,
                                 payload=EDIT_SCHEDULE_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_KB.add_row()
EDIT_SCHEDULE_KB.add_text_button(text=EDIT_SCHEDULE_BUTTONS[2],
                                 color=ButtonColor.PRIMARY,
                                 payload=EDIT_SCHEDULE_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_KB.add_text_button(text=EDIT_SCHEDULE_BUTTONS[3],
                                 color=ButtonColor.PRIMARY,
                                 payload=EDIT_SCHEDULE_BUTTONS_PAYLOAD[3])


'''
***
Создание клавиатур для факультетов
***
'''

EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS: list = ['ИТ', 'КиИБ', 'РИТ', 'ЦЭиМК',
                                                'СиСС', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_faculty_button': 'it'}, {'edit_schedule_personal_faculty_button': 'kiib'}, {'edit_schedule_personal_faculty_button': 'rit'},
                                                        {'edit_schedule_personal_faculty_button': 'tseimk'}, {'edit_schedule_personal_faculty_button': 'siss'}, {'edit_schedule_personal_faculty_button': 'back'}, {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_FACULTY_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_FACULTY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS[0],
                                                  color=ButtonColor.SECONDARY,
                                                  payload=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_FACULTY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS[1],
                                                  color=ButtonColor.SECONDARY,
                                                  payload=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_FACULTY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS[2],
                                                  color=ButtonColor.SECONDARY,
                                                  payload=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_FACULTY_KB.add_row()
EDIT_SCHEDULE_PERSONAL_FACULTY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS[3],
                                                  color=ButtonColor.SECONDARY,
                                                  payload=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS_PAYLOAD[3])
EDIT_SCHEDULE_PERSONAL_FACULTY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS[4],
                                                  color=ButtonColor.SECONDARY,
                                                  payload=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS_PAYLOAD[4])
EDIT_SCHEDULE_PERSONAL_FACULTY_KB.add_row()
EDIT_SCHEDULE_PERSONAL_FACULTY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS[5],
                                                  color=ButtonColor.PRIMARY,
                                                  payload=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS_PAYLOAD[5])
EDIT_SCHEDULE_PERSONAL_FACULTY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS[6],
                                                  color=ButtonColor.PRIMARY,
                                                  payload=EDIT_SCHEDULE_PERSONAL_FACULTY_BUTTONS_PAYLOAD[6])

'''
***
Создание клавиатур для потоков
***
'''

EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS: list = ['БФИ', 'БВТ', 'БСТ', 'БЭИ',
                                                  'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_stream_button': 'bfi'}, {'edit_schedule_personal_stream_button': 'bvt'},
                                                          {'edit_schedule_personal_stream_button': 'bst'}, {'edit_schedule_personal_stream_button': 'bei'}, {'edit_schedule_personal_stream_button': 'back'}, {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_STREAM_IT_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_STREAM_IT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_STREAM_IT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS[1],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_STREAM_IT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS[2],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_STREAM_IT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS[3],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS_PAYLOAD[3])
EDIT_SCHEDULE_PERSONAL_STREAM_IT_KB.add_row()
EDIT_SCHEDULE_PERSONAL_STREAM_IT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS[4],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS_PAYLOAD[4])
EDIT_SCHEDULE_PERSONAL_STREAM_IT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS[5],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_STREAM_IT_BUTTONS_PAYLOAD[5])

EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS: list = ['БАП', 'БПМ', 'БУТ',
                                                    'ЗРС', 'БИБ', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_stream_button': 'bap'}, {'edit_schedule_personal_stream_button': 'bpm'}, {'edit_schedule_personal_stream_button': 'but'},
                                                            {'edit_schedule_personal_stream_button': 'zrs'}, {'edit_schedule_personal_stream_button': 'bib'}, {'edit_schedule_personal_stream_button': 'back'}, {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS[0],
                                                      color=ButtonColor.SECONDARY,
                                                      payload=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS[1],
                                                      color=ButtonColor.SECONDARY,
                                                      payload=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS[2],
                                                      color=ButtonColor.SECONDARY,
                                                      payload=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_KB.add_row()
EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS[3],
                                                      color=ButtonColor.SECONDARY,
                                                      payload=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS_PAYLOAD[3])
EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS[4],
                                                      color=ButtonColor.SECONDARY,
                                                      payload=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS_PAYLOAD[4])
EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_KB.add_row()
EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS[5],
                                                      color=ButtonColor.PRIMARY,
                                                      payload=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS_PAYLOAD[5])
EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS[6],
                                                      color=ButtonColor.PRIMARY,
                                                      payload=EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_BUTTONS_PAYLOAD[6])

EDIT_SCHEDULE_PERSONAL_STREAM_RIT_BUTTONS: list = [
    'БРТ', 'БИК', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_STREAM_RIT_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_stream_button': 'brt'}, {'edit_schedule_personal_stream_button': 'bik'},
                                                           {'edit_schedule_personal_stream_button': 'back'}, {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_STREAM_RIT_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_STREAM_RIT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_RIT_BUTTONS[0],
                                                     color=ButtonColor.SECONDARY,
                                                     payload=EDIT_SCHEDULE_PERSONAL_STREAM_RIT_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_STREAM_RIT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_RIT_BUTTONS[1],
                                                     color=ButtonColor.SECONDARY,
                                                     payload=EDIT_SCHEDULE_PERSONAL_STREAM_RIT_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_STREAM_RIT_KB.add_row()
EDIT_SCHEDULE_PERSONAL_STREAM_RIT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_RIT_BUTTONS[2],
                                                     color=ButtonColor.PRIMARY,
                                                     payload=EDIT_SCHEDULE_PERSONAL_STREAM_RIT_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_STREAM_RIT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_RIT_BUTTONS[3],
                                                     color=ButtonColor.PRIMARY,
                                                     payload=EDIT_SCHEDULE_PERSONAL_STREAM_RIT_BUTTONS_PAYLOAD[3])

EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_BUTTONS: list = [
    'БЭЭ', 'БЭР', 'ББИ', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_stream_button': 'bee'}, {'edit_schedule_personal_stream_button': 'ber'},
                                                              {'edit_schedule_personal_stream_button': 'bbi'}, {'edit_schedule_personal_stream_button': 'back'}, {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_BUTTONS[0],
                                                        color=ButtonColor.SECONDARY,
                                                        payload=EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_BUTTONS[1],
                                                        color=ButtonColor.SECONDARY,
                                                        payload=EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_BUTTONS[2],
                                                        color=ButtonColor.SECONDARY,
                                                        payload=EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_KB.add_row()
EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_BUTTONS[3],
                                                        color=ButtonColor.PRIMARY,
                                                        payload=EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_BUTTONS_PAYLOAD[3])
EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_BUTTONS[4],
                                                        color=ButtonColor.PRIMARY,
                                                        payload=EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_BUTTONS_PAYLOAD[4])

EDIT_SCHEDULE_PERSONAL_STREAM_SISS_BUTTONS: list = ['БИН', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_STREAM_SISS_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_stream_button': 'bin'},
                                                            {'edit_schedule_personal_stream_button': 'back'}, {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_STREAM_SISS_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_STREAM_SISS_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_SISS_BUTTONS[0],
                                                      color=ButtonColor.SECONDARY,
                                                      payload=EDIT_SCHEDULE_PERSONAL_STREAM_SISS_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_STREAM_SISS_KB.add_row()
EDIT_SCHEDULE_PERSONAL_STREAM_SISS_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_SISS_BUTTONS[1],
                                                      color=ButtonColor.PRIMARY,
                                                      payload=EDIT_SCHEDULE_PERSONAL_STREAM_SISS_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_STREAM_SISS_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_STREAM_SISS_BUTTONS[2],
                                                      color=ButtonColor.PRIMARY,
                                                      payload=EDIT_SCHEDULE_PERSONAL_STREAM_SISS_BUTTONS_PAYLOAD[2])

'''
***
Создание клавиатур для групп
***
'''

# ----- БФИ ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BFI_BUTTONS: list = ['БФИ2101', 'БФИ2102',
                                                  'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BFI_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'bfi2101'}, {'edit_schedule_personal_group_button': 'bfi2102'},
                                                          {'edit_schedule_personal_group_button': 'back'}, {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BFI_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BFI_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BFI_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BFI_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BFI_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BFI_BUTTONS[1],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BFI_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BFI_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BFI_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BFI_BUTTONS[2],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BFI_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_GROUP_BFI_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BFI_BUTTONS[3],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BFI_BUTTONS_PAYLOAD[3])

# ----- БВТ ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS: list = ['БВТ2101', 'БВТ2102', 'БВТ2103', 'БВТ2104', 'БВТ2105',
                                                  'БВТ2106', 'БВТ2107', 'БВТ2108', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'bvt2101'},
                                                          {'edit_schedule_personal_group_button': 'bvt2102'},
                                                          {'edit_schedule_personal_group_button': 'bvt2103'},
                                                          {'edit_schedule_personal_group_button': 'bvt2104'},
                                                          {'edit_schedule_personal_group_button': 'bvt2105'},
                                                          {'edit_schedule_personal_group_button': 'bvt2106'},
                                                          {'edit_schedule_personal_group_button': 'bvt2107'},
                                                          {'edit_schedule_personal_group_button': 'bvt2108'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS[1],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS[2],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS[3],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS_PAYLOAD[3])
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS[4],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS_PAYLOAD[4])
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS[5],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS_PAYLOAD[5])
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS[6],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS_PAYLOAD[6])
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS[7],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS_PAYLOAD[7])
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS[8],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS_PAYLOAD[8])
EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS[9],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BVT_BUTTONS_PAYLOAD[9])

# ----- БСТ ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS: list = ['БСТ2101', 'БСТ2102', 'БСТ2103', 'БСТ2104', 'БСТ2105',
                                                  'БСТ2106', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'bst2101'},
                                                          {'edit_schedule_personal_group_button': 'bst2102'},
                                                          {'edit_schedule_personal_group_button': 'bst2103'},
                                                          {'edit_schedule_personal_group_button': 'bst2104'},
                                                          {'edit_schedule_personal_group_button': 'bst2105'},
                                                          {'edit_schedule_personal_group_button': 'bst2106'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BST_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BST_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BST_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS[1],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BST_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS[2],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_GROUP_BST_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BST_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS[3],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS_PAYLOAD[3])
EDIT_SCHEDULE_PERSONAL_GROUP_BST_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS[4],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS_PAYLOAD[4])
EDIT_SCHEDULE_PERSONAL_GROUP_BST_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS[5],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS_PAYLOAD[5])
EDIT_SCHEDULE_PERSONAL_GROUP_BST_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BST_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS[6],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS_PAYLOAD[6])
EDIT_SCHEDULE_PERSONAL_GROUP_BST_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS[7],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BST_BUTTONS_PAYLOAD[7])

# ----- БЭИ ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BEI_BUTTONS: list = ['БЭИ2101', 'БЭИ2102', 'БЭИ2103',
                                                  'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BEI_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'bei2101'},
                                                          {'edit_schedule_personal_group_button': 'bei2102'},
                                                          {'edit_schedule_personal_group_button': 'bei2103'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BEI_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BEI_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BEI_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BEI_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BEI_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BEI_BUTTONS[1],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BEI_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BEI_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BEI_BUTTONS[2],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BEI_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_GROUP_BEI_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BEI_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BEI_BUTTONS[3],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BEI_BUTTONS_PAYLOAD[3])
EDIT_SCHEDULE_PERSONAL_GROUP_BEI_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BEI_BUTTONS[4],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BEI_BUTTONS_PAYLOAD[4])

# ----- БАП ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BAP_BUTTONS: list = ['БАП2101', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BAP_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'bap2101'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BAP_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BAP_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BAP_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BAP_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BAP_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BAP_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BAP_BUTTONS[1],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BAP_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BAP_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BAP_BUTTONS[2],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BAP_BUTTONS_PAYLOAD[2])

# ----- БПМ ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BPM_BUTTONS: list = ['БПМ2101', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BPM_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'bpm2101'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BPM_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BPM_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BPM_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BPM_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BPM_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BPM_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BPM_BUTTONS[1],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BPM_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BPM_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BPM_BUTTONS[2],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BPM_BUTTONS_PAYLOAD[2])

# ----- БУТ ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BUT_BUTTONS: list = ['БУТ2101', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BUT_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'but2101'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BUT_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BUT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BUT_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BUT_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BUT_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BUT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BUT_BUTTONS[1],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BUT_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BUT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BUT_BUTTONS[2],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BUT_BUTTONS_PAYLOAD[2])

# ----- ЗРС ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_BUTTONS: list = ['ЗРС2101', 'ЗРС2102',
                                                  'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'zrs2101'},
                                                          {'edit_schedule_personal_group_button': 'zrs2102'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_BUTTONS[1],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_BUTTONS[2],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_BUTTONS[3],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_BUTTONS_PAYLOAD[3])


# ----- БИБ ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS: list = ['БИБ2101', 'БИБ2102', 'БИБ2103',
                                                  'БИБ2104', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'bib2101'},
                                                          {'edit_schedule_personal_group_button': 'bib2102'},
                                                          {'edit_schedule_personal_group_button': 'bib2103'},
                                                          {'edit_schedule_personal_group_button': 'bib2104'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BIB_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BIB_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BIB_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS[1],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BIB_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS[2],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_GROUP_BIB_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BIB_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS[3],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS_PAYLOAD[3])
EDIT_SCHEDULE_PERSONAL_GROUP_BIB_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BIB_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS[4],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS_PAYLOAD[4])
EDIT_SCHEDULE_PERSONAL_GROUP_BIB_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS[5],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIB_BUTTONS_PAYLOAD[5])

# ----- БРТ ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BRT_BUTTONS: list = ['БРТ2101', 'БРТ2102',
                                                  'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BRT_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'brt2101'},
                                                          {'edit_schedule_personal_group_button': 'brt2102'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BRT_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BRT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BRT_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BRT_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BRT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BRT_BUTTONS[1],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BRT_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BRT_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BRT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BRT_BUTTONS[2],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BRT_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_GROUP_BRT_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BRT_BUTTONS[3],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BRT_BUTTONS_PAYLOAD[3])

# ----- БИК ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS: list = ['БИК2101', 'БИК2102', 'БИК2103', 'БИК2104', 'БИК2105',
                                                  'БИК2106', 'БИК2107', 'БИК2108', 'БИК2109', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'bik2101'},
                                                          {'edit_schedule_personal_group_button': 'bik2102'},
                                                          {'edit_schedule_personal_group_button': 'bik2103'},
                                                          {'edit_schedule_personal_group_button': 'bik2104'},
                                                          {'edit_schedule_personal_group_button': 'bik2105'},
                                                          {'edit_schedule_personal_group_button': 'bik2106'},
                                                          {'edit_schedule_personal_group_button': 'bik2107'},
                                                          {'edit_schedule_personal_group_button': 'bik2108'},
                                                          {'edit_schedule_personal_group_button': 'bik2109'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS[1],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS[2],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS[3],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS_PAYLOAD[3])
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS[4],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS_PAYLOAD[4])
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS[5],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS_PAYLOAD[5])
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS[6],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS_PAYLOAD[6])
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS[7],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS_PAYLOAD[7])
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS[8],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS_PAYLOAD[8])
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS[9],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS_PAYLOAD[9])
EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS[10],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIK_BUTTONS_PAYLOAD[10])

# ----- БЭЭ ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BEE_BUTTONS: list = ['БЭЭ2101', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BEE_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'bee2101'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BEE_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BEE_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BEE_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BEE_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BEE_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BEE_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BEE_BUTTONS[1],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BEE_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BEE_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BEE_BUTTONS[2],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BEE_BUTTONS_PAYLOAD[2])

# ----- БЭР ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BER_BUTTONS: list = ['БЭР2101', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BER_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'ber2101'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BER_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BER_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BER_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BER_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BER_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BER_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BER_BUTTONS[1],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BER_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BER_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BER_BUTTONS[2],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BER_BUTTONS_PAYLOAD[2])

# ----- ББИ ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BBI_BUTTONS: list = ['ББИ2101', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BBI_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'bbi2101'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BBI_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BBI_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BBI_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BBI_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BBI_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BBI_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BBI_BUTTONS[1],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BBI_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BBI_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BBI_BUTTONS[2],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BBI_BUTTONS_PAYLOAD[2])

# ----- БИН ----- #

EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS: list = ['БИН2101', 'БИН2102', 'БИН2103', 'БИН2104', 'БИН2105',
                                                  'БИН2106', 'БИН2107', 'БИН2108', 'БИН2109', 'БИН2110', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_group_button': 'bin2101'},
                                                          {'edit_schedule_personal_group_button': 'bin2102'},
                                                          {'edit_schedule_personal_group_button': 'bin2103'},
                                                          {'edit_schedule_personal_group_button': 'bin2104'},
                                                          {'edit_schedule_personal_group_button': 'bin2105'},
                                                          {'edit_schedule_personal_group_button': 'bin2106'},
                                                          {'edit_schedule_personal_group_button': 'bin2107'},
                                                          {'edit_schedule_personal_group_button': 'bin2108'},
                                                          {'edit_schedule_personal_group_button': 'bin2109'},
                                                          {'edit_schedule_personal_group_button': 'bin2110'},
                                                          {'edit_schedule_personal_group_button': 'back'},
                                                          {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS[0],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS[1],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS[2],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS[3],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS_PAYLOAD[3])
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS[4],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS_PAYLOAD[4])
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS[5],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS_PAYLOAD[5])
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS[6],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS_PAYLOAD[6])
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS[7],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS_PAYLOAD[7])
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS[8],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS_PAYLOAD[8])
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS[9],
                                                    color=ButtonColor.SECONDARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS_PAYLOAD[9])
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_row()
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS[10],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS_PAYLOAD[10])
EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS[11],
                                                    color=ButtonColor.PRIMARY,
                                                    payload=EDIT_SCHEDULE_PERSONAL_GROUP_BIN_BUTTONS_PAYLOAD[11])


EDIT_SCHEDULE_PERSONAL_FACULTY_MATCHING = {
    'it': EDIT_SCHEDULE_PERSONAL_STREAM_IT_KB,
    'kiib': EDIT_SCHEDULE_PERSONAL_STREAM_KIIB_KB,
    'rit': EDIT_SCHEDULE_PERSONAL_STREAM_RIT_KB,
    'tseimk': EDIT_SCHEDULE_PERSONAL_STREAM_TSEIMK_KB,
    'siss': EDIT_SCHEDULE_PERSONAL_STREAM_SISS_KB
}

EDIT_SCHEDULE_PERSONAL_STREAM_MATCHING = {
    'bfi': EDIT_SCHEDULE_PERSONAL_GROUP_BFI_KB,
    'bvt': EDIT_SCHEDULE_PERSONAL_GROUP_BVT_KB,
    'bst': EDIT_SCHEDULE_PERSONAL_GROUP_BST_KB,
    'bei': EDIT_SCHEDULE_PERSONAL_GROUP_BEI_KB,
    'bap': EDIT_SCHEDULE_PERSONAL_GROUP_BAP_KB,
    'bpm': EDIT_SCHEDULE_PERSONAL_GROUP_BPM_KB,
    'but': EDIT_SCHEDULE_PERSONAL_GROUP_BUT_KB,
    'zrs': EDIT_SCHEDULE_PERSONAL_GROUP_ZRS_KB,
    'bib': EDIT_SCHEDULE_PERSONAL_GROUP_BIB_KB,
    'brt': EDIT_SCHEDULE_PERSONAL_GROUP_BRT_KB,
    'bik': EDIT_SCHEDULE_PERSONAL_GROUP_BIK_KB,
    'bee': EDIT_SCHEDULE_PERSONAL_GROUP_BEE_KB,
    'ber': EDIT_SCHEDULE_PERSONAL_GROUP_BER_KB,
    'bbi': EDIT_SCHEDULE_PERSONAL_GROUP_BBI_KB,
    'bin': EDIT_SCHEDULE_PERSONAL_GROUP_BIN_KB
}

'''
***
Создание клавиатур для четности
***
'''

EDIT_SCHEDULE_PERSONAL_PARITY_BUTTONS: list = ['Четная неделя', 'Нечетная неделя',
                                               'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_PARITY_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_parity_button': 'even'},
                                                       {'edit_schedule_personal_parity_button': 'odd'},
                                                       {'edit_schedule_personal_parity_button': 'back'},
                                                       {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_PARITY_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_PARITY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_PARITY_BUTTONS[0],
                                                 color=ButtonColor.SECONDARY,
                                                 payload=EDIT_SCHEDULE_PERSONAL_PARITY_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_PARITY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_PARITY_BUTTONS[1],
                                                 color=ButtonColor.SECONDARY,
                                                 payload=EDIT_SCHEDULE_PERSONAL_PARITY_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_PARITY_KB.add_row()
EDIT_SCHEDULE_PERSONAL_PARITY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_PARITY_BUTTONS[2],
                                                 color=ButtonColor.PRIMARY,
                                                 payload=EDIT_SCHEDULE_PERSONAL_PARITY_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_PARITY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_PARITY_BUTTONS[3],
                                                 color=ButtonColor.PRIMARY,
                                                 payload=EDIT_SCHEDULE_PERSONAL_PARITY_BUTTONS_PAYLOAD[3])

'''
***
Создание клавиатур для дней недели
***
'''

EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS: list = ['Понедельник', 'Вторник', 'Среда',
                                            'Четверг', 'Пятница', 'Суббота',
                                            'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_day_button': 'ponedelnik'},
                                                    {'edit_schedule_personal_day_button': 'vtornik'},
                                                    {'edit_schedule_personal_day_button': 'sreda'},
                                                    {'edit_schedule_personal_day_button': 'chetverg'},
                                                    {'edit_schedule_personal_day_button': 'pjatnitsa'},
                                                    {'edit_schedule_personal_day_button': 'subbota'},
                                                    {'edit_schedule_personal_day_button': 'back'},
                                                    {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_DAY_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_DAY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS[0],
                                              color=ButtonColor.SECONDARY,
                                              payload=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_DAY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS[1],
                                              color=ButtonColor.SECONDARY,
                                              payload=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_DAY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS[2],
                                              color=ButtonColor.SECONDARY,
                                              payload=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_DAY_KB.add_row()
EDIT_SCHEDULE_PERSONAL_DAY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS[3],
                                              color=ButtonColor.SECONDARY,
                                              payload=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS_PAYLOAD[3])
EDIT_SCHEDULE_PERSONAL_DAY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS[4],
                                              color=ButtonColor.SECONDARY,
                                              payload=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS_PAYLOAD[4])
EDIT_SCHEDULE_PERSONAL_DAY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS[5],
                                              color=ButtonColor.SECONDARY,
                                              payload=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS_PAYLOAD[5])
EDIT_SCHEDULE_PERSONAL_DAY_KB.add_row()
EDIT_SCHEDULE_PERSONAL_DAY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS[6],
                                              color=ButtonColor.PRIMARY,
                                              payload=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS_PAYLOAD[6])
EDIT_SCHEDULE_PERSONAL_DAY_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS[7],
                                              color=ButtonColor.PRIMARY,
                                              payload=EDIT_SCHEDULE_PERSONAL_DAY_BUTTONS_PAYLOAD[7])

'''
***
Создание клавиатур для выбора пары
***
'''

EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS: list = ['1 пара', '2 пара', '3 пара',
                                             '4 пара', '5 пара', 'Общ. аннотация',
                                             'Сбросить все изменения', 'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_pair_button': 'first_pair'},
                                                     {'edit_schedule_personal_pair_button': 'second_pair'},
                                                     {'edit_schedule_personal_pair_button': 'third_pair'},
                                                     {'edit_schedule_personal_pair_button': 'fourth_pair'},
                                                     {'edit_schedule_personal_pair_button': 'fifth_pair'},
                                                     {'edit_schedule_personal_pair_button': 'whole_day'},
                                                     {'edit_schedule_personal_pair_button': 'reset_day'},
                                                     {'edit_schedule_personal_pair_button': 'back'},
                                                     {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_PAIR_KB: Keyboard = Keyboard(one_time=False)

EDIT_SCHEDULE_PERSONAL_PAIR_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS[0],
                                               color=ButtonColor.SECONDARY,
                                               payload=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_PAIR_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS[1],
                                               color=ButtonColor.SECONDARY,
                                               payload=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_PAIR_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS[2],
                                               color=ButtonColor.SECONDARY,
                                               payload=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_PAIR_KB.add_row()
EDIT_SCHEDULE_PERSONAL_PAIR_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS[3],
                                               color=ButtonColor.SECONDARY,
                                               payload=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS_PAYLOAD[3])
EDIT_SCHEDULE_PERSONAL_PAIR_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS[4],
                                               color=ButtonColor.SECONDARY,
                                               payload=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS_PAYLOAD[4])
EDIT_SCHEDULE_PERSONAL_PAIR_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS[5],
                                               color=ButtonColor.SECONDARY,
                                               payload=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS_PAYLOAD[5])
EDIT_SCHEDULE_PERSONAL_PAIR_KB.add_row()
EDIT_SCHEDULE_PERSONAL_PAIR_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS[6],
                                               color=ButtonColor.NEGATIVE,
                                               payload=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS_PAYLOAD[6])
EDIT_SCHEDULE_PERSONAL_PAIR_KB.add_row()
EDIT_SCHEDULE_PERSONAL_PAIR_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS[7],
                                               color=ButtonColor.PRIMARY,
                                               payload=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS_PAYLOAD[7])
EDIT_SCHEDULE_PERSONAL_PAIR_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS[8],
                                               color=ButtonColor.PRIMARY,
                                               payload=EDIT_SCHEDULE_PERSONAL_PAIR_BUTTONS_PAYLOAD[8])

'''
***
Создание клавиатур для выбора действия с парой
***
'''

EDIT_SCHEDULE_PERSONAL_MOVE_BUTTONS: list = ['Перезаписать(записать)', 'Удалить',
                                             'Назад', 'Меню']
EDIT_SCHEDULE_PERSONAL_MOVE_BUTTONS_PAYLOAD: list = [{'edit_schedule_personal_move_button': 'rewrite'},
                                                     {'edit_schedule_personal_move_button': 'delete'},
                                                     {'edit_schedule_personal_move_button': 'back'},
                                                     {'button': 'menu'}]
EDIT_SCHEDULE_PERSONAL_MOVE_KB: Keyboard = Keyboard(one_time=True)

EDIT_SCHEDULE_PERSONAL_MOVE_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_MOVE_BUTTONS[0],
                                               color=ButtonColor.SECONDARY,
                                               payload=EDIT_SCHEDULE_PERSONAL_MOVE_BUTTONS_PAYLOAD[0])
EDIT_SCHEDULE_PERSONAL_MOVE_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_MOVE_BUTTONS[1],
                                               color=ButtonColor.SECONDARY,
                                               payload=EDIT_SCHEDULE_PERSONAL_MOVE_BUTTONS_PAYLOAD[1])
EDIT_SCHEDULE_PERSONAL_MOVE_KB.add_row()
EDIT_SCHEDULE_PERSONAL_MOVE_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_MOVE_BUTTONS[2],
                                               color=ButtonColor.PRIMARY,
                                               payload=EDIT_SCHEDULE_PERSONAL_MOVE_BUTTONS_PAYLOAD[2])
EDIT_SCHEDULE_PERSONAL_MOVE_KB.add_text_button(text=EDIT_SCHEDULE_PERSONAL_MOVE_BUTTONS[3],
                                               color=ButtonColor.PRIMARY,
                                               payload=EDIT_SCHEDULE_PERSONAL_MOVE_BUTTONS_PAYLOAD[3])
