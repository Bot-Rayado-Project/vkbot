def print_schedule(start, end):

    global groups_id, group, t, k
    schedule = []
    schedule.append(time[k])

    for i in range(start, end + 1):

        temp = str(sheet.cell_value(i, t))

        if temp != '':

            if 'дистанционно' in temp or 'Дистанционно' in temp:

                schedule.append(temp[len(temp) - 12: len(temp)])
                schedule[len(schedule) - 2] += ' ' + temp[0:len(temp) - 12]

            else:

                schedule.append(temp)

    if schedule[len(schedule) - 1] == 'Физическая культура и спорт  на 16, 17 нед.':

        temp = schedule[len(schedule) - 1]
        schedule.pop(len(schedule) - 1)
        schedule[len(schedule) - 2] += '\n' + temp

    if len(schedule) > 1 and schedule[1] == 'КУЛЬТУРА И СПОРТ ':

        temp = ' ФИЗИЧЕСКАЯ' + ' ' + schedule[1]

        for i in range(2):
            schedule.pop(1)

        schedule.append(temp)
        schedule.append('дистанционно')

    if len(schedule) == 4:

        temp = schedule[1] + ' ' + schedule[2]
        temp_dist = schedule[3]

        for i in range(3):
            schedule.pop(1)

        schedule.append(temp)
        schedule.append(temp_dist)

    if len(schedule) == 5:

        if 'на 1 нед.' not in schedule:

            temp = schedule[2] + ' ' + schedule[3] + ' ' + schedule[4]

            for i in range(4):
                schedule.pop(1)

            schedule.append(temp)
            schedule.append('дистанционно')

        else:

            temp = ' ' + schedule[1] + ' ' + schedule[2] + ' ' + schedule[3]

            for i in range(4):
                schedule.pop(1)

            schedule.append(temp)
            schedule.append('дистанционно')

    return schedule


def calculationv2(days_of_week_2, t_2, j_2):

    global t, coef
    days_of_week = days_of_week_2
    j = j_2

    if (sheet.cell_value(days_of_week + coef[j], t) == ''
            and sheet.cell_value(days_of_week + coef[j] + 1, t) != '') \
            or sheet.cell_value(days_of_week + coef[j], t) == 'дистанционно' \
            or sheet.cell_value(days_of_week + coef[j], t) == 'на 1 нед.':

        start = days_of_week + coef[j]
        end = days_of_week + 3 + coef[j]

        return start, end

    else:

        if whataweek.get_week() == "четная":

            start = days_of_week + 2 + coef[j]
            end = days_of_week + 3 + coef[j]

        else:

            start = days_of_week + coef[j]
            end = days_of_week + 1 + coef[j]

        return start, end


def calculation(days_of_week, j):

    global groups_id, group, t, coef
    coef = {0: 0,
            1: 4,
            2: 8,
            3: 12,
            4: 16
            }
    if sheet.cell_value(days_of_week + coef[j], groups_id[group]) == '' and \
            sheet.cell_value(days_of_week + coef[j], groups_id[group]) == '' and \
            sheet.cell_value(days_of_week + coef[j], groups_id[group]) == '' and \
            sheet.cell_value(days_of_week + coef[j], groups_id[group]) == '' and \
            ([days_of_week + coef[j], groups_id[group]] in mas or [days_of_week + 2 + coef[j], groups_id[group]] in mas):

        t = groups_id[group] - 1

        return calculationv2(days_of_week, t, j)

    else:

        t = groups_id[group]

        return calculationv2(days_of_week, t, j)


def pred_print(day, i):

    start, end = calculation(day, i)

    return print_schedule(start, end)


def table_ui(stroka1):
    global stroka

    print_group = '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n' + 'Группа: ' + group.upper() + '\n' \
        + 'День недели: ' + day.capitalize() + '\n' + 'Неделя: ' + whataweek.get_week().capitalize() + '\n' \
        + '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

    for i in range(len(stroka)):

        print_group += '\n' + 'Пара №' + \
            str(i + 1) + ' (' + str(stroka[i][0]) + ')' + '\n'

        if len(stroka[i]) > 2:

            boolean = True
            boolean_2 = True

            if stroka[i][2] == 'КУЛЬТУРА И СПОРТ' and stroka[i][1] == ' ФИЗИЧЕСКАЯ':

                print_group += stroka[i][1][1:len(stroka[i][1])] + \
                    ' ' + stroka[i][2] + '\n'
                boolean = False

            else:

                if 'ФИЗИЧЕСКАЯ' in stroka[i][1]:

                    print_group += stroka[i][1][1:len(stroka[i][1])] + '\n'

                else:

                    if day == 'понедельник' and group == 'бвт2103' and '15-25' in print_group:

                        print_group += 'Пары нет' + '\n' + '\n'
                        boolean_2 = False

                    else:
                        print_group += stroka[i][1] + '\n'

            if boolean:

                if boolean_2:

                    print_group += 'Кабинет: ' + stroka[i][2] + '\n' + '\n'

            else:
                print_group += 'Кабинет: ' + 'дистанционно' + '\n' + '\n'
        else:

            if day == 'вторник' and group == 'бвт2103' and '09-30' in print_group:

                print_group += 'Философия пр.з.' + '\n' + \
                    'Кабинет: ' + 'дистанционно' + '\n' + '\n'

            else:

                print_group += 'Пары нет' + '\n' + '\n'

    print_group += '⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n'

    return print_group


def get_schedule(day_of_week, group_input):

    global sheet, time, k, stroka, groups, group, day
    group = group_input
    day = day_of_week
    stroka = []
    k = 0
    time = ['09-30', '11-20', '13-10', '15-25', '17-15']
    sheet = get_sheet()
    days_of_week = {
        'понедельник': 11,
        'вторник': 31,
        'среда': 51,
        'четверг': 71,
        'пятница': 91,
        'суббота': 111,
    }

    for i in range(5):
        stroka.append(pred_print(days_of_week[day], i))
        k += 1