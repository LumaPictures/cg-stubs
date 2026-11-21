# Houdini stubs generated from Houdini 22.0.466

import hou
import re
import typing
from .. import rtypes as rtypes
from collections.abc import Mapping
from typing import Any, Literal, Sequence

from typing import TypeVar
from typing import TypeVar
_K = TypeVar('_K')
_V = TypeVar('_V')
_KwargsT = TypeVar('_KwargsT', bound=dict[str, Any])
DATAMODEL_VERSION: str
special_nodetypes: list[str]
nodetype_categories_mapping: dict[str, hou.NodeTypeCategory]
ramp_point_parmnames: dict[hou.EnumValue[hou.rampParmType], tuple[str, ...]]

class DataCollector:
    def __init__(self) -> None: ...
    def setData(self, key: str, value: bool) -> None: ...
    def data(self) -> dict[str, bool]: ...

def findType(match_string: str) -> str: ...
def nodeTypeNameFromEditablePath(node_type: hou.OpNodeType, editable_path: str) -> str | None:
    """
    Loads the CPIO Data for a digital asset to check for the node types making up the editable path.
    There is no other way to get this information.
    """
def findCategoryName(data: Mapping[str, rtypes.NetworkItemData]) -> str: ...
def validateType(type_name: str, nodetype_category: hou.NodeTypeCategory, invalid_types: dict[str, dict[str, list[str]]] = ..., data_path: str = '') -> hou.NodeType | Literal[False]:
    """
    This function checks for type_name in type category. If not found, the invalid_types dict
    will be updated with the missing types in the following manner:

    {
        'category_name': {
            'type_name': [path_in_data1, ]
        }
    }

    The 'type_name' could contain multiple instances of the same type in the data, therefore all occurances
    are recorded using a list.

    For example,
    {
        'Sop': {
            'pyrosolver': [pyrosolver1, pyrosolver2, ],
            'bulletsolver': [subnet1/bulletsolver1, ],
        }
        'Lop': {
            'sopimport': [sopimport1, ],
        }
    }
    """
def validateTypes(data: Mapping[str, rtypes.NetworkItemData], parent_nodetype_category: hou.NodeTypeCategory | None = None, invalid_types: dict[str, dict[str, list[str]]] = ..., path: str = '') -> None:
    """
    Validates the given network item dictionary for existing nodes types.

    It expects an empty dictionary for invalid_types,
    that will be populated with the missing types in the following fashion:

    {
        'category_name': {
            'type_name': [path_in_data1, ]
        }
    }

    For example,
    {
        'Sop': {
            'pyrosolver': [pyrosolver1, pyrosolver2, ],
            'bulletsolver': [subnet1/bulletsolver1, ],
        }
        'Lop': {
            'sopimport': [sopimport1, ],
        }
    }

    NOTE: This only validates against the items recorded in the data. It will not validate for any missing type
    that is part of a locked digital asset.
    """
def checkObject(x: object, t: type | tuple[type, ...]) -> None: ...
def skipSetter(o: object, v: object, opts: object) -> None: ...
def uniquePrefix(length: int = 12) -> str: ...
def formatFloat(value: float, precision: int = 2) -> int | float: ...
def formatString(string: str) -> str | list[str]: ...
def unFormatString(string: str | list[str]) -> str: ...
def filetype(file: str) -> str | None: ...
def joinItemHierarchy(parent: str, name: str) -> str: ...
def itemNameFromPath(path: str) -> str: ...
def itemParentFromPath(path: str) -> str: ...
def needDopLicense(item: hou.OpNode) -> bool: ...
def shouldRecordChildren(node: hou.OpNode) -> bool: ...
def hasEditableContext(node: hou.OpNode) -> bool: ...
def editablePaths(node: hou.OpNode) -> list[str]: ...
def isItemLockedEditable(item: hou.NetworkMovableItem) -> bool: ...
def padList(l: list[_V], content: _V, width: int) -> list[_V]: ...
def digitsInName(name: str) -> int: ...
def incrementNameDigits(name: str) -> str: ...
def isExpression(data: object) -> bool | None: ...

channel_ref_hscript_expr: re.Pattern[str]
channel_ref_python_expr: re.Pattern[str]

def parmPathFromExpression(data: rtypes.ExpressionData, parm: hou.ParmTuple) -> str | None: ...

class Colors:
    HEADER: str
    OKBLUE: str
    OKCYAN: str
    OKGREEN: str
    WARNING: str
    FAIL: str
    ENDC: str
    BOLD: str
    UNDERLINE: str

def validateCallback(callback: rtypes.ParsingCallback | None, raise_error: bool = False) -> rtypes.ParsingCallback | None:
    """ Ensures input callback is callable, returns None or raises
        error otherwise.
    """
def invokeCallback(callback: rtypes.ParsingCallback | None, key: str, value: object) -> None: ...
def jumpToEditContext(node: hou.Node) -> None: ...
def findBranchInput(node: hou.Node, limit_items: Sequence[hou.NetworkMovableItem] | None = None) -> hou.Node:
    """ This function searches the start_node's hierarchy limit to the search nodes, to find the most leftest output.
    """
def findBranchOutput(node: hou.Node, limit_items: Sequence[hou.NetworkMovableItem] | None = None) -> hou.Node:
    """ This function searches the start_node's hierarchy limit to the search nodes, to find the most leftest output.
    """
def insertAtIndex(data: Mapping[_K, _V], new_key: _K, new_value: _V, index: int = 0) -> dict[_K, _V]:
    """generates a new dictionary with an additional key inserted at the given index.
    :param data: the dictionary to insert a new key into.
    :param new_key: the new key to insert into data.
    :param new_value: the value of the newly inserted key.
    :param index: the index at which to insert the new key.
    :returns: the updated parmetemplate data dictionary.
    """
def insertAtKey(data: Mapping[_K, _V], at_key: _K, new_key: _K, new_value: _V, before_key: bool = True) -> dict[_K, _V]:
    """generates a new dictionary with an additional key inserted before or after a given key.
    :param data: the dictionary to insert a new key into.
    :param data: the key at which to insert the new key.
    :param new_key: the new key to insert into data.
    :param new_value: the value of the newly inserted key.
    :param before_key: when True, the new key is inserted before the given key.
     When False, the new key will be inserted after.
    :returns: the updated parmetemplate data dictionary.
    """
def getAuthor() -> str: ...
def getDate() -> str: ...
@typing.overload
def runScript(source: str, d: _KwargsT, return_kwargs: Literal[True] = ...) -> _KwargsT: ...
@typing.overload
def runScript(source: str, d: None = ..., return_kwargs: Literal[True] = ...) -> dict[str, Any]: ...
@typing.overload
def runScript(source: str, d: dict[str, Any] | None, return_kwargs: bool) -> Any: ...
@typing.overload
def runScript(source: str, d: dict[str, Any] | None = ..., *, return_kwargs: bool) -> Any: ...
def parmsForNetworkItemData(node: hou.OpNode | None, networkitem_data: rtypes.NetworkItemData) -> list[hou.ParmTuple]:
    """
    Given a node and a NetworkItemData with 'parms' key,
    it returns a list of associated hou.ParmTuple objects.
    """
@typing.overload
def tagInClusterData(cluster_data: rtypes.ClusterData, tag_name: str, join: Literal[True] = ...) -> str: ...
@typing.overload
def tagInClusterData(cluster_data: rtypes.ClusterData, tag_name: str, join: bool) -> str | list[str]: ...
def dataForTargetInClusterData(cluster_data: rtypes.ClusterData) -> rtypes.NetworkItemData | None: ...
def targetParmNames(data: rtypes.NetworkItemData | rtypes.ClusterData) -> list[str]: ...
def getParameterMode(has_target_parms: bool, options: Mapping[str, object]) -> str: ...
def isTargetWithItems(data: rtypes.NetworkItemData | rtypes.ClusterData, key: str = 'children') -> bool: ...
def createRecipeContainer(name: str, nodetype_category: str | None, voptype: str | None, container: hou.Node | None = None) -> tuple[hou.Node, hou.Node]:
    """Creates an empty container in which a recipe can be applied for editing.

    :returns: The first hou.Node is the top container, which is always /obj/RECIPE_EDITOR.
    The second node is the parent node in which the recipe can be created safely.
    """
def scanFromCWD(node: hou.Node | None, search_category_name: str) -> hou.Node | None: ...
def handleNetworkChanges(cluster_output_data: rtypes.ClusterOutputData, network_editor: hou.NetworkEditor | None = None, avoid_overlap: bool = False, frame: bool = False, frame_nodes: Sequence[hou.NetworkMovableItem] = ..., default_home_node: hou.NetworkMovableItem | None = None, select: bool = False, select_nodes: Sequence[hou.NetworkMovableItem] = ..., default_selection_node: hou.NetworkMovableItem | None = None, set_current: bool = False, current_node: hou.Node | None = None, default_current_node: hou.Node | None = None) -> None:
    """Handles various network editor changes related to selection, homing and node overlapping based on the
    cluster output data dictionary.
    """
def renameTargetKeys(data: Mapping[str, _V], recipe_category: rtypes.RecipeCategory) -> Mapping[str, _V]: ...
def matchNodeType(pattern: Sequence[str], node_type: hou.NodeType) -> bool | None:
    """ Checks if the given node type matches any of the patterns.
    """
def matchParmType(pattern: Sequence[str], parm: hou.ParmTuple) -> bool:
    """ Checks if the parameter type matches any of the patterns.
    """
def matchParmName(pattern: Sequence[str], parm: hou.ParmTuple) -> bool:
    """ Checks if the parameter name matches any of the patterns.
    """
def matchPattern(pattern: Sequence[str], needle: str) -> bool:
    """
    Checks if the needle string matches any of the patterns.
    """
