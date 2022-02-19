import openpyxl
import whataweek
from pathlib import Path
from recieve import recieve_time_table
import asyncio


async def get_sheet(group: str) -> openpyxl.Workbook:
    data = await recieve_time_table(group)
    wb_obj = openpyxl.load_workbook(Path('table.xlsx'))
    match data:
        case "бвт", number:
            wb_obj.active = groups[group_text]
        case "бфи", number:
            wb_obj.active = groups[group_text] - 8
        case "бст", number:
            wb_obj.active = groups[group_text] - 10
    sheet = wb_obj.active
    print(groups[group_text], group, wb_obj.active, sheet)
    return sheet


async def week_check():

    if week_type == 'текущая неделя':
        week = await whataweek.get_week()
    else:
        if await whataweek.get_week() == 'четная':
            week = 'нечетная'
        else:
            week = 'четная'
    return week


async def get_schedule():
    global schedule_output

    schedule_output = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
        + 'День недели: ' + day.capitalize() + '\n' + 'Неделя: ' + (await week_check()).capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

    for i in range(days_of_week[day], days_of_week[day] + 5):

        if schedule[week_column + str(i)].value != None:
            schedule_output += str(time[i - days_of_week[day] + 1]) + '  ' \
                + str(schedule[week_column + str(i)].value) + '\n\n' \
                + 'Преподаватель: ' + str(schedule[chr(ord(week_column) + 1 * const) + str(i)].value) + '\n'\
                + 'Вид занятия: ' + str(supplements[str(schedule[chr(ord(week_column) + 2 * const) + str(i)].value)]) + '\n' \
                + 'Форма проведения: ' + str(supplements[str(schedule[chr(ord(week_column) + 3 * const) + str(i)].value)]) + '\n' \
                + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
        else:
            schedule_output += 'Пары нет\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    return schedule_output


async def get_full_schedule():

    full_schedule = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group_text.upper() + '\n' \
        + 'Неделя: ' + (await week_check()).capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'
    full_schedule_tuple = ()
    full_schedule_list = []

    for k in range(14, 49, 6):

        current_day_column = 0
        full_schedule = str(schedule['A' + str(k - 1)].value) + '\n' + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

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

    return full_schedule_tuple


async def print_schedule(day_input, group_input, week_type_input,id_user):  # тоже пиздец
    global days_of_week, day, week_column, groups, group_text, \
        time, week_type, supplements, week_checked, const, schedule

    week_type = week_type_input
    days_of_week = {
        'понедельник': 14,
        'вторник': 20,
        'среда': 26,
        'четверг': 32,
        'пятница': 38,
        'суббота': 44,
    }
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
    group_text = group_input
    schedule = await get_sheet(group_input)
    week_checked = await week_check()

    const = 1 if week_checked == 'четная' else -1
    week_column = 'H' if week_checked == 'четная' else 'G'
    if day_input == 'вся неделя':
        return await get_full_schedule()
    else:
        day = day_input
        return await get_schedule()


if __name__ == '__main__':
    async def main():
        s = await print_schedule('вся неделя', 'бвт2103', 'текущая неделя')
        print(s)

    asyncio.run(main())
