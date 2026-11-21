# Houdini stubs generated from Houdini 22.0.466

import hou
import types
import typing
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from houtypes import ParmActionButtonKwargs, ParmCallbackKwargs, ShelfToolKwargs
from typing import Any, Literal

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
_NodeT = TypeVar('_NodeT', bound=hou.Node)
def safe_reload(module: types.ModuleType) -> None:
    """ Reloads the given module when the HOUDINI_PYTHON_DEVELOPMENT
        environment is set to 1
    """
def dataTree(tree_type: str | None) -> hou.DataTree:
    """ Returns an existing open Data Tree pane if there is one. If a tree
        type is provided, the Data Tree must be set to that tree type to be
        acceptable.
    """
def sceneViewer(can_switch_tabs: bool = True, must_be_current: bool = True, allow_pinned_to_network: hou.Node | None = None) -> hou.SceneViewer:
    """
    Returns an existing open Scene Viewer pane if there is one. A
    Context viewer is also acceptable if no dedicated scene viewer
    is found. An existing pane tab will be made current if necessary.

    :param can_switch_tabs: set this to True if you want to switch the current pane tab to the scene viewer,
        if any exists, in case it was not already the active pane
    :type can_switch_tabs: bool
    :param must_be_current: if must_be_current is True, this method will raise hou.NotAvailable if no scene viewer is found that
        is also the current tab; set must_be_current to False if you wish to return a scene viewer if any exists,
        no matter if it a current tab or not
    :type must_be_current: bool
    :param allow_pinned_to_network: if allow_pinned_to_network is not None, this method will raise hou.NotAvailable if no scene viewer is found that
        is pinned to some network other than the one specified.
    :type allow_pinned_to_network: hou.Node
    :return: scene viewer pane tab or raises hou.NotAvailable if no scene viewer is available
        
    :rtype: hou.PaneTab
    """
def compositorViewer() -> hou.CompositorViewer:
    """ Returns an existing open Compositing Viewer pane if there is one. A
        Context viewer is also acceptable is no dedicated compositing viewer
        is found.
    """
def networkEditor() -> hou.NetworkEditor:
    """ Returns an existing open Network Editor pane if there is one.
    """
def activePane(scriptargs: Mapping[str, Any]) -> hou.PaneTab:
    ''' Returns the current active pane. If the current tool was launched
        from a Tab menu, the "pane" scriptarg will be set, and indicates the
        active pane. Otherwise the tool was launched from the shelf and
        we have to look for an open viewer pane of the right type for the
        running tool.
    '''
def activeCompositorPane(scriptargs: Mapping[str, Any]) -> hou.PaneTab: ...
def homeToSelectionNetworkEditorsFor(node: hou.NetworkMovableItem) -> None:
    """ Homes to their selection all network editors to that are showing the
    network that contains node. """
def homeToItems(items: Sequence[hou.NetworkMovableItem]) -> None:
    """ Homes to their selection all network editors that are showing the
        network that contains items. Assumes that all items have the same
        parent."""
def selectionPrompt(nodetypecategory: hou.NodeTypeCategory | None, multisel: bool = True, whichprompt: int = 0) -> str:
    """ Generates a generic selection prompt string when no specific prompt
        string is available in the toolprompts module.
    """
def replaceOutputConnections(olditem: hou.Node | hou.IndirectInput, oldoutputindex: int, newnode: hou.NetworkMovableItem, newoutputindex: int) -> None:
    """ Stick the new node between the input node and all nodes it
        is connected to (insert operation).
    """
def replaceInputConnections(olditem: hou.Node | hou.NetworkDot, oldinputindex: int, newnode: hou.Node | hou.NetworkDot, newinputindex: int) -> None:
    """ Stick the new node between the output node and the node it
        is connected to (insert operation). Note there can be only one.
    """
def getBestConnector(innode: hou.NetworkMovableItem, outidx: int, outnode: hou.NetworkMovableItem, inidx: int, defaultidx: int) -> int: ...
def connectMultiInputsAndOutputs(newnode: hou.Node, branch: bool, inputs: Sequence[tuple[hou.Node | hou.IndirectInput, int] | tuple[hou.Node | hou.IndirectInput, int, int]], outputs: Sequence[tuple[hou.Node | hou.NetworkDot, int] | tuple[hou.Node | hou.NetworkDot, int, int]]) -> None:
    """ Wire the network so that new node connects to the provided inputs
        and outputs. This isn't always possible, but get as close as we can.
        If branch is false, all of the inputs outputs will be made
        newnode's outputs. Both inputs and outputs are optional.
    """
def connectInputsAndOutputs(newnode: hou.Node, branch: bool, inputitem: hou.Node | hou.IndirectInput | None, outputitem: hou.Node | hou.NetworkDot | None, inputindex: int, outputindex: int) -> None:
    """ Simplified version of connectMultiInputsAndOutputs that takes at
        most a single input and output. Provided for backward compatibility
        with code written before the Multi code was written.
    """
@typing.overload
def nodeTypeNameBase(node: hou.Node) -> str: ...
@typing.overload
def nodeTypeNameBase(node: None) -> None: ...
@typing.overload
def nodeTypeNameBase(node: hou.Node | None) -> str | None: ...
@typing.overload
def nodeTypeNameVersion(node: hou.Node) -> str: ...
@typing.overload
def nodeTypeNameVersion(node: None) -> None: ...
@typing.overload
def nodeTypeNameVersion(node: hou.Node | None) -> str | None: ...
def nodeTypeNameMatches(node: hou.Node, matchtype: str | None) -> bool:
    """ Returns true if the node's type base name matches the given type.
        A matchtype of None is assumed to match any node.
    """
def nodeTypeBaseNameMatches(node: hou.Node, matchtype: str | None) -> bool:
    """ Returns true if the node's type base name matches the given type.
        A matchtype of None is assumed to match any node.
    """
def nodeTypeNameComponentsMatch(node: hou.Node, matchtype: str | None) -> bool:
    """ Returns true if the node's type name components matches the given type.
        The components present in matchtype are checked against the node's type,
        and this function returns true if they do match.  Eg,
        matchtype 'hda' will match 'hda', 'hda::1.5', 'userX::hda', etc
        matchtype 'userX::hda' will match 'userX::hda', 'userX::hda::1.5', etc
        matchtype 'hda::1.5' will match 'hda::1.5', 'userX::hda::1.5', etc
        matchtype '::hda' will match 'hda' and 'hda::1.5', but not 'userX::hda'
        matchtype 'hda::' will match 'hda' and 'userX::hda' but not 'hda::1.5'
        A matchtype of None is assumed to match any node.
    """
def findConnectionChainToInputNode(startnode: hou.Node | None, endnode: hou.Node) -> list[hou.NodeConnection] | None:
    """ Finds a chain of hou.Connections that lead to endnode.

        Returns None if no such chain exists.
    """
def findAllConnectionChainsToInputNode(startnode: hou.Node | None, endnode: hou.Node) -> list[list[hou.NodeConnection]]:
    """ Finds all chains of hou.Connections that lead to endnode.

        Returns an empty list if no such chain exists.
    """
def findConnectionChainToOutputNode(startnode: hou.Node | None, endnode: hou.Node) -> list[hou.NodeConnection] | None:
    """ Finds a chain of hou.Connections that lead to endnode.

        Returns None if no such chain exists.
    """
def findAllConnectionChainsToOutputNode(startnode: hou.Node | None, endnode: hou.Node) -> list[list[hou.NodeConnection]]:
    """ Finds all chains of hou.Connections that lead to endnode.

        Returns an empty list if no such chain exists.
    """
def findConnectedNodes(startnode: hou.Node | None, connection_type: Literal['input', 'output'], match_method: Callable[[hou.Node], bool] | None, find_first: bool = False, seennodes: set[hou.Node] | None = None, includeme: bool = False, incoming_conn: hou.NodeConnection | None = None, connection_chains: list[list[hou.NodeConnection | None]] | None = None, all_paths: bool = False, connector_index: int | None = None, stop_method: Callable[[hou.Node | None, hou.NodeConnection | None], bool] | None = None) -> list[hou.Node]:
    """ Finds all nodes that are connected to startnode for which match_method
        returns True. Searches either inputs or outputs, depending on the value
        of connection_type (either 'input' or 'output').

        match_method may be a method taking a hou.Node as it's argument.
        In that case only nodes for which it returns True are matched.

        If connection_chains is a list, for each node it'll be populated with
        the hou.NodeConnections by which the node was found. If additionally
        all_paths is True, all paths to the node will be returned, so nodes
        may appear multiple times in the returned list.

        If find_first is True, the method will exit early as soon as a matching
        node is found. Having both find_first and all_paths True will raise
        a hou.Error.

        stop_method may be a method taking a hou.Node and a hou.NodeConnection
        by which that node was reached. If it returns True, the node and
        further connected nodes will be ignored.
    """
def findAllInputNodesOfTypeWithParms(endnode: _NodeT | None, nodetype: str | None, parmlist: Mapping[str, object], includeme: bool = False, findfirst: bool = False, seennodes: set[hou.Node] | None = None, basetypematch: bool = False) -> list[_NodeT]:
    """Finds all nodes that are an ancestor of endnode, match
        nodetype, and have the parameters & value pairs listed in the
        parmlist dictionary.
        If basetypematch is true, only the node type's base name is checked,
        ie, node type's namespace and version components are ignored
        when testing against the matchtype (eg, matchtype 'hda' will match
        node types 'hda', 'hda::1.5' and 'userx::hda', etc). Otherwise,
        the node type name must match exactly the matchtype string.
    """
def findInputNodeOfTypeWithParms(endnode: _NodeT | None, nodetype: str | None, parmlist: Mapping[str, object], includeme: bool = False, seennodes: set[hou.Node] | None = None, basetypematch: bool = False) -> _NodeT | None:
    """Finds any nodes that are an ancestor of endnode, match
        nodetype, and have the parameters & value pairs listed in the
        parmlist dictionary.
        If basetypematch is true, only the node type's base name is checked,
        ie, node type's namespace and version components are ignored
        when testing against the matchtype (eg, matchtype 'hda' will match
        node types 'hda', 'hda::1.5' and 'userx::hda', etc). Otherwise,
        the node type name must match exactly the matchtype string.
    """
def findGreatestCommonDescendent(endnode: _NodeT | None, searchnodes: Sequence[hou.Node], seennodes: set[hou.Node] | None = None) -> _NodeT | None:
    """ Starting from end node and heading up the input chain
        locate the first node that doesn't have all of searchnodes
        on the same input wire.
    """
def findInputNode(endnode: hou.Node | None, searchnode: hou.Node | None, seennodes: set[hou.Node] | None = None) -> bool:
    """ This function searches the endnode's hierarchy to find if the
        given search node is connected
    """
def findInputNodeOfType(endnode: _NodeT | None, nodetype: str | None, includeme: bool = False, seennodes: set[hou.Node] | None = None, basetypematch: bool = False) -> _NodeT | None:
    """ This function does a depth first traversal of the node input hierarchy
        to find the first node of a particular type.
        If basetypematch is true, only the node type's base name is checked,
        ie, node type's namespace and version components are ignored
        when testing against the matchtype (eg, matchtype 'hda' will match
        node types 'hda', 'hda::1.5' and 'userx::hda', etc). Otherwise,
        the node type name must match exactly the matchtype string.
    """
def findInputNodeOfBaseType(endnode: _NodeT | None, nodetype: str | None, includeme: bool = False, seennodes: set[hou.Node] | None = None) -> _NodeT | None:
    """ This function does a depth first traversal of the node input hierarchy
        to find the first node whose type's base name (ie, type name stripped of
        any namespace or version) matches the given type.
    """
@typing.overload
def findOutputNodeOfTypeWithParms(startnode: _NodeT | None, nodetype: str | None, parmlist: Mapping[str, object], includeme: bool = ..., seennodes: set[hou.Node] | None = ..., basetypematch: bool = ..., returnall: Literal[False] = ...) -> _NodeT | None: ...
@typing.overload
def findOutputNodeOfTypeWithParms(startnode: _NodeT, nodetype: str | None, parmlist: Mapping[str, object], includeme: Literal[False] = ..., seennodes: None = ..., basetypematch: bool = ..., *, returnall: Literal[True]) -> list[_NodeT]: ...
@typing.overload
def findOutputNodeOfTypeWithParms(startnode: _NodeT | None, nodetype: str | None, parmlist: Mapping[str, object], includeme: Literal[False] = ..., seennodes: set[hou.Node] | None = ..., basetypematch: bool = ..., *, returnall: Literal[True]) -> list[_NodeT] | None: ...
@typing.overload
def findOutputNodeOfTypeWithParms(startnode: _NodeT | None, nodetype: str | None, parmlist: Mapping[str, object], includeme: bool = ..., seennodes: set[hou.Node] | None = ..., basetypematch: bool = ..., returnall: bool = ...) -> _NodeT | list[_NodeT] | None: ...
@typing.overload
def findOutputNodeOfType(startnode: _NodeT | None, nodetype: str | None, includeme: bool = ..., seennodes: set[hou.Node] | None = ..., basetypematch: bool = ..., returnall: Literal[False] = ...) -> _NodeT | None: ...
@typing.overload
def findOutputNodeOfType(startnode: _NodeT, nodetype: str | None, includeme: bool = ..., seennodes: None = ..., basetypematch: bool = ..., *, returnall: Literal[True]) -> list[_NodeT]: ...
@typing.overload
def findOutputNodeOfType(startnode: _NodeT | None, nodetype: str | None, includeme: bool = ..., seennodes: set[hou.Node] | None = ..., basetypematch: bool = ..., *, returnall: Literal[True]) -> list[_NodeT] | None: ...
@typing.overload
def findOutputNodeOfType(startnode: _NodeT | None, nodetype: str | None, includeme: bool = ..., seennodes: set[hou.Node] | None = ..., basetypematch: bool = ..., returnall: bool = ...) -> _NodeT | list[_NodeT] | None: ...
@typing.overload
def findOutputNodeOfBaseType(endnode: _NodeT | None, nodetype: str | None, includeme: bool = ..., seennodes: set[hou.Node] | None = ..., returnall: Literal[False] = ...) -> _NodeT | None: ...
@typing.overload
def findOutputNodeOfBaseType(endnode: _NodeT, nodetype: str | None, includeme: bool = ..., seennodes: None = ..., *, returnall: Literal[True]) -> list[_NodeT]: ...
@typing.overload
def findOutputNodeOfBaseType(endnode: _NodeT | None, nodetype: str | None, includeme: bool = ..., seennodes: set[hou.Node] | None = ..., *, returnall: Literal[True]) -> list[_NodeT] | None: ...
@typing.overload
def findOutputNodeOfBaseType(endnode: _NodeT | None, nodetype: str | None, includeme: bool = ..., seennodes: set[hou.Node] | None = ..., returnall: bool = ...) -> _NodeT | list[_NodeT] | None: ...
@typing.overload
def findAllChildNodesOfTypeWithParms(parentnode: hou.OpNode, nodetype: str | None, parmlist: Mapping[str, object], dorecurse: bool = ..., findfirst: bool = ..., basetypematch: bool = ...) -> list[hou.OpNode]: ...
@typing.overload
def findAllChildNodesOfTypeWithParms(parentnode: hou.Node, nodetype: str | None, parmlist: Mapping[str, object], dorecurse: bool = ..., findfirst: bool = ..., basetypematch: bool = ...) -> list[hou.Node]: ...
@typing.overload
def findChildNodeOfTypeWithParms(parentnode: hou.OpNode, nodetype: str | None, parmlist: Mapping[str, object], dorecurse: bool = ..., basetypematch: bool = ...) -> hou.OpNode | None: ...
@typing.overload
def findChildNodeOfTypeWithParms(parentnode: hou.Node, nodetype: str | None, parmlist: Mapping[str, object], dorecurse: bool = ..., basetypematch: bool = ...) -> hou.Node | None: ...
@typing.overload
def findChildNodeOfType(parentnode: hou.OpNode, nodetype: str | None, dorecurse: bool = ..., basetypematch: bool = ...) -> hou.OpNode | None: ...
@typing.overload
def findChildNodeOfType(parentnode: hou.Node, nodetype: str | None, dorecurse: bool = ..., basetypematch: bool = ...) -> hou.Node | None: ...
@typing.overload
def findAllChildNodesOfType(parentnode: hou.OpNode, nodetype: str | None, dorecurse: bool = ..., findfirst: bool = ..., basetypematch: bool = ...) -> list[hou.OpNode]: ...
@typing.overload
def findAllChildNodesOfType(parentnode: hou.Node, nodetype: str | None, dorecurse: bool = ..., findfirst: bool = ..., basetypematch: bool = ...) -> list[hou.Node]: ...
@typing.overload
def findAncestorOfType(startnode: hou.OpNode | None, category: hou.NodeTypeCategory, nodetype: str | None, basetypematch: bool = ...) -> hou.OpNode | None: ...
@typing.overload
def findAncestorOfType(startnode: hou.Node | None, category: hou.NodeTypeCategory, nodetype: str | None, basetypematch: bool = ...) -> hou.Node | None: ...
@typing.overload
def findAncestorOfBaseType(startnode: hou.OpNode | None, category: hou.NodeTypeCategory, nodetype: str | None) -> hou.OpNode | None: ...
@typing.overload
def findAncestorOfBaseType(startnode: hou.Node | None, category: hou.NodeTypeCategory, nodetype: str | None) -> hou.Node | None: ...
def chooseNode(possible_nodes: Sequence[_NodeT], title: str, message: str) -> _NodeT | None:
    """ Prompts the user to select on of the given nodes. If there is only a
        single node, then that node is automatically returned. The title
        and message parameters determine what will show up in the prompt.
    """

class OrientInfo:
    parmname: str
    defaultup: hou.EnumValue[hou.orientUpAxis]
    def __init__(self, parmname: str, defaultup: hou.EnumValue[hou.orientUpAxis] = ...) -> None: ...

def setUpOrientation(node: hou.OpNode, parmname: str, defaultup: hou.EnumValue[hou.orientUpAxis] = ...) -> None:
    """ Assumes that the default value of the specified parameter in the given
        node corresponds to the orientation specified in defaultup and applies
        the necessary change to convert the node to the current orientation
        mode.
    """
def baseUpOrientation() -> hou.Matrix3:
    """This function returns the base orientation (rotation) matrix that aligns
       the standard world axes to those of the global orientation preference.
    """
def ocioColorSpaceMenuList(include_roles: bool = True, extra_choices: list[str] = ...) -> list[str]: ...
def ocioColorSpaceMenu(include_roles: bool = True, extra_choices: list[str] = ...) -> str: ...
def ocioViewMenuList(display: str = ..., extra_choices: list[str] | None = None) -> list[str]: ...
def ocioViewMenu(display: str = ..., extra_choices: list[str] | None = None) -> str: ...
def ocioDisplayMenuList(extra_choices: list[str] | None = None) -> list[str]: ...
def ocioDisplayMenu(extra_choices: list[str] | None = None) -> str: ...
def ocioLookMenuList(extra_choices: list[str] | None = None) -> list[str]: ...
def ocioLookMenu(extra_choices: list[str] | None = None) -> str: ...
@typing.overload
def parseDialogScriptMenu(filename: str, defchoices: Sequence[Sequence[str]] = ..., forhscript: Literal[True] = ...) -> str: ...
@typing.overload
def parseDialogScriptMenu(filename: str, defchoices: Sequence[Sequence[str]], forhscript: Literal[False]) -> list[str]: ...
@typing.overload
def parseDialogScriptMenu(filename: str, defchoices: Sequence[Sequence[str]] = ..., *, forhscript: Literal[False]) -> list[str]: ...
@typing.overload
def parseDialogScriptMenu(filename: str, defchoices: Sequence[Sequence[str]] = ..., forhscript: bool = ...) -> str | list[str]: ...
def updatePlaneType(planeindex: int, variable: str) -> None:
    '''This function is intended to update deep raster plane parameters
       based on the newly set plane variable name.  Use this in a callback
       script as follows:

       callback "`pythonexprs("__import__(\'toolutils\').updatePlaneType($script_multiparm_index, \'$script_value\')")`"
    '''
def updateBakeExtractImageFormat() -> None:
    """ Obsolete as of H16.0 - but is required for old hip files"""
def updateBakePlanes(parm: str) -> None:
    """ Obsolete as of H16.0 - but is required for old hip files"""
def mapTypeCategoriesToSubnetName(nodetypecategory: hou.NodeTypeCategory | None, acceptedtypecategory: hou.NodeTypeCategory) -> str | None:
    """This function returns a name of the subnet that accepts nodetypecategory
       as child type and can be created in a container whose child type is
       acceptedtypecategory.
       Returns None if these two categories are the same (ie, no need for
       a subnet to accommodate nodetypecategory). Also returns None if
       the mapping has not been defined yet.
    """
def removeDefaultGeometryObjectContents(objectnode: hou.Node) -> None:
    """ Destroy the File SOP that gets created inside a default Geometry
        Object.
    """
@typing.overload
def createNodeInContainer(container: hou.OpNode, nodetypecategory: hou.NodeTypeCategory | None, nodetypename: str, nodename: str | None, exact_node_type: bool) -> tuple[hou.OpNode, hou.OpNode]: ...
@typing.overload
def createNodeInContainer(container: hou.Node, nodetypecategory: hou.NodeTypeCategory | None, nodetypename: str, nodename: str | None, exact_node_type: bool) -> tuple[hou.Node, hou.Node]: ...
def reformatPermissionErrors(function: Callable[_P, _R]) -> Callable[_P, _R]:
    """This function decorator will trap any permission error exceptions and
       raise a different exception with a nicer message."""
@reformatPermissionErrors
def genericTool(scriptargs: ShelfToolKwargs | ParmCallbackKwargs, nodetypename: str, nodename: str | None = None, nodetypecategory: hou.NodeTypeCategory | None = None, exact_node_type: bool = True) -> hou.OpNode:
    """ Handles the creation of any node in a Network Editor pane.

        This function is intended to instantiate a node of a given type from
        shelf tools, and thus, if exact_node_type argument is True, it creates
        the node of the exact type specified by nodetypename.
        However, if exact_node_type argument is False, then the base type may
        get resolved to another namespace or another version, and
        the created node may be of that resolved type (eg 'hda' may resolve to
        'mynamespace::hda::2.0').
    """
def genericStateTool(scriptargs: ShelfToolKwargs, statename: str) -> None:
    """ Runs a specific state in an open viewer pane. """
def moveNodesToGoodPosition(movenodes: Iterable[hou.Node]) -> None:
    """ Moves a list of nodes to good positions. """
def generateToolScriptForNode(nodepath_or_list: str | Sequence[str], input_nodepath: str | None = None, output_nodepath: str | None = None) -> str: ...
def createModuleFromSection(module_name: str, node_type: hou.OpNodeType, section_name: str) -> Any:
    """Create and return a module-like object with the given name from the
       contents of a section in an HDA.  This module will not appear in
       sys.modules.  If the source code has a syntax error, an exception will
       be raised.  Use this function to create submodules in the PythonModule
       section of an HDA.  For example:
           submod = toolutils.createModuleFromSection(
                'submod', kwargs['type'], 'PythonSubmod')
    """
def nodeNameFromTypeName(nodetypename: str) -> str:
    """Given an operator node type name, return a valid node name
       corresponding to that type. For example, if the type name contains
       any namespace or version components, they are stripped off.
       The returned node name contains only characters that are allowed
       to appear in the node names.
    """
def placeToolImmediately(kwargs: ShelfToolKwargs | ParmActionButtonKwargs | ParmCallbackKwargs) -> bool:
    """ Returns true if the provided kwargs has a modifier key suggesting
        the tool be placed right away.  This is a ctrl click or a cmd click
        depending on the platform.
    """
def getImmediatePlacementPosition(scene_viewer: hou.SceneViewer) -> hou.Vector3:
    """ Returns the world space position to use for immediate placement of a
        new tool given a scene viewer.
    """
def getImmediatePlacementOrientedPosition(scene_viewer: hou.SceneViewer, base_orientation: hou.Matrix3 | None = None) -> tuple[hou.Vector3, hou.Matrix3 | None]:
    """ Returns the world space position and world space orientation to use for
        immediate placement of a new tool given a scene viewer.
    """
def getSubnetOutputNodes(subnet: hou.OpNode) -> list[hou.OpNode | None]:
    """ Returns a list of output nodes. The position of a node within the list
        corresponds to it's output index.

        Intermediate entries that don't have an output equal None.
    """

class ToolboxTemplateGroup:
    """Generates a UI code block and a template group for toolbox hou.SceneViewer.selectObjects"""
    def __init__(self) -> None: ...
    def buildHelpStr(self, h: str) -> str: ...
    def addMenu(self, name: str, label: str, values: Sequence[str], default_value: int, helpstr: str = '') -> None:
        """Adds a menu select control with a label to the toolbox"""
    def addToggle(self, name: str, label: str, default_value: bool, helpstr: str = '') -> None:
        """Adds a toggle control with a label to the toolbox"""
    def addFloatField(self, name: str, label: str, default_value: Sequence[float], num_components: int = 1, helpstr: str = '') -> None:
        """Adds a float field control with a label to the toolbox"""
    def addStringField(self, name: str, label: str, default_value: Sequence[str], num_components: int = 1, helpstr: str = '') -> None:
        """Adds a string field control with a label to the toolbox"""
    def addIntField(self, name: str, label: str, default_value: Sequence[int], num_components: int = 1, helpstr: str = '') -> None:
        """Adds an integer field control with a label to the toolbox"""
    def addToggleList(self, name: str, labels: Iterable[str], default_value: Sequence[int], helpstr: str = '') -> None:
        """Adds a TRS mask control with a label to the toolbox"""
    def getValue(self, name: str) -> int | tuple[int, ...] | tuple[float, ...] | tuple[str, ...] | None:
        """Returns a UI Toolbox value"""
    def update(self, layout_opt: str = 'JUSTIFY(center,center)') -> None:
        """Updates UI code block and TemplateGroup."""
    def ui(self) -> str:
        """Returns the UI code block"""
    def templategroup(self) -> hou.ParmTemplateGroup | None:
        """Returns the TemplateGroup"""

def testTool(tool: hou.Tool, debug: bool = False, kwargs: ShelfToolKwargs | None = None, pane: hou.PaneTab | None = None, ctrlclick: bool = False, altclick: bool = False, shiftclick: bool | None = None) -> None:
    """ executes a shelf tool.

        If debug is True, the tool will be executed within pdb.run()

        If 'kwargs' is not None, it is passed to the tool script as is and the
        remaining parameters are ignored, along with everything described
        below.

        If 'pane' is None, hou.ui.paneTabOfType(hou.paneTabType.SceneViewer) is
        passed to the tool instead.
    """
def recursiveShowPane(p: hou.Pane) -> None:
    """ Maximize all the parent Pane splits and make the given panel visible."""
def findPythonPanel(pypanel_interface_name: str) -> hou.PythonPanel | None: ...
def createOrShowPythonPanel(kwargs: ShelfToolKwargs, pypanel_interface_name: str, floating_panel_label: str | None, split_type: int) -> list[hou.PythonPanel]:
    """ creates a new float panel from a pypanel interface name or
        make existing ones visible.

        split_type of 0, always creates a floating panel
        split_type of 1, adds a tab on the current panel
        split_type of 2, splits vertically and creates a new tab
        split_type of 3, splits horizontally and creates a new tab
        split_type of 4, splits vertically but only on viewports and creates a new tab
        Returns the python panels tab found
    """
def minimizePythonPanel(kwargs: ShelfToolKwargs, pypanel_interface_name: str) -> list[hou.PythonPanel]:
    """ minimize pypanel interfaces."""
def outputConnectionsAtIndex(node: hou.Node | hou.IndirectInput, index: int) -> tuple[hou.NodeConnection, ...]:
    """ Returns the output connection of a node at a specified index."""
def inputConnectionsAtIndex(node: hou.Node | hou.NetworkDot, index: int) -> tuple[hou.NodeConnection, ...]:
    """ Returns the input connection of a node at a specified index."""
def insertNodeAbove(node: hou.Node, newnode: _NodeT, nodeinputindex: int = 0, newinputindex: int = 0, newoutputindex: int = 0, connectall: bool = True) -> _NodeT:
    """ Inserts a new node (newnode) between the given node (node) and the given
        node's input node.

        :param node: the new node will be inserted above this node.
        :param newnode: the new node to insert above.
        :param nodeinputindex: the input index of node. This input index will be
            connected to the new node's output.
        :param newinputindex: the input index of new node. This input index will
            be connected to existing nodes above.
        :param newoutputindex: the output index of new node. This output index
            will be connected with node's input index.
        :param connectall: When the given node's input node has multiple outputs
            make sure all the connections are adjusted.

    """
def branchNodeAbove(node: hou.Node, newnode: _NodeT, inputindex: int = 0) -> _NodeT:
    """ Inserts a new node (newnode) between the given node (node) and the given
    node's input node.

    :param node: the new node will be inserted above this node.
    :param newnode: the new node to insert above.
    :param inputindex: the input index of new node. This input index will join with the output of the node which is the input of node.

    """
def findLopInsertionNode(cwd: hou.LopNode | hou.LopNetwork, respect_insertion_point: bool = True) -> hou.OpNode | None:
    """
        Returns a node to insert a new node above or below, if such a node
        exists.

        :param cwd: A LopNode or LopNetwork.
    """
def buildRelOrAbsPath(srcnode: hou.NetworkMovableItem | None, dstnode: hou.NetworkMovableItem | None) -> str:
    """ Builds either a relative or absolute path from scrnode to
        dstnode.  This will be relative unless we go through the root,
        in which case well just use an absolute path of dstnode.
    """
def getChildrenBoundingRect(node: hou.Node) -> hou.BoundingRect:
    """ Calculates the bounding rectangle of all children of a node.
    """
