from datetime import datetime, timedelta
from utils.constants_schedule import time, days, supplements


async def get_schedule_zrc(day_type: str, group_text: str, week_type: str, schedule) -> str:

    day_time_utc = datetime.weekday(datetime.today().utcnow() + timedelta(hours=3))  # Получение нынешнего времени
    start_cell = 14
    week_column = 'G' if week_type == 'нечетная' else 'H'
    const = 1 if week_type == 'четная' else -1

    if day_type == 'завтра':

        if day_time_utc == 6:
            # Обрабатываем исключение воскресенья для вывода, то есть автоматом понедельник в day
            day = start_cell
            day_time_utc = 0
        else:
            day_time_utc += 1
            day = int(day_time_utc) * 6 + start_cell

    else:
        day = int(day_time_utc) * 6 + start_cell

    try:
        schedule_output = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
            + 'День недели: ' + days[day_time_utc].capitalize() + '\n' + 'Неделя: ' + week_type.capitalize() + '\n' \
            + '⸻⸻⸻⸻⸻\n'  # Добавляем заголовок вывода, группа и тд.

    except KeyError:
        return 'Ошибка в выводе расписания #1'


    for i in range(day, day + 5):

        if schedule[week_column + str(i)].value != None:
            schedule_output += str(time[i - day + 1]) + '  ' \
                + str(schedule[week_column + str(i)].value) + '\n\n' \
                + 'Преподаватель: ' + str(schedule[chr(ord(week_column) + 1 * const) + str(i)].value) + '\n'\
                + 'Вид занятия: ' + str(supplements[str(schedule[chr(ord(week_column) + 2 * const) + str(i)].value)]) + '\n' \
                + 'Форма проведения: ' + str(supplements[str(schedule[chr(ord(week_column) + 3 * const) + str(i)].value)]) + '\n' \
                + '⸻⸻⸻⸻⸻\n'
        else:
            schedule_output += 'Пары нет\n' + '⸻⸻⸻⸻⸻\n'
    
    return schedule_output


async def get_full_schedule_zrc(group_text: str, week_type: str, schedule) -> tuple:

    full_schedule = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
        + 'Неделя: ' + week_type.capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻\n'
    full_schedule_tuple = ()
    full_schedule_list = []
    const = 1 if week_type == 'четная' else -1
    week_column = 'G' if week_type == 'нечетная' else 'H'


    for k in range(14, 49, 6):

        current_day_column = 0
        full_schedule = str(
            schedule['A' + str(k - 1)].value) + '\n' + '⸻⸻⸻⸻⸻\n'

        for i in range(k + current_day_column, k + current_day_column + 5):
            print('1')
            if schedule[week_column + str(i)].value != None:
                print('2')
                full_schedule += str(current_day_column + 1) + '. ' \
                    + str(schedule[week_column + str(i)].value) + '(' + str(str(schedule[chr(ord(week_column) + 3 * const) + str(i)].value)) \
                    + ' ' + str(str(schedule[chr(ord(week_column) + 2 * const) + str(i)].value)) + ')' + '\n'\
                    + '⸻⸻⸻⸻⸻\n'
            else:
                full_schedule += str(current_day_column + 1) + \
                    '. ' + 'Пары нет\n' + '⸻⸻⸻⸻⸻\n'

            current_day_column += 1

        full_schedule_list.append(full_schedule)

    full_schedule_tuple = tuple(full_schedule_list)

    return full_schedule_tuple

'''full_schedule = '⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
        + 'Неделя: ' + (week_checked).capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻\n'
    full_schedule_tuple = ()
    full_schedule_list = []
    groups = {
        'бвт2101': 0,
        'бвт2102': 1,
        'бвт2103': 2,
        'бвт2104': 3,
        'бвт2105': 4,
        'бвт2106': 5,
        'бвт2107': 6,
        'бвт2108': 7,
        'бфи2101': 8,
        'бфи2102': 9,
        'бст2101': 10,
        'бст2102': 11,
        'бст2103': 12,
        'бст2104': 13,
        'бст2105': 14,
        'бст2106': 15
    }
    schedule = await get_sheet(group_text, id, groups[group_text])

    for k in range(14, 49, 6):

        current_day_column = 0
        full_schedule = str(
            schedule['A' + str(k - 1)].value) + '\n' + '⸻⸻⸻⸻⸻\n'

        for i in range(k + current_day_column, k + current_day_column + 5):

            if schedule[week_column + str(i)].value != None:
                full_schedule += str(current_day_column + 1) + '. ' \
                    + str(schedule[week_column + str(i)].value) + '(' + str(str(schedule[chr(ord(week_column) + 3 * const) + str(i)].value)) \
                    + ' ' + str(str(schedule[chr(ord(week_column) + 2 * const) + str(i)].value)) + ')' + '\n'\
                    + '⸻⸻⸻⸻⸻\n'
            else:
                full_schedule += str(current_day_column + 1) + \
                    '. ' + 'Пары нет\n' + '⸻⸻⸻⸻⸻\n'

            current_day_column += 1

        full_schedule_list.append(full_schedule)

    full_schedule_tuple = tuple(full_schedule_list)

    return full_schedule_tuple'''