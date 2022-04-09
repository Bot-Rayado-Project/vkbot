import os


class NoneException(Exception):
    pass


USERSIDS = os.environ.get('USERSIDS').split()
GROUPID = os.environ.get('GROUPID')
TOKENS = os.environ.get('TOKENS').split()
EADRESS = os.environ.get('EADRESS')
EPASSWORD = os.environ.get('EPASSWORD')
DEBUG = os.environ.get('DEBUG') or False
RESTIP = os.environ.get('RESTIP') or 'localhost'
RESTPORT = os.environ.get('RESTPORT') or '8000'
VOLUMENAME = os.environ.get('VOLUMENAME')

if GROUPID is None or TOKENS is None:
    raise NoneException

_USERSIDS = []

for user in USERSIDS:
    _USERSIDS += [user]

# Команды SQLITE
C_SQLITE_ADD_COMMAND: str = 'INSERT INTO users VALUES({0}, (STRFTIME("%Y-%m-%d %H:%M:%f", "NOW")), "{1}");'
C_SQLITE_SELECT_COMMAND: str = "SELECT command, max(date), user_id FROM users GROUP BY user_id HAVING user_id={0};"
C_SQLITE_SELLECT_ALL_COMMANDS: str = "SELECT command FROM users WHERE user_id={0} ORDER BY date DESC;"
C_SQLITE_FIRST_ADD_CONFIG_BUTTONS: str = 'INSERT INTO config VALUES({0}, "Пустая ячейка, Пустая ячейка, Пустая ячейка", False, "first_btn");'  # Вызывается только первый раз для каждого пользователя.
C_SQLITE_UPDATE_CONFIG_BUTTONS: str = 'UPDATE config SET keyboard_buttons = "{0}, {1}, {2}", is_writing=False where user_id={3};'  # Обновить кнопки по записи.
C_SQLITE_SELECT_CONFIG_KEYBOARD_BUTTONS: str = 'SELECT keyboard_buttons FROM config WHERE user_id={0};'
C_SQLITE_SET_IS_WRITING_TRUE: str = 'UPDATE config SET is_writing = True where user_id={0};'
C_SQLITE_SET_IS_WRITING_FALSE: str = 'UPDATE config SET is_writing = False where user_id={0};'
C_SQLITE_SET_BUTTON_TO_WRITE: str = 'UPDATE config SET button_to_write="{0}" where user_id={1};'
C_SQLITE_GET_IS_WRITING: str = 'SELECT is_writing FROM config WHERE user_id={0};'
C_SQLITE_GET_BUTTON_TO_WRITE: str = 'SELECT button_to_write FROM config WHERE user_id={0};'

STREAMS: list = ['бвт', 'бст', 'бфи', 'биб', 'бэи', 'бик', 'бмп', 'зрс', 'бап', 'бут', 'брт', 'бээ', 'бби', 'бэр', 'бин']

DAYS_ENG = ['ponedelnik', 'vtornik', 'sreda', 'chetverg', 'pjatnitsa', 'subbota']
DAYS_RU = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
