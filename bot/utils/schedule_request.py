from typing import NamedTuple


class ScheduleRequest(NamedTuple):
    day: str = None
    parity: str = None
    faculty: str = None
    stream_group: str = None


user_schedule_requests = {}
