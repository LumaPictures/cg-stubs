# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
from Utils.EventModuleCommon import GetAllRegisteredEventTypes as GetAllRegisteredEventTypes, GetNumRegisteredHandlersForEventType as GetNumRegisteredHandlersForEventType, IsCollapsedHandlerRegisteredAfterEventLoop as IsCollapsedHandlerRegisteredAfterEventLoop, IsCollapsedRegistered as IsCollapsedRegistered, IsEventFilterRegistered as IsEventFilterRegistered, IsHandlerRegistered as IsHandlerRegistered, IsHandlerRegisteredAfterEventLoop as IsHandlerRegisteredAfterEventLoop, IsHandlerRegisteredForEventType as IsHandlerRegisteredForEventType, RegisterCollapsedHandler as RegisterCollapsedHandler, RegisterEventFilter as RegisterEventFilter, RegisterEventHandler as RegisterEventHandler, SetRegistrationCallbackForType as SetRegistrationCallbackForType, UnregisterCollapsedHandler as UnregisterCollapsedHandler, UnregisterEventFilter as UnregisterEventFilter, UnregisterEventHandler as UnregisterEventHandler, UnregisterObjectEventHandlers as UnregisterObjectEventHandlers
from Utils.EventModuleDefault import Initialize as Initialize, ProcessAllEvents as ProcessAllEvents, ProcessEvents as ProcessEvents, PumpIdleQueue as PumpIdleQueue, QueueEvent as QueueEvent, QueuePriorityEvent as QueuePriorityEvent
from typing import Set, Tuple

def RegisterDebugEventHandler(): ...
def SynchronousEventProcessingScope(): ...
