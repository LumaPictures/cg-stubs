from collections.abc import Callable
from typing import Concatenate, Never, ParamSpec, TypeAlias, TypeVar, Unpack

import _pdgd
from _pdgd import _PythonValue
from typing_extensions import TypedDict

_S = TypeVar("_S")
_P = ParamSpec("_P")
_R = TypeVar("_R")

# Property name -> python value (a list or set for a collection), plus '__container__' -> the
# PDGDObject.
class _PDGDObjectDict(TypedDict, extra_items=_PythonValue):  # type: ignore[call-arg]
    __container__: "PDGDObject"

# Called with (object path, the object's property dict, the message that changed it).
_Listener: TypeAlias = Callable[[str, _PDGDObjectDict, _pdgd.Message], object]

class ListenerWeakRef:
    def __init__(self, fn: _Listener) -> None: ...
    def __call__(self, *args: Unpack[tuple[str, _PDGDObjectDict, _pdgd.Message]], **kwargs: Never) -> object: ...

class PDGDObjectError(Exception): ...
class PDGDObjectNotSubscribed(PDGDObjectError): ...

def synchronized_method(
    method: Callable[Concatenate[_S, _P], _R],
) -> Callable[Concatenate[_S, _P], _R]: ...

class PDGDObject:
    debug: bool
    object: _PDGDObjectDict
    path: str
    subscribed: bool
    data_layer: _pdgd.DataLayerInterface
    __listeners: set[ListenerWeakRef]
    def __init__(
        self, path: str, data_layer: _pdgd.DataLayerInterface | None = ..., debug: bool = ...
    ) -> None: ...
    def __del__(self) -> None: ...
    def unsubscribe(self) -> None: ...
    def processMessage(self, message: _pdgd.Message, sender: str) -> None: ...
    def addListener(self, listener: _Listener) -> None: ...
    def removeListener(self, listener: _Listener) -> None: ...
    def subscriptionLost(self) -> None: ...
