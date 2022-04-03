from datetime import datetime, timedelta

from utils.terminal_codes import print_info, print_error


async def get_week() -> str:
    try:
        dat = datetime.now() + timedelta(hours=3)
        if (datetime.timestamp(datetime.now() + timedelta(hours=3)) 
        - datetime.timestamp(datetime.strptime('{}-09-01'.format(
        str(int(str(datetime.date(datetime.today()
        + timedelta(hours=3)))[:4]) - 1)), "%Y-%m-%d"))) % 2 == 0:
            print_info('Whataweek ' + str((datetime.now() + timedelta(hours=3)) - dat))
            return 'четная'
        else:
            print_info('Whataweek ' + str((datetime.now() + timedelta(hours=3)) - dat))
            return 'нечетная'

    except:
        print_error('Ошибка в whataweek')
        return False

