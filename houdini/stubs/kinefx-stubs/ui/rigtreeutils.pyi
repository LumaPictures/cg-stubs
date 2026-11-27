import hou
from collections.abc import Callable as Callable, Collection, Iterable, Sequence
from enum import Enum
from houtypes import NodeEventKwargs, ParmActionButtonKwargs, ParmMenuScriptKwargs
from kinefx import motioncliputils as motioncliputils
from kinefx.ui.rigtreeconfig import GroupRigTreeConfig as GroupRigTreeConfig
from kinefx.ui.rigtreewidget import RigTreeWidget as RigTreeWidget, selection_item as selection_item
from typing import Literal, ReadOnly, Required, TypeIs, TypedDict
from typing_extensions import Unpack

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_T = TypeVar('_T')
_ItemId: TypeAlias = int | str
_TreeSelection: TypeAlias = hou.Selection | list[int] | list[str]
class _SelectArgs(TypedDict, total=False):
    selection: Required[Sequence[_ItemId]]
    inputindex: int
    outputindex: int
    nodepath: str
    pick_mod: hou.EnumValue[hou.pickModifier]

class _SelectKwargs(_SelectArgs, total=False):
    selected: Required[Sequence[_ItemId]]
    deselected: Required[Sequence[_ItemId]]

class _SelectionSourceArgs(TypedDict, total=False):
    node: Required[ReadOnly[hou.OpNode | None]]
    event_type: Required[ReadOnly[hou.EnumValue[hou.nodeEventType] | None]]
    input_node: ReadOnly[hou.OpNode | None]
    nodepath: ReadOnly[str | None]
    parm_name: ReadOnly[str]
    folders_mode: ReadOnly[bool]

class _GetSelectionKwargs(TypedDict, total=False):
    node: Required[hou.OpNode | None]
    items: Required[list[selection_item]]
    event_type: Required[hou.EnumValue[hou.nodeEventType] | None]
    input_node: Required[hou.OpNode | None]
    parm_name: str
    folders_mode: bool
    nodepath: str
    outputindex: int
    default_output: int
    states: list[str]

class _GetSelectionsArgs(TypedDict, total=False):
    node: ReadOnly[hou.OpNode | None]

class _StateCommandKwargs(TypedDict, total=False):
    clear_ui_event: bool

class _DragDropKwargs(_StateCommandKwargs, total=False):
    items: Required[list[_ItemId]]
    old_parent_items: Required[list[_ItemId | None]]
    new_parent_item: Required[_ItemId | None]

class _RenameKwargs(_StateCommandKwargs, total=False):
    item: Required[_ItemId]
    selection: Required[list[_ItemId]]
    old_name: Required[str]
    new_name: Required[str]

class _DeleteKwargs(_StateCommandKwargs, total=False):
    selection: Required[list[_ItemId]]

class _RigAction(TypedDict, total=False):
    action: Callable[[], object]
    enable: bool

class _ActionsKwargs(_StateCommandKwargs, total=False):
    selection: Required[list[_ItemId]]
    current_item: Required[_ItemId | None]
    actions: dict[str, _RigAction | None]

class _DefaultOutputKwargs(TypedDict):
    node: hou.OpNode | None
    default_output: int
    show_dropdown: bool
    subnet_outputs: bool

class _ControlVisibilityKwargs(TypedDict):
    show_accept_button: bool
    show_cancel_button: bool

class _RigTreePanel(hou.PythonPanel):
    def activeInterfaceRootWidget(self) -> RigTreeWidget | None: ...

RIG_TREE_DEFAULT_STATE: str
RIG_TREE_DEFAULT_STATE_ICON: str

class SelectionMode(Enum):
    SINGLE_SELECTION = ...
    MULTI_SELECTION = ...
    NO_SELECTION = ...

def setRigTreePanesSelectionMode(node: hou.Node | None, sel_mode: SelectionMode, unpinned_only: bool = False) -> None:
    """
    Set the selection mode on all open rig tree panes.

    :param sel_mode: SelectionMode.SELECTIONMODE_DEFAULT will revert the selection mode back to
        what the node config dictates
    :type sel_mode: rigtreeutils.SelectionMode
    """
def resetRigTreePanesSelectionMode(node: hou.Node | None, unpinned_only: bool = False) -> None:
    """
    Reset the selection mode on all open rig tree panes from the configs.
    """
def updateRigTreeSelection(node: hou.SopNode) -> None:
    """
    Wrapper around faking a selection event on the passed in node to trigger
    the rig tree get selection callback.

    Called in the python states.
    """
def disableRigTreeItems(node: hou.Node | None, items: Collection[_ItemId], unpinned_only: bool = False) -> None:
    """
    Disable the passed in items in all open rig tree instances.

    :param items: list of index data (i.e. point number)
    :type items: list of int
    """
def clearRigTreeSelection(node: hou.Node | None, unpinned_only: bool = True) -> None:
    """
    Clear the selection in all open rig tree instances.
    """
def rigTreeExitState(node: hou.Node | None) -> None:
    """
    Convenience method to be called in onExit in the python states that make use
    of the rig tree.
    """
def is_vop_node(node: hou.Node | None) -> TypeIs[hou.VopNode]:
    """Return True if node is not None and is a vop node."""
def is_sop_node(node: hou.Node | None) -> TypeIs[hou.SopNode]:
    """Return True if node is not None and is a sop node."""
def is_obj_node(node: hou.Node | None) -> bool:
    """Return True if all of these conditions are true:

    * node is not None
    * node is an obj node or manager
    * node contains OBJ nodes or SOP nodes (i.e. excluding CHOP network object
      nodes.)

    """
def selectStateCommand(select_callback: Callable[[_T], object], node_state: str | None) -> Callable[[_T], None]:
    """
    Wrapper that allows us to check for the state we are in before running the select command from that state.
    We want to enter the node state if we are not already in it, before firing the state commands.

    This only applies to node's that have a state config under the rigtreeconfig.
    """
def selectNodeInNetwork(node: hou.Node | None) -> None: ...
def getCurrentNode() -> hou.Node | None:
    """
    Get the currently selected node.
    """
def enterCustomState(node_state: str | None = None) -> None:
    """
    Switch the scene_viewer from View to a custom state: rigtreeselect or the current node's state.
    """
def exitCustomState() -> None:
    """
    Switch the scene_viewer back to View and exit the current state.
    """
def isCurrentState(node_state: str | None = None) -> bool:
    """
    Check if we are in node_state.
    """

class SelectionHandler:
    """
    Helper class to manage selections when we want to use the rig tree default state selector OR when 
    we are selecting at OBJ level.
    If our rig tree has a state config, we do NOT use this class but rather call rigtreeutils.select.
    """
    def __init__(self, node_path: str) -> None: ...
    def select(self, kwargs: _SelectKwargs) -> None: ...
    def get_selection(self, kwargs: _GetSelectionKwargs) -> bool: ...

def swap_input(node: hou.Node, old_input_node: hou.Node | None, new_input_node: hou.Node | None) -> bool:
    """
    Detaches node from old_input_node and connects new_input_node in the same
    connector.

    Returns True of a swap actually happened, False otherwise. A swap does not
    happen if the node doesn't actually have inputs. A swap also doesn't happen
    if `old_input_node` is the same as `new_input_node`.

    :param old_input_node: if None or this cannot be found as an input of `node`, then the first unoccupied input will be used.
    """
def getBoolPref(pref: str, default_val: bool = False) -> bool: ...
def setBoolPref(pref: str, val: bool) -> bool: ...
def getCloseAfterSelPref() -> bool: ...
def setCloseAfterSelPref(val: bool) -> bool: ...
def getOpenBeforeSelPref() -> bool: ...
def setOpenBeforeSelPref(val: bool) -> bool: ...
def getCloseAfterStatePref() -> bool: ...
def setCloseAfterStatePref(val: bool) -> bool: ...
def getOpenBeforeStatePref() -> bool: ...
def setOpenBeforeStatePref(val: bool) -> bool: ...

class ScriptSelectionHandler:
    """
    A class to handle the selection changed events from the active state
    when making a point group selection from an action button.
    """
    selection_node: hou.OpNode
    selection_event_added: bool
    def __init__(self, selectionnode: hou.OpNode, add_prefix: bool = True) -> None:
        """
        Constructor method.
        Initialises an event callback to run whenever the selection changes
        on the node

        :param selectionnode: The node from which the selection is obtained
        """
    def clearEventCallbacks(self) -> None:
        """ Removes the selection changed event callback from the selection node """
    def setOrigStateNode(self, node: hou.Node | None) -> None:
        """
        Set the node whose state we return to when done if the node is still
        current.  If not set, we switch to the view state when done.
        """
    def parmString(self) -> str:
        """ Returns the parameter string """
    def selectionAccepted(self) -> bool:
        '''
        Returns whether this handler recorded whether the selection was
        accepted.
        This is set when the "Accept" button on the rig tree is pressed or
        when the "Enter" key is pressed in the rig tree select state.
        '''
    def acceptSelection(self) -> None:
        """
        Accepts the current selection and reverts the current state to the
        node state or the view state. This will force the script selection to end.
        """
    def selectionCancelled(self) -> bool:
        '''
        Returns whether this handler cancelled the selection.

        This is set when the "Cancel" button on the rig tree is pressed or
        when the "Escape" key is pressed in the rig tree select state.
        '''
    def cancelSelection(self) -> None:
        """
        Cancels the current selection and reverts the current state to the
        node state or the view state. This will force the script selection
        to end.
        """
    def handleSelectionChanged(self, **kwargs: Unpack[NodeEventKwargs]) -> None:
        """
        A handler for the selection changed event on the selection node.
        """
    def select(self, kwargs: _SelectKwargs) -> None: ...

def selectPointGroupParm(kwargs: ParmActionButtonKwargs, inputindex: int = 0, add_prefix: bool = True, single_selection: bool = False, folders_mode: bool = False) -> None:
    '''
    Opens the kinefx__rigtreeselect viewer state and uses a ScriptSelectionHandler
    to respond to changes in the state\'s selection.

    The rig tree view is based upon user preferences and makes visible its
    accept button.

    :parm kwargs: The dictionary used to define many of the settings for the
                  selection.
    :type kwargs: dict
    :parm inputindex: The index of the input on which the selection is being
                      made. This is ignored if \'nodepath\' is defined by the
                      kwargs dictionary.
    :type inputindex: int
    :parm add_prefix: If false and if the selection geometry has a "name"
                      attribute, the parameter will be given the names of the
                      selected points. Otherwise, it will be given regular
                      group syntax for point selection.
    :type add_prefix: bool
    :parm single_selection: If true only a single point can be selected at a
                            time.
    :type single_selection: bool
    :parm folders_mode: If true select from a Packed Folders tree instead of a
                        Rig tree.
    :type folders_mode: bool
    '''
def closeRigTreePane(panetab: _RigTreePanel | None, is_persistent: bool | None = False, during_selection: bool = False, by_state: bool = False) -> None:
    """
    Close a RigTree Pane if it isn't persistent(it was created via the selector for example).
    """
def getPersistentRigTreePanes(node: hou.Node | None, unpinned_only: bool = True, cur_desktop_only: bool = False) -> list[_RigTreePanel]:
    """
    Look for any persistent rig tree pane so we can use it for all future operations,
    like selections and state actions, without opening a new one.

    The first index in the returned list will be the pane that is under the cursor when this
    is called or, if no panes are under the cursor, the 1st found instance of a pane that is 
    a current tab.
    """
def disableRigTreePanes(cur_panetab: _RigTreePanel | None, disable: bool = True, unpinned_only: bool = True) -> None:
    """
    Disable/enable all panes except the current one.
    """
def createRigTreePane(node: hou.OpNode, reuse: bool = False, pin: bool = False, during_selection: bool = False, by_state: bool = False, inputindex_or_config: int | GroupRigTreeConfig = -1, folders_mode: bool = False) -> tuple[_RigTreePanel, bool] | tuple[None, None]:
    '''
    Create a RigTree Pane for a given node and return the panetab.
    This is used by the select buttons in parameter editors and the "Rig Tree..."
    menu in the operator contextual menu.

    :return: returns the pane tab and whether the pane tab is persistent or not
    :type return: hou.paneTab and bool
    '''
def _selectUsingStateCommand(sv: hou.SceneViewer, selected: Sequence[_ItemId], nodepath: str | None = None, pick_mod: hou.EnumValue[hou.pickModifier] | None = None) -> bool:
    """
    Let a viewport state handle the selection.
    """
def select_items(items: Iterable[selection_item], geo: hou.Geometry | None, sel: hou.Selection | None) -> None:
    """ 
    Select rig tree view items based on a geo selection.

    :param sel: selection of points
    :type sel: hou.Selection
    """
def select_item_numbers(items: Iterable[selection_item], sel: Iterable[int]) -> None:
    """ 
    Select rig tree view items based on a geo selection.

    :param sel: numbers of selected points
    :type sel: list of point numbers
    """
def select_item_names(items: Iterable[selection_item], names: Iterable[str]) -> None:
    """ 
    Select rig tree view items based on a name list and expand them.
    We use this for obj-level get selection so we do not want to expand all,
    like we do on parm selections.

    :param names: name of the items - the shown data
    :type names: list of item names
    """
def get_selection_sceneviewer(kwargs: _GetSelectionKwargs) -> bool:
    """ Update the tree view selection from the scene viewer selection"""
def get_selection_and_geo(kwargs: _SelectionSourceArgs) -> tuple[_TreeSelection | None, hou.Geometry | None]:
    """
    Get the current selection and the corresponding geometry from the active
    state.
    """
def get_selections(kwargs: _GetSelectionsArgs) -> dict[hou.SopNode, list[int]] | None:
    """
    Get the current selections object from the State, organized by node
    """
def get_selection_parm(kwargs: _GetSelectionKwargs) -> Literal[True]:
    """ Update the tree view selection from the state selection """
def get_selection_parm_string(kwargs: _SelectionSourceArgs, add_prefix: bool = True) -> str:
    """
    Get the active state's selection and compute the corresponding group
    string using the name attribute if possible.
    """
def get_selection_name_pattern(kwargs: _GetSelectionKwargs) -> Literal[True]:
    """ Update the tree view selection from a pattern matching joint names """
def get_selection_obj_nodes(kwargs: _GetSelectionKwargs) -> Literal[True]:
    """ Update the tree view selection from the selected obj nodes """
def select(kwargs: _SelectArgs) -> None:
    """
    Select callback default implementation.
    First try to redirect to the viewer state.
    Then, try extending the current geometry selection.
    """
def createGeometrySpreadsheetWindow(node: hou.Node | None, show_decomposed: bool = True, group_filter: str | None = None, attrib_filter: str | None = None) -> hou.GeometrySpreadsheet | None:
    """
    Open a Geometry Spreadsheet window for the passed in node and show the attrib_filter point attributes
    for the passed in group_filter.
    """
def selectMotionMixerApexParm(kwargs: ParmActionButtonKwargs) -> None: ...
def selectMotionMixerApexSkelParm(kwargs: ParmActionButtonKwargs) -> None: ...
def selectMotionMixerApexShapeParm(kwargs: ParmActionButtonKwargs) -> None: ...
def menuMotionMixerApexOutputPath(kwargs: ParmMenuScriptKwargs) -> tuple[str, ...]: ...
def menuMotionMixerApexOutputKey(kwargs: ParmMenuScriptKwargs) -> tuple[str, ...]: ...
