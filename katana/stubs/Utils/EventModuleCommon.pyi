# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import typing
from Utils.Exceptions import GetExceptionMessage as GetExceptionMessage
from _typeshed import Incomplete
from typing import Set, Tuple

_CollapsedHandlers: dict
_CollapsedHandlersByObjectID: dict
_EventFilters: list
_EventHandlers: dict
_EventHandlersByObjectID: dict
_RegistrationCallbacks: dict
_insideHandler: bool
_removedCollapsed: list
_removedHandlers: list

def CallRegistrationCallbacks(instance: object): ...
def FilterEvent(eventType, eventID, **kwargs): ...
def GetAllRegisteredEventTypes(): ...
def GetNumRegisteredHandlersForEventType(eventType): ...
def IsCollapsedHandlerRegisteredAfterEventLoop(handler, eventType, eventID): ...
def IsCollapsedRegistered(handler, eventType: Incomplete | None = ..., eventID: Incomplete | None = ...): ...
def IsEventFilterRegistered(eventFilter: typing.Callable) -> bool: ...
def IsHandlerRegistered(handler, eventType: Incomplete | None = ..., eventID: Incomplete | None = ...): ...
def IsHandlerRegisteredAfterEventLoop(handler, eventType, eventID): ...
def IsHandlerRegisteredForEventType(eventType, checkEventID: bool = ...): ...
def ProcessDeadHandlers(): ...
def RegisterCollapsedHandler(handler, eventType: Incomplete | None = ..., eventID: Incomplete | None = ..., enabled: bool = ...): ...
def RegisterEventFilter(eventFilter): ...
def RegisterEventHandler(handler, eventType: Incomplete | None = ..., eventID: Incomplete | None = ..., enabled: bool = ...): ...
def SetRegistrationCallbackForType(cls: type, callback: typing.Callable): ...
def UnregisterCollapsedHandler(handler, eventType: Incomplete | None = ..., eventID: Incomplete | None = ...): ...
def UnregisterEventFilter(eventFilter: typing.Callable): ...
def UnregisterEventHandler(handler, eventType: Incomplete | None = ..., eventID: Incomplete | None = ...): ...
def UnregisterObjectEventHandlers(objectID: int): ...
def _registerCollapsedHandler(handler, eventType, eventID): ...
def _registerEventHandler(handler, eventType, eventID): ...
def _unregisterCollapsedHandler(handler, eventType, eventID): ...
def _unregisterCollapsedHandlerReal(handler, eventType, eventID): ...
def _unregisterEventHandler(handler, eventType, eventID): ...
def _unregisterEventHandlerReal(handler, eventType, eventID): ...
