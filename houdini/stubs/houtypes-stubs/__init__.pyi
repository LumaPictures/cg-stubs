"""Types of the `kwargs` dictionaries that Houdini passes to Python callbacks.

This module exists only in the stubs: there is no `houtypes` module at runtime, so import it
for type checking only:

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from houtypes import ViewerStateEventKwargs

    class State:
        def onMouseEvent(self, kwargs: "ViewerStateEventKwargs") -> bool: ...

Keys that Houdini always passes are required; keys a callback only sometimes gets are not, so
check for them (`"node" in kwargs`, `kwargs.get("node")`) before using them.

The viewer state, viewer handle and parameter dictionaries can also hold keys whose names are
only known at runtime (the values of a state's menu items, `script_value0`, ...). These are
typed with PEP 728's `extra_items`, which pyright supports and mypy does not yet: under mypy,
read such keys with `kwargs.get(...)`.

It also has the types of JSON data, which much of Houdini's Python reads and writes:
`JSONValue` is what `json.loads` gives, `JSONLike` what can be serialized (read-only, so a
`dict[str, int]` or a tuple is accepted).
"""

from collections.abc import Mapping, Sequence
from typing import Any, Generic, TypeAlias

import hou
from typing_extensions import NotRequired, ReadOnly, Required, TypedDict, TypeVar

JSONValue: TypeAlias = None | bool | int | float | str | list["JSONValue"] | dict[str, "JSONValue"]
JSONLike: TypeAlias = (
    None | bool | int | float | str | Sequence["JSONLike"] | Mapping[str, "JSONLike"]
)

class ViewerParmProperties(TypedDict):
    """A viewer state's or handle's parameter, in `state_parms` / `handle_parms`: its value (a
    list for multi-component parameters) and whether it is enabled and visible."""

    value: bool | int | float | str | list[int] | list[float]
    enable: bool | int
    visible: bool | int
    label: NotRequired[str]

class ViewerMenuState(TypedDict, total=False):
    """`menu_states`: the state of the menu being opened, for `onMenuPreOpen` to update."""

    enable: bool | int
    value: str
    """For radio strip menus: the id of the selected item."""

class ViewerMenuItemState(TypedDict, total=False):
    """A menu item's entry in `menu_item_states`, for `onMenuPreOpen` to update."""

    enable: bool | int
    label: str
    visible: bool | int
    value: bool | int
    """A toggle item's state."""

_EventT = TypeVar("_EventT", bound=hou.UIEvent, default=hou.ViewerEvent)
_ViewerT = TypeVar("_ViewerT", bound=hou.PathBasedPaneTab, default=hou.SceneViewer)
_SelectionT = TypeVar(
    "_SelectionT",
    default=hou.GeometrySelection
    | list[hou.OpNode]
    | list[str]
    | list[hou.DopData]
    | list[tuple[hou.DopData, hou.GeometrySelection]],
)

# Shelf tools

class ShelfToolKwargs(TypedDict, total=False, extra_items=Any):  # type: ignore[call-arg]
    """The `kwargs` of a shelf tool script, also used for the tools in the Tab menus.

    Houdini's tool helpers (`toolutils.genericTool`, `soptoolutils.genericTool`,
    `objecttoolutils.genericCameraLightTool`, ...) take this dictionary. A tool can carry
    extra keys of its own.
    """

    pane: Required[hou.PaneTab | None]
    """The pane the tool was invoked in, or None when it was clicked on the shelf."""
    viewport: Required[hou.GeometryViewport | None]
    panename: Required[str]
    toolname: Required[str]
    shiftclick: Required[bool]
    ctrlclick: Required[bool]
    altclick: Required[bool]
    cmdclick: Required[bool]
    requestnew: Required[bool]
    branch: Required[bool]
    autoplace: Required[bool]
    inputs: Required[list[tuple[str, int]]]
    """The paths of the nodes, and their output indices, to wire into the new node."""
    outputs: Required[list[tuple[str, int]]]
    """The paths of the nodes, and their input indices, to wire the new node into."""
    inputnodename: Required[str]
    outputindex: Required[int]
    outputnodename: Required[str]
    inputindex: Required[int]
    bbox: hou.BoundingBox
    """Set by a `bbox` attribute in the tool's `.shelf` file."""
    nodepositionx: str
    nodepositiony: str
    parms: dict[str, Any]
    """Parameter values for `toolutils.genericTool` to set on the new node."""
    do_not_jump_to_child: bool
    ghostnodes: list[tuple[hou.Vector2, str | None]]
    ghostconnections: list[tuple[hou.Vector2, hou.Vector2]]

class RadialMenuKwargs(TypedDict, total=False):
    """The `kwargs` of a radial menu item's script, e.g. `radialmenu.runShelfTool(kwargs, ...)`."""

    pane: Required[hou.PaneTab]

# Parameters

class ParmCallbackKwargs(TypedDict, total=False, extra_items=ReadOnly[Any]):  # type: ignore[call-arg]
    """The `kwargs` of a parameter's callback script.

    Houdini passes the values as strings, whatever the parameter's type. The dictionary also
    has `script_value0`, `script_value1`, ... (one per component, also strings) and, for
    nested multiparms, `script_multiparm_index2`, ...
    """

    node: Required[hou.OpNode]
    parm: Required[hou.Parm]
    parm_name: Required[str]
    script_parm: Required[str]
    """The name of the parameter tuple."""
    script_value: Required[str]
    script_multiparm_index: Required[str]
    """The multiparm instance number, or `"-1"`."""
    script_multiparm_nesting: Required[str]
    ui_change_type: str
    """For a UI callback: `"multiparm_tab_changed"` or `"ramp_current_point_changed"`."""
    new_tab: Any
    new_point: Any

class ParmMenuScriptKwargs(TypedDict, total=False, extra_items=ReadOnly[Any]):  # type: ignore[call-arg]
    """The `kwargs` of a parameter's menu script (and of a menu's item generator).

    Unlike in callbacks, the multiparm numbers are ints. For nested multiparms the dictionary
    also has `script_multiparm_index2`, ...
    """

    node: Required[hou.OpNode]
    parm: Required[hou.Parm]
    script_multiparm_index: Required[int]
    script_multiparm_nesting: Required[int]

class ParmActionButtonKwargs(TypedDict, total=False, extra_items=ReadOnly[Any]):  # type: ignore[call-arg]
    """The `kwargs` of a parameter's action button script (its `script_action` tag).

    Scripts often add keys before handing the dictionary to a helper, e.g.
    `soputils.selectGroupParm(kwargs)` after setting `kwargs["geometrytype"]`.
    """

    node: Required[hou.OpNode]
    parmtuple: Required[hou.ParmTuple]
    alt: Required[int]
    shift: Required[int]
    ctrl: Required[int]
    command: Required[int]
    script_multiparm_index: Required[int]
    script_multiparm_nesting: Required[int]
    # Keys scripts add before handing the dictionary to soputils.selectGroupParm and its relatives.
    geometrytype: hou.EnumValue[hou.geometryType] | Sequence[hou.EnumValue[hou.geometryType]] | hou.ParmTuple
    inputindex: int
    outputindex: int
    ordered: bool | int
    nodepath: str
    noderefparm: str
    nameattr: str
    attribname: str
    volumename: str
    geometry: hou.Geometry
    use_asterisk_to_select_all: bool
    prev_sels: Sequence[tuple[hou.EnumValue[hou.geometryType] | Sequence[hou.EnumValue[hou.geometryType]] | hou.ParmTuple, hou.ParmTuple | None]]

class NodeContextMenuKwargs(TypedDict, total=False):
    """The `kwargs` of the scripts and expressions in `OPmenu.xml` (a node's right-click menu)."""

    node: Required[hou.OpNode]
    items: Required[Sequence[hou.NetworkMovableItem]]
    """The selected items."""
    commonparent: Required[bool]
    toolname: str
    altclick: bool
    ctrlclick: bool
    shiftclick: bool
    cmdclick: bool
    networkeditor: hou.NetworkEditor
    networkeditorpos: hou.Vector2
    selectedtoken: str

class ParmContextMenuKwargs(TypedDict, total=False):
    """The `kwargs` of the scripts and expressions in `PARMmenu.xml` (a parameter's right-click menu)."""

    parms: Required[Sequence[hou.Parm]]
    """The unlocked parameters the menu was opened on."""
    locked_parms: Required[Sequence[hou.Parm]]
    toolname: str
    altclick: bool
    ctrlclick: bool
    shiftclick: bool
    cmdclick: bool
    instance: int
    """The multiparm instance, when the menu was opened on one."""
    selectedtoken: str

# Asset (and node type) event handlers, and scene file scripts

class HDAEventKwargs(TypedDict, total=False):
    """The `kwargs` of the node type events `PreFirstCreate`, `PostLastDelete`, `OnInstall` and
    `OnUninstall`, and of an asset's `PythonModule` (and other module sections).
    """

    type: Required[hou.OpNodeType]

class HDANodeEventKwargs(HDAEventKwargs, total=False):
    """The `kwargs` of the `OnCreated`, `OnLoaded`, `OnUpdated` and `OnDeleted` event handlers,
    in an asset or in a `scripts/<category>/<node>_<event>.py` file.
    """

    node: Required[hou.OpNode]

class HDAInputChangedKwargs(HDANodeEventKwargs, total=False):
    """The `kwargs` of the `OnInputChanged` event handler."""

    input_index: Required[int]

class HDANameChangedKwargs(HDANodeEventKwargs, total=False):
    """The `kwargs` of the `OnNameChanged` event handler."""

    old_name: Required[str]

class HDASyncNodeVersionKwargs(HDANodeEventKwargs, total=False):
    """The `kwargs` of the `SyncNodeVersion` event handler."""

    old_version: Required[str]
    current_version: Required[str]

class BeforeSceneSaveKwargs(TypedDict, total=False):
    """The `kwargs` of `scripts/beforescenesave.py`."""

    file: Required[str]
    autosave: Required[bool]

class AfterSceneSaveKwargs(BeforeSceneSaveKwargs, total=False):
    """The `kwargs` of `scripts/afterscenesave.py`."""

    success: Required[bool]

# Viewer states

class _ViewerStateFlags(TypedDict, total=False):
    mouse_drag: bool
    redraw: bool
    indirect_handle_drag: bool
    exit_on_node_select: bool

class _VolatileClient(TypedDict, total=False):
    name: Required[str]
    sticky: bool

class _DropOptions(TypedDict, total=False):
    ids: Sequence[str]
    labels: Sequence[str]

class ViewerStateInitKwargs(TypedDict, Generic[_ViewerT], total=False):
    """The keyword arguments of a viewer state factory (`hou.ViewerStateTemplate.bindFactory`)."""

    state_name: Required[str]
    scene_viewer: Required[_ViewerT]

class ViewerStateKwargs(TypedDict, total=False, extra_items=ReadOnly[Any]):  # type: ignore[call-arg]
    """The `kwargs` common to every viewer state callback, and those of `onExit`, `onInterrupt`,
    `onResume` and `onGenerate`.

    It also holds the value of each of the state's menu items, keyed by the item's name.
    """

    node: ReadOnly[hou.OpNode]
    """The state's node; not passed to nodeless states, nor to `onGenerate`."""
    state_parms: Required[dict[str, ViewerParmProperties]]
    """The state's parameters: a dictionary of properties (`value`, `enable`, `visible`) for each."""
    state_flags: Required[_ViewerStateFlags]
    interrupt_state: str
    """For `onInterrupt` and `onResume`: the name of the volatile state that interrupts this one."""

class ViewerStateEnterKwargs(ViewerStateKwargs, total=False):
    """The `kwargs` of a viewer state's `onEnter`."""

    # PEP 705 lets a subclass make a read-only item required; mypy does not support that yet.
    node: Required[ReadOnly[hou.OpNode]]  # type: ignore[misc]

class ViewerStateEventKwargs(ViewerStateKwargs, Generic[_EventT], total=False):
    """The `kwargs` of a viewer state's `onMouseEvent`, `onMouseDoubleClickEvent`,
    `onMouseWheelEvent`, `onKeyEvent` and `onKeyTransitEvent`.

    `ui_event` is a `hou.ViewerEvent`, or in a compositor viewer a `hou.CompositorViewerEvent`
    (`ViewerStateEventKwargs[hou.CompositorViewerEvent]`).
    """

    ui_event: Required[_EventT]
    hotkey: str
    """For a key event, the symbol of the state's hotkey that the key invokes, if any."""
    add_volatile_client: _VolatileClient
    """Set by `onKeyTransitEvent` to make the key a volatile client of the state."""

class ViewerStateMenuActionKwargs(ViewerStateKwargs, Generic[_EventT], total=False):
    """The `kwargs` of a viewer state's `onMenuAction`."""

    menu_item: Required[str]
    ui_event: _EventT

class ViewerStateMenuPreOpenKwargs(ViewerStateKwargs, total=False):
    """The `kwargs` of a viewer state's `onMenuPreOpen`: set the states of the menu and its items."""

    menu: Required[str]
    menu_states: Required[ViewerMenuState]
    menu_item_states: Required[dict[str, ViewerMenuItemState]]

class ViewerStateParmChangeKwargs(ViewerStateKwargs, Generic[_EventT], total=False):
    """The `kwargs` of a viewer state's `onParmChangeEvent`."""

    parm_name: Required[str]
    parm_value: Required[Any]
    """The new value: a list for a parameter with several components."""
    ui_event: _EventT

class ViewerStateCommandKwargs(ViewerStateKwargs, total=False):
    """The `kwargs` of a viewer state's `onCommand` (`hou.SceneViewer.runStateCommand`)."""

    command: Required[str]
    command_args: Required[Any]
    """Whatever the caller passed to `runStateCommand`."""

class ViewerStateDrawKwargs(ViewerStateKwargs, total=False):
    """The `kwargs` of a viewer state's `onDraw` and `onDrawInterrupt`."""

    draw_handle: Required[Any]
    """The opaque handle to pass to the drawables' `draw()`."""

class ViewerStateHandleToStateKwargs(ViewerStateKwargs, Generic[_EventT], total=False):
    """The `kwargs` of a viewer state's `onHandleToState`."""

    handle: Required[str]
    parms: Required[dict[str, Any]]
    mod_parms: Required[list[str]]
    prev_parms: Required[dict[str, Any]]
    ui_event: Required[_EventT]

class ViewerStateStateToHandleKwargs(ViewerStateKwargs, total=False):
    """The `kwargs` of a viewer state's `onStateToHandle`."""

    handle: Required[str]
    parms: Required[dict[str, Any]]

class ViewerStateHandleDragKwargs(ViewerStateKwargs, Generic[_EventT], total=False):
    """The `kwargs` of a viewer state's `onBeginHandleToState` and `onEndHandleToState`."""

    handle: Required[str]
    ui_event: Required[_EventT]

class ViewerStateSelectionKwargs(ViewerStateKwargs, Generic[_SelectionT], total=False):
    """The `kwargs` of a viewer state's `onStartSelection`, `onSelection`, `onStopSelection` and
    `onLocatedSelection`.

    `selection` depends on the selector: a `hou.GeometrySelection` from a geometry selector
    (`ViewerStateSelectionKwargs[hou.GeometrySelection]`), nodes from an object selector, prim
    paths from a scene graph selector, `hou.DopData`s from a dynamics selector.
    """

    name: Required[str]
    """The name of the active selector."""
    selection: _SelectionT
    drawable_selection: dict[str, Any]
    drawable_mask: list[str]

class ViewerStateDragDropKwargs(ViewerStateKwargs, Generic[_EventT], total=False):
    """The `kwargs` of a viewer state's `onDragTest`, `onDropGetOptions` and `onDropAccept`."""

    drop_options: _DropOptions
    """For `onDropGetOptions` to fill in."""
    drop_selection: str
    """For `onDropAccept`: the id of the chosen option."""
    ui_event: _EventT

class ViewerStateNodeChangeKwargs(ViewerStateKwargs, total=False):
    """The `kwargs` of a viewer state's `onNodeChangeEvent`."""

    event_type: Required[hou.EnumValue[hou.nodeEventType]]
    node: Required[ReadOnly[hou.OpNode]]  # type: ignore[misc]
    parm_tuple: hou.ParmTuple

class ViewerStatePlaybackChangeKwargs(ViewerStateKwargs, total=False):
    """The `kwargs` of a viewer state's `onPlaybackChangeEvent`."""

    event_type: Required[hou.EnumValue[hou.playbarEvent]]
    frame: Required[float]
    reason: hou.EnumValue[hou.channelListChangedReason]
    """For `hou.playbarEvent.ChannelListChanged`."""

class ViewerStateVolatileClientKwargs(ViewerStateKwargs, total=False):
    """The `kwargs` of a viewer state's `onVolatileClientEvent`, for a key it registered with
    `add_volatile_client`.
    """

    client_name: Required[str]
    event_type: Required[str]
    """`"release"` or `"sticky_release"`."""

# Viewer handles

class ViewerHandleInitKwargs(TypedDict, Generic[_ViewerT], total=False):
    """The keyword arguments of a Python viewer handle's `__init__`.

    `scene_viewer` is a `hou.CompositorViewer` for a 2D handle in a compositor viewer
    (`ViewerHandleInitKwargs[hou.CompositorViewer]`).
    """

    handle_name: Required[str]
    handle_label: Required[str]
    handle_instance_name: Required[str]
    scene_viewer: Required[_ViewerT]
    handle_context: Required[hou.ViewerHandleContext]
    handle_parms: Required[dict[str, ViewerParmProperties]]
    handle_gadgets: dict[str, hou.GadgetDrawable]
    """Only for 3D handles."""

class ViewerHandleKwargs(TypedDict, total=False, extra_items=ReadOnly[Any]):  # type: ignore[call-arg]
    """The `kwargs` common to every viewer handle callback, and those of `onActivate`,
    `onDeactivate`, `onDrawSetup` and `onLoadSettings`.

    It also holds the value of each of the handle's menu items, keyed by the item's name.
    """

    handle_context: Required[hou.ViewerHandleContext]
    handle_parms: Required[dict[str, ViewerParmProperties]]
    """The handle's parameters and settings: a dictionary of properties (`value`, ...) for each."""
    handle_gadgets: dict[str, hou.GadgetDrawable]
    node: hou.OpNode

class ViewerHandleActivateKwargs(ViewerHandleKwargs, total=False):
    """The `kwargs` of a viewer handle's `onBeginActivate` and `onEndActivate`."""

    initializing: Required[bool]

class ViewerHandleVisibilityKwargs(ViewerHandleKwargs, total=False):
    """The `kwargs` of a viewer handle's `onVisibilityChange`."""

    visibility: Required[bool]

class ViewerHandleEventKwargs(ViewerHandleKwargs, Generic[_EventT], total=False):
    """The `kwargs` of a viewer handle's `onMouseEvent`, `onMouseIndirectEvent`,
    `onMouseWheelEvent`, `onKeyEvent` and `onKeyTransitEvent`.
    """

    ui_event: Required[_EventT]
    hotkey: str
    """For a key event, the symbol of the handle's hotkey that the key invokes, if any."""
    indirect_component_index: int
    """For `onMouseIndirectEvent`."""

class ViewerHandleMenuActionKwargs(ViewerHandleKwargs, total=False):
    """The `kwargs` of a viewer handle's `onMenuAction`."""

    menu_item: Required[str]

class ViewerHandleMenuPreOpenKwargs(ViewerHandleKwargs, total=False):
    """The `kwargs` of a viewer handle's `onMenuPreOpen`."""

    menu: Required[str]
    menu_states: Required[ViewerMenuState]
    menu_item_states: Required[dict[str, ViewerMenuItemState]]

class ViewerHandleParmChangeKwargs(ViewerHandleKwargs, Generic[_EventT], total=False):
    """The `kwargs` of a viewer handle's `onParmChangeEvent`."""

    parm_name: Required[str]
    parm_value: Required[Any]
    """The new value: a list for a parameter with several components."""
    ui_event: _EventT

class ViewerHandleDrawKwargs(ViewerHandleKwargs, total=False):
    """The `kwargs` of a viewer handle's `onDraw`."""

    draw_handle: Required[Any]
    """The opaque handle to pass to the drawables' `draw()`."""

# Event callbacks (hou.OpNode.addEventCallback, hou.hda.addEventCallback, ...)
#
# Houdini calls these callbacks with the dictionary's items as keyword arguments, and passes the
# keys an event type adds whether or not the callback takes them, so a callback that handles more
# than one event takes `**kwargs`: `def callback(event_type, node, **kwargs)` or
# `def callback(**kwargs: Unpack[NodeEventKwargs])`.

class NodeEventKwargs(TypedDict, total=False):
    """The keyword arguments of a node event callback (`hou.OpNode.addEventCallback`).

    `event_type` and `node` are passed for every event; the other keys only for the events
    noted (see `hou.nodeEventType`).
    """

    event_type: Required[hou.EnumValue[hou.nodeEventType]]
    node: Required[hou.OpNode]
    """The node the callback was added to."""
    change_type: hou.EnumValue[hou.appearanceChangeType]
    """`AppearanceChanged`."""
    input_index: int
    """`InputRewired`."""
    parm_tuple: hou.ParmTuple | None
    """`ParmTupleChanged`, `ParmTupleAnimated`, `ParmTupleChannelChanged` and
    `ParmTupleLockChanged`: None when many parameters changed at once."""
    child_node: hou.OpNode
    """`ChildCreated`, `ChildDeleted` and `ChildSwitched`."""
    child_item: hou.NetworkBox | hou.StickyNote | hou.IndirectInput
    """The network box, sticky note or indirect input of the `NetworkBox*`, `StickyNote*` and
    `IndirectInput*` events."""
    old_name: str
    """`NameChanged`."""
    work_item_id: int
    """`WorkItemSelectionChanged`, when a work item is selected."""
    selected_node: hou.TopNode
    """`WorkItemSelectionChanged`, when a work item is selected."""

class HDALibraryEventKwargs(TypedDict, total=False):
    """The keyword arguments of an asset library event callback (`hou.hda.addEventCallback`).

    The other keys are only passed for the events noted (see `hou.hdaEventType`).
    """

    event_type: Required[hou.EnumValue[hou.hdaEventType]]
    asset_definition: hou.HDADefinition
    """`AssetCreated`, `AssetSaved`, `BeforeAssetDeleted` and `BeforeAssetSaved`."""
    asset_name: str
    """`AssetDeleted` and `BeforeAssetCreated`."""
    library_path: str
    """`AssetDeleted`, `BeforeAssetCreated`, `LibraryInstalled` and `LibraryUninstalled`."""
    node_type_category: hou.OpNodeTypeCategory
    """`AssetDeleted` and `BeforeAssetCreated`."""

class SceneViewerEventKwargs(TypedDict, total=False):
    """The keyword arguments of a scene viewer event callback (`hou.SceneViewer.addEventCallback`).

    The other keys are only passed for some events (see `hou.SceneViewer.addEventCallback`).
    """

    event_type: Required[hou.EnumValue[hou.sceneViewerEvent]]
    desktop: Required[hou.Desktop]
    viewer: Required[hou.SceneViewer]
    viewport: hou.GeometryViewport
    """`SelectedViewportChanged`."""
    state_name: str
    """The resize, layout, activation and viewer state events."""
    volatile_state_name: str
    """`StateInterrupted` and `StateResumed`."""
    pref_name: str
    """`PrefChanged`."""
    pref_registry_name: str
    """`PrefChanged`."""

class ViewportVisualizerEventKwargs(TypedDict, total=False):
    """The keyword arguments of a viewport visualizer event callback
    (`hou.viewportVisualizers.addEventCallback`).

    The other keys are only passed for the events noted (see `hou.viewportVisualizerEventType`).
    """

    event_type: Required[hou.EnumValue[hou.viewportVisualizerEventType]]
    visualizer: hou.ViewportVisualizer
    """The `Visualizer*` events."""
    category: hou.EnumValue[hou.viewportVisualizerCategory]
    """`CategoryActiveChanged` and `CategoryDeleted`."""
    category_node: hou.OpNode | None
    """`CategoryActiveChanged` and `CategoryDeleted`: the node of a `Node` category."""
