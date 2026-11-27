import hou
import typing
from collections.abc import Callable as Callable, Mapping
from constraint_browser.browser import ConstraintBrowser as ConstraintBrowser
from typing import Any, Literal, NamedTuple, TypedDict

class _ButtonKwargs(TypedDict):
    browser: ConstraintBrowser
    group: str

class _Button(NamedTuple):
    callback: Callable[[_ButtonKwargs], object] | None
    icon: str | None
    label: str | None

class ConstraintFactoryObject:
    node: hou.Node
    editnodetype: str | None
    editnodegroupparm: str | None
    typeattrib: str | None
    typename: str | None
    defaultwireindex: int
    def __init__(self, node: hou.Node) -> None: ...
    def inputIndex(self) -> int:
        """inputIndex(): 
            returns the node's input index for constraint geometry."""
    def outputIndex(self) -> int:
        """outputIndex(): 
            returns the node's output index for constraint geometry."""
    @typing.overload
    def geometry(self, group: None = ...) -> hou.Geometry | None: ...
    @typing.overload
    def geometry(self, group: str) -> hou.Geometry: ...
    def primitiveCount(self, group: str | None = None) -> int:
        """primitiveCount(group=None):
            return the prim count - if a group is specified, return the prim count in the group.
        """
    def validate(self) -> bool:
        """validate():
            method used to determine whether the node contains constraints of the desired type when selecting or searching for nodes. 
            returns True or False
            """
    def geometryIndex(self) -> int:
        """geometryIndex():
            returns the node's constraint geometry input or output index."""
    def defaultEditParmValues(self, group: str) -> dict[str, int | float | str]:
        """defaultEditParmValues(group):
            returns a dictionary of parm names and values to be applied to a fresh edit constraint node."""
    def attribsToBrowserParms(self) -> dict[str, str]:
        """attribsToBrowserParms():
            returns a dictionary of attribute names to parameter labels.
            Attributes not found in the returned dictionary will be labeled as-is."""
    def attribsToEditNodeParms(self, group: str, attribdata: Mapping[str, Any]) -> dict[str, hou.ParmArgType | hou.ParmTupleArgType]:
        """attribsToEditNodeParms(group, attribdata):
            returns a dictionary of parameter names and values to set on the edit node when editing from the constraint browser interface.
            attribdata is a dictionary of attribute names and values coming from the constraint browser parameter pane."""
    def dataIds(self) -> list[hou.AttribDataId | None]:
        """dataIds():
            returns a list of attribute dataIds (hou.AttribDataId) necessary to check whether a constraint has changed in a significant way. 
            This is used to determine whether or not to rebuild the constraint browser treeview, which can be slow."""
    def getGroupsAndLayers(self, group: str | None = None) -> dict[str, set[str]]:
        """getGroupsAndLayers(group=None):
            returns a dictionary of constraint tag (groups) with their associated layers.
            if group is supplied, will only consider prims in the given group.
            """
    def getAllGroups(self, filter: str | None = None, group: str | None = None) -> set[str]:
        """getAllGroups(filter=None):
            returns a list of all possible group strings identifying varying constraints in the node's geometry.
            If a filter is provided, groups that have overlaps with prims belonging to the group defined by the filter will not be included in the output list.
        """
    def getConstraintAttributes(self, geometry: hou.Geometry) -> list[str]:
        """getConstraintAttributes(geometry):
            returns an ordered list of attribute names to be displayed in the constraint browser's parameter pane.
            This method must be implemented in the constraint plugin class."""
    def getCreationDirection(self, group: str) -> Literal['up', 'down']:
        '''getCreationDirection(group):
            returns the direction a new node should be created:
            "up" - a node will be created upstream of the current node.
            "down" - a new node will be created downstream of the current node.'''
    def findCreatorNode(self, group: str) -> hou.SopNode | None:
        """findCreatorNode(group)
            Find the node which created the constraints defined by the given group.
            By default, will return the node where the first constraint appears for the first time. 
            Upwards traversal is restricted to working in the same hierarchy - no fetches or object merges will be considered. 

            returns the node object or None if none found."""
    def findEditNode(self, group: str, direction: str = 'both') -> list[hou.SopNode | str | None]:
        '''findEditNode(group, direction="both")
            find an editnode affecting the current group.
            direction can be set to "up" to look upstream only, 
               "down" to look downstream of the current node only, 
               or "both" to first look downstream and then upstream if no suitable node is found.
            
            returns a node and the direction the node was found.
        '''
    def getOrCreateEditNode(self, group: str) -> hou.SopNode | None:
        """getOrCreateEditNode(group):
            given a constraint group, finds an existing edit node, or creates one if no suitable node is found."""
    def viewportGeometry(self, group: str) -> hou.Geometry:
        '''viewportGeometry(group):
            return the hou.Geometry for the given group to be drawn in the viewport. 
            The geometry must only contain polygons and must have the original primitive indices stored as "__index" int primitive attribute.'''
    def nodeButtons(self, group: str) -> list[_Button]:
        '''nodeButtons(group):
            returns a list of namedtuple("button", ["callback", "icon", "label"]) for action buttons to be displayed to the right of the top level treeview item.'''
    def constraintButtons(self, group: str) -> list[_Button]:
        '''constraintButtons(group):
            returns a list of namedtuple("button", ["callback", "icon", "label"]) for action buttons to be displayed to the right of the top level treeview item.'''
    def icon(self) -> str | None:
        """icon():
            returns the icon name or path for the top level treeview item."""
    def contextMenuActions(self, group: str) -> dict[str, Callable[[], object]]:
        """contextMenuActions(grouo):
            returns a dictionary of labels and callbacks for custom context menu options."""

def onInit(obj: object) -> None: ...
