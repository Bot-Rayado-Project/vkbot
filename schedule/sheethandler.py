import openpyxl
import os
from datetime import datetime, timedelta

import schedule.whataweek as whataweek
from schedule.recieve import recieve_time_table
# Закомментировать для локального тестирования
""" from recieve import recieve_time_table
import whataweek
import asyncio """
# Раскоментить для локального тестирования


async def week_check(week_type: str) -> str:
    if week_type == 'текущая неделя':
        return await whataweek.get_week()
    else:
        if await whataweek.get_week() == 'четная':
            return 'нечетная'
        else:
            return 'четная'  # Тут и тупой поймёт чо происходит


'''async def get_sheet(group: str, user_id, temp_number) -> openpyxl.Workbook:
    if not os.path.isdir("tables"):
        os.mkdir("tables")
    data = await recieve_time_table(group, user_id)
    wb_obj = openpyxl.load_workbook('tables/table_{}.xlsx'.format(user_id))
    match data:
        case "бвт", number:
            wb_obj.active = temp_number
        case "бфи", number:
            wb_obj.active = temp_number - 8
        case "бст", number:
            wb_obj.active = temp_number - 10
    sheet = wb_obj.active
    return sheet'''


async def get_sheet(group: str, user_id: str, temp_number: str) -> openpyxl.Workbook:
    try:
        if not os.path.isdir("tables"):
            os.mkdir("tables")
    except:
        # Тут происходит обработки ошибки с папкой tables, вдруг её нет или не создаётся
        return 'Ошибка в скачке таблицы #3'
    data = await recieve_time_table(group, user_id)  # Запрос на скачку таблицы
    if 'Ошибка' in data:
        return 'Ошибка в скачке таблицы #4'  # Проверка, что скачалось без ошибки
    try:
        wb_obj = openpyxl.load_workbook('tables/table_{}.xlsx'.format(user_id))
    except:
        # Проверка вторая так как иногда ссылки меняют, и ест ьвероятность простого парса еррор сайта
        return 'Ошибка в скачке таблицы #2'
    wb_obj.active = temp_number  # Задача листа таблицы
    sheet = wb_obj.active  # Выборка правильной таблицы
    return sheet

'''async def get_schedule(group_text, week_column, const, day_type, id, week_type):

    time = {
        1: '9:30 - 11:05\n',
        2: '11:20 - 12:55\n',
        3: '13:10 - 14:45\n',
        4: '15:25 - 17:00\n',
        5: '17:15 - 18:50\n'
    }
    supplements = {
        'лек': 'лекция',
        'лаб': 'лабораторная',
        'пр': 'практика',
        'дист': 'дистанционно',
        'очно': 'очно'}
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
    days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
    if day_type == 'завтра':
        if datetime.weekday(datetime.today()) == 6:
            day = 14
            day_print = 0
        else:
            day = datetime.weekday(datetime.today()) * 6 + 14 + 6
            day_print = datetime.weekday(datetime.today()) + 1
    else:
        day = datetime.weekday(datetime.today()) * 6 + 14
        day_print = datetime.weekday(datetime.today())
    schedule = await get_sheet(group_text, id, groups[group_text])
    schedule_output = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
        + 'День недели: ' + days[day_print].capitalize() + '\n' + 'Неделя: ' + (await week_check(week_type)).capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

    for i in range(day, day + 5):

        if schedule[week_column + str(i)].value != None:
            schedule_output += str(time[i - day + 1]) + '  ' \
                + str(schedule[week_column + str(i)].value) + '\n\n' \
                + 'Преподаватель: ' + str(schedule[chr(ord(week_column) + 1 * const) + str(i)].value) + '\n'\
                + 'Вид занятия: ' + str(supplements[str(schedule[chr(ord(week_column) + 2 * const) + str(i)].value)]) + '\n' \
                + 'Форма проведения: ' + str(supplements[str(schedule[chr(ord(week_column) + 3 * const) + str(i)].value)]) + '\n' \
                + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
        else:
            schedule_output += 'Пары нет\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    return schedule_output'''


async def get_schedule(group_text: str, group_column: str, day_type: str, id: str, week_type: str, start_cell: int) -> str:

    time = {
        1: '9:30 - 11:05\n',
        2: '11:20 - 12:55\n',
        3: '13:10 - 14:45\n',
        4: '15:25 - 17:00\n',
        5: '17:15 - 18:50\n'
    }  # Задача времени для вывода по номеру пары
    groups = {
        'бвт2101': 0,
        'бвт2102': 0,
        'бвт2103': 0,
        'бвт2104': 0,
        'бвт2105': 1,
        'бвт2106': 1,
        'бвт2107': 1,
        'бвт2108': 1,
        'бфи2101': 0,
        'бфи2102': 0,
        'бст2101': 0,
        'бст2102': 0,
        'бст2103': 0,
        'бст2104': 1,
        'бст2105': 1,
        'бст2106': 1,
        'бэи2101': 0,
        'бэи2102': 0,
        'бэи2103': 0
    }  # Список с группами для определения листа в файле
    days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
    days_num = {
        '0': start_cell,
        '1': start_cell + 11,
        '2': start_cell + 22,
        '3': start_cell + 33,
        '4': start_cell + 44,
        '5': start_cell + 55
    }  # Задача ячейки с которой нужно начинать по дням
    day_time_utc = datetime.weekday(
        datetime.today().utcnow() + timedelta(hours=3))  # Получение нынешнего времени

    if day_type == 'завтра':
        if day_time_utc == 6:
            # Обрабатываем исключение воскресенья для вывода, то есть автоматом понедельник в day
            day = start_cell
        else:
            try:
                # Определяем стартовую строчку для вывода с +1 так как завтрашний день
                day = days_num[str(day_time_utc + 1)]
            except KeyError:
                return 'Ошибка в выводе расписания #1'
        # Добавляем плюс один так как день завтра и надо вывести другой день
        day_print = day_time_utc + 1
    else:
        if day_time_utc == 6:
            return 'занятий нет'  # Обработка воскресенья сегодня, так как пар нет
        else:
            try:
                # Определяем стартовую строчку для вывода
                day = days_num[str(day_time_utc)]
            except KeyError:
                return 'Ошибка в выводе расписания #1'
            day_print = day_time_utc  # Опять же, без плюс один, так как сегодняшний день
    # Скачиваем таблицу
    try:
        schedule = await get_sheet(group_text, id, groups[group_text])
        if 'Ошибка' in schedule:
            return schedule  # Проверка на ошибку при скачке таблицы
    except KeyError:
        return 'Ошибка в выводе расписания #1'
    try:
        schedule_output = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
            + 'День недели: ' + days[day_print].capitalize() + '\n' + 'Неделя: ' + (await week_check(week_type)).capitalize() + '\n' \
            + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'  # Добавляем заголовок вывода, группа и тд.
    except KeyError:
        return 'Ошибка в выводе расписания #1'
    time_par = 1  # Номер пары для времени
    try:
        for i in range(day, day + 10, 2):

            try:
                if schedule[group_column + str(i)].value != None:
                    try:
                        schedule_output += str(time[time_par]) + '  ' \
                            + str(schedule[group_column + str(i)].value) + '\n\n' \
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

            time_par += 1  # Счётчик пары плюс один
    except:
        # Если же по каким-то причинам цикл не заработает, то выведет ошибку
        return 'Ошибка в выводе расписания #1'
    return schedule_output


'''async def get_full_schedule(group_text, week_column, const, id, week_type):

    full_schedule = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
        + 'Неделя: ' + (await week_check(week_type)).capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
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
            schedule['A' + str(k - 1)].value) + '\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

        for i in range(k + current_day_column, k + current_day_column + 5):

            if schedule[week_column + str(i)].value != None:
                full_schedule += str(current_day_column + 1) + '. ' \
                    + str(schedule[week_column + str(i)].value) + '(' + str(str(schedule[chr(ord(week_column) + 3 * const) + str(i)].value)) \
                    + ' ' + str(str(schedule[chr(ord(week_column) + 2 * const) + str(i)].value)) + ')' + '\n'\
                    + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
            else:
                full_schedule += str(current_day_column + 1) + \
                    '. ' + 'Пары нет\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

            current_day_column += 1

        full_schedule_list.append(full_schedule)

    full_schedule_tuple = tuple(full_schedule_list)

    return full_schedule_tuple'''


async def get_full_schedule(group_text, week_column, id, week_type, start_cell) -> tuple:

    full_schedule_tuple = ()
    # Формируем список и кортеж для будущего возврата в другой файл, чтобы вернуть пользователю
    full_schedule_list = []
    full_schedule_list.append('⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n'
                              + 'Неделя: ' + (await week_check(week_type)).capitalize() + '\n'
                              + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n')  # Добавляем заголовок вывода расписания с группой и тд.
    groups = {
        'бвт2101': 0,
        'бвт2102': 0,
        'бвт2103': 0,
        'бвт2104': 0,
        'бвт2105': 1,
        'бвт2106': 1,
        'бвт2107': 1,
        'бвт2108': 1,
        'бфи2101': 0,
        'бфи2102': 0,
        'бст2101': 0,
        'бст2102': 0,
        'бст2103': 0,
        'бст2104': 1,
        'бст2105': 1,
        'бст2106': 1,
        'бэи2101': 0,
        'бэи2102': 0,
        'бэи2103': 0
    }  # Список с группами для определения листа в файле
    try:
        # Скачиваем таблицу изспользуя функцию
        schedule = await get_sheet(group_text, id, groups[group_text])
        if 'Ошибка' in schedule:
            return schedule  # Проверяем есть ли ошибка в скачке таблицы или нет
    except KeyError:
        # Это выведет если в будет какая-то ошибка с ключём словаря а не со скачкой таблицы
        return ('Ошибка в выводе расписания #1')
    # Это определение константы для вывода дня недели, в зависимости от чётности
    day_of_week = {
        '1':'Понедельник',
        '2':'Вторник',
        '3':'Среда',
        '4':'Четверг',
        '5':'Пятница',
        '6':'Суббота',
    }
    subject = 1

    for k in range(start_cell, 67, 11):
        full_schedule = str(day_of_week[str(subject)]) + '\n\n'  # Добавление в конечный вывод дня недели то есть значения ячейки из таблицы

        for i in range(k, k + 10, 2):

            if schedule[week_column + str(i)].value != None:
                full_schedule += str(schedule[week_column + str(i)].value) + '\n'\
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


'''async def print_schedule(day_input, group_input, id, week_type): 

    week_checked = await week_check(week_type)

    const = 1 if week_checked == 'четная' else -1
    week_column = 'H' if week_checked == 'четная' else 'G'
    if day_input == 'вся неделя':
        return await get_full_schedule(group_input, week_column, const, id, week_type)
    else:
        return await get_schedule(group_input, week_column, const, day_input, id, week_type)'''


async def print_schedule(day_input: str, group_input: str, id: str, week_type: str) -> str | tuple:

    if 'Ошибка' in await week_check(week_type):
        return await week_check(week_type)  # Проверка ошибки в чётности недели

    weeks_bvt_01_04_bfi = {
        '1': 'D',
        '2': 'E',
        '3': 'F',
        '4': 'G'
    }
    weeks_bvt_05_08 = {
        '5': 'E',
        '6': 'F',
        '7': 'G',
        '8': 'H',
    }
    weeks_bst_bei = {
        '1': 'D',
        '2': 'E',
        '3': 'F',
        '4': 'D',
        '5': 'E',
        '6': 'F',
    } # Три словаря для определения столбца

    week_type_v2 = week_type  # Создаём вторую версию week_type для обработки воскресенья
    groups = ('бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106',
              'бвт2107', 'бвт2108', 'бфи2101', 'бфи2102', 'бст2101', 'бст2102', 'бст2103',
              'бст2104', 'бст2105', 'бст2106', 'бэи2101', 'бэи2102', 'бэи2103')  # Все группы для проверки введённой группы

    if day_input not in ('завтра', 'сегодня', 'вся неделя') or group_input not in groups or week_type not in ('следующая неделя', 'текущая неделя'):
        return 'Ошибка ввода #1'  # Проверяем на ошибку ввода переменных
    else:
        if day_input == 'завтра' and datetime.weekday(datetime.today().utcnow() + timedelta(hours=3)) == 6:
            week_type_v2 = 'следующая неделя'
        elif day_input == 'завтра':
            # В данном куске кода мы делаем обработку исключения для завтра в воскресенье
            week_type_v2 = 'текущая неделя'
        # Определяем стартовую ячейку для вывода пар
        try:
            if group_input[1] == 'ф' or group_input[1] == 'в' and group_input[-1] not in ('5', '6', '7', '8'):
                # Бвт 01-04 и бфи
                group_column = weeks_bvt_01_04_bfi[group_input[-1]]
                start_cell = 2 if await week_check(week_type) == 'нечетная' else 3 
                # Определяем стартовую ячейку для вывода пар
            else:
                if group_input[1] == 'в':
                    # Исключающиеся бвт(05-08)
                    group_column = weeks_bvt_05_08[group_input[-1]]
                    start_cell = 2 if await week_check(week_type) == 'нечетная' else 3
                    # Определяем стартовую ячейку для вывода пар
                else:
                    if group_input[1] == 'с' or group_input[1] == 'э':
                        # То есть у нас номер колонки зависит от номера группы, в данном случае лист бст
                        group_column = weeks_bst_bei[group_input[-1]]
                        start_cell = 2 if await week_check(week_type) == 'нечетная' else 3
                        # Определяем стартовую ячейку для вывода пар

        except IndexError:
            # В данном случае, при ошибке вернёт пользователю эту строку.
            return 'Ошибка ввода #2'

        if day_input == 'вся неделя':  # В данном куске кода мы уже делаем отправку определённую фукнцию в зависимости от ввода данных
            return await get_full_schedule(group_input, group_column, id, week_type_v2, start_cell)
        else:
            return await get_schedule(group_input, group_column, day_input, id, week_type_v2, start_cell)

""" if __name__ == '__main__':
    async def main():
        s = await print_schedule('вся неделя', 'бфи2101', '123', 'текущая неделя')
        print(s)
asyncio.run(main()) """