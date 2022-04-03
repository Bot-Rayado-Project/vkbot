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

STREAMS_IDS: dict = {'бвт': 'it_09.03.01', 'бст': 'it_09.03.02', 'бфи': 'it_02.03.02', 'бэи': 'it_09.03.03',
                     'биб': 'kiib_10.03.01', 'бмп': 'kiib_01.03.04', 'зрс': 'kiib_10.05.02', 'бап': 'kiib_15.03.04', 'бут': 'kiib_27.03.04',
                     'брт': 'rit_11.03.01', 'бик': 'rit_11.03.02',
                     'бин': 'siss_11.03.02',
                     'бби': 'tseimk_38.03.05', 'бэр': 'tseimk_42.03.01', 'бээ': 'tseimk_38.03.01'}
STREAMS: list = ['бвт', 'бст', 'бфи', 'биб', 'бэи', 'бик', 'бмп', 'зрс', 'бап', 'бут', 'брт', 'бээ', 'бби', 'бэр', 'бин']
