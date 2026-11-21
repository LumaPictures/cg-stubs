# Houdini stubs generated from Houdini 22.0.466

import dataclasses
import hou
import os
import pathlib
import typing
from . import rtypes as rtypes
from collections.abc import Iterator, Mapping as Mapping, MutableMapping as MutableMapping
from houtypes import JSONLike
from typing import Callable as Callable, Iterable, Literal, Sequence, TypedDict, Unpack

from typing import TypeAlias
_NetworkItemsData: TypeAlias = rtypes.ClusterData | rtypes.NetworkItemData | rtypes.NetworkItemDataDict | Sequence[rtypes.NetworkItemData]
class _ParmTupleUserData(TypedDict, total=False):
    is_spare: bool
    use: bool
    off_default: bool
    is_enabled: bool
    value: rtypes.ParmUnionData | list[dict[str, rtypes.RampPointDataList | rtypes.MultiParmInstanceDataList]] | None

class _UserMetaData(TypedDict, total=False, extra_items=JSONLike):  # type: ignore[call-arg]
    input_names: Sequence[str]
    output_names: Sequence[str]
    item_size: Sequence[float]
    color: Sequence[float]
    type: str
    name: str
    node_type_category: str
    position: Sequence[float]
    is_network: bool
    network_category: str

class _UserDataContents(TypedDict, total=False, extra_items=JSONLike):  # type: ignore[call-arg]
    parm_tuple: dict[str, _ParmTupleUserData]
    meta_data: _UserMetaData
    version: str

class _WithUserData(TypedDict, total=False):
    sidefx: _UserDataContents

class _LegacyParmTemplateData(rtypes.ParmTemplateData, total=False):
    default: Sequence[int | float | str]
    interface: str
    template_type: str

class _UserDataOptionsDict(TypedDict):
    extra_opts: dict[str, JSONLike]
    save_pos_and_size: bool
    save_vop_connector_names: bool
    save_children: bool

class _UserDataOptionsChanges(TypedDict, total=False):
    extra_opts: dict[str, JSONLike]
    save_pos_and_size: bool
    save_vop_connector_names: bool
    save_children: bool

DECIMAL_PLACES: int
DEFAULT_TAB_SUBMENU: str
DEFAULT_SHELF_TAB: str
PRESET_DIR_NAME: str
DEFAULT_LIBRARY_NAME: str
DEFAULT_RECIPE_ICON_NAME: str
PARM_PRESET_ICON_NAME: str
NODE_PRESET_ICON_NAME: str
DECORATION_RECIPE_ICON_NAME: str
TOOL_RECIPE_ICON_NAME: str
DATA_RECIPE_ICON_NAME: str
LIBRARY_URL_SCHEME: str
DEFAULT_SAVE_PATH: str
folders: list[str]
tabbed_folders: list[str]
simple_folders: list[str]
multiparms: list[str]
nonvalueparms: list[str]
menus: list[str]
ramps: list[str]
colors: list[str]

def expandString(string: str) -> str:
    """ Resolves the env vars included as $<var name} in <string>.
        Returns the expanded string.
    """
@typing.overload
def expandedPath(pathstr: str, extension: str | None = ..., canonical: bool = ..., as_string: Literal[False] = ...) -> pathlib.Path: ...
@typing.overload
def expandedPath(pathstr: str, extension: str | None, canonical: bool, as_string: Literal[True]) -> str: ...
@typing.overload
def expandedPath(pathstr: str, extension: str | None = ..., canonical: bool = ..., *, as_string: Literal[True]) -> str: ...
@typing.overload
def expandedPath(pathstr: str, extension: str | None = ..., canonical: bool = ..., as_string: bool = ...) -> pathlib.Path | str: ...
def expandedPathString(pathstr: str) -> str: ...

HFS_PATH: pathlib.Path
UID_CHARS: str

def userPrefsDir() -> pathlib.Path: ...
def presetDir() -> pathlib.Path: ...
def shortenLocation(path: str | os.PathLike[str]) -> str: ...
def isUnderHFS(path: str | os.PathLike[str]) -> bool: ...
def isOnHoudiniPath(pathstr: str) -> bool: ...
def generateUniqueId(length: int = 14, prefix: str = '_') -> str: ...
def parseOpdefParts(opdef_path: str) -> tuple[str, str]: ...
def locationFromOpdef(location: str) -> str: ...
def findAssetDefinition(library_path: str | os.PathLike[str], typename_with_category: str) -> hou.HDADefinition | None: ...
def splitAssetLocationUrl(location: str) -> tuple[str, str, str]: ...
def reduceAssetUrlToOpdef(location: str) -> str: ...
def isDataAsset(defn: hou.HDADefinition) -> bool: ...
def isDataOpNodeType(nodetype: hou.NodeType) -> bool: ...
def makeXMLMenu(tokens: Sequence[str], labels: Sequence[str]) -> list[str]: ...
def constructToolLabels(tool_labels: Iterable[str], default_label: str) -> list[str]: ...
def legacyPresetNamesForNodeType(node_type: hou.NodeType) -> str: ...

@dataclasses.dataclass
class ParmTupleMetaData:
    is_spare: bool
    use: bool
    off_default: bool
    is_enabled: bool
    def asdict(self) -> _ParmTupleUserData: ...
    def replace(self, /, **changes: bool) -> ParmTupleMetaData: ...

class UserData:
    ''' Helper for centralizing the recipe user data mostly used 
        by the recipe UI.
        
        The UserData content is stored in the recipe json object
        under the "sidefx_user_data" object. Data that doesn\'t
        belong to the recipe data model should be added to 
        UserData avoid poluting the data model with junk.
    '''
    IDKEY: Literal['sidefx']
    PTKEY: Literal['parm_tuple']
    MDKEY: Literal['meta_data']
    VKEY: Literal['version']
    KEYS: tuple[Literal['parm_tuple'], Literal['meta_data'], Literal['version']]
    VERSION: str
    @dataclasses.dataclass
    class Options:
        extra_opts: dict[str, JSONLike] = dataclasses.field(default_factory=dict)
        save_pos_and_size: bool = ...
        save_vop_connector_names: bool = ...
        save_children: bool = ...
        def asdict(self) -> _UserDataOptionsDict: ...
        def replace(self, /, **changes: Unpack[_UserDataOptionsChanges]) -> UserData.Options: ...
    def __init__(self, data: _WithUserData | None = None) -> None: ...
    @typing.overload
    def __getitem__(self, index: Literal['parm_tuple']) -> dict[str, _ParmTupleUserData]: ...
    @typing.overload
    def __getitem__(self, index: Literal['meta_data']) -> _UserMetaData: ...
    @typing.overload
    def __getitem__(self, index: Literal['version']) -> str: ...
    @typing.overload
    def __getitem__(self, index: str) -> dict[str, _ParmTupleUserData] | _UserMetaData | JSONLike: ...
    @typing.overload
    def __setitem__(self, key: Literal['parm_tuple'], value: dict[str, _ParmTupleUserData]) -> None: ...
    @typing.overload
    def __setitem__(self, key: Literal['meta_data'], value: _UserMetaData) -> None: ...
    @typing.overload
    def __setitem__(self, key: Literal['version'], value: str) -> None: ...
    @typing.overload
    def __setitem__(self, key: str, value: JSONLike) -> None: ...
    def clear(self) -> None: ...
    def data(self) -> _UserDataContents: ...
    def attachTo(self, out_data: _WithUserData, key: str | None = None) -> None: ...
    def detachFrom(self, data: _WithUserData, key: str | None = None) -> None: ...
    def duplicate(self, key: str) -> None: ...
    def saveMetadata(self, node: hou.OpNode | None, opts: UserData.Options | None = None) -> None: ...

def itemSize(size: hou.Vector2 | Sequence[float]) -> tuple[float, float]: ...
def networkDataItems(data: _NetworkItemsData) -> Iterator[tuple[str, rtypes.NetworkItemData]]: ...
def wiresFromData(item_dicts: _NetworkItemsData, renamed: Callable[[str], str] | None = None, network: hou.Node | None = None) -> list[rtypes.ConnectionData]: ...
def indexSortKey(ix: str | int) -> str: ...
def desimplifyWireData(wiredata: str | rtypes.ConnectionData | rtypes.NetworkItemInputData | rtypes.NetworkItemOutputData, key: str, target_name: str, renamed: Callable[[str], str] | None = None) -> rtypes.ConnectionData: ...
def desimplifyWireList(wires: str | rtypes.ConnectionData | rtypes.NetworkItemInputData | rtypes.NetworkItemOutputData | Sequence[str | rtypes.ConnectionData | rtypes.NetworkItemInputData | rtypes.NetworkItemOutputData], key: str, target_name: str, renamed: Callable[[str], str] | None = None) -> list[rtypes.ConnectionData]: ...
def nodeTypeCategoryForName(category_name: str) -> hou.NodeTypeCategory | None: ...
def countContentsOfItem(item_data: rtypes.NetworkItemData, recursive: bool = True, count_editables: bool = True) -> int: ...
def isRampPoints(value: object) -> bool: ...
def isMultiparmValue(value: object) -> bool: ...
def parmTupleDataValues(data: rtypes.RecipeData) -> Sequence[rtypes.ParmValueType] | None: ...
def parmDataValue(value: rtypes.ParmValueType) -> rtypes.ParmValueType:
    """ Returns value as is or the nested value if value is a 
        dictionary.
    """
def parmTemplateDataDefaultValue(data: rtypes.ParmTemplateData | _LegacyParmTemplateData) -> Sequence[int | float | str]: ...
def debriefRecipeParmData(data: rtypes.ParmUnionData | rtypes.RampPointDataList) -> rtypes.ParmData:
    """ Makes a recipe parm data value non-brief
        NOTE: We assume data is already brief.
    """
def clusterCentralName(cluster_data: rtypes.ClusterData) -> str | None: ...
def countNetworkItemsInCluster(cluster_data: rtypes.ClusterData, recursive: bool = True, count_central_editables: bool = True, count_other_editables: bool = True) -> int: ...

nodetype_categories_mapping: dict[str, hou.NodeTypeCategory]
