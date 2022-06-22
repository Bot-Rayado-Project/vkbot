from typing import NamedTuple


class ScheduleRequest(NamedTuple):
    '''Модель запроса расписания'''
    day: str = None
    parity: str = None
    faculty: str = None
    stream_group: str = None


# Активные реквесты пользователей на вывод расписания

user_schedule_requests = {}
