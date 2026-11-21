from pdgjob.pdgmq import *
from collections import Counter

from typing import TypeAlias
from pdgjob.pdgmq import AcquireJobSlotsEvent
from pdgjob.pdgmq import AddSubItemBatchEvent
from pdgjob.pdgmq import AppendLogEvent
from pdgjob.pdgmq import CanceledEvent
from pdgjob.pdgmq import FailedEvent
from pdgjob.pdgmq import GetWorkItemJSONEvent
from pdgjob.pdgmq import InvalidateCacheEvent
from pdgjob.pdgmq import IsWorkItemReadyEvent
from pdgjob.pdgmq import KeepaliveEvent
from pdgjob.pdgmq import ReleaseJobSlotsEvent
from pdgjob.pdgmq import ResultDataArrayEvent
from pdgjob.pdgmq import ResultDataEvent
from pdgjob.pdgmq import SetCookPercentEvent
from pdgjob.pdgmq import SetCustomStateEvent
from pdgjob.pdgmq import SetDictAttribArrayEvent
from pdgjob.pdgmq import SetDictAttribEvent
from pdgjob.pdgmq import SetFileAttribArrayEvent
from pdgjob.pdgmq import SetFileAttribEvent
from pdgjob.pdgmq import SetFloatAttribArrayEvent
from pdgjob.pdgmq import SetFloatAttribEvent
from pdgjob.pdgmq import SetIntAttribArrayEvent
from pdgjob.pdgmq import SetIntAttribEvent
from pdgjob.pdgmq import SetPyObjectAttribEvent
from pdgjob.pdgmq import SetStringAttribArrayEvent
from pdgjob.pdgmq import SetStringAttribEvent
from pdgjob.pdgmq import SharedServerStartedEvent
from pdgjob.pdgmq import StartCookEvent
from pdgjob.pdgmq import SuccessEvent
from pdgjob.pdgmq import WarningEvent
from pdgjob.pdgmq import WriteAttrEvent
from typing import TypeAlias
_Event: TypeAlias = SuccessEvent | CanceledEvent | FailedEvent | KeepaliveEvent | StartCookEvent | SharedServerStartedEvent | IsWorkItemReadyEvent | AddSubItemBatchEvent | ReleaseJobSlotsEvent | AcquireJobSlotsEvent | GetWorkItemJSONEvent | ResultDataEvent | ResultDataArrayEvent | WriteAttrEvent | SetStringAttribArrayEvent | SetIntAttribArrayEvent | SetFloatAttribArrayEvent | SetFileAttribArrayEvent | SetDictAttribArrayEvent | SetStringAttribEvent | SetIntAttribEvent | SetFloatAttribEvent | SetFileAttribEvent | SetDictAttribEvent | SetPyObjectAttribEvent | SetCustomStateEvent | SetCookPercentEvent | AppendLogEvent | InvalidateCacheEvent | WarningEvent
class EventDispatchMixin:
    """
    Intended to be subclassed by PyScheduler implementations.  Will dispatch
    corresponding PyScheduler event-state methods when execEvent is called with
    event objects.
    """
    event_counts: Counter[str]
    last_count_reset: float
    def __init__(self) -> None: ...
    def pop_counts(self) -> tuple[float, int]: ...
    def counts_summary(self) -> str: ...
    def execEvent(self, event: _Event) -> str | None:
        """
        Called when an event is received by relay listener
        """
