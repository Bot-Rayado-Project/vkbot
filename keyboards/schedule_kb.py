from vkwave.bots import Keyboard, ButtonColor

GROUP_BUTTONS_BFI_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BVT_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BST_KB: Keyboard = Keyboard(one_time=False)
STREAM_KB: Keyboard = Keyboard(one_time=False)
DAYS_OF_WEEK_KB: Keyboard = Keyboard(one_time=False)
CURRENT_OR_NEXT_WEEK_KB: Keyboard = Keyboard(one_time=False)


# Названия кнопок
STREAM_BUTTONS: list = ['бфи', 'бвт', 'бст']
DAYS_OF_WEEK_BUTTONS: list = ['сегодня', 'завтра', 'вся неделя']
CURRENT_OR_NEXT_WEEK_BUTTONS: list = ['текущая неделя', 'следующая неделя']
GROUP_BUTTONS_BFI: list = ['бфи2101', 'бфи2102']
GROUP_BUTTONS_BVT: list = ['бвт2101', 'бвт2102', 'бвт2103', 'бвт2104',
                           'бвт2105', 'бвт2106', 'бвт2107', 'бвт2108']
GROUP_BUTTONS_BST: list = ['бст2101', 'бст2102', 'бст2103',
                           'бст2104', 'бст2105', 'бст2106']
GROUP_BUTTONS: list = ['бфи2101', 'бфи2102', 'бвт2101', 'бвт2102', 'бвт2103', 'бвт2104',
                       'бвт2105', 'бвт2106', 'бвт2107', 'бвт2108', 'бст2101', 'бст2102',
                       'бст2103', 'бст2104', 'бст2105', 'бст2106']


# Генерация кнопок

for i in range(1, len(STREAM_BUTTONS)+1):
    STREAM_KB.add_text_button(
        STREAM_BUTTONS[i-1].upper(), ButtonColor.SECONDARY)
    if i == len(STREAM_BUTTONS):
        STREAM_KB.add_row()
        STREAM_KB.add_text_button('Меню', ButtonColor.PRIMARY)
for i in range(1, len(DAYS_OF_WEEK_BUTTONS)+1):
    DAYS_OF_WEEK_KB.add_text_button(
        DAYS_OF_WEEK_BUTTONS[i-1].capitalize(), ButtonColor.SECONDARY)
    if i == len(DAYS_OF_WEEK_BUTTONS):
        DAYS_OF_WEEK_KB.add_row()
        DAYS_OF_WEEK_KB.add_text_button('Меню', ButtonColor.PRIMARY)
for i in range(1, len(GROUP_BUTTONS_BFI)+1):
    GROUP_BUTTONS_BFI_KB.add_text_button(
        GROUP_BUTTONS_BFI[i-1].upper(), ButtonColor.SECONDARY)
    if i == len(GROUP_BUTTONS_BFI):
        GROUP_BUTTONS_BFI_KB.add_row()
        GROUP_BUTTONS_BFI_KB.add_text_button('Меню', ButtonColor.PRIMARY)
for i in range(1, len(GROUP_BUTTONS_BVT)+1):
    GROUP_BUTTONS_BVT_KB.add_text_button(
        GROUP_BUTTONS_BVT[i-1].upper(), ButtonColor.SECONDARY)
    if i == 3 or i == 6:
        GROUP_BUTTONS_BVT_KB.add_row()
    if i == len(GROUP_BUTTONS_BVT):
        GROUP_BUTTONS_BVT_KB.add_row()
        GROUP_BUTTONS_BVT_KB.add_text_button('Меню', ButtonColor.PRIMARY)
for i in range(1, len(GROUP_BUTTONS_BST)+1):
    GROUP_BUTTONS_BST_KB.add_text_button(
        GROUP_BUTTONS_BST[i-1].upper(), ButtonColor.SECONDARY)
    if i == 3:
        GROUP_BUTTONS_BST_KB.add_row()
    if i == len(GROUP_BUTTONS_BST):
        GROUP_BUTTONS_BST_KB.add_row()
        GROUP_BUTTONS_BST_KB.add_text_button('Меню', ButtonColor.PRIMARY)
for i in range(1, len(CURRENT_OR_NEXT_WEEK_BUTTONS) + 1):
    CURRENT_OR_NEXT_WEEK_KB.add_text_button(
        CURRENT_OR_NEXT_WEEK_BUTTONS[i-1].capitalize(), ButtonColor.SECONDARY)
    if i == len(CURRENT_OR_NEXT_WEEK_BUTTONS):
        CURRENT_OR_NEXT_WEEK_KB.add_row()
        CURRENT_OR_NEXT_WEEK_KB.add_text_button('Меню', ButtonColor.PRIMARY)
