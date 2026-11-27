import hou
import typing
from collections.abc import Callable as Callable
from houtypes import JSONValue
from typing import ClassVar

from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
_T = TypeVar('_T')
_P = ParamSpec('_P')
_R = TypeVar('_R')
_DeviceRecord: TypeAlias = dict[str, bool | int | float | str]
_SerializedValue: TypeAlias = str | tuple[hou.Vector3, hou.Vector3] | _DeviceRecord | bool | int | float | list[float] | tuple[int, ...] | tuple[float, ...] | tuple[str, ...] | None
_RecordedValue: TypeAlias = 'None | bool | int | float | str | list[_RecordedValue] | dict[str, _RecordedValue] | EventRecorder.MethodDict | hou.OpNode | hou.Vector3'
instance_method_name: str

class EventRecorder:
    events: ClassVar[list[tuple[str, JSONValue]]]
    enabled: ClassVar[bool]
    class MethodDict:
        """ Provides basic getter methods constructed from a dictionary.
            Every key in the dict is a valid method returning the
            corresponding dict value.
        """
        mydict: dict[str, _RecordedValue]
        def __init__(self, literal: dict[str, _RecordedValue]) -> None: ...
        def __getattribute__(self, name: str) -> Callable[..., _RecordedValue | hou.EnumValue[hou.uiEventReason]]: ...
    @classmethod
    def clear(myclass: type[EventRecorder]) -> None: ...
    @classmethod
    def enable(myclass: type[EventRecorder]) -> None: ...
    @classmethod
    def disable(myclass: type[EventRecorder]) -> None: ...
    @typing.overload
    @classmethod
    def serializeHook(myclass: type[EventRecorder], obj: hou.UIEventDevice) -> _DeviceRecord: ...
    @typing.overload
    @classmethod
    def serializeHook(myclass: type[EventRecorder], obj: _T) -> dict[str, _SerializedValue] | _T | None: ...
    @classmethod
    def unserializeHook(myclass: type[EventRecorder], literal: dict[str, _RecordedValue]) -> EventRecorder.MethodDict | hou.OpNode | hou.Vector3 | dict[str, _RecordedValue] | None: ...
    @classmethod
    def writeEvents(myclass: type[EventRecorder], filepath: str) -> None: ...
    @classmethod
    def readEvents(myclass: type[EventRecorder], filepath: str) -> list[list[str | dict[str, _RecordedValue]]]: ...
    @classmethod
    def recordEvent(myclass: type[EventRecorder], func: Callable[_P, _R]) -> Callable[_P, _R]: ...
