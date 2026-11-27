from collections.abc import Callable
from typing import ClassVar, ParamSpec, TypeAlias, TypeVar, overload

import hou
from houtypes import JSONValue

_T = TypeVar("_T")
_P = ParamSpec("_P")
_R = TypeVar("_R")

# serializeHook()'s dictionary values: a hou.UIEvent's reason name, ray, device record and value,
# a hou.UIEventDevice record (the values of its argument-less methods), a hou.Vector3's
# components or a node's path.
_DeviceRecord: TypeAlias = dict[str, bool | int | float | str]
_SerializedValue: TypeAlias = (
    str
    | tuple[hou.Vector3, hou.Vector3]
    | _DeviceRecord
    | bool
    | int
    | float
    | list[float]
    | tuple[int, ...]
    | tuple[float, ...]
    | tuple[str, ...]
    | None
)
# What json.load gives with unserializeHook as its object_hook.
_RecordedValue: TypeAlias = "None | bool | int | float | str | list[_RecordedValue] | dict[str, _RecordedValue] | EventRecorder.MethodDict | hou.OpNode | hou.Vector3"

instance_method_name: str

class EventRecorder:
    # The (method name, kwargs) of each recorded event, the kwargs made plain JSON data.
    events: ClassVar[list[tuple[str, JSONValue]]]
    enabled: ClassVar[bool]

    class MethodDict:
        mydict: dict[str, _RecordedValue]
        def __init__(self, literal: dict[str, _RecordedValue]) -> None: ...
        # A key of mydict is a method that gives its value ("reason" as a hou.uiEventReason).
        def __getattribute__(self, name: str) -> Callable[..., _RecordedValue | hou.EnumValue[hou.uiEventReason]]: ...

    @classmethod
    def clear(myclass: "type[EventRecorder]") -> None: ...
    @classmethod
    def enable(myclass: "type[EventRecorder]") -> None: ...
    @classmethod
    def disable(myclass: "type[EventRecorder]") -> None: ...
    @overload
    @classmethod
    def serializeHook(myclass: "type[EventRecorder]", obj: hou.UIEventDevice) -> _DeviceRecord: ...
    @overload
    @classmethod
    def serializeHook(myclass: "type[EventRecorder]", obj: _T) -> dict[str, _SerializedValue] | _T | None: ...
    @classmethod
    def serializeHook(myclass: "type[EventRecorder]", obj: _T) -> dict[str, _SerializedValue] | _DeviceRecord | _T | None: ...
    @classmethod
    def unserializeHook(
        myclass: "type[EventRecorder]", literal: dict[str, _RecordedValue]
    ) -> "EventRecorder.MethodDict | hou.OpNode | hou.Vector3 | dict[str, _RecordedValue] | None": ...
    @classmethod
    def writeEvents(myclass: "type[EventRecorder]", filepath: str) -> None: ...
    # The [method name, kwargs] pairs that writeEvents wrote.
    @classmethod
    def readEvents(myclass: "type[EventRecorder]", filepath: str) -> list[list[str | dict[str, _RecordedValue]]]: ...
    # Records the state callback's kwargs (its second argument) while the recorder is enabled.
    @classmethod
    def recordEvent(myclass: "type[EventRecorder]", func: Callable[_P, _R]) -> Callable[_P, _R]: ...
