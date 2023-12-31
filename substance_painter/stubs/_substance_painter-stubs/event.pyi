from typing import ClassVar

import datetime

class TextureStateEventAction:
    __members__: ClassVar[dict] = ...  # read-only
    ADD: ClassVar[TextureStateEventAction] = ...
    REMOVE: ClassVar[TextureStateEventAction] = ...
    UPDATE: ClassVar[TextureStateEventAction] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...

def get_ts_event_cache_key_invalidation_throttling_period() -> datetime.timedelta: ...
def set_ts_event_cache_key_invalidation_throttling_period(arg0: datetime.timedelta) -> None: ...
def trigger_test_event() -> None: ...
