from vkwave.bots import Keyboard, ButtonColor

CHOOSE_WEEK_PERSONAL_BUTTONS: list = ['четная неделя', 'нечетная неделя']
CHOOSE_WEEK_PERSONAL_PAYLOAD: list = [{"cwp_button": "even"},
                                      {"cwp_button": "odd"}]
# Создание экземпляров клавиатуры

CHOOSE_WEEK_PERSONAL_KB: Keyboard = Keyboard(one_time=False)

for i in range(len(CHOOSE_WEEK_PERSONAL_BUTTONS)):
    CHOOSE_WEEK_PERSONAL_KB.add_text_button(text=CHOOSE_WEEK_PERSONAL_BUTTONS[i].capitalize(
    ), color=ButtonColor.SECONDARY, payload=CHOOSE_WEEK_PERSONAL_PAYLOAD[i])
    if i == 1:
        CHOOSE_WEEK_PERSONAL_KB.add_row()
        CHOOSE_WEEK_PERSONAL_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})

CHOOSE_DAY_OF_WEEK_PERSONAL_BUTTONS: list = [
    'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
CHOOSE_DAY_OF_WEEK_PERSONAL_PAYLOAD: list = [{"cdowp_button": "ponedelnik"}, {"cdowp_button": "vtornik"}, {
    "cdowp_button": "sreda"}, {"cdowp_button": "chetverg"}, {"cdowp_button": "pjatnitsa"}, {"cdowp_button": "subbota"}]
# Создание экземпляров клавиатуры

CHOOSE_DAY_OF_WEEK_PERSONAL_KB: Keyboard = Keyboard(one_time=False)

for i in range(len(CHOOSE_DAY_OF_WEEK_PERSONAL_BUTTONS)):
    CHOOSE_DAY_OF_WEEK_PERSONAL_KB.add_text_button(text=CHOOSE_DAY_OF_WEEK_PERSONAL_BUTTONS[i].capitalize(
    ), color=ButtonColor.SECONDARY, payload=CHOOSE_DAY_OF_WEEK_PERSONAL_PAYLOAD[i])
    if i == 2:
        CHOOSE_DAY_OF_WEEK_PERSONAL_KB.add_row()
    if i == len(CHOOSE_DAY_OF_WEEK_PERSONAL_BUTTONS) - 1:
        CHOOSE_DAY_OF_WEEK_PERSONAL_KB.add_row()
        CHOOSE_DAY_OF_WEEK_PERSONAL_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})


CHOOSE_PAIR_PERSONAL_BUTTONS: list = ['1 пара', '2 пара', '3 пара',
                                      '4 пара', '5 пара', 'общ. аннотация', 'сбросить все изменения']
CHOOSE_PAIR_PERSONAL_PAYLOAD: list = [{"cpp_button": "first"}, {"cpp_button": "second"}, {"cpp_button": "third"}, {
    "cpp_button": "fourth"}, {"cpp_button": "fifth"}, {"cpp_button": "forall"}, {"cpp_button": "resetall"}]
# Создание экземпляров клавиатуры

CHOOSE_PAIR_PERSONAL_KB: Keyboard = Keyboard(one_time=False)

for i in range(len(CHOOSE_PAIR_PERSONAL_BUTTONS)):
    CHOOSE_PAIR_PERSONAL_KB.add_text_button(text=CHOOSE_PAIR_PERSONAL_BUTTONS[i].capitalize(
    ), color=ButtonColor.SECONDARY, payload=CHOOSE_PAIR_PERSONAL_PAYLOAD[i])
    if i == 2:
        CHOOSE_PAIR_PERSONAL_KB.add_row()
    if i == 5:
        CHOOSE_PAIR_PERSONAL_KB.add_row()
        CHOOSE_PAIR_PERSONAL_KB.add_text_button(text=CHOOSE_PAIR_PERSONAL_BUTTONS[i + 1].capitalize(
        ), color=ButtonColor.NEGATIVE, payload=CHOOSE_PAIR_PERSONAL_PAYLOAD[i + 1])
        CHOOSE_PAIR_PERSONAL_KB.add_row()
        CHOOSE_PAIR_PERSONAL_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})
        break

CHOOSE_MOVE_PERSONAL_BUTTONS: list = ['перезаписать(Записать)', 'удалить']
CHOOSE_MOVE_PERSONAL_PAYLOAD: list = [
    {"cmp_button": "rewrite"}, {"cmp_button": "remove"}]
# Создание экземпляров клавиатуры

CHOOSE_MOVE_PERSONAL_KB: Keyboard = Keyboard(one_time=True)

for i in range(len(CHOOSE_MOVE_PERSONAL_BUTTONS)):
    CHOOSE_MOVE_PERSONAL_KB.add_text_button(text=CHOOSE_MOVE_PERSONAL_BUTTONS[i].capitalize(
    ), color=ButtonColor.SECONDARY, payload=CHOOSE_MOVE_PERSONAL_PAYLOAD[i])
    if i == 2:
        CHOOSE_MOVE_PERSONAL_KB.add_row()
    if i == len(CHOOSE_MOVE_PERSONAL_BUTTONS) - 1:
        CHOOSE_MOVE_PERSONAL_KB.add_row()
        CHOOSE_MOVE_PERSONAL_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={'button': 'menu'})

# Создание экземпляров клавиатур для групп
GROUP_BUTTONS_BFI_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BVT_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BST_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BEI_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BIB_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BAP_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BMP_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BUT_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_ZRC_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BRT_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BIK_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BEE_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BER_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BBI_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BIN_KB: Keyboard = Keyboard(one_time=False)

# Создание экземпляров клавиатур для факультетов
FACULTIES_BUTTONS_KB: Keyboard = Keyboard(one_time=False)

# Создание экземпляров клавиатур для потоков
STREAM_IT_BUTTONS_KB: Keyboard = Keyboard(one_time=False)
STREAM_TSEIMK_BUTTONS_KB: Keyboard = Keyboard(one_time=False)
STREAM_RIT_BUTTONS_KB: Keyboard = Keyboard(one_time=False)
STREAM_KIIB_BUTTONS_KB: Keyboard = Keyboard(one_time=False)
STREAM_SISS_BUTTONS_KB: Keyboard = Keyboard(one_time=False)
STREAM_KB: Keyboard = Keyboard(one_time=False)

# Создание экземпляров клавиатур для дней недели
DAYS_OF_WEEK_KB: Keyboard = Keyboard(one_time=False)
CURRENT_OR_NEXT_WEEK_KB: Keyboard = Keyboard(one_time=False)

# Названия кнопок для групп
GROUP_BUTTONS_BFI: list = ['бфи2101', 'бфи2102']
GROUP_BUTTONS_BVT: list = ['бвт2101', 'бвт2102', 'бвт2103',
                           'бвт2104', 'бвт2105', 'бвт2106', 'бвт2107', 'бвт2108']
GROUP_BUTTONS_BST: list = ['бст2101', 'бст2102',
                           'бст2103', 'бст2104', 'бст2105', 'бст2106']
GROUP_BUTTONS_BEI: list = ['бэи2101', 'бэи2102', 'бэи2103']
GROUP_BUTTONS_BIB: list = ['биб2101', 'биб2102', 'биб2103', 'биб2104']
GROUP_BUTTONS_BAP: list = ['бап2101']
GROUP_BUTTONS_BMP: list = ['бмп2101']
GROUP_BUTTONS_BUT: list = ['бут2101']
GROUP_BUTTONS_BEE: list = ['бээ2101']
GROUP_BUTTONS_BER: list = ['бэр2101']
GROUP_BUTTONS_BBI: list = ['бби2101']
GROUP_BUTTONS_ZRC: list = ['зрс2101', 'зрс2102']
GROUP_BUTTONS_BRT: list = ['брт2101', 'брт2102']
GROUP_BUTTONS_BIK: list = ['бик2101', 'бик2102', 'бик2103',
                           'бик2104', 'бик2105', 'бик2106', 'бик2107', 'бик2108', 'бик2109']
GROUP_BUTTONS_BIN: list = ['бин2101', 'бин2102', 'бин2103', 'бин2104',
                           'бин2105', 'бин2106', 'бин2107', 'бин2108', 'бин2109', 'бин2110']

# Названия кнопок для факультетов
FACULTIES_BUTTONS: list = ['ИТ', 'КиИБ', 'РиТ', 'ЦЭиМК', 'СиСС']

# Названия кнопок для потоков
STREAM_IT_BUTTONS: list = ['бфи', 'бвт', 'бст', 'бэи']
STREAM_TSEIMK_BUTTONS: list = ['бээ', 'бэр', 'бби']
STREAM_KIIB_BUTTONS: list = ['бап', 'бмп', 'бут', 'зрс', 'биб']
STREAM_RIT_BUTTONS: list = ['брт', 'бик']
STREAM_SISS_BUTTONS: list = ['бин']

# Названия кнопок для дней недели
DAYS_OF_WEEK_BUTTONS: list = [
    'сегодня', 'завтра', 'вся неделя', 'редактировать расписание', 'посмотреть аннотации']
CURRENT_OR_NEXT_WEEK_BUTTONS: list = ['текущая неделя', 'следующая неделя']


# Payload кнопок для групп
GROUP_BUTTONS_BFI_PAYLOAD: list = [
    {"group_button_p": "bfi2101"}, {"group_button_p": "bfi2102"}]
GROUP_BUTTONS_BVT_PAYLOAD: list = [{"group_button_p": "bvt2101"}, {"group_button_p": "bvt2102"}, {"group_button_p": "bvt2103"}, {
    "group_button_p": "bvt2104"}, {"group_button_p": "bvt2105"}, {"group_button_p": "bvt2106"}, {"group_button_p": "bvt2107"}, {"group_button_p": "bvt2108"}]
GROUP_BUTTONS_BST_PAYLOAD: list = [{"group_button_p": "bst2101"}, {"group_button_p": "bst2102"}, {
    "group_button_p": "bst2103"}, {"group_button_p": "bst2104"}, {"group_button_p": "bst2105"}, {"group_button_p": "bst2106"}]
GROUP_BUTTONS_BEI_PAYLOAD: list = [{"group_button_p": 'bei2101'}, {
    "group_button_p": 'bei2102'}, {"group_button_p": 'bei2103'}]
GROUP_BUTTONS_BIB_PAYLOAD: list = [{"group_button_p": 'bib2101'}, {
    "group_button_p": 'bib2102'}, {"group_button_p": 'bib2103'}, {"group_button_p": 'bib2104'}]
GROUP_BUTTONS_BMP_PAYLOAD: list = [{"group_button_p": "bmp2101"}]
GROUP_BUTTONS_ZRC_PAYLOAD: list = [
    {"group_button_p": 'zrc2101'}, {"group_button_p": 'zrc2102'}]
GROUP_BUTTONS_BAP_PAYLOAD: list = [{"group_button_p": 'bap2101'}]
GROUP_BUTTONS_BEE_PAYLOAD: list = [{"group_button_p": 'bee2101'}]
GROUP_BUTTONS_BBI_PAYLOAD: list = [{"group_button_p": 'bbi2101'}]
GROUP_BUTTONS_BER_PAYLOAD: list = [{"group_button_p": 'ber2101'}]
GROUP_BUTTONS_BUT_PAYLOAD: list = [{"group_button_p": "but2101"}, {
    "group_button_p": "but2102"}, {"group_button_p": "but2103"}]
GROUP_BUTTONS_BRT_PAYLOAD: list = [
    {"group_button_p": 'brt2101'}, {"group_button_p": 'brt2102'}]
GROUP_BUTTONS_BIK_PAYLOAD: list = [{"group_button_p": "bik2101"}, {"group_button_p": "bik2102"}, {"group_button_p": "bik2103"}, {
    "group_button_p": "bik2104"}, {"group_button_p": "bik2105"}, {"group_button_p": "bik2106"}, {"group_button_p": "bik2107"}, {"group_button_p": "bik2108"},
    {"group_button_p": "bik2109"}]
GROUP_BUTTONS_BIN_PAYLOAD: list = [{"group_button_p": "bin2101"}, {"group_button_p": "bin2102"}, {"group_button_p": "bin2103"}, {
    "group_button_p": "bin2104"}, {"group_button_p": "bin2105"}, {"group_button_p": "bin2106"}, {"group_button_p": "bin2107"}, {"group_button_p": "bin2108"},
    {"group_button_p": "bin2109"}, {"group_button_p": "bin2110"}]

# Payload кнопок для факультетов
FACULTIES_BUTTONS_PAYLOAD: list = [{"faculty_button_p": "it"}, {"faculty_button_p": "kiib"}, {
    "faculty_button_p": "rit"}, {"faculty_button_p": "tseimk"}, {"faculty_button_p": "siss"}]

# Payload кнопок для потоков
STREAM_IT_BUTTONS_PAYLOAD: list = [{'stream_button_p': 'бфи'}, {
    'stream_button_p': 'бвт'}, {'stream_button_p': 'бст'}, {'stream_button_p': 'бэи'}]
STREAM_TSEIMK_BUTTONS_PAYLOAD: list = [{'stream_button_p': 'бээ'}, {
    'stream_button_p': 'бэр'}, {'stream_button_p': 'бби'}]
STREAM_KIIB_BUTTONS_PAYLOAD: list = [{'stream_button_p': 'бап'}, {'stream_button_p': 'бмп'}, {
    'stream_button_p': 'бут'}, {'stream_button_p': 'зрс'}, {'stream_button_p': 'биб'}]
STREAM_RIT_BUTTONS_PAYLOAD: list = [
    {'stream_button_p': 'брт'}, {'stream_button_p': 'бик'}]
STREAM_SISS_BUTTONS_PAYLOAD: list = [{'stream_button_p': 'бин'}]

# Генерация кнопок для групп
for i in range(1, len(GROUP_BUTTONS_BFI) + 1):
    GROUP_BUTTONS_BFI_KB.add_text_button(text=GROUP_BUTTONS_BFI[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BFI_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BFI):
        GROUP_BUTTONS_BFI_KB.add_row()
        GROUP_BUTTONS_BFI_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BVT) + 1):
    GROUP_BUTTONS_BVT_KB.add_text_button(text=GROUP_BUTTONS_BVT[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BVT_PAYLOAD[i - 1])
    if i == 3 or i == 6:
        GROUP_BUTTONS_BVT_KB.add_row()
    if i == len(GROUP_BUTTONS_BVT):
        GROUP_BUTTONS_BVT_KB.add_row()
        GROUP_BUTTONS_BVT_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BST) + 1):
    GROUP_BUTTONS_BST_KB.add_text_button(text=GROUP_BUTTONS_BST[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BST_PAYLOAD[i - 1])
    if i == 3:
        GROUP_BUTTONS_BST_KB.add_row()
    if i == len(GROUP_BUTTONS_BST):
        GROUP_BUTTONS_BST_KB.add_row()
        GROUP_BUTTONS_BST_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BEI) + 1):
    GROUP_BUTTONS_BEI_KB.add_text_button(text=GROUP_BUTTONS_BEI[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BEI_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BEI):
        GROUP_BUTTONS_BEI_KB.add_row()
        GROUP_BUTTONS_BEI_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BIB) + 1):
    GROUP_BUTTONS_BIB_KB.add_text_button(text=GROUP_BUTTONS_BIB[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BIB_PAYLOAD[i - 1])
    if i % 3 == 0:
        GROUP_BUTTONS_BIB_KB.add_row()
    if i == len(GROUP_BUTTONS_BIB):
        GROUP_BUTTONS_BIB_KB.add_row()
        GROUP_BUTTONS_BIB_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BMP) + 1):
    GROUP_BUTTONS_BMP_KB.add_text_button(text=GROUP_BUTTONS_BMP[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BMP_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BMP):
        GROUP_BUTTONS_BMP_KB.add_row()
        GROUP_BUTTONS_BMP_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BUT) + 1):
    GROUP_BUTTONS_BUT_KB.add_text_button(text=GROUP_BUTTONS_BUT[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BUT_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BUT):
        GROUP_BUTTONS_BUT_KB.add_row()
        GROUP_BUTTONS_BUT_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_ZRC) + 1):
    GROUP_BUTTONS_ZRC_KB.add_text_button(text=GROUP_BUTTONS_ZRC[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_ZRC_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_ZRC):
        GROUP_BUTTONS_ZRC_KB.add_row()
        GROUP_BUTTONS_ZRC_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BAP) + 1):
    GROUP_BUTTONS_BAP_KB.add_text_button(text=GROUP_BUTTONS_BAP[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BAP_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BAP):
        GROUP_BUTTONS_BAP_KB.add_row()
        GROUP_BUTTONS_BAP_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BRT) + 1):
    GROUP_BUTTONS_BRT_KB.add_text_button(text=GROUP_BUTTONS_BRT[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BRT_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BRT):
        GROUP_BUTTONS_BRT_KB.add_row()
        GROUP_BUTTONS_BRT_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BBI) + 1):
    GROUP_BUTTONS_BBI_KB.add_text_button(text=GROUP_BUTTONS_BBI[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BBI_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BBI):
        GROUP_BUTTONS_BBI_KB.add_row()
        GROUP_BUTTONS_BBI_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BER) + 1):
    GROUP_BUTTONS_BER_KB.add_text_button(text=GROUP_BUTTONS_BER[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BER_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BER):
        GROUP_BUTTONS_BER_KB.add_row()
        GROUP_BUTTONS_BER_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BEE) + 1):
    GROUP_BUTTONS_BEE_KB.add_text_button(text=GROUP_BUTTONS_BEE[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BEE_PAYLOAD[i - 1])
    if i == len(GROUP_BUTTONS_BEE):
        GROUP_BUTTONS_BEE_KB.add_row()
        GROUP_BUTTONS_BEE_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BIK) + 1):
    GROUP_BUTTONS_BIK_KB.add_text_button(text=GROUP_BUTTONS_BIK[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BIK_PAYLOAD[i - 1])
    if i == 3 or i == 6:
        GROUP_BUTTONS_BIK_KB.add_row()
    if i == len(GROUP_BUTTONS_BIK):
        GROUP_BUTTONS_BIK_KB.add_row()
        GROUP_BUTTONS_BIK_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(GROUP_BUTTONS_BIN) + 1):
    GROUP_BUTTONS_BIN_KB.add_text_button(text=GROUP_BUTTONS_BIN[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=GROUP_BUTTONS_BIN_PAYLOAD[i - 1])
    if i % 3 == 0:
        GROUP_BUTTONS_BIN_KB.add_row()
    if i == len(GROUP_BUTTONS_BIN):
        GROUP_BUTTONS_BIN_KB.add_row()
        GROUP_BUTTONS_BIN_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})

# Генерация кнопок для факультетов
for i in range(1, len(FACULTIES_BUTTONS) + 1):
    FACULTIES_BUTTONS_KB.add_text_button(
        text=FACULTIES_BUTTONS[i - 1], color=ButtonColor.SECONDARY, payload=FACULTIES_BUTTONS_PAYLOAD[i - 1])
    if i == len(FACULTIES_BUTTONS):
        FACULTIES_BUTTONS_KB.add_row()
        FACULTIES_BUTTONS_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
    elif i % 3 == 0:
        FACULTIES_BUTTONS_KB.add_row()

# Генерация кнопок для потоков
for i in range(1, len(STREAM_IT_BUTTONS) + 1):
    STREAM_IT_BUTTONS_KB.add_text_button(text=STREAM_IT_BUTTONS[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=STREAM_IT_BUTTONS_PAYLOAD[i - 1])
    if i == len(STREAM_IT_BUTTONS):
        STREAM_IT_BUTTONS_KB.add_row()
        STREAM_IT_BUTTONS_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(STREAM_RIT_BUTTONS) + 1):
    STREAM_RIT_BUTTONS_KB.add_text_button(text=STREAM_RIT_BUTTONS[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=STREAM_RIT_BUTTONS_PAYLOAD[i - 1])
    if i % 3 == 0:
        STREAM_RIT_BUTTONS_KB.add_row()
    elif i == len(STREAM_RIT_BUTTONS):
        STREAM_RIT_BUTTONS_KB.add_row()
        STREAM_RIT_BUTTONS_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(STREAM_SISS_BUTTONS) + 1):
    STREAM_SISS_BUTTONS_KB.add_text_button(text=STREAM_SISS_BUTTONS[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=STREAM_SISS_BUTTONS_PAYLOAD[i - 1])
    if i % 3 == 0:
        STREAM_SISS_BUTTONS_KB.add_row()
    elif i == len(STREAM_SISS_BUTTONS):
        STREAM_SISS_BUTTONS_KB.add_row()
        STREAM_SISS_BUTTONS_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(STREAM_KIIB_BUTTONS) + 1):
    STREAM_KIIB_BUTTONS_KB.add_text_button(text=STREAM_KIIB_BUTTONS[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=STREAM_KIIB_BUTTONS_PAYLOAD[i - 1])
    if i % 3 == 0:
        STREAM_KIIB_BUTTONS_KB.add_row()
    elif i == len(STREAM_KIIB_BUTTONS):
        STREAM_KIIB_BUTTONS_KB.add_row()
        STREAM_KIIB_BUTTONS_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
for i in range(1, len(STREAM_TSEIMK_BUTTONS) + 1):
    STREAM_TSEIMK_BUTTONS_KB.add_text_button(text=STREAM_TSEIMK_BUTTONS[i - 1].upper(
    ), color=ButtonColor.SECONDARY, payload=STREAM_TSEIMK_BUTTONS_PAYLOAD[i - 1])
    if i == 3:
        STREAM_TSEIMK_BUTTONS_KB.add_row()
        STREAM_TSEIMK_BUTTONS_KB.add_text_button(
            text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
# Задание получения клавиатур

KB = {'бфи': GROUP_BUTTONS_BFI_KB.get_keyboard,
      'бвт': GROUP_BUTTONS_BVT_KB.get_keyboard,
      'бст': GROUP_BUTTONS_BST_KB.get_keyboard,
      'бэи': GROUP_BUTTONS_BEI_KB.get_keyboard,
      'биб': GROUP_BUTTONS_BIB_KB.get_keyboard,
      'бмп': GROUP_BUTTONS_BMP_KB.get_keyboard,
      'зрс': GROUP_BUTTONS_ZRC_KB.get_keyboard,
      'бап': GROUP_BUTTONS_BAP_KB.get_keyboard,
      'бут': GROUP_BUTTONS_BUT_KB.get_keyboard,
      'брт': GROUP_BUTTONS_BRT_KB.get_keyboard,
      'бби': GROUP_BUTTONS_BBI_KB.get_keyboard,
      'бээ': GROUP_BUTTONS_BEE_KB.get_keyboard,
      'бэр': GROUP_BUTTONS_BER_KB.get_keyboard,
      'бик': GROUP_BUTTONS_BIK_KB.get_keyboard,
      'бин': GROUP_BUTTONS_BIN_KB.get_keyboard}


KB_STREAMS = {'it': STREAM_IT_BUTTONS_KB.get_keyboard,
              'tseimk': STREAM_TSEIMK_BUTTONS_KB.get_keyboard,
              'rit': STREAM_RIT_BUTTONS_KB.get_keyboard,
              'kiib': STREAM_KIIB_BUTTONS_KB.get_keyboard,
              'siss': STREAM_SISS_BUTTONS_KB.get_keyboard, }
