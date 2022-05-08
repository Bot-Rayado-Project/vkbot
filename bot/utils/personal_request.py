from typing import NamedTuple


class EditPersonalRequest(NamedTuple):
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


edit_personal_requests: dict = {}
