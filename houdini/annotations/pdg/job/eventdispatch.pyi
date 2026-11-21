from collections import Counter
from typing import TypeAlias

from pdgjob.pdgmq import (
    AcquireJobSlotsEvent,
    AddSubItemBatchEvent,
    AppendLogEvent,
    CanceledEvent,
    FailedEvent,
    GetWorkItemJSONEvent,
    InvalidateCacheEvent,
    IsWorkItemReadyEvent,
    KeepaliveEvent,
    ReleaseJobSlotsEvent,
    ResultDataArrayEvent,
    ResultDataEvent,
    SetCookPercentEvent,
    SetCustomStateEvent,
    SetDictAttribArrayEvent,
    SetDictAttribEvent,
    SetFileAttribArrayEvent,
    SetFileAttribEvent,
    SetFloatAttribArrayEvent,
    SetFloatAttribEvent,
    SetIntAttribArrayEvent,
    SetIntAttribEvent,
    SetPyObjectAttribEvent,
    SetStringAttribArrayEvent,
    SetStringAttribEvent,
    SharedServerStartedEvent,
    StartCookEvent,
    SuccessEvent,
    WarningEvent,
    WriteAttrEvent,
)

_Event: TypeAlias = (
    SuccessEvent
    | CanceledEvent
    | FailedEvent
    | KeepaliveEvent
    | StartCookEvent
    | SharedServerStartedEvent
    | IsWorkItemReadyEvent
    | AddSubItemBatchEvent
    | ReleaseJobSlotsEvent
    | AcquireJobSlotsEvent
    | GetWorkItemJSONEvent
    | ResultDataEvent
    | ResultDataArrayEvent
    | WriteAttrEvent
    | SetStringAttribArrayEvent
    | SetIntAttribArrayEvent
    | SetFloatAttribArrayEvent
    | SetFileAttribArrayEvent
    | SetDictAttribArrayEvent
    | SetStringAttribEvent
    | SetIntAttribEvent
    | SetFloatAttribEvent
    | SetFileAttribEvent
    | SetDictAttribEvent
    | SetPyObjectAttribEvent
    | SetCustomStateEvent
    | SetCookPercentEvent
    | AppendLogEvent
    | InvalidateCacheEvent
    | WarningEvent
)

class EventDispatchMixin:
    event_counts: Counter[str]
    last_count_reset: float
    def __init__(self) -> None: ...
    def pop_counts(self) -> tuple[float, int]: ...
    def counts_summary(self) -> str: ...
    def execEvent(self, event: _Event) -> str | None: ...
