# Houdini stubs generated from Houdini 22.0.466

from husd.utils import *
import hou
import husdui.prefs
import typing
from collections.abc import Iterable, Iterator, Sequence
from dbg import DbgPrinter
from husdui.common import debugPerfPaneEvent as debugPerfPaneEvent, debug_print as debug_print, error_print as error_print, getAttrBase as getAttrBase, getAttrIndex as getAttrIndex, getAttrIndexAndBase as getAttrIndexAndBase
from husdui.models.items import _ItemJson, _ItemJsonData
from pxr import Sdf, Usd
from typing import Never

from typing import TypeAlias
from typing import TypeVar
from husd.typeutils import _SdfValue
from typing import TypeAlias
from typing_extensions import TypeVar
_T = TypeVar('_T')
_D = TypeVar('_D', default=None)
_PathLike: TypeAlias = str | Sdf.Path
_PrimTypes: TypeAlias = Sequence[type[Usd.SchemaBase]]
_PathSpec: TypeAlias = str | Sdf.Path | list[str] | tuple[str, ...] | set[str]
_PrimPathSet: TypeAlias = set[Sdf.Path] | list[Sdf.Path] | tuple[Sdf.Path, ...]
_LinkTuple: TypeAlias = tuple[str, str, str, int, bool, str, str, bool, bool]
_StageValue: TypeAlias = _SdfValue | tuple[float, ...]
_AttrValue: TypeAlias = _StageValue | Sequence[float]
_ParmValueArg: TypeAlias = float | str | Sequence[float] | Sequence[str]
dbg: DbgPrinter
COLLECTIONS_FOLDER_NAME: str
SETTINGS_FOLDER_NAME: str
ATTRIBUTES_FOLDER_NAME: str

def getNewDbId() -> int: ...

class PathError(Exception): ...
class AttrNameError(Exception): ...
class ReadOnlyCollection(Exception): ...

def isCollectionParm(parm: hou.Parm | hou.ParmTuple | str) -> bool:
    """
    Given a parm, returns True if the parm is involved in defining collections.
    """
def addLink(node: hou.LopNode, prim: str, includes: _PathSpec, excludes: _PathSpec, linktype: int | str, is_reversed: bool, is_enabled: bool = True, is_path_expr: bool = False) -> None: ...
def removeLink(node: hou.LopNode, linknum: int) -> None: ...
def getLinks(node: hou.LopNode) -> list[_LinkTuple]: ...
def renameInLinks(node: hou.LopNode, primpath: str, newprimpath: str, rename_owner: bool = True, rename_target: bool = True) -> bool:
    """
    Looks for an explicit primpath in the links on a node and renames those primpaths.
    Renaming the link target and or owner can be optionally disabled.
    """
def removeInLinks(node: hou.LopNode, primpath: str) -> bool:
    """
    Looks for an explicit primpath in the links on a node and renames those primpaths.
    Renaming the link target and or owner can be optionally disabled.
    """
def setLink(node: hou.LopNode, linknum: int, prim: str | None = None, includes: _PathSpec | None = None, excludes: _PathSpec | None = None, is_enabled: bool | None = None, linktype: int | str | None = None, is_reversed: bool | None = None, is_path_expr: bool | None = None) -> None: ...
def linkParmNames(node: hou.Node | None, linknum: int) -> dict[str, str]: ...
def getPathFromParmName(parm_name: str) -> str: ...

class InputStageDB:
    """
    This class caches data from the input stage so it can be retrieved
    efficiently when needed.  Switching from the current stage to the input
    stage is an expensive process that should be avoided when possible.
    """
    id: int
    _prim_paths: set[Sdf.Path] | None
    def __init__(self, node: hou.LopNode | None, attr_names: list[str] | set[str], prefs: husdui.prefs.Prefs, prim_types: _PrimTypes | None = None) -> None: ...
    def node(self) -> hou.LopNode | None:
        """
        Returns the node this object is referencing.
        """
    def setNode(self, node: hou.LopNode | None) -> None:
        """
        Sets the node this object is referencing.
        """
    def primPaths(self) -> list[Sdf.Path]:
        """
        Returns the list of prims this object is caching.
        """
    def setPrimPaths(self, prim_paths: _PrimPathSet | None, update: bool = True) -> None:
        """
        Sets the list of prims this object is caching.
        """
    def addPrimPaths(self, prim_paths: _PrimPathSet | Sdf.Path | str, update: bool = True) -> None:
        """
        Adds to the list of prims this object is caching.
        """
    def getAttr(self, prim_path: _PathLike, attr_name: str) -> _StageValue | None:
        """
        Returns the value of the given attribute.

        :param prim_path: The path to the USD primitive with the attribute.
        :param attr_name: The name of the attribute to read.
        """
    def update(self) -> None:
        """
        Rebuild the whole cache and drop the cached input stage handle.
        Cache misses in between refreshes are filled incrementally by _cachePrim() instead.
        """

class StageDB:
    """
    This class wraps the API for getting values from the stage, for use by the
    light source model. It is designed so it can be replaced by the
    OverrideData subclass for use by the light mixer mode, which enhances the
    API to allow changing values by creating parameters on the light mixer
    node.
    """
    id: int
    def __init__(self, node: hou.LopNode, attr_names: list[str] | set[str], prefs: husdui.prefs.Prefs, prim_types: _PrimTypes | None = None) -> None: ...
    def node(self) -> hou.LopNode:
        """
        Returns the node this object is modifying.
        """
    def setNode(self, node: hou.LopNode) -> None:
        """
        Sets the node this object is modifying.
        """
    def prefs(self) -> husdui.prefs.Prefs:
        """
        Returns the is object's prefs object.
        """
    def cacheStage(self) -> None:
        """
        Cache the output stage handle for a synchronous tree build, so it
        isn't re-fetched once per prim. Pair with clearStageCache(), or a
        later cook will see a stale stage.
        """
    def clearStageCache(self) -> None: ...
    def stage(self) -> Usd.Stage:
        """
        Returns the post-cook USD stage of the node this object is modifying.
        """
    def update(self) -> None:
        """
        Update any caches that this DB is using
        """
    def primPaths(self) -> list[Sdf.Path]:
        """
        Returns the list of prims this object is caching.
        """
    def setPrimPaths(self, prim_paths: _PrimPathSet | None, update: bool = False) -> None:
        """
        Sets the list of prims this object is caching.
        """
    def setSolo(self, prim_paths: Iterable[str]) -> None:
        """
        Set the list of all soloed lights, clearing the previous list.
        """
    def remSolo(self, prim_paths: Iterable[str]) -> None:
        """
        remove the specified lights from the list of soloed lights.
        """
    def primIsSolo(self, prim_path: _PathLike) -> bool:
        """
        Solo is a special override case for muting all but the lights that
        are soloed.  There is a separate overrides layer just for soloing.
        """
    def setMute(self, prim_paths: Iterable[str]) -> None:
        """
        Mute the given lights in a single override transaction.
        """
    def remMute(self, prim_paths: Iterable[str]) -> None:
        """
        Un-mute the given lights in a single override transaction.
        """
    def primIsMute(self, prim_path: _PathLike) -> bool:
        """
        Muted means the prim has an override set that deactivates the prim.
        """
    def primIsActive(self, prim_path: _PathLike) -> bool:
        """
        Active means that the prim is active on the stage regardless of any
        overrides to the contrary.
        """
    def primIsValid(self, prim_path: _PathLike) -> bool: ...
    def attrIsOverridden(self, path: _PathLike, attr_name: str) -> bool:
        '''
        Returns True if the given attribute is overridden by parameters on the
        current node.

        Note that StageDB.attrIsOverridden() will report the same as
        OverrideData.attrIsOverridden() (True or False depending on whether a
        parameter exists to rewrite the given attribute) even though
        StageDB.getAttr() will only ever return the stage (pre- override)
        value. This allows the "source" interface to display an indicator of
        which items have overrides.
        '''
    def getInputAttr(self, prim_path: _PathLike, attr_name: str, default: _D | None = None, std_default: bool = True) -> _StageValue | Sequence[float] | _D:
        """
        Returns the value of the given attribute from the input stage.

        :param prim_path: The path to the USD primitive with the attribute.
        :param attr_name: The name of the attribute to read.
        """
    def getAttr(self, prim_path: _PathLike, attr_name: str, default: _D | None = None, std_default: bool = True) -> _AttrValue | _D | None:
        """
        Returns the value of the given attribute.

        :param prim_path: The path to the USD primitive with the attribute.
        :param attr_name: The name of the attribute to read.
        :param default: What to return if the given attribute does not exist.
            This is only used if `std_default` is False or the attribute
            is unknown.
        :param std_default: Use the standard default for the given attribute
            name. If this is False or the attribute is unknown, use the
            `default` argument.
        """
    def usdCollectionsOnPrim(self, prim_path: _PathLike) -> list[Usd.CollectionAPI]:
        """
        Returns a list of USD CollectionAPI objects on the given primitive.
        Returns an empty list if the primitive does not exist.
        """
    def collectionIsIncoming(self, prim_path: _PathLike, name: str) -> bool:
        """
        Returns True if the collection existed in the incoming stage.
        """
    def collectionContents(self, prim_path: _PathLike, name: str | None) -> list[str]:
        """
        Returns a sequence containing the paths currently in the given
        collection.

        :param prim_path: The path to the USD primitive that has the collection.
        :param name: The collection name.
        """
    def color(self, prim_path: _PathLike) -> hou.Color | None:
        '''
        Return a tuple of (red_float, green_float, blue_float) for the "inputs:color"
        attribute on the light primitive at the given path.
        '''

class ParmDB(StageDB):
    """
    While StageDB gets its values only from the stage, this object checks
    whether a value has been overridden by a parameter on the light mixer node.
    It also adds API for creating/setting override parameters.
    """
    UnknownType: int
    EditAttrType: int
    CreateCollectionType: int
    EditCollectionAttrType: int
    CustomAttrType: int
    DetailType: int
    LayoutType: int
    def __init__(self, node: hou.LopNode, attr_names: list[str] | set[str], prefs: husdui.prefs.Prefs, prim_types: _PrimTypes | None = None) -> None: ...
    def deleteAttrParm(self, prim_path: _PathLike, attr_name: str) -> None: ...
    def deleteAttrParms(self, prim_path_pairs: Iterable[tuple[_PathLike, str]]) -> None: ...
    def stageAttr(self, prim_path: _PathLike, attr_name: str, default: _D | None = None, std_default: bool = True) -> _AttrValue | _D | None:
        """
        Returns the pre-override value for the given attribute from the incoming
        stage. This has the same arguments as StageDB.getAttr().
        """
    def isShowingExpression(self, prim_path: _PathLike, attr_name: str) -> bool | None:
        """
        """
    def showExpression(self, prim_path: _PathLike, attr_name: str, value: bool) -> None:
        """
        """
    def getAttr(self, prim_path: _PathLike, attr_name: str, default: _D | None = None, on_stage: bool = True, std_default: bool = True) -> _AttrValue | _D | None:
        '''
        This method overrides StageDB.getAttr() and adds a "fallback"
        argument. If on_stage=True (the default), if the attribute is not
        overridden by a parameter, the method gets the value from the stage.
        '''
    def getAttrExpr(self, prim_path: _PathLike, attr_name: str, default: _D | None = None, on_stage: bool = True, std_default: bool = True) -> _AttrValue | list[str] | _D | None:
        '''
        This method overrides StageDB.getAttr() and adds a "fallback"
        argument. If on_stage=True (the default), if the attribute is not
        overridden by a parameter, the method gets the value from the stage.
        '''
    def getAttrRange(self, path: _PathLike, attr_name: str) -> tuple[float, float]: ...
    def setAttrRange(self, path: _PathLike, attr_name: str, minval: float, maxval: float) -> None: ...
    @typing.overload
    def getBooleanAttr(self, prim_path: _PathLike, attr_name: str, default: None = ..., on_stage: bool = ..., std_default: bool = ...) -> bool | None: ...
    @typing.overload
    def getBooleanAttr(self, prim_path: _PathLike, attr_name: str, default: _T, on_stage: bool = ..., std_default: bool = ...) -> bool | _T: ...
    def primIsActiveOnStage(self, prim_path: _PathLike) -> bool: ...
    def primIsActive(self, prim_path: _PathLike) -> bool: ...
    def isDefaultValue(self, prim_path: _PathLike, attr_name: str, value: _ParmValueArg | None) -> bool:
        """
        Is the value passed in the 'default' value, i.e. is it the value the
        same as the input stage.  This indicates the associated parm can be
        removed.
        """
    def collectionIsMute(self, coll_path: _PathLike) -> bool:
        """
        Muted means all prims in the collection are muted.
        """
    def isMute(self, prim_path: _PathLike) -> bool:
        """
        Return the mute state for either a collection or a prim.
        """
    def collectionIsSolo(self, coll_path: _PathLike) -> bool:
        """
        For a collection to be considered soloed, all members must be soloed.
        """
    def isSolo(self, prim_path: _PathLike) -> bool:
        """
        Return the solo state for either a collection or a prim.
        """
    def setAttrExpressionLanguage(self, prim_path: _PathLike, attr_name: str, language: hou.EnumValue[hou.exprLanguage]) -> None: ...
    def setAttrKeyFrame(self, prim_path: _PathLike, attr_name: str) -> None: ...
    def removeAttrKeyFrame(self, prim_path: _PathLike, attr_name: str) -> None: ...
    def setAttrLocked(self, prim_path: _PathLike, attr_name: str, value: bool, custom: bool = False) -> None: ...
    def setAttr(self, prim_path: _PathLike, attr_name: str, value: _ParmValueArg, custom: bool = False) -> None: ...
    def setTuple(self, parmtup: hou.ParmTuple, value: _ParmValueArg, comp_index: int) -> None: ...
    def setAttrs(self, attr_data: Sequence[tuple[str, str, _ParmValueArg, bool, bool]]) -> bool:
        """
        Like setAttr, but this will take an iterable (list) of parms so that
        the data can be written with as few event updates as possible.
        `attr_data` contains tuples of (prim_path, attr_name, value, custom)
        """
    def inspectParmTuple(self, parmtup: hou.ParmTuple) -> tuple[str, str, int]:
        '''
        Gets meta-data about the given parm-tuple from the USD-specific tags.
        Returns a tuple of ("prim_path", "attr_name", parm_type_enum).
        '''
    def usdCollectionsOnPrim(self, prim_path: _PathLike, include_new: bool = True) -> list[Usd.CollectionAPI]:
        """
        Returns a list of USD CollectionAPI objects on the given primitive.
        Returns an empty list if the primitive does not exist.
        """
    def collectionsOnPrim(self, prim_path: _PathLike, include_new: bool = True) -> list[str]: ...
    def stageCollectionContents(self, prim_path: _PathLike, name: str | None) -> list[str]: ...
    def collectionContents(self, prim_path: _PathLike, name: str | None = None) -> list[str]:
        """
        Returns a sequence containing the paths currently in the given
        collection, whether they come from the incoming stage, or from a parm on
        the node.
        """
    def collectionsCreatedHere(self) -> Iterator[tuple[str, str]]:
        '''
        Yields a series of `("prim_path", "collection_name")` pairs for
        collections created on this node.
        '''
    def createCollection(self, prim_path: _PathLike, name: str | None, includes: Iterable[str], excludes: Iterable[str] | None = None) -> str:
        '''
        Implements a "create an untitled collection" UI action. You can pass
        None as `name` and the function will pick a name that hasn\'t been
        used yet. If you do supply a name, the function will raise NameError
        if the name is already used.
        '''
    def setCollectionContents(self, prim_path: _PathLike, name: str, includes: Iterable[str], excludes: Iterable[str] | None = None) -> None:
        """
        Creates or updates a parameter on the node that tells it to create a
        colection (or rewrite the contents of an existing selection?) with the
        given list of paths.

        :param prim_path: The path to the USD primitive on which to create the
            new collection as a property.
        :param name: the name of the collection to create/rewrite.
        :param paths: a sequence of USD primitive paths to set as the collection
            contents.
        """
    def removeFromCollection(self, prim_path: _PathLike, name: str, paths: Iterable[_PathLike]) -> None: ...
    def deleteCollectionParm(self, prim_path: _PathLike, name: str) -> None:
        """
        Removes a parameter on the node that tells it to create a new
        collection. This does not remove a collection that existed in the
        incoming stage.

        :param prim_path: The path to the USD primitive that has the collection.
        :param name: The name of the collection to remove.
        """
    def removeCollection(self, prim_path: _PathLike, name: str) -> bool | list[Never]: ...
    def renameCollection(self, prim_path: _PathLike, name: str, new_name: str) -> None:
        """
        Simply does a delete followed by a set, to change the name of a
        collection created by a parameter on the node. You can't use this to
        rename a collection that exists in the incoming stage.

        :param prim_path: The path to the USD primitive that has the collection.
        :param name: The current name of the collection.
        :param new_name: The new collection name.
        """
    def collectionCreatedHere(self, prim_path: _PathLike, name: str) -> bool:
        """
        Returns True if the given collection is created/rewritten by a parameter
        on the node.

        :param prim_path: The path to the USD primitive that has the collection.
        :param name: The collection name.
        """
    def getLayoutJSON(self) -> list[_ItemJsonData | str]: ...
    def setLayoutJSON(self, jsondata: Sequence[_ItemJson | _ItemJsonData | str]) -> None: ...
    def getCollectionBranches(self) -> list[str]: ...
    def setCollectionBranches(self, pathlist: Iterable[str]) -> None: ...
    def inputStageColor(self, path: _PathLike, attr_name: str = 'inputs:color') -> _StageValue | Sequence[float]: ...
    def stageColor(self, path: _PathLike, attr_name: str = 'inputs:color') -> hou.Color | None:
        """
        Get a light's final color on the stage.  For collections this is the
        set value on the node or the identity color.
        """
    def color(self, path: _PathLike, attr_name: str = 'inputs:color', on_stage: bool = True) -> hou.Color:
        """
        Get a light's set color, this is what is being set to explicitly at
        this node, if nothing then it is its value on the input stage.
        """
    def parmTupleForDetail(self, name: str, create: bool = False) -> hou.ParmTuple | None: ...
    def parmAndTupleForAttr(self, prim_path: _PathLike, attr_name: str, create: bool = False, custom: bool = False, value: _ParmValueArg | None = None) -> tuple[str, hou.Parm | None, hou.ParmTuple | None]: ...
    def parmTupleForAttr(self, prim_path: _PathLike, attr_name: str, create: bool = False, custom: bool = False, value: _ParmValueArg | None = None) -> hou.ParmTuple | None:
        """
        Returns the parameter representing the given USD primitive attribute.
        If the parameter does not exist and create=True the method will create
        it on the current node.
        """
    def parmsForCollection(self, prim_path: _PathLike, name: str) -> dict[str, hou.Parm] | None: ...
    def parmForCollection(self, prim_path: _PathLike, name: str) -> hou.Parm | None: ...
    def getDetailString(self, name: str) -> str: ...
    def setDetailString(self, name: str, value: str) -> None: ...

def setup() -> None: ...
def teardown() -> None: ...
def test_get_from_stage() -> None: ...
def test_get_default() -> None: ...
def test_set_attr() -> None: ...
def test_create_collection() -> None: ...
def test_rewrite_collection() -> None: ...
def test_rename_collection() -> None: ...
def run_tests() -> None: ...
