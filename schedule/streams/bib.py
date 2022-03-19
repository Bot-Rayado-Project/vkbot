from datetime import datetime, timedelta

async def get_schedule_bib(day_type: str, group_text: str, group_column: str, week_type: str, schedule) -> str:
    
    time = {
        1: '9:30 - 11:05\n',
        2: '11:20 - 12:55\n',
        3: '13:10 - 14:45\n',
        4: '15:25 - 17:00\n',
        5: '17:15 - 18:50\n'
    }  # Задача времени для вывода по номеру пары
    days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
    day_time_utc = datetime.weekday(datetime.today().utcnow() + timedelta(hours=3))  # Получение нынешнего времени
    start_cell = 15 if week_type == 'четная' else 14

    if day_type == 'завтра':

        if day_time_utc == 6:
            # Обрабатываем исключение воскресенья для вывода, то есть автоматом понедельник в day
            day = start_cell
            day_time_utc = 0
        else:
            day_time_utc += 1
            day = int(day_time_utc) * 11 + start_cell

    else:
        day = int(day_time_utc) * 11 + start_cell

    try:
        schedule_output = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
            + 'День недели: ' + days[day_time_utc].capitalize() + '\n' + 'Неделя: ' + week_type.capitalize() + '\n' \
            + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'  # Добавляем заголовок вывода, группа и тд.

    except KeyError:
        return 'Ошибка в выводе расписания #1'

    time_para = 1  # Номер пары для времени

    for para_cell in range(day, day + 10, 2):

        try:
            if schedule[group_column + str(para_cell)].value != None:

                try:
                    schedule_output += str(time[time_para]) + '  ' \
                        + str(schedule[group_column + str(para_cell)].value) + '\n\n' \
                        + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'  # Добавляем пару, то есть ячейку если она не пустая

                except KeyError:
                    # Это обработка что ключ будет существовать во времени, то есть номер пары
                    return 'Ошибка в выводе расписания #1'
            else:
                # Если же ячейка пустая, значит пары нет
                schedule_output += 'Пары нет\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
        except:
            # Обрабатываем ошибку в считывании таблицы
            return 'Ошибка в считывании таблицы #1'
        
        time_para += 1  # Счётчик пары плюс один

    return schedule_output


async def get_full_schedule_bib(group_text: str, week_type: str, schedule, week_column: str) -> tuple:

    day_of_week = {
        '1': 'Понедельник',
        '2': 'Вторник',
        '3': 'Среда',
        '4': 'Четверг',
        '5': 'Пятница',
        '6': 'Суббота',
    }
    subject = 1
    full_schedule_tuple = ()
    full_schedule_list = []
    start_cell = 15 if week_type == 'четная' else 14
    # Формируем список и кортеж для будущего возврата в другой файл, чтобы вернуть пользователю

    full_schedule_list.append('⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n'
                              + 'Неделя: ' + (week_type.capitalize()) + '\n'
                              + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n')  # Добавляем заголовок вывода расписания с группой и тд.

    for day_of_week_cell in range(start_cell, 74, 11):

        # Добавление в конечный вывод дня недели то есть значения ячейки из таблицы
        full_schedule = str(day_of_week[str(subject)]) + '\n\n'

        for para_cell in range(day_of_week_cell, day_of_week_cell + 10, 2):

            if schedule[week_column + str(para_cell)].value != None:

                full_schedule += str(schedule[week_column + str(para_cell)].value) + '\n'\
                    + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
                # Если ячейка не пустая добавляем значение ячейки в конечный вывод

            else:
                full_schedule += 'Пары нет\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
                # Если же пустая, то пары нет
        
        # Добавляем полученный день в список
        full_schedule_list.append(full_schedule)
        subject += 1

    # Из списка делаем кортеж и возвращаем
    full_schedule_tuple = tuple(full_schedule_list)

    return full_schedule_tuple