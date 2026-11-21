# Houdini stubs generated from Houdini 22.0.466

import hou
from . import datahandler as datahandler, networkitemconnection as networkitemconnection, parmtemplategroup as parmtemplategroup, parmtemplatemapper as parmtemplatemapper, utils as utils
from .. import rtypes as rtypes
from collections.abc import Callable as Callable, Mapping, MutableMapping, MutableSequence
from typing import Any

def _getParmDataDict(item: hou.OpNode, opts: dict[str, Any]) -> rtypes.ParmDataDict:
    """
    Gets a dictionary of parm data for the node.
    """
def createNewItem(parent: hou.OpNode, item_type: str, item_name: str) -> hou.NetworkBox | hou.NetworkDot | hou.StickyNote | hou.OpNode | None:
    """
    Responsible to create a new network item
    """
def findNewName(current_name: str, existing_names: MutableSequence[str]) -> str: ...
def renameOutOfTheWay(item_list: MutableMapping[hou.NetworkMovableItem, str], item_to_rename: hou.NetworkMovableItem, to_name: str, prefix: str = '') -> None: ...
def revertNames(renamed_target: Mapping[hou.NetworkMovableItem, str], renamed_existing: Mapping[hou.NetworkMovableItem, str], renamed_new: Mapping[hou.NetworkMovableItem, str]) -> None: ...

class NetworkItemBase(datahandler.DataHandler[hou.NetworkMovableItem, rtypes.NetworkItemData]):
    is_at_default_chooser: dict[str, Callable[[Any, Any, dict[str, Any]], object]]
    getter_method_chooser: dict[str, Callable[[Any, dict[str, Any]], Any]]
    setter_method_chooser: dict[str, Callable[[Any, Any, dict[str, Any]], object]]
    def __init__(self) -> None: ...
    def dataForItem(self, item: hou.NetworkMovableItem, **opts: Any) -> rtypes.NetworkItemData: ...
    def setData(self, hou_obj: hou.NetworkMovableItem, data: rtypes.NetworkItemData, **opts: Any) -> None: ...

class Node(NetworkItemBase):
    """
    Class that gets/sets the data for a node.
    """
    def __init__(self) -> None: ...
    def setData(self, hou_obj: hou.NetworkMovableItem, data: rtypes.NetworkItemData, **opts: Any) -> None: ...

class NetworkDot(NetworkItemBase):
    def __init__(self) -> None: ...

class SubnetIndirectInput(NetworkItemBase):
    def __init__(self) -> None: ...

class Connection(NetworkItemBase):
    """
    Not implemented. Connections are stored as input connections for each item.
    """
    def __init__(self) -> None: ...

class NetworkBox(NetworkItemBase):
    def __init__(self) -> None: ...

class StickyNote(NetworkItemBase):
    def __init__(self) -> None: ...

def nodeParmsAsData(node: hou.OpNode, **opts: Any) -> rtypes.ParmDataDict:
    """
    Retrieves parms data for a node.
    """
def setNodeParmsFromData(node: hou.OpNode, data: rtypes.ParmDataDict) -> None: ...
def networkItemAsData(item: hou.NetworkMovableItem, **opts: Any) -> rtypes.NetworkItemData:
    """
    Retrieves the network item data for a node, network dot, network box, sticky note, subnet indirect input.
    """
def setNetworkItemFromData(item: hou.NetworkMovableItem, data: rtypes.NetworkItemData, **opts: Any) -> rtypes.NetworkMovableItemDict:
    """
    Sets an existing item according to the given data. As this item could be a node network containing further
    items, we must create (resolve) all-item existence before we can set the properties of those items.

    The Item Resolver is used first to create and identify items, as well as to build
    an item lookup table for all recorded items in the incoming data.


    """
def networkItemsAsData(items: list[hou.NetworkMovableItem], **opts: Any) -> rtypes.NetworkItemDataDict | None:
    """
    Retrieves the network items data for all input items.
    """
def setNetworkItemsFromData(parent: hou.OpNode, data: rtypes.NetworkItemDataDict, **opts: Any) -> rtypes.NetworkMovableItemDict:
    """
    Sets an existing item according to the given data. In case of a node item, any children or editables of this node,
    will be created.
    """
def childrenAsData(node: hou.OpNode, **opts: Any) -> rtypes.NetworkItemDataDict | None:
    """
    Retrieves the network items data for the children of the incoming node.
    """
def setChildrenFromData(node: hou.OpNode, data: rtypes.NetworkItemDataDict, **opts: Any) -> rtypes.NetworkMovableItemDict: ...
def editablesAsData(node: hou.OpNode, **opts: Any) -> rtypes.NetworkItemDataDict | None:
    """
    Retrieves the network items data for the children of the incoming node.
    """
def setEditablesFromData(node: hou.OpNode, data: rtypes.NetworkItemDataDict, **opts: Any) -> rtypes.NetworkMovableItemDict: ...
