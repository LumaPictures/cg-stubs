# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Utils.EventModuleCommon as EventModuleCommon
from Utils.Exceptions import GetExceptionMessage as GetExceptionMessage
from typing import Any
from typing import Hashable

_EventQueue: list
_SynchronousEventProcessing: bool

def Initialize(): ...
def ProcessAllEvents(): ...
def ProcessEvents() -> bool: ...
def PumpIdleQueue(): ...
def QueueEvent(eventType: str, eventID: Hashable, priority: int = ..., **kwargs): ...
def QueuePriorityEvent(eventType: str, eventID: Hashable, **kwargs): ...
def _handleEvents(events: list[tuple]): ...
def _invokeCollapsedDict(mask: tuple[str, Any], args: list[tuple[str, Any, dict]]): ...
def _invokeHandlerDict(mask: tuple[str, Any], eventType: str, eventID: Any, kwargs: dict): ...