from vkwave.bots import Keyboard, ButtonColor

GROUP_BUTTONS_BFI_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BVT_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BST_KB: Keyboard = Keyboard(one_time=False)
GROUP_BUTTONS_BEI_KB: Keyboard = Keyboard(one_time=False)
STREAM_KB: Keyboard = Keyboard(one_time=False)
DAYS_OF_WEEK_KB: Keyboard = Keyboard(one_time=False)
CURRENT_OR_NEXT_WEEK_KB: Keyboard = Keyboard(one_time=False)


# Названия кнопок
STREAM_BUTTONS: list = ['бфи', 'бвт', 'бст', 'бэи']
DAYS_OF_WEEK_BUTTONS: list = ['сегодня', 'завтра', 'вся неделя']
CURRENT_OR_NEXT_WEEK_BUTTONS: list = ['текущая неделя', 'следующая неделя']
GROUP_BUTTONS_BFI: list = ['бфи2101', 'бфи2102']
GROUP_BUTTONS_BVT: list = ['бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106', 'бвт2107', 'бвт2108']
GROUP_BUTTONS_BST: list = ['бст2101', 'бст2102', 'бст2103', 'бст2104', 'бст2105', 'бст2106']
GROUP_BUTTONS_BEI: list = ['бэи2101', 'бэи2102', 'бэи2103']
GROUP_BUTTONS: list = ['бфи2101', 'бфи2102', 'бвт2101', 'бвт2102', 'бвт2103', 'бвт2104',
                       'бвт2105', 'бвт2106', 'бвт2107', 'бвт2108', 'бст2101', 'бст2102',
                       'бст2103', 'бст2104', 'бст2105', 'бст2106', 'бэи2101', 'бэи2102', 'бэи2103']

# Payload кнопок
STREAM_BUTTONS_PAYLOAD: list = [{"stream_button": "bfi"}, {"stream_button": "bvt"}, {"stream_button": "bst"}, {"stream_button": "bei"}]
DAYS_OF_WEEK_BUTTONS_PAYLOAD: list = [{"dow_button": "today"}, {"dow_button": "tommorow"}, {"dow_button": "full week"}]
CURRENT_OR_NEXT_WEEK_BUTTONS_PAYLOAD: list = [{"conw_button": "current week"}, {"conw_button": "next week"}]
GROUP_BUTTONS_BFI_PAYLOAD: list = [{"group_button": "bfi2101"}, {"group_button": "bfi2102"}]
GROUP_BUTTONS_BVT_PAYLOAD: list = [{"group_button": "bvt2101"}, {"group_button": "bvt2102"}, {"group_button": "bvt2103"}, {
    "group_button": "bvt2104"}, {"group_button": "bvt2105"}, {"group_button": "bvt2106"}, {"group_button": "bvt2107"}, {"group_button": "bvt2108"}]
GROUP_BUTTONS_BST_PAYLOAD: list = [{"group_button": "bst2101"}, {"group_button": "bst2102"}, {"group_button": "bst2103"}, {"group_button": "bst2104"}, {"group_button": "bst2105"}, {"group_button": "bst2106"}]
GROUP_BUTTONS_BEI_PAYLOAD: list = [{"group_button": 'bei2101'}, {"group_button": 'bei2102'}, {"group_button": 'bei2103'}]


# Генерация кнопок

for i in range(1, len(STREAM_BUTTONS) + 1):
    STREAM_KB.add_text_button(text=STREAM_BUTTONS[i - 1].upper(), color=ButtonColor.SECONDARY, payload=STREAM_BUTTONS_PAYLOAD[i - 1])
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
for i in range(1, len(CURRENT_OR_NEXT_WEEK_BUTTONS) + 1):
    CURRENT_OR_NEXT_WEEK_KB.add_text_button(text=CURRENT_OR_NEXT_WEEK_BUTTONS[i - 1].capitalize(), color=ButtonColor.SECONDARY, payload=CURRENT_OR_NEXT_WEEK_BUTTONS_PAYLOAD[i - 1])
    if i == len(CURRENT_OR_NEXT_WEEK_BUTTONS):
        CURRENT_OR_NEXT_WEEK_KB.add_row()
        CURRENT_OR_NEXT_WEEK_KB.add_text_button(text='Меню', color=ButtonColor.PRIMARY, payload={"button": "menu"})
