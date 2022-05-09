from typing import NamedTuple


class EditHeadmanRequest(NamedTuple):
    stream_group: str = None
    parity: str = None
    day: str = None
    pair_number: int = None
    changes: int = None
    annotation: str = None
    writing_changes_or_annotation: bool = False


edit_headman_requests: dict = {}
