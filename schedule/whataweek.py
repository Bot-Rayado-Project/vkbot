from utils.terminal_codes import print_error
from datetime import datetime, timedelta
import calendar


async def get_week() -> str:
    try:
        date = datetime.date(datetime.today() + timedelta(hours=3))
        month = str(date)[5:7]
        month = int(str(date)[6:7]) if month[0] == '0' else int(str(date)[5:7])
        format = "%Y-%m-%d"
        past_year = str(int(str(datetime.date(datetime.today() + timedelta(hours=3)))[:4]) - 1)
        current_year = str(datetime.date(datetime.today() + timedelta(hours=3)))[:4]

        if month < 9:
            week = date.isocalendar()[1]
            weeks_past_year = datetime.strptime('{}-12-31'.format(past_year), format).isocalendar()[1] - datetime.strptime('{}-09-01'.format(past_year), format).isocalendar()[1] + 1
            week += weeks_past_year

        if month >= 9:
            week = date.isocalendar()[1]
            weeks_past_sem = datetime.strptime(date, format).isocalendar()[1] - datetime.strptime('{}-09-01'.format(current_year), format).isocalendar()[1] + 1
            week += weeks_past_sem

        if week % 2 == 0:
            return 'четная'
        else:
            return 'нечетная'

    except:
        return False