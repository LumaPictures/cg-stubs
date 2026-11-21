# Houdini stubs generated from Houdini 22.0.466

import _pdgd
from _pdgd import _PythonValue
from collections.abc import Callable, Collection, Iterable
from pdgd.subscriptionhandler import PyDataLayerSubscriptionHandler as PyDataLayerSubscriptionHandler
from typing import Any

from typing import TypeVar
from typing import TypeVar
_F = TypeVar('_F', bound=Callable[..., object])
_V = TypeVar('_V', bound=_PythonValue)
def register_new_handler(handler: type[PyDataLayerSubscriptionHandler], name: str, path: str | None = None) -> None:
    """
    Registers a handler type and creates a root instance in the Data Layer
    """

class NonDataLayerCollectionType(Exception):
    """
    Exception raised when a property type is not
    supported by the current operation
    """
class CommandNameAlreadyUsed(Exception):
    """
    Exception raised when a command name was already used
    """

def check_valid_collection(value: object) -> None:
    """
    Checks if value's type is a collection supported by the data layer
    """
def create_prop_list(values: Iterable[_PythonValue]) -> list[_pdgd.ObjectProperty]:
    """
    Returns a list with data layer property values
    """

class HandlerMeta(type):
    """
    Meta class for building class's callback map
    """
    command_callbacks: dict[str, Callable[[SimpleHandler, _PythonValue], object]]
    @classmethod
    def command(cls, command_name: str) -> Callable[[_F], _F]: ...
    def __init__(cls, name: str, bases: tuple[type, ...], dct: dict[str, Any]) -> None: ...

class SimpleHandler(PyDataLayerSubscriptionHandler):
    """
    Base subscription handler class that provides
    utility methods that simplify subscription handlers
    implementation
    """
    snapshot: dict[str, list[_PythonValue] | set[int | float | str | bool]]
    def __init__(self, handler: _pdgd.SubscriptionHandler) -> None:
        """
        Performs the parent class initialization and
        creates an empty object for acting as snapshot
        """
    def buildSnapshot(self) -> _pdgd.ObjectSnapshot:
        """
        Converts the stored snapshot dictionary into
        a data layer snapshot and returns it
        """
    def setValues(self, prop_name: str, values: list[_V] | set[_V]) -> None:
        """
        Called when all values of a property should
        be replaced
        """
    def addValues(self, prop_name: str, values: list[_V] | set[_V]) -> None:
        """
        Called when values should be added to a property
        """
    def removeValues(self, prop_name: str, values: Collection[_PythonValue]) -> None:
        """
        Called when values should be removed from a property
        """
    def processCommand(self, command: _pdgd.Command) -> None:
        """
        Handles data layer commands
        """
    def processCommandWithCallback(self, command: _pdgd.Command) -> _pdgd.ObjectProperty | None:
        """
        Handles commands and returns a value
        """
