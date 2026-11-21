import types
from collections.abc import Callable
from typing import Any, ClassVar, Never, Protocol, TypeAlias, TypedDict

import _pdgd

# What ObjectProperty.FromPython converts: values of any other type become int 0.
_PythonValue: TypeAlias = int | float | str | bool | list["_PythonValue"] | set[int | float | str | bool]

class _MessageDict(TypedDict):
    type: Message.MessageType
    property_name: str
    property_array: list[_PythonValue]
    object_snapshot: dict[str, _PythonValue] | None

class _RegisterType(Protocol):
    # pdgd/__init__.py assigns plain python functions to these class attributes. Callers use
    # them on TypeRegistry.Instance(), which binds the registry, so it is left out here.
    def __call__(self, type_object: type[object], name: str | None = ..., label: str | None = ..., /) -> BaseType: ...

class _RegisterModuleTypes(Protocol):
    def __call__(self, module: types.ModuleType, quiet: bool = ..., /) -> None: ...

class DataBackend:
    def buildFilteredSet(self, *args, **kwargs) -> Never: ...

class DataBackendQueryResults:
    InitialResults: Never
    SortedAndFiltered: Never

class DataLayerInterface:
    def getHandler(self, arg0: str, arg1: bool) -> SubscriptionHandler | None: ...
    def sendCommand(self, arg0: str, arg1: _PythonValue, arg2: str) -> None: ...
    def sendCommandWithCallback(self, arg0: str, arg1: _PythonValue, arg2: str, arg3: Callable[[ObjectProperty], object]) -> None: ...

class DataLayerInterfaceManager:
    def createInterface(self, arg0: str, arg1: str) -> DataLayerInterface | None: ...
    def getInterfaceById(self, arg0: int) -> DataLayerInterface | None: ...

class DataLayerServerManager:
    def createServer(self, arg0: str, arg1: int) -> DataLayerServer | None: ...
    def listActiveServers(self) -> list[DataLayerServer]: ...

class Message:
    class MessageType:
        __members__: ClassVar[dict[str, Message.MessageType]]
    def toPython(self) -> _MessageDict: ...

class ObjectProperty:
    class Type:
        __members__: ClassVar[dict[str, ObjectProperty.Type]]
    @staticmethod
    def FromPython(arg0: _PythonValue) -> ObjectProperty: ...
    def getPythonValue(self) -> _PythonValue: ...

class ObjectSnapshot:
    def getPythonValue(self) -> dict[str, _PythonValue]: ...

class PyDataLayerInterfaceType:
    # The python class registered with TypeRegistry.registerInterface: any user class.
    @property
    def typeObject(self) -> type[Any]: ...

class PyDataLayerServerType:
    @property
    def typeObject(self) -> type[Any]: ...

class PyDataLayerVisualizer:
    # The instance of the user's registered visualizer class.
    def pyObject(self) -> Any: ...

class PySubscriptionHandler:
    def pyObject(self) -> Any: ...

class PySubscriptionHandlerType:
    @property
    def typeObject(self) -> type[Any]: ...

class SubscriptionHandlerManager:
    def createSubscriptionHandler(self, *args, **kwargs) -> SubscriptionHandler | None: ...

class TypeRegistry:
    registerBackend: ClassVar[_RegisterType]
    registerInterface: ClassVar[_RegisterType]
    registerModuleTypes: ClassVar[_RegisterModuleTypes]
    registerServer: ClassVar[_RegisterType]
    registerSubscriptionHandler: ClassVar[_RegisterType]
    registerVisualizer: ClassVar[_RegisterType]
    @staticmethod
    def globPythonModules() -> list[str]: ...
    def registeredType(self, arg0: _pdgd.registeredType, arg1: str) -> BaseType | None: ...
    @staticmethod
    def searchPath() -> list[str]: ...

class language:
    __members__: ClassVar[dict[str, language]]

class registeredType:
    __members__: ClassVar[dict[str, registeredType]]
