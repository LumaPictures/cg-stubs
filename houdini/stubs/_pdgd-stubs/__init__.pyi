# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Sequence
import _pdg
import _pdg
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
import _pdgd
from _typeshed import Incomplete
from typing import Any, Callable, ClassVar, overload

class AppendValuesMessage(Message):
    def __init__(self, arg0: str, arg1: Sequence[ObjectProperty]) -> None:
        """__init__(self: _pdgd.AppendValuesMessage, arg0: str, arg1: UT_Array[PDGD_ObjectProperty]) -> None"""

class BaseType:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def instanceCount(self) -> int: ...
    @property
    def language(self) -> _pdgd.language: ...
    @property
    def typeLabel(self) -> str: ...
    @property
    def typeName(self) -> str: ...

class BaseTypeRegistry:
    def __init__(self, *, no_constructor: Never) -> None: ...

class Command:
    def __init__(self, arg0: str, arg1: ObjectProperty) -> None:
        """__init__(self: _pdgd.Command, arg0: str, arg1: _pdgd.ObjectProperty) -> None"""
    def getName(self) -> str:
        """getName(self: _pdgd.Command) -> str"""
    def getParameter(self) -> ObjectProperty:
        """getParameter(self: _pdgd.Command) -> _pdgd.ObjectProperty"""

class DataBackend:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def buildFilteredSet(self, *args, **kwargs) -> Never:
        """buildFilteredSet(self: _pdgd.DataBackend, arg0: UT_SortedSet<PDGD_DataBackend::QueryResultEntry, PDGD_DataBackend::QueryResultEntryComparer>, arg1: PDGD_QueryDefinition, arg2: _pdgd.DataLayerInterface) -> UT_SortedSet<PDGD_DataBackend::QueryResultEntry, PDGD_DataBackend::QueryResultEntryComparer>"""
    def getDataLayerInterface(self) -> DataLayerInterface:
        """getDataLayerInterface(self: _pdgd.DataBackend) -> _pdgd.DataLayerInterface"""
    def getMemoryUsage(self) -> int:
        """getMemoryUsage(self: _pdgd.DataBackend) -> int"""
    def toJson(self) -> str:
        """toJson(self: _pdgd.DataBackend) -> str"""

class DataBackendQueryResultEntry:
    position: int
    result: str
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdgd.DataBackendQueryResultEntry) -> None

        2. __init__(self: _pdgd.DataBackendQueryResultEntry, arg0: str, arg1: int) -> None
        """
    @overload
    def __init__(self, arg0: str, arg1: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdgd.DataBackendQueryResultEntry) -> None

        2. __init__(self: _pdgd.DataBackendQueryResultEntry, arg0: str, arg1: int) -> None
        """

class DataBackendQueryResults:
    InitialResults: Never
    SortedAndFiltered: Never
    def __init__(self) -> None:
        """__init__(self: _pdgd.DataBackendQueryResults) -> None"""

class DataBackendType(BaseType):
    def __init__(self, *, no_constructor: Never) -> None: ...

class DataLayerInterface(TypeInstance):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def getBackend(self) -> DataBackend:
        """getBackend(self: _pdgd.DataLayerInterface) -> PDGD_DataBackend

        Returns the backend being used by the interface
        """
    def getHandler(self, arg0: str, arg1: bool) -> SubscriptionHandler | None:
        """getHandler(self: _pdgd.DataLayerInterface, arg0: str, arg1: bool) -> PDGD_SubscriptionHandler

        Returns the handler for the given path
        """
    def getId(self) -> int:
        """getId(self: _pdgd.DataLayerInterface) -> int

        Returns the unique identifier for the interface
        """
    def init(self) -> bool:
        """init(self: _pdgd.DataLayerInterface) -> bool

        Performs any necessary initialization, called as soon as the interface is created
        """
    def sendCommand(self, arg0: str, arg1: _PythonValue, arg2: str) -> None:
        """sendCommand(self: _pdgd.DataLayerInterface, arg0: str, arg1: object, arg2: str) -> None"""
    def sendCommandWithCallback(self, arg0: str, arg1: _PythonValue, arg2: str, arg3: Callable[[ObjectProperty], object]) -> None:
        """sendCommandWithCallback(self: _pdgd.DataLayerInterface, arg0: str, arg1: object, arg2: str, arg3: object) -> None"""
    def subscribe(self, arg0: DataLayerVisualizer, arg1: str) -> None:
        """subscribe(self: _pdgd.DataLayerInterface, arg0: _pdgd.DataLayerVisualizer, arg1: str) -> None

        Creates a new subscription for the given visualizer and path
        """
    def term(self) -> None:
        """term(self: _pdgd.DataLayerInterface) -> None

        Performs any necessary cleanup, called when destroying the interface
        """
    def unsubscribe(self, arg0: DataLayerVisualizer, arg1: str) -> None:
        """unsubscribe(self: _pdgd.DataLayerInterface, arg0: _pdgd.DataLayerVisualizer, arg1: str) -> None

        Removes the subscription from the visualizer to the path
        """

class DataLayerInterfaceManager:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @staticmethod
    def Instance() -> DataLayerInterfaceManager:
        """Instance() -> _pdgd.DataLayerInterfaceManager"""
    def clear(self) -> None:
        """clear(self: _pdgd.DataLayerInterfaceManager) -> None"""
    def createInterface(self, arg0: str, arg1: str) -> DataLayerInterface | None:
        """createInterface(self: _pdgd.DataLayerInterfaceManager, arg0: str, arg1: str) -> PDGD_DataLayerInterface"""
    def destroyInterface(self, arg0: DataLayerInterface) -> None:
        """destroyInterface(self: _pdgd.DataLayerInterfaceManager, arg0: PDGD_DataLayerInterface) -> None"""
    def getInterfaceById(self, arg0: int) -> DataLayerInterface | None:
        """getInterfaceById(self: _pdgd.DataLayerInterfaceManager, arg0: int) -> PDGD_DataLayerInterface"""

class DataLayerInterfaceType(BaseType):
    def __init__(self, *, no_constructor: Never) -> None: ...

class DataLayerServer(TypeInstance):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def getPort(self) -> int:
        """getPort(self: _pdgd.DataLayerServer) -> int"""
    def isServing(self) -> bool:
        """isServing(self: _pdgd.DataLayerServer) -> bool"""
    def serve(self) -> None:
        """serve(self: _pdgd.DataLayerServer) -> None"""
    def stop(self) -> None:
        """stop(self: _pdgd.DataLayerServer) -> None"""

class DataLayerServerManager:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @staticmethod
    def Instance() -> DataLayerServerManager:
        """Instance() -> _pdgd.DataLayerServerManager"""
    def clear(self) -> None:
        """clear(self: _pdgd.DataLayerServerManager) -> None"""
    def createServer(self, arg0: str, arg1: int) -> DataLayerServer | None:
        """createServer(self: _pdgd.DataLayerServerManager, arg0: str, arg1: int) -> PDGD_DataLayerServer"""
    def destroyServer(self, arg0: DataLayerServer) -> None:
        """destroyServer(self: _pdgd.DataLayerServerManager, arg0: PDGD_DataLayerServer) -> None"""
    def listActiveServers(self) -> list[DataLayerServer]:
        """listActiveServers(self: _pdgd.DataLayerServerManager) -> list"""

class DataLayerServerType(BaseType):
    def __init__(self, *, no_constructor: Never) -> None: ...

class DataLayerVisualizer:
    def __init__(self) -> None:
        """__init__(self: _pdgd.DataLayerVisualizer) -> None"""
    def processMessage(self, arg0: Message, arg1: str) -> None:
        """processMessage(self: _pdgd.DataLayerVisualizer, arg0: _pdgd.Message, arg1: str) -> None"""
    def subscriptionLost(self, arg0: str) -> None:
        """subscriptionLost(self: _pdgd.DataLayerVisualizer, arg0: str) -> None"""

class DataLayerVisualizerManager:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @staticmethod
    def Instance() -> DataLayerVisualizerManager:
        """Instance() -> _pdgd.DataLayerVisualizerManager"""
    def clear(self) -> None:
        """clear(self: _pdgd.DataLayerVisualizerManager) -> None"""
    def createVisualizer(self, *args, **kwargs) -> DataLayerVisualizer:
        """createVisualizer(*args, **kwargs) -> PDGD_DataLayerVisualizer"""
    def destroyVisualizer(self, arg0: DataLayerVisualizer) -> None:
        """destroyVisualizer(self: _pdgd.DataLayerVisualizerManager, arg0: PDGD_DataLayerVisualizer) -> None"""

class GlobalDataLayerInstance:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @staticmethod
    def Instance() -> DataLayerInterface:
        """Instance() -> PDGD_DataLayerInterface"""

class LocalDataLayer(DataLayerInterface):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def addRootSubscriptionHandler(self, arg0: str, arg1: str) -> None:
        """addRootSubscriptionHandler(self: _pdgd.LocalDataLayer, arg0: str, arg1: str) -> None

        Register a root subscription handler
        """
    def getMemoryUsage(self) -> int:
        """getMemoryUsage(self: _pdgd.LocalDataLayer) -> int"""

class Message:
    class MessageType:
        __members__: ClassVar[dict[str, Message.MessageType]] = ...  # read-only
        __entries: ClassVar[dict[str, tuple[Message.MessageType, str | None]]] = ...
        eMessageTypeAppendValues: ClassVar[Message.MessageType] = ...
        eMessageTypeObjectSnapshot: ClassVar[Message.MessageType] = ...
        eMessageTypeRemoveValues: ClassVar[Message.MessageType] = ...
        eMessageTypeSetValue: ClassVar[Message.MessageType] = ...
        eMessageTypeSetValues: ClassVar[Message.MessageType] = ...
        def __init__(self, value: int) -> None:
            """__init__(self: _pdgd.Message.MessageType, value: int) -> None"""
        def __eq__(self, other: object) -> bool:
            """__eq__(self: object, other: object) -> bool"""
        def __hash__(self) -> int:
            """__hash__(self: object) -> int"""
        def __index__(self) -> int:
            """__index__(self: _pdgd.Message.MessageType) -> int"""
        def __int__(self) -> int:
            """__int__(self: _pdgd.Message.MessageType) -> int"""
        def __ne__(self, other: object) -> bool:
            """__ne__(self: object, other: object) -> bool"""
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...
    eMessageTypeAppendValues: ClassVar[Message.MessageType] = ...
    eMessageTypeObjectSnapshot: ClassVar[Message.MessageType] = ...
    eMessageTypeRemoveValues: ClassVar[Message.MessageType] = ...
    eMessageTypeSetValue: ClassVar[Message.MessageType] = ...
    eMessageTypeSetValues: ClassVar[Message.MessageType] = ...
    def __init__(self, *, no_constructor: Never) -> None: ...
    def getObjectSnapshot(self) -> ObjectSnapshot:
        """getObjectSnapshot(self: _pdgd.Message) -> _pdgd.ObjectSnapshot"""
    def getPropertyArray(self) -> list[ObjectProperty]:
        """getPropertyArray(self: _pdgd.Message) -> UT_Array[PDGD_ObjectProperty]"""
    def getPropertyName(self) -> str:
        """getPropertyName(self: _pdgd.Message) -> str"""
    def getType(self) -> Message.MessageType:
        """getType(self: _pdgd.Message) -> PDGD_Message::PDGD_MessageType"""
    def toJson(self) -> str:
        """toJson(self: _pdgd.Message) -> str"""
    def toPython(self) -> _MessageDict:
        """toPython(self: _pdgd.Message) -> dict"""

class ObjectProperty:
    class Type:
        __members__: ClassVar[dict[str, ObjectProperty.Type]] = ...  # read-only
        __entries: ClassVar[dict[str, tuple[ObjectProperty.Type, str | None]]] = ...
        eTypeArray: ClassVar[ObjectProperty.Type] = ...
        eTypeBool: ClassVar[ObjectProperty.Type] = ...
        eTypeFloat: ClassVar[ObjectProperty.Type] = ...
        eTypeInt: ClassVar[ObjectProperty.Type] = ...
        eTypeSet: ClassVar[ObjectProperty.Type] = ...
        eTypeString: ClassVar[ObjectProperty.Type] = ...
        def __init__(self, value: int) -> None:
            """__init__(self: _pdgd.ObjectProperty.Type, value: int) -> None"""
        def __eq__(self, other: object) -> bool:
            """__eq__(self: object, other: object) -> bool"""
        def __hash__(self) -> int:
            """__hash__(self: object) -> int"""
        def __index__(self) -> int:
            """__index__(self: _pdgd.ObjectProperty.Type) -> int"""
        def __int__(self) -> int:
            """__int__(self: _pdgd.ObjectProperty.Type) -> int"""
        def __ne__(self, other: object) -> bool:
            """__ne__(self: object, other: object) -> bool"""
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...
    eTypeArray: ClassVar[ObjectProperty.Type] = ...
    eTypeBool: ClassVar[ObjectProperty.Type] = ...
    eTypeFloat: ClassVar[ObjectProperty.Type] = ...
    eTypeInt: ClassVar[ObjectProperty.Type] = ...
    eTypeSet: ClassVar[ObjectProperty.Type] = ...
    eTypeString: ClassVar[ObjectProperty.Type] = ...
    def __init__(self, arg0: float) -> None:
        """__init__(self: _pdgd.ObjectProperty, arg0: float) -> None"""
    @staticmethod
    def FromPython(arg0: _PythonValue) -> ObjectProperty:
        """FromPython(arg0: object) -> _pdgd.ObjectProperty"""
    def getArrayValue(self) -> list[ObjectProperty]:
        """getArrayValue(self: _pdgd.ObjectProperty) -> UT_Array[_pdgd.ObjectProperty]"""
    def getBoolValue(self) -> bool:
        """getBoolValue(self: _pdgd.ObjectProperty) -> bool"""
    def getFloatValue(self) -> float:
        """getFloatValue(self: _pdgd.ObjectProperty) -> float"""
    def getIntValue(self) -> int:
        """getIntValue(self: _pdgd.ObjectProperty) -> int"""
    def getPythonValue(self) -> _PythonValue:
        """getPythonValue(self: _pdgd.ObjectProperty) -> object"""
    def getSetValue(self) -> set[ObjectProperty]:
        """getSetValue(self: _pdgd.ObjectProperty) -> UT_Set[_pdgd.ObjectProperty]"""
    def getStringValue(self) -> str:
        """getStringValue(self: _pdgd.ObjectProperty) -> str"""
    def getType(self) -> ObjectProperty.Type:
        """getType(self: _pdgd.ObjectProperty) -> PDGD_ObjectProperty::Type"""

class ObjectSnapshot:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdgd.ObjectSnapshot) -> None

        2. __init__(self: _pdgd.ObjectSnapshot, arg0: str) -> None
        """
    @overload
    def __init__(self, arg0: str) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdgd.ObjectSnapshot) -> None

        2. __init__(self: _pdgd.ObjectSnapshot, arg0: str) -> None
        """
    def appendPropertyValue(self, arg0: str, arg1: ObjectProperty) -> None:
        """appendPropertyValue(self: _pdgd.ObjectSnapshot, arg0: str, arg1: PDGD_ObjectProperty) -> None"""
    def appendPropertyValues(self, arg0: str, arg1: Sequence[ObjectProperty]) -> None:
        """appendPropertyValues(self: _pdgd.ObjectSnapshot, arg0: str, arg1: UT_Array[PDGD_ObjectProperty]) -> None"""
    def getProperties(self) -> dict[str, ObjectProperty]:
        """getProperties(self: _pdgd.ObjectSnapshot) -> dict[str, PDGD_ObjectProperty]"""
    def getProperty(self, arg0: str) -> ObjectProperty:
        """getProperty(self: _pdgd.ObjectSnapshot, arg0: str) -> PDGD_ObjectProperty"""
    def getPropertyKeys(self) -> list[str]:
        """getPropertyKeys(self: _pdgd.ObjectSnapshot) -> UT_Array[str]"""
    def getPythonValue(self) -> dict[str, _PythonValue]:
        """getPythonValue(self: _pdgd.ObjectSnapshot) -> object"""
    def hasProperty(self, arg0: str) -> bool:
        """hasProperty(self: _pdgd.ObjectSnapshot, arg0: str) -> bool"""
    def removeProperty(self, arg0: str) -> None:
        """removeProperty(self: _pdgd.ObjectSnapshot, arg0: str) -> None"""
    def removePropertyValueAtIndex(self, arg0: str, arg1: int) -> None:
        """removePropertyValueAtIndex(self: _pdgd.ObjectSnapshot, arg0: str, arg1: int) -> None"""
    def removePropertyValues(self, arg0: str, arg1: Sequence[ObjectProperty]) -> None:
        """removePropertyValues(self: _pdgd.ObjectSnapshot, arg0: str, arg1: UT_Array[PDGD_ObjectProperty]) -> None"""
    def setName(self, arg0: str) -> None:
        """setName(self: _pdgd.ObjectSnapshot, arg0: str) -> None"""
    def setProperty(self, arg0: str, arg1: ObjectProperty) -> None:
        """setProperty(self: _pdgd.ObjectSnapshot, arg0: str, arg1: PDGD_ObjectProperty) -> None"""
    def setPropertyArrayValue(self, arg0: str, arg1: ObjectProperty) -> None:
        """setPropertyArrayValue(self: _pdgd.ObjectSnapshot, arg0: str, arg1: PDGD_ObjectProperty) -> None"""
    def setPropertyValues(self, arg0: str, arg1: Sequence[ObjectProperty]) -> None:
        """setPropertyValues(self: _pdgd.ObjectSnapshot, arg0: str, arg1: UT_Array[PDGD_ObjectProperty]) -> None"""
    def setPropertyValuesSet(self, arg0: str, arg1: set[ObjectProperty]) -> None:
        """setPropertyValuesSet(self: _pdgd.ObjectSnapshot, arg0: str, arg1: UT_Set[PDGD_ObjectProperty]) -> None"""
    def toJson(self) -> str:
        """toJson(self: _pdgd.ObjectSnapshot) -> str"""

class ObjectSnapshotMessage(Message):
    def __init__(self, arg0: ObjectSnapshot) -> None:
        """__init__(self: _pdgd.ObjectSnapshotMessage, arg0: _pdgd.ObjectSnapshot) -> None"""

class Preferences:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @staticmethod
    def getAutoServePDGState() -> bool:
        """getAutoServePDGState() -> bool"""
    @staticmethod
    def getDefaultBackend() -> str:
        """getDefaultBackend() -> str"""
    @staticmethod
    def getDefaultPDGStateServerPort() -> str:
        """getDefaultPDGStateServerPort() -> str"""
    @staticmethod
    def load() -> None:
        """load() -> None"""
    @staticmethod
    def save() -> None:
        """save() -> None"""
    @staticmethod
    def setAutoServePDGState(arg0: bool) -> None:
        """setAutoServePDGState(arg0: bool) -> None"""
    @staticmethod
    def setDefaultDataBackend(arg0: str) -> None:
        """setDefaultDataBackend(arg0: str) -> None"""
    @overload
    @staticmethod
    def setDefaultPDGStateServerPort(arg0: str) -> None:
        """setDefaultPDGStateServerPort(*args, **kwargs)
        Overloaded function.

        1. setDefaultPDGStateServerPort(arg0: str) -> None

        2. setDefaultPDGStateServerPort(arg0: int) -> None
        """
    @overload
    @staticmethod
    def setDefaultPDGStateServerPort(arg0: int) -> None:
        """setDefaultPDGStateServerPort(*args, **kwargs)
        Overloaded function.

        1. setDefaultPDGStateServerPort(arg0: str) -> None

        2. setDefaultPDGStateServerPort(arg0: int) -> None
        """

class PropertyNames:
    AttributePrefix: ClassVar[str] = ...  # read-only
    BatchIndex: ClassVar[str] = ...  # read-only
    BatchParentId: ClassVar[str] = ...  # read-only
    BatchParentIndex: ClassVar[str] = ...  # read-only
    BatchParentName: ClassVar[str] = ...  # read-only
    Children: ClassVar[str] = ...  # read-only
    Command: ClassVar[str] = ...  # read-only
    CookTime: ClassVar[str] = ...  # read-only
    DataDir: ClassVar[str] = ...  # read-only
    Dependencies: ClassVar[str] = ...  # read-only
    Dependents: ClassVar[str] = ...  # read-only
    ExpectedInputData: ClassVar[str] = ...  # read-only
    ExpectedInputTag: ClassVar[str] = ...  # read-only
    ExpectedResultData: ClassVar[str] = ...  # read-only
    ExpectedResultTag: ClassVar[str] = ...  # read-only
    Frame: ClassVar[str] = ...  # read-only
    GraphList: ClassVar[str] = ...  # read-only
    HasFrame: ClassVar[str] = ...  # read-only
    Icon: ClassVar[str] = ...  # read-only
    Id: ClassVar[str] = ...  # read-only
    InProcess: ClassVar[str] = ...  # read-only
    Index: ClassVar[str] = ...  # read-only
    InputData: ClassVar[str] = ...  # read-only
    InputTag: ClassVar[str] = ...  # read-only
    Inputs: ClassVar[str] = ...  # read-only
    IsCooking: ClassVar[str] = ...  # read-only
    IsDirtying: ClassVar[str] = ...  # read-only
    LastError: ClassVar[str] = ...  # read-only
    LastWarning: ClassVar[str] = ...  # read-only
    LogDir: ClassVar[str] = ...  # read-only
    Name: ClassVar[str] = ...  # read-only
    NoGenerate: ClassVar[str] = ...  # read-only
    Node: ClassVar[str] = ...  # read-only
    NodeList: ClassVar[str] = ...  # read-only
    NodeName: ClassVar[str] = ...  # read-only
    OutputSize: ClassVar[str] = ...  # read-only
    Outputs: ClassVar[str] = ...  # read-only
    Parents: ClassVar[str] = ...  # read-only
    Path: ClassVar[str] = ...  # read-only
    Position: ClassVar[str] = ...  # read-only
    Priority: ClassVar[str] = ...  # read-only
    Progress: ClassVar[str] = ...  # read-only
    QueryId: ClassVar[str] = ...  # read-only
    ResultData: ClassVar[str] = ...  # read-only
    ResultTag: ClassVar[str] = ...  # read-only
    Results: ClassVar[str] = ...  # read-only
    RootHandlerName: ClassVar[str] = ...  # read-only
    Scheduler: ClassVar[str] = ...  # read-only
    Schedulers: ClassVar[str] = ...  # read-only
    ScriptDir: ClassVar[str] = ...  # read-only
    SelectedWorkItem: ClassVar[str] = ...  # read-only
    State: ClassVar[str] = ...  # read-only
    StateCounts: ClassVar[str] = ...  # read-only
    SubType: ClassVar[str] = ...  # read-only
    Type: ClassVar[str] = ...  # read-only
    WorkItems: ClassVar[str] = ...  # read-only
    WorkingDir: ClassVar[str] = ...  # read-only
    def __init__(self, *, no_constructor: Never) -> None: ...

class PyDataLayerInterfaceType(DataLayerInterfaceType, _pdg.PyBaseObject):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def typeObject(self) -> type[Any]: ...

class PyDataLayerServerType(DataLayerServerType, _pdg.PyBaseObject):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def typeObject(self) -> type[Any]: ...

class PyDataLayerVisualizer(DataLayerVisualizer):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def pyObject(self) -> Any:
        """pyObject(self: _pdgd.PyDataLayerVisualizer) -> object"""

class PySubscriptionHandler(SubscriptionHandler):
    def __init__(self, *, no_constructor: Never) -> None: ...
    def pyObject(self) -> Any:
        """pyObject(self: _pdgd.PySubscriptionHandler) -> object"""

class PySubscriptionHandlerType(SubscriptionHandlerType, _pdg.PyBaseObject):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def typeObject(self) -> type[Any]: ...

class QueryDefinition:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdgd.QueryDefinition) -> None

        2. __init__(self: _pdgd.QueryDefinition, arg0: str) -> None
        """
    @overload
    def __init__(self, arg0: str) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdgd.QueryDefinition) -> None

        2. __init__(self: _pdgd.QueryDefinition, arg0: str) -> None
        """
    def addFilterArray(self, arg0: Sequence[QueryDefinitionFilter]) -> None:
        """addFilterArray(self: _pdgd.QueryDefinition, arg0: UT_Array[_pdgd.QueryDefinitionFilter]) -> None"""
    def addPropertyPath(self, arg0: str) -> None:
        """addPropertyPath(self: _pdgd.QueryDefinition, arg0: str) -> None"""
    def getFilterArray(self) -> list[list[QueryDefinitionFilter]]:
        """getFilterArray(self: _pdgd.QueryDefinition) -> UT_Array[UT_Array[_pdgd.QueryDefinitionFilter]]"""
    def getFormatString(self) -> str:
        """getFormatString(self: _pdgd.QueryDefinition) -> str"""
    def getPartialSortCount(self) -> int:
        """getPartialSortCount(self: _pdgd.QueryDefinition) -> int"""
    def getPropertyPaths(self) -> dict[str, list[str]]:
        """getPropertyPaths(self: _pdgd.QueryDefinition) -> dict[str, UT_Array[str]]"""
    def getPropertyPathsArray(self) -> list[str]:
        """getPropertyPathsArray(self: _pdgd.QueryDefinition) -> UT_Array[str]"""
    def getSortProperty(self) -> str:
        """getSortProperty(self: _pdgd.QueryDefinition) -> str"""
    def isPartiallySorted(self) -> bool:
        """isPartiallySorted(self: _pdgd.QueryDefinition) -> bool"""
    def isSortReversed(self) -> bool:
        """isSortReversed(self: _pdgd.QueryDefinition) -> bool"""
    def isSorted(self) -> bool:
        """isSorted(self: _pdgd.QueryDefinition) -> bool"""
    def readFromJson(self, arg0: str) -> bool:
        """readFromJson(self: _pdgd.QueryDefinition, arg0: str) -> bool"""
    def setFormatString(self, arg0: str) -> None:
        """setFormatString(self: _pdgd.QueryDefinition, arg0: str) -> None"""
    def setPartialSortCount(self, arg0: int) -> None:
        """setPartialSortCount(self: _pdgd.QueryDefinition, arg0: int) -> None"""
    def setPartiallySorted(self, arg0: bool) -> None:
        """setPartiallySorted(self: _pdgd.QueryDefinition, arg0: bool) -> None"""
    def setSortProperty(self, arg0: str) -> None:
        """setSortProperty(self: _pdgd.QueryDefinition, arg0: str) -> None"""
    def setSorted(self, arg0: bool) -> None:
        """setSorted(self: _pdgd.QueryDefinition, arg0: bool) -> None"""
    def toJson(self) -> str:
        """toJson(self: _pdgd.QueryDefinition) -> str"""

class QueryDefinitionFilter:
    FilterValue: ObjectProperty
    Negate: bool
    PropertyName: str
    @overload
    def __init__(self, arg0: str, arg1: str, arg2: bool) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdgd.QueryDefinitionFilter, arg0: str, arg1: str, arg2: bool) -> None

        2. __init__(self: _pdgd.QueryDefinitionFilter, arg0: str, arg1: int, arg2: bool) -> None

        3. __init__(self: _pdgd.QueryDefinitionFilter, arg0: str, arg1: float, arg2: bool) -> None

        4. __init__(self: _pdgd.QueryDefinitionFilter, arg0: str, arg1: bool, arg2: bool) -> None
        """
    @overload
    def __init__(self, arg0: str, arg1: int, arg2: bool) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdgd.QueryDefinitionFilter, arg0: str, arg1: str, arg2: bool) -> None

        2. __init__(self: _pdgd.QueryDefinitionFilter, arg0: str, arg1: int, arg2: bool) -> None

        3. __init__(self: _pdgd.QueryDefinitionFilter, arg0: str, arg1: float, arg2: bool) -> None

        4. __init__(self: _pdgd.QueryDefinitionFilter, arg0: str, arg1: bool, arg2: bool) -> None
        """
    @overload
    def __init__(self, arg0: str, arg1: float, arg2: bool) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _pdgd.QueryDefinitionFilter, arg0: str, arg1: str, arg2: bool) -> None

        2. __init__(self: _pdgd.QueryDefinitionFilter, arg0: str, arg1: int, arg2: bool) -> None

        3. __init__(self: _pdgd.QueryDefinitionFilter, arg0: str, arg1: float, arg2: bool) -> None

        4. __init__(self: _pdgd.QueryDefinitionFilter, arg0: str, arg1: bool, arg2: bool) -> None
        """

class RemoveValuesMessage(Message):
    def __init__(self, arg0: str, arg1: Sequence[ObjectProperty]) -> None:
        """__init__(self: _pdgd.RemoveValuesMessage, arg0: str, arg1: UT_Array[PDGD_ObjectProperty]) -> None"""

class SetValueMessage(Message):
    def __init__(self, arg0: str, arg1: ObjectProperty) -> None:
        """__init__(self: _pdgd.SetValueMessage, arg0: str, arg1: PDGD_ObjectProperty) -> None"""

class SetValuesMessage(Message):
    def __init__(self, arg0: str, arg1: Sequence[ObjectProperty]) -> None:
        """__init__(self: _pdgd.SetValuesMessage, arg0: str, arg1: UT_Array[PDGD_ObjectProperty]) -> None"""

class SubscriptionHandler:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def addChildHandler(self, arg0: str, arg1: SubscriptionHandler) -> None:
        """addChildHandler(self: _pdgd.SubscriptionHandler, arg0: str, arg1: _pdgd.SubscriptionHandler) -> None"""
    def buildSnapshot(self) -> ObjectSnapshot:
        """buildSnapshot(self: _pdgd.SubscriptionHandler) -> _pdgd.ObjectSnapshot"""
    def disableSnapshotStorage(self) -> None:
        """disableSnapshotStorage(self: _pdgd.SubscriptionHandler) -> None"""
    def enableSnapshotStorage(self) -> None:
        """enableSnapshotStorage(self: _pdgd.SubscriptionHandler) -> None"""
    def getObjectName(self) -> str:
        """getObjectName(self: _pdgd.SubscriptionHandler) -> str"""
    def isSnapshotStorageEnabled(self) -> bool:
        """isSnapshotStorageEnabled(self: _pdgd.SubscriptionHandler) -> bool"""
    def onVisualizerAdded(self, arg0: DataLayerVisualizer) -> None:
        """onVisualizerAdded(self: _pdgd.SubscriptionHandler, arg0: PDGD_DataLayerVisualizer) -> None"""
    def processAndSendMessage(self, arg0: Message) -> None:
        """processAndSendMessage(self: _pdgd.SubscriptionHandler, arg0: _pdgd.Message) -> None"""
    def processCommand(self, arg0: Command) -> None:
        """processCommand(self: _pdgd.SubscriptionHandler, arg0: PDGD_Command) -> None"""
    def processCommandWithCallback(self, arg0: Command) -> ObjectProperty:
        """processCommandWithCallback(self: _pdgd.SubscriptionHandler, arg0: PDGD_Command) -> _pdgd.ObjectProperty"""
    def removeChildHandler(self, arg0: str) -> None:
        """removeChildHandler(self: _pdgd.SubscriptionHandler, arg0: str) -> None"""

class SubscriptionHandlerManager:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @staticmethod
    def Instance() -> SubscriptionHandlerManager:
        """Instance() -> _pdgd.SubscriptionHandlerManager"""
    def clear(self) -> None:
        """clear(self: _pdgd.SubscriptionHandlerManager) -> None"""
    def createSubscriptionHandler(self, *args, **kwargs) -> SubscriptionHandler | None:
        """createSubscriptionHandler(*args, **kwargs) -> PDGD_SubscriptionHandler"""
    def destroySubscriptionHandler(self, arg0: SubscriptionHandler) -> None:
        """destroySubscriptionHandler(self: _pdgd.SubscriptionHandlerManager, arg0: PDGD_SubscriptionHandler) -> None"""

class SubscriptionHandlerType(BaseType):
    def __init__(self, *, no_constructor: Never) -> None: ...

class TypeInstance:
    def __init__(self, *, no_constructor: Never) -> None: ...
    @property
    def type(self) -> BaseType: ...
    @property
    def typeName(self) -> str: ...

class TypeRegistry(BaseTypeRegistry):
    registerBackend: ClassVar[_RegisterType] = ...
    registerInterface: ClassVar[_RegisterType] = ...
    registerModuleTypes: ClassVar[_RegisterModuleTypes] = ...
    registerServer: ClassVar[_RegisterType] = ...
    registerSubscriptionHandler: ClassVar[_RegisterType] = ...
    registerVisualizer: ClassVar[_RegisterType] = ...
    def __init__(self, *, no_constructor: Never) -> None: ...
    @staticmethod
    def Instance() -> TypeRegistry:
        """Instance() -> _pdgd.TypeRegistry"""
    def getInterfaceProtocol(self, arg0: str) -> str:
        """getInterfaceProtocol(self: _pdgd.TypeRegistry, arg0: str) -> str"""
    @staticmethod
    def globPythonModules() -> list[str]:
        """globPythonModules() -> object

        Return the list of all .py files in the types subpath

        """
    def registeredType(self, arg0: _pdgd.registeredType, arg1: str) -> BaseType | None:
        """registeredType(self: _pdgd.TypeRegistry, arg0: _pdgd.registeredType, arg1: str) -> _pdgd.BaseType"""
    @staticmethod
    def searchPath() -> list[str]:
        """searchPath() -> object

        Returns the pdg search path

        """
    def typeNames(self, type: _pdgd.registeredType, include_aliases: bool = ...) -> list[str]:
        """typeNames(self: _pdgd.TypeRegistry, type: _pdgd.registeredType, include_aliases: bool = False) -> UT_Array[str]"""

class language:
    __members__: ClassVar[dict[str, language]] = ...  # read-only
    Cpp: ClassVar[language] = ...
    Python: ClassVar[language] = ...
    __entries: ClassVar[dict[str, tuple[language, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdgd.language, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdgd.language) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdgd.language) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class registeredType:
    __members__: ClassVar[dict[str, registeredType]] = ...  # read-only
    DataLayerBackend: ClassVar[registeredType] = ...
    DataLayerInterface: ClassVar[registeredType] = ...
    DataLayerServer: ClassVar[registeredType] = ...
    DataLayerSubscriptionHandler: ClassVar[registeredType] = ...
    DataLayerVisualizer: ClassVar[registeredType] = ...
    __entries: ClassVar[dict[str, tuple[registeredType, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _pdgd.registeredType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _pdgd.registeredType) -> int"""
    def __int__(self) -> int:
        """__int__(self: _pdgd.registeredType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...
