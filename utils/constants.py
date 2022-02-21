# Команды SQLITE
C_SQLITE_ADD_COMMAND: str = 'INSERT INTO users VALUES({0}, current_timestamp, "{1}");'
C_SQLITE_SELECT_COMMAND: str = "SELECT command, max(date), user_id FROM users GROUP BY user_id HAVING user_id={0};"
C_SQLITE_SELLECT_ALL_COMMANDS: str = "SELECT command FROM users WHERE user_id={0} ORDER BY date DESC;"
