from typing import *
import abc
import hou
from . import brush as lb
from _typeshed import Incomplete
from collections import defaultdict as defaultdict
from collections.abc import Callable as Callable, Sequence
from layout.utils import AssetGeneratorSig as _AssetGenerator
from typing import Any, ClassVar, Literal, Protocol, TypedDict

from typing import TypeAlias
from houtypes import HDALibraryEventKwargs
from houtypes import NodeEventKwargs
from typing import TypeAlias
_ALIEventKwargs: TypeAlias = NodeEventKwargs | HDALibraryEventKwargs | _ALISelectionChangedKwargs | _ALICustomEventKwargs
_DataSourceArg: TypeAlias = hou.AssetGalleryDataSource | list[str] | tuple[str, str]
class _AssetGenerateKwargs(TypedDict):
    container: hou.OpNode | None
    id: str
    data: bytes
    node: hou.LopNode
    prototype_node: hou.OpNode | None

class _LayoutAsset(Protocol):
    generator: ClassVar[_AssetGenerator]
    def __init__(self, ident: str, datasource: hou.AssetGalleryDataSource) -> None: ...
    def onGenerate(self, kwargs: _AssetGenerateKwargs) -> None: ...
    def validate(self, ident: str) -> None: ...

class _ALICustomEventKwargs(TypedDict):
    event_type: int
    data: Any

class _ALISelectionChangedKwargs(TypedDict):
    event_type: hou.EnumValue[hou.nodeEventType]

BRUSH_CATEGORY: str
BRUSH_TYPE_DEFAULT: str
COMMON_VARS: list[str]

class Asset(Incomplete, metaclass=abc.ABCMeta):
    def __init__(self, id: str) -> None:
        """
        All assets should have an ID field.
        """
    @property
    def id(self) -> str: ...
    def isValidAt(self, point: object) -> bool:
        """
        This function is called to prune assets placement
        points. This will allow us to define rules on
        where an asset is allowed to be placed.
        """
    @abc.abstractmethod
    def getBoundingBox(self) -> hou.BoundingBox:
        """
        All assets should override this to return a
        bounding box.
        """
    @abc.abstractmethod
    def onGenerate(self, kwargs: _AssetGenerateKwargs) -> None:
        """
        This function is called when a state wants to use an
        asset, and the asset layout interface for the associated node
        does not have access to a prototype of that asset.
        """
    @abc.abstractmethod
    def getPrototypeDescriptor(self) -> str:
        """
        This function should return a string describing
        the object this asset represents in a format
        houdini can understand.
        For example, in Solaris this should be the primpath.
        """
    @abc.abstractmethod
    def reload(self) -> None:
        """
        This function is called when the user triggers a reload
        of some or all assets. For regular USD assets this would
        just be reloading the reference LOP. This is meant to be an
        easy way to resolve differences between the asset database
        and the nodes that import the asset.
        """

def protoPathFromId(prototype_id: str) -> str: ...
def getFileNamePath(ident: str, datasource: _DataSourceArg | None = None) -> tuple[str, str, str]:
    """
    This function returns an assets filepath, its name, and a valid
    primitive path for it.

    ident must be a valid identifier in the AssetGallery
    """
def buildAsset(type_name: str, identifier: str, datasource: hou.AssetGalleryDataSource) -> _LayoutAsset: ...
def assetGenerator(type_name: str) -> _AssetGenerator: ...

class ALI:
    HDA_EVENT_TYPES: tuple[hou.EnumValue[hou.hdaEventType], ...]
    BRUSH_NODE_EVENT_TYPES: tuple[hou.EnumValue[hou.nodeEventType], ...]
    class eventType:
        BrushSelected: int
        StartPresetApplication: int
        EndPresetApplication: int
        PrototypesAdded: int
        RequestHUDUpdate: int
        AssetUpdated: int
    def __init__(self) -> None: ...
    @staticmethod
    def instance() -> ALI: ...
    @staticmethod
    def term() -> None: ...
    def setCurrentNode(self, node: hou.LopNode | None) -> None: ...
    def currentLayoutNode(self) -> hou.LopNode | None: ...
    def canSelectBrushNode(self) -> bool: ...
    def brushContainer(self) -> hou.ObjNode | None: ...
    def debugNodes(self) -> tuple[hou.SopNode | None, hou.SopNode | None]: ...
    def findNodeForBrush(self, node_type: hou.NodeType, preset_name: str) -> hou.SopNode | None: ...
    def findOrCreateNodeForBrush(self, node_type: hou.NodeType, preset_name: str) -> tuple[str, hou.SopNode, bool]: ...
    def selectBrush(self, node_type: hou.NodeType, preset_name: str = '') -> tuple[hou.SopNode, bool] | tuple[None, Literal[False]]: ...
    def emitCustomEvent(self, event_type: int, data: object) -> None:
        """ Emit an event defined as a ALI.eventType attribute. The
            data should be handled by the client(s) receiving the event.
        """
    def selectedBrushNode(self) -> hou.SopNode | None: ...
    def selectedBrushType(self, node: hou.Node | None = None) -> hou.SopNodeType: ...
    def addEventCallback(self, observer: Callable[[_ALIEventKwargs], object]) -> None: ...
    def removeEventCallback(self, observer: Callable[[_ALIEventKwargs], object]) -> None: ...
    def brushDefinitions(self) -> list[hou.HDADefinition]: ...
    def prototypesAdded(self, asset_ids: Sequence[str]) -> None: ...
    def prototypes(self) -> list[str]: ...
    def workingSet(self, ids: list[str] | None = None) -> list[str]: ...
    def createAsset(self, asset_id: str, datasource: _DataSourceArg) -> _LayoutAsset: ...
    def brushInterface(self, id: str) -> None: ...
    def getBrushInterface(self) -> lb.BrushInterface: ...

def instance() -> ALI: ...
def registerAsset(id: str, asset_defn: type[_LayoutAsset]) -> None: ...
def loadPlugins() -> None: ...
def onCreateLayoutNode() -> None: ...
def defaultBrushType() -> hou.SopNodeType | None:
    """ Returns the default brush type. Typically used by a UI such
        as the brush panel for initialization purposes.
    """
