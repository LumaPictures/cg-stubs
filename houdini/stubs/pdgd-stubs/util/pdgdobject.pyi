# Houdini stubs generated from Houdini 22.0.466

import _pdgd
from _pdgd import _PythonValue
from collections.abc import Callable
from pdgd import DataLayerVisualizer as DataLayerVisualizer, GlobalDataLayerInstance as GlobalDataLayerInstance, Message as Message, ObjectProperty as ObjectProperty
from typing import Concatenate, Never, Unpack
from typing_extensions import TypedDict

from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
_S = TypeVar('_S')
_P = ParamSpec('_P')
_R = TypeVar('_R')
_Listener: TypeAlias = Callable[[str, _PDGDObjectDict, _pdgd.Message], object]
class _PDGDObjectDict(TypedDict, extra_items=_PythonValue):  # type: ignore[call-arg]
    __container__: PDGDObject

class ListenerWeakRef:
    def __init__(self, fn: _Listener) -> None: ...
    def __call__(self, *args: Unpack[tuple[str, _PDGDObjectDict, _pdgd.Message]], **kwargs: Never) -> object: ...

class PDGDObjectError(Exception):
    """ Raised when a pdg object error happens """
class PDGDObjectNotSubscribed(PDGDObjectError):
    """ Raised when someone attempts to listen an inactive object """

def synchronized_method(method: Callable[Concatenate[_S, _P], _R]) -> Callable[Concatenate[_S, _P], _R]:
    """
    Prevent parallel execution of non thread safe methods
    """

class PDGDObject(DataLayerVisualizer):
    """
        A generic visualizer that keeps a copy of the
        subscription target internally and triggers
        callbacks whenever the object is updated
    """
    debug: bool
    object: _PDGDObjectDict
    path: str
    subscribed: bool
    data_layer: _pdgd.DataLayerInterface
    __listeners: set[ListenerWeakRef]
    def __init__(self, path: str, data_layer: _pdgd.DataLayerInterface | None = None, debug: bool = False) -> None:
        """
            Subscribes to 'path' object
        """
    def __del__(self) -> None:
        """ Unsubscribes from the data layer"""
    @synchronized_method
    def unsubscribe(self) -> None: ...
    def processMessage(self, message: _pdgd.Message, sender: str) -> None:
        """
            A message from pdg data layer was received,
            this updates the object information
        """
    def addListener(self, listener: _Listener) -> None:
        """ Adds a listener to the object """
    def removeListener(self, listener: _Listener) -> None:
        """ Removes a listener from the object """
    def subscriptionLost(self) -> None:
        """ Called when the subscription to the data layer is interrupted """
