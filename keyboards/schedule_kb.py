from vkwave.bots import Keyboard, ButtonColor

GROUP_BUTTONS_BFI_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BVT_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BST_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BEI_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BIB_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BIN_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BAP_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BMP_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BUT_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_ZRC_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BRT_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BIK_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BEE_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BER_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BBI_KB: Keyboard = Keyboard(one_time=False)
STREAM_KB: Keyboard = Keyboard(one_time=False)
DAYS_OF_WEEK_KB: Keyboard = Keyboard(one_time=False)
CURRENT_OR_NEXT_WEEK_KB: Keyboard = Keyboard(one_time=False)


# Названия кнопок
STREAM_BUTTONS: list = ['бфи', 'бвт', 'бст', 'бэи', 'биб', 'бин', 'бап', 'бмп', 'бут', 'зрс', 'брт', 'бээ', 'бэр', 'бби']
DAYS_OF_WEEK_BUTTONS: list = ['сегодня', 'завтра', 'вся неделя']
CURRENT_OR_NEXT_WEEK_BUTTONS: list = ['текущая неделя', 'следующая неделя']
GROUP_BUTTONS_BFI: list = ['бфи2101', 'бфи2102']
GROUP_BUTTONS_BVT: list = ['бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106', 'бвт2107', 'бвт2108']
GROUP_BUTTONS_BST: list = ['бст2101', 'бст2102', 'бст2103', 'бст2104', 'бст2105', 'бст2106']
GROUP_BUTTONS_BEI: list = ['бэи2101', 'бэи2102', 'бэи2103']
GROUP_BUTTONS_BIB: list = ['биб2101', 'биб2102', 'биб2103', 'биб2104']
GROUP_BUTTONS_BIN: list = ['бин2101', 'бин2102', 'бин2103', 'бин2104', 'бин2105', 'бин2106', 'бин2107', 'бин2108', 'бин2109', 'бин2110']
GROUP_BUTTONS_BAP: list = ['бап2101']
GROUP_BUTTONS_BMP: list = ['бмп2101']
GROUP_BUTTONS_BUT: list = ['бут2101']
GROUP_BUTTONS_BEE: list = ['бээ2101']
GROUP_BUTTONS_BER: list = ['бэр2101']
GROUP_BUTTONS_BBI: list = ['бби2101']
GROUP_BUTTONS_ZRC: list = ['зрс2101', 'зрс2102']
GROUP_BUTTONS_BRT: list = ['брт2101', 'брт2102']
""" GROUP_BUTTONS_BIK: list = ['бик2101', 'бик2102', 'бик2103', 'бик2104', 'бик2105', 'бик2106', 'бик2107', 'бик2108', 'бик2109'] """
GROUP_BUTTONS: list = ['бфи2101', 'бфи2102', 'бвт2101', 'бвт2102', 'бвт2103', 'бвт2104',
                       'бвт2105', 'бвт2106', 'бвт2107', 'бвт2108', 'бст2101', 'бст2102',
                       'бст2103', 'бст2104', 'бст2105', 'бст2106', 'бэи2101', 'бэи2102',
                       'бэи2103', 'биб2102', 'биб2103', 'биб2104', 'бин2101', 'бин2102',
                       'бин2103', 'бин2104', 'бин2105', 'бин2106', 'бин2107', 'бин2108',
                       'бин2109', 'бин2110', 'бмп2101', 'зрс2101', 'зрс2102', 'бап2101',
                       'бут2101', 'брт2101', 'брт2102', 'бби2101', 'бэр2101', 'бээ2101']

# Payload кнопок
STREAM_BUTTONS_PAYLOAD: list = [{"stream_button": "bfi"}, {"stream_button": "bvt"}, {"stream_button": "bst"}, {"stream_button": "bei"},
                                {"stream_button": "bib"}, {"stream_button": "bin"}, {"stream_button": "bmp"}, {"stream_button": "zrc"},
                                {"stream_button": "bap"}, {"stream_button": "but"},  {"stream_button": "brt"}, {"stream_button": "bee"},
                                {"stream_button": "ber"}, {"stream_button": "bbi"}]
DAYS_OF_WEEK_BUTTONS_PAYLOAD: list = [{"dow_button": "today"}, {"dow_button": "tommorow"}, {"dow_button": "full week"}]
CURRENT_OR_NEXT_WEEK_BUTTONS_PAYLOAD: list = [{"conw_button": "current week"}, {"conw_button": "next week"}]
GROUP_BUTTONS_BFI_PAYLOAD: list = [{"group_button": "bfi2101"}, {"group_button": "bfi2102"}]
GROUP_BUTTONS_BVT_PAYLOAD: list = [{"group_button": "bvt2101"}, {"group_button": "bvt2102"}, {"group_button": "bvt2103"}, {
    "group_button": "bvt2104"}, {"group_button": "bvt2105"}, {"group_button": "bvt2106"}, {"group_button": "bvt2107"}, {"group_button": "bvt2108"}]
GROUP_BUTTONS_BST_PAYLOAD: list = [{"group_button": "bst2101"}, {"group_button": "bst2102"}, {"group_button": "bst2103"}, {"group_button": "bst2104"}, {"group_button": "bst2105"}, {"group_button": "bst2106"}]
GROUP_BUTTONS_BEI_PAYLOAD: list = [{"group_button": 'bei2101'}, {"group_button": 'bei2102'}, {"group_button": 'bei2103'}]
GROUP_BUTTONS_BIB_PAYLOAD: list = [{"group_button": 'bib2101'}, {"group_button": 'bib2102'}, {"group_button": 'bib2103'}, {"group_button": 'bib2104'}]
GROUP_BUTTONS_BIN_PAYLOAD: list = [{"group_button": "bin2101"}, {"group_button": "bin2102"}, {"group_button": "bin2103"}, {
    "group_button": "bin2104"}, {"group_button": "bin2105"}, {"group_button": "bin2106"}, {"group_button": "bin2107"}, {"group_button": "bin2108"},
    {"group_button": "bin2109"}, {"group_button": "bin2110"}]
GROUP_BUTTONS_BMP_PAYLOAD: list = [{"group_button": "bmp2101"}]
GROUP_BUTTONS_ZRC_PAYLOAD: list = [{"group_button": 'zrc2101'}, {"group_button": 'zrc2102'}]
GROUP_BUTTONS_BAP_PAYLOAD: list = [{"group_button": 'bap2101'}]
GROUP_BUTTONS_BEE_PAYLOAD: list = [{"group_button": 'bee2101'}]
GROUP_BUTTONS_BBI_PAYLOAD: list = [{"group_button": 'bbi2101'}]
GROUP_BUTTONS_BER_PAYLOAD: list = [{"group_button": 'ber2101'}]
GROUP_BUTTONS_BUT_PAYLOAD: list = [{"group_button": "but2101"}, {"group_button": "but2102"}, {"group_button": "but2103"}]
GROUP_BUTTONS_BRT_PAYLOAD: list = [{"group_button": 'brt2101'}, {"group_button": 'brt2102'}]
""" GROUP_BUTTONS_BIK_PAYLOAD: list = [{"group_button": "bik2101"}, {"group_button": "bik2102"}, {"group_button": "bik2103"}, {
    "group_button": "bik2104"}, {"group_button": "bik2105"}, {"group_button": "bik2106"}, {"group_button": "bik2107"}, {"group_button": "bik2108"},
    {"group_button": "bik2109"}] """

# Генерация кнопок

for i in range(1, len(STREAM_BUTTONS) + 1):
    STREAM_KB.add_text_button(text=STREAM_BUTTONS[i - 1].upper(), color=ButtonColor.SECONDARY, payload=STREAM_BUTTONS_PAYLOAD[i - 1])
    if i % 3 == 0:
        STREAM_KB.add_row()
    if i == len(STREAM_BUTTONS):
        STREAM_KB.add_row()
        STREAM_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(DAYS_OF_WEEK_BUTTONS) + 1):
    DAYS_OF_WEEK_KB.add_text_button(text=DAYS_OF_WEEK_BUTTONS[i - 1].capitalize(), color=ButtonColor.SECONDARY, payload=DAYS_OF_WEEK_BUTTONS_PAYLOAD[i - 1])
    if i == len(DAYS_OF_WEEK_BUTTONS):
        DAYS_OF_WEEK_KB.add_row()
        DAYS_OF_WEEK_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BFI) + 1):
    GROUP_BUTTONS_BFI_KB.add_text_button(text=GROUP_BUTTONS_BFI[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BFI_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BFI):
        GROUP_BUTTONS_BFI_KB.add_row()
        GROUP_BUTTONS_BFI_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BVT) + 1):
    GROUP_BUTTONS_BVT_KB.add_text_button(text=GROUP_BUTTONS_BVT[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BVT_PAYLOAD[i - 1])
    if i == 3 or i == 6:
        GROUP_BUTTONS_BVT_KB.add_row()
    if i == len(GROUP_BUTTONS_BVT):
        GROUP_BUTTONS_BVT_KB.add_row()
        GROUP_BUTTONS_BVT_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BST) + 1):
    GROUP_BUTTONS_BST_KB.add_text_button(text=GROUP_BUTTONS_BST[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BST_PAYLOAD[i - 1])
    if i == 3:
        GROUP_BUTTONS_BST_KB.add_row()
    if i == len(GROUP_BUTTONS_BST):
        GROUP_BUTTONS_BST_KB.add_row()
        GROUP_BUTTONS_BST_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BEI) + 1):
    GROUP_BUTTONS_BEI_KB.add_text_button(text=GROUP_BUTTONS_BEI[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BEI_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BEI):
        GROUP_BUTTONS_BEI_KB.add_row()
        GROUP_BUTTONS_BEI_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BIB) + 1):
    GROUP_BUTTONS_BIB_KB.add_text_button(text=GROUP_BUTTONS_BIB[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BIB_PAYLOAD[i - 1])
    if i % 3 == 0:
        GROUP_BUTTONS_BIB_KB.add_row()
    if i == len(GROUP_BUTTONS_BIB):
        GROUP_BUTTONS_BIB_KB.add_row()
        GROUP_BUTTONS_BIB_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BIN) + 1):
    GROUP_BUTTONS_BIN_KB.add_text_button(text=GROUP_BUTTONS_BIN[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BIN_PAYLOAD[i - 1])
    if i % 3 == 0:
        GROUP_BUTTONS_BIN_KB.add_row()
    if i == len(GROUP_BUTTONS_BIN):
        GROUP_BUTTONS_BIN_KB.add_row()
        GROUP_BUTTONS_BIN_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BMP) + 1):
    GROUP_BUTTONS_BMP_KB.add_text_button(text=GROUP_BUTTONS_BMP[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BMP_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BMP):
        GROUP_BUTTONS_BMP_KB.add_row()
        GROUP_BUTTONS_BMP_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BUT) + 1):
    GROUP_BUTTONS_BUT_KB.add_text_button(text=GROUP_BUTTONS_BUT[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BUT_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BUT):
        GROUP_BUTTONS_BUT_KB.add_row()
        GROUP_BUTTONS_BUT_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_ZRC) + 1):
    GROUP_BUTTONS_ZRC_KB.add_text_button(text=GROUP_BUTTONS_ZRC[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_ZRC_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_ZRC):
        GROUP_BUTTONS_ZRC_KB.add_row()
        GROUP_BUTTONS_ZRC_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BAP) + 1):
    GROUP_BUTTONS_BAP_KB.add_text_button(text=GROUP_BUTTONS_BAP[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BAP_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BAP):
        GROUP_BUTTONS_BAP_KB.add_row()
        GROUP_BUTTONS_BAP_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BRT) + 1):
    GROUP_BUTTONS_BRT_KB.add_text_button(text=GROUP_BUTTONS_BRT[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BRT_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BRT):
        GROUP_BUTTONS_BRT_KB.add_row()
        GROUP_BUTTONS_BRT_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
""" for i in range(1, len(GROUP_BUTTONS_BIK) + 1):
    GROUP_BUTTONS_BIK_KB.add_text_button(text=GROUP_BUTTONS_BIK[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BIK_PAYLOAD[i - 1])
    if i % 3 == 0:
        GROUP_BUTTONS_BIK_KB.add_row()
    if i == len(GROUP_BUTTONS_BIK):
        GROUP_BUTTONS_BIK_KB.add_row()
        GROUP_BUTTONS_BIK_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"}) """
for i in range(1, len(GROUP_BUTTONS_BBI) + 1):
    GROUP_BUTTONS_BBI_KB.add_text_button(text=GROUP_BUTTONS_BBI[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BBI_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BBI):
        GROUP_BUTTONS_BBI_KB.add_row()
        GROUP_BUTTONS_BBI_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BER) + 1):
    GROUP_BUTTONS_BER_KB.add_text_button(text=GROUP_BUTTONS_BER[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BER_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BER):
        GROUP_BUTTONS_BER_KB.add_row()
        GROUP_BUTTONS_BER_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BEE) + 1):
    GROUP_BUTTONS_BEE_KB.add_text_button(text=GROUP_BUTTONS_BEE[i - 1].upper(), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BEE_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BEE):
        GROUP_BUTTONS_BEE_KB.add_row()
        GROUP_BUTTONS_BEE_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(CURRENT_OR_NEXT_WEEK_BUTTONS) + 1):
    CURRENT_OR_NEXT_WEEK_KB.add_text_button(text=CURRENT_OR_NEXT_WEEK_BUTTONS[i - 1].capitalize(), color=ButtonColor.SECONDARY, payload=CURRENT_OR_NEXT_WEEK_BUTTONS_PAYLOAD[i - 1])
    if i == len(CURRENT_OR_NEXT_WEEK_BUTTONS):
        CURRENT_OR_NEXT_WEEK_KB.add_row()
        CURRENT_OR_NEXT_WEEK_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})

# Задание получения клавиатур

KB = {'бфи': GROUP_BUTTONS_BFI_KB.get_keyboard,
      'бвт': GROUP_BUTTONS_BVT_KB.get_keyboard,
      'бст': GROUP_BUTTONS_BST_KB.get_keyboard,
      'бэи': GROUP_BUTTONS_BEI_KB.get_keyboard,
      'биб': GROUP_BUTTONS_BIB_KB.get_keyboard,
      'бин': GROUP_BUTTONS_BIN_KB.get_keyboard,
      'бмп': GROUP_BUTTONS_BMP_KB.get_keyboard,
      'зрс': GROUP_BUTTONS_ZRC_KB.get_keyboard,
      'бап': GROUP_BUTTONS_BAP_KB.get_keyboard,
      'бут': GROUP_BUTTONS_BUT_KB.get_keyboard,
      'брт': GROUP_BUTTONS_BRT_KB.get_keyboard,
      'бби': GROUP_BUTTONS_BBI_KB.get_keyboard,
      'бээ': GROUP_BUTTONS_BEE_KB.get_keyboard,
      'бэр': GROUP_BUTTONS_BER_KB.get_keyboard}
