from typing import NamedTuple


class EditHeadmanRequest(NamedTuple):
    '''Модель измененного расписания старостой'''
    stream_group: str = None
    parity: str = None
    day: str = None
    pair_number: int = None
    changes: int = None
    annotation: str = None
    writing_changes_or_annotation: bool = False

# Активные реквесты редактора старост


edit_headman_requests: dict = {}
