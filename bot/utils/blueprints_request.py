from typing import NamedTuple


class BlueprintsRequest(NamedTuple):
    '''Модель запроса пользователя на создание шаблона'''
    day: str = None
    parity: str = None
    faculty: str = None
    stream_group: str = None
    cell: int = None

# Активные реквесты пользователей


user_blueprints_requests: dict = {}
