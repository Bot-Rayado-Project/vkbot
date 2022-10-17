import calendar
from datetime import datetime, timedelta


'''
*
Этот файл отвечает за определение чётности недели, одна единственная функция
*
'''


def get_parity() -> str:

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    calendar_ = calendar.TextCalendar(calendar.MONDAY)
    lines = calendar_.formatmonth(year, month).split('\n')
    days_by_week = [week.lstrip().split() for week in lines[2:]]
    str_day = str(day)
    for index, week in enumerate(days_by_week):
        if str_day in week:
            number = index + 1
            break
    return "четная" if number % 2 == 0 else "нечетная"
