from vkwave.bots import Keyboard, ButtonColor
import os


class Settings():
    def __init__(self) -> None:
        self.__ALLOWED_USER_IDS = (os.getenv('ALLOWED_USER_IDS')).split()
        self.__API_TOKEN = os.getenv('API_TOKEN')
        self.__GROUP_ID = os.getenv('GROUP_ID')
        self.__STATE = os.getenv('STATE')

    def GET_ALLOWED_USER_IDS(self) -> list:
        return self.__ALLOWED_USER_IDS

    def GET_API_TOKEN(self) -> str:
        return self.__API_TOKEN

    def GET_GROUP_ID(self) -> str:
        return self.__GROUP_ID

    def GET_STATE(self) -> str:
        return self.__STATE


settings = Settings()


# Команды SQLITE
C_SQLITE_ADD_COMMAND: str = 'INSERT INTO users VALUES({0}, current_timestamp, "{1}");'
C_SQLITE_SELECT_COMMAND: str = "SELECT command, max(date), user_id FROM users GROUP BY user_id HAVING user_id={0};"
C_SQLITE_SELLECT_ALL_COMMANDS: str = "SELECT command FROM users WHERE user_id={0} ORDER BY date DESC;"

# Создание экземпляров клавиатуры

START_KB: Keyboard = Keyboard(one_time=False)
GROUPS_KB: Keyboard = Keyboard(one_time=False)
DAYS_OF_WEEK_KB: Keyboard = Keyboard(one_time=False)
CURRENT_OR_NEXT_WEEK_KB: Keyboard = Keyboard(one_time=False)


# Названия кнопок
START_BUTTONS: list = ['Расписание', 'Анекдот', 'MI AMOR?', 'Помощь']
GROUPS_BUTTONS: list = ['бфи2101', 'бфи2102', 'бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106',
                        'бвт2107', 'бвт2108', 'бст2101', 'бст2102', 'бст2103', 'бст2104', 'бст2105', 'бст2106']
DAYS_OF_WEEK_BUTTONS: list = ['понедельник', 'вторник', 'среда',
                              'четверг', 'пятница', 'суббота', 'вся неделя']
CURRENT_OR_NEXT_WEEK_BUTTONS: list = ['текущая неделя', 'следующая неделя']

# Список всех команд

COMMANDS: list = ["привет", "начать", "начало",
                  "старт", "меню", "mi amor?",
                  "помощь", "дима", "анекдот"]

# Генерация кнопок
for i in range(len(START_BUTTONS)):
    START_KB.add_text_button(START_BUTTONS[i], ButtonColor.SECONDARY)
    if i == 0:
        START_KB.add_row()
for i in range(1, len(GROUPS_BUTTONS)+1):
    GROUPS_KB.add_text_button(
        GROUPS_BUTTONS[i-1].upper(), ButtonColor.SECONDARY)
    if i % 3 == 0:
        GROUPS_KB.add_row()
    if i == len(GROUPS_BUTTONS):
        GROUPS_KB.add_row()
        GROUPS_KB.add_text_button('Меню', ButtonColor.PRIMARY)
for i in range(1, len(DAYS_OF_WEEK_BUTTONS)+1):
    DAYS_OF_WEEK_KB.add_text_button(
        DAYS_OF_WEEK_BUTTONS[i-1].capitalize(), ButtonColor.SECONDARY)
    if i % 3 == 0:
        DAYS_OF_WEEK_KB.add_row()
    if i == len(DAYS_OF_WEEK_BUTTONS):
        DAYS_OF_WEEK_KB.add_row()
        DAYS_OF_WEEK_KB.add_text_button('Меню', ButtonColor.PRIMARY)
for i in range(len(CURRENT_OR_NEXT_WEEK_BUTTONS)):
    CURRENT_OR_NEXT_WEEK_KB.add_text_button(
        CURRENT_OR_NEXT_WEEK_BUTTONS[i].capitalize(), ButtonColor.SECONDARY)
    if i == len(CURRENT_OR_NEXT_WEEK_BUTTONS)-1:
        CURRENT_OR_NEXT_WEEK_KB.add_row()
        CURRENT_OR_NEXT_WEEK_KB.add_text_button(
            'Меню', ButtonColor.PRIMARY)
