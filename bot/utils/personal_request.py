from typing import NamedTuple


class EditPersonalRequest(NamedTuple):
    '''Модель реквеста пользователя при редактировании расписания'''
    id: int
    faculty: str = None
    stream: str = None
    stream_group: str = None
    parity: str = None
    day: str = None
    pair_number: int = None
    changes: int = None
    annotation: str = None
    writing_changes_or_annotation: bool = False

# Активные реквесты пользователей на редакторе расписания


edit_personal_requests: dict = {}
