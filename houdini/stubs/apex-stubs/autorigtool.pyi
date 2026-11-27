import apex
import apex.autorigcomponentgadget as acg
import apex.autorigsubtools as am
import apex.autorigutils as ar
import apex.jointgadget as jg
import apex.taggadget as tg
import hou
import resourceui
import statehud.utils
import statehud.window as shud
from apex.apexutils import BijectiveMap as BijectiveMap
from apex.autorigutils import ADD_MAPPING_TOOL as ADD_MAPPING_TOOL, ADD_TAG_TOOL as ADD_TAG_TOOL, COMPONENT_TOOL as COMPONENT_TOOL, LOCATE_JOINTTAG_TOOL as LOCATE_JOINTTAG_TOOL, MAP_COMPONENT_TOOL as MAP_COMPONENT_TOOL, MAP_JOINTS_TOOL as MAP_JOINTS_TOOL, MODIFY_MAPPING_TOOL as MODIFY_MAPPING_TOOL, MODIFY_TAG_TOOL as MODIFY_TAG_TOOL, ROOT_COMPONENT as ROOT_COMPONENT, SELECT_CONTROLS_TOOL as SELECT_CONTROLS_TOOL, SELECT_JOINTS_TOOL as SELECT_JOINTS_TOOL, SELECT_JOINTTAG_TOOL as SELECT_JOINTTAG_TOOL, SELECT_JOINT_TOOL as SELECT_JOINT_TOOL, TAG_COMPONENT_TOOL as TAG_COMPONENT_TOOL, _AnimateState as _AutoRigUtilsState
from apex.constraintposing import PoseConstraintManager as PoseConstraintManager
from apex.control_2 import AbstractControl as AbstractControl, controlRigPath as controlRigPath
from apex.pickwalker import PickWalkRig as PickWalkRig
from apex.promptutils import Prompter as Prompter
from apex.ui.animationhudwidgets import ParameterWidget as ParameterWidget
from apex.ui.settingshudwidgets import AnimateSettingsWidget as AnimateSettingsWidget
from apex.xformgadget import _HandleStartUpdateKwargs, _HandleUpdateKwargs
from collections.abc import Callable as Callable, Mapping, Sequence
from houtypes import NodeEventKwargs, ViewerParmProperties, ViewerStateDragDropKwargs, ViewerStateDrawKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateVolatileClientKwargs
from statehud.baseconfig import AbstractConfig
from typing import Concatenate, Literal, Never, Protocol
from typing_extensions import TypedDict, Unpack

from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
_SubTool: TypeAlias = am.TagSelector | am.TagLocator | am.ControlSelector | am.ComponentJointModify | am.ComponentJointCreate | am.ComponentTagCreate | am.ComponentCreate
class _AnimateState(_AutoRigUtilsState, acg._AnimateState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""
    icon_override: bool
    click_and_drag: bool
    @property
    def hud_pin_mgr(self) -> statehud.utils.PinManager: ...
    @property
    def hud_parameter_panel(self) -> AnimateSettingsWidget | None: ...
    @property
    def pose_constraint_manager(self) -> PoseConstraintManager | None: ...
    @property
    def prompter(self) -> Prompter: ...
    def handleCursorIcon(self, iconpath: str | None = ..., force: bool = ...) -> None: ...
    def _showControlDrawable(self, rig_path: str, on: bool) -> None: ...
    def _handleXformGadgetVisibility(self, check_primary_control: bool = ..., selection_changed: bool = ...) -> None: ...
    def setCursorFontsize(self, size: float = ...) -> None: ...

class _ToolActivateKwargs(TypedDict, total=False):
    settings_hud_tab_info: tuple[shud.WidgetBundleWindow, str, str | None]
    channel_hud_tab_info: tuple[shud.WidgetBundleWindow, str, str]
    state_parms: dict[str, ViewerParmProperties]

class _ToolCommandArgs(TypedDict, total=False):
    mode: str
    rigpath: str
    tag: str
    primary: str
    primary_name: str
    parm: str
    nodeparm: str
    force: bool
    update: bool
    templatename: str
    templateattrib: str
    old_pattern: str
    new_pattern: str

class _SegmentValueKwargs(TypedDict, total=False):
    parm: str
    nodeparm: str
    default: int
    conditional_values: Sequence[str]

TOOL_NAME: str
GUIDE_MODE: str
GUIDE_TAG_MODE: str
RIG_TAG_MODE: str
DUAL_TAG_MODE: str
EXIT_HK: str
GUIDE_DISPLAY_BTN: str
GUIDE_COLOR_MODE: str
GUIDE_LINK: str
GUIDE_AXES: str
GUIDE_TWIST: str
GUIDE_REFERENCE: str
GUIDE_DISPLAY_MODES: list[str]
GUIDE_DISPLAY_ICONS: list[str]
GUIDE_MAP_FILTER_FIELD: str
USENUMBERS_TOGGLE: str
SPRITE_GUIDES: str
SPRITE_RIG: str
SPRITE_RIG_NO_UPDATE: str
SPRITE_SHAPES: str
BTN_GUIDE_DISPLAY: str
BTN_HIERARCHY: str
BTN_AUTOAIM: str
BTN_PINAIM: str
BTNGRP_GUIDE_ICONS: str
BTN_SHAPES: str
BTNGRP_RIG_ICONS: str
BTN_RIG_RESET: str
BTN_GUIDE_RESET: str
BTN_RIG_RELOAD: str
OK_BTN: str
APPLY_MODE: str
CANCEL_MODE: str
OK_MODES: list[str]
OK_ICONS: list[str]
COMPONENT_FIELD: str
REMOVE_UNMAPPED: str
TAG_FIELD: str
PRIMARY_BTN: str
SECONDARY_BTN: str
AXIS_MODES: list[str]
AXIS_MODE_VECTORS: dict[str, hou.Vector3]
CONFIG_CTRL_IDENTIFIER: str
SEGMENT_PARM: str
NODE_SETTINGS_CMD: str
VIEWPORT_CMD: str
UPDATE_CMD: str
RELOAD_CMD: str
MIRRPR_CMD: str
TWIST_CMD: str
TOGGLE_CMD: str
RENAME_CMD: str
MAP_JNTS_CMD: str
SELECT_TAGS_CMD: str
SELECT_GUIDE_TAGS_CMD: str
SET_TAGS_CMD: str
SELECT_CONTROLS_CMD: str
SELECT_GUIDES_CMD: str
RENAME_CONTROLPARMS_CMD: str
UPDATE_TEMPLATE_CMD: str
GUIDE_FILTER: str
UPDATE_NEEDED_MESSAGE: str

class DeviceCache:
    data: dict[str, bool | int | float | str]
    def __init__(self, device: hou.UIEventDevice) -> None: ...
    def isAltKey(self) -> bool: ...
    def isArrowDown(self) -> bool: ...
    def isArrowLeft(self) -> bool: ...
    def isArrowRight(self) -> bool: ...
    def isArrowUp(self) -> bool: ...
    def isAutoRepeat(self) -> bool: ...
    def isCapsLock(self) -> bool: ...
    def isCtrlKey(self) -> bool: ...
    def isFunctionKey(self) -> bool: ...
    def isKeyDown(self) -> bool: ...
    def isKeyPad(self) -> bool: ...
    def isKeyPressed(self) -> bool: ...
    def isKeyUp(self) -> bool: ...
    def isLeftButton(self) -> bool: ...
    def isLeftButtonReleased(self) -> bool: ...
    def isMiddleButton(self) -> bool: ...
    def isMiddleButtonReleased(self) -> bool: ...
    def isRightButton(self) -> bool: ...
    def isRightButtonReleased(self) -> bool: ...
    def isShiftKey(self) -> bool: ...
    def isTablet(self) -> bool: ...
    def isTouchPad(self) -> bool: ...
    def keyString(self) -> str: ...
    def keyValue(self) -> int: ...
    def modifierString(self) -> str: ...
    def mouseWheel(self) -> float: ...
    def mouseX(self) -> float: ...
    def mouseY(self) -> float: ...
    def tabletAngle(self) -> float: ...
    def tabletPressure(self) -> float: ...
    def tabletRoll(self) -> float: ...
    def tabletTilt(self) -> float: ...
    def time(self) -> float: ...

class ComponentWidget:
    """ 
    """
    name: str
    scene_viewer: hou.SceneViewer
    hud_window: shud.WidgetBundleWindow | None
    is_visible: bool
    mute_value_update: int
    finished: bool
    callbacks: dict[str, Callable[[], object]]
    group_pattern: str
    add: resourceui.HUDWidgetWrapper
    remove_unmapped: statehud.utils.KeyableToggle
    def __init__(self, tool: AutoRigTool, scene_viewer: hou.SceneViewer, name: str | None = None) -> None: ...
    @property
    def tool(self) -> AutoRigTool | None: ...
    def setCallback(self, callback: Callable[[], object], event: str | None = None) -> None: ...
    def initWindow(self, title: str = 'Add', width: int = 240) -> None:
        """
        creates a new window instance 
        """
    def show(self, on: bool = True) -> Literal[True]: ...
    def onHandleApply(self, name: str = '', v: bool | None = None) -> None: ...
    def onApply(self, name: str = '', v: bool | None = None) -> None:
        """
        we either add or remove a tag directly on enter in the tag field
        """
    def onCancel(self) -> None: ...
    def componentName(self) -> str | None: ...
    def setComponentName(self, name: str) -> None: ...
    def tags(self) -> str | None: ...
    def doRemoveUnmapped(self) -> bool: ...
    def setTags(self, name: str) -> None: ...
    def setTagsVisible(self, on: bool) -> None:
        """shows or hides the tag input field"""
    def setMapVisible(self, on: bool) -> None:
        """shows or hides the tag input field"""
    def activateWindow(self) -> None:
        """
        activates the current window with the settings based on the add or remove mode
        """
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> Literal[False]: ...

class AutorigSettingsWidget(ParameterWidget[_AnimateState]):
    mute_value_update: int
    DEFAULT_SIZE: int
    DEFAULT_LABEL_WIDTH: int
    is_visible: bool
    finished: bool
    def __init__(self, tool: AutoRigTool, hud_window: shud.WidgetBundleWindow | None = None, tab_widget_name: str | None = None, tab_name: str | None = None) -> None: ...
    @property
    def tool(self) -> AutoRigTool | None: ...
    def onHandleGuideDisplayCallback(self, name: str | None = None, v: bool | None = None) -> None:
        """manages the visibility for the 
        :param name: _description_
        :param v: _description_
        """
    def onHandleLightMode(self, v: bool, n: str | None = None) -> None:
        """defines which colors the default joints should have. 
        """
    def onNumberMode(self, v: bool, n: str | None = None) -> None:
        """defines which colors the default joints should have. 
        """
    def onGuideFilterChanged(self, v: list[str] | None = None, n: str | None = None) -> None: ...
    def updateAxes(self, primary: hou.Vector3, secondary: hou.Vector3) -> None:
        """update the axes in the dialog based on external axis updates"""
    def onAxisUpdate(self, v: str | None = None, n: bool | None = None) -> None:
        """updates the primary and secondary axis for the joint orientation hotkey"""
    def loadFromConfig(self, the_config: AbstractConfig, **kwargs: Never) -> None:
        """ Load from userdata on entering tool. """
    def saveToConfig(self, the_config: AbstractConfig, **kwargs: Never) -> None:
        """ Save to userdata on exiting tool. """

class AutoRigTool:
    show_rig_hk: str
    update_rig_hk: str
    control_shape_hk: str
    confirm_hk: str
    add_tag_hk: str
    remove_tag_hk: str
    name: str
    hud_rows: list[hou._HudRow]
    node_manager: ar.AutoRigNodeManager
    guide_tag_gadget: tg.TagGadget | None
    guide_tag_config: tg.TagConfig | None
    rig_tag_gadget: tg.TagGadget | None
    rig_tag_config: None
    tag_mode: str | None
    joint_gadget: jg.JointGadget | None
    guide_skeleton: hou.Geometry | None
    rig_skeleton: hou.Geometry | None
    settings_widget: AutorigSettingsWidget | None
    active_sub_tool: _SubTool | None
    active_sub_tool_kwargs: am._SubToolKwargs
    active_sub_tool_name: str | None
    subtools: dict[str, _SubTool]
    last_parm: str | None
    tagmodify_widget: tg.TagModifyWidget | None
    component_gadget: acg.ComponentJointMapper | None
    component_cache: ar.GuideComponentCache
    component_widget: ComponentWidget | None
    prev_drag_test: bool | None
    device: DeviceCache | None
    orient_manager: ar.OrientationManager
    parm_CB: hou._NodeEventParmTuple
    show_guide_tags: bool
    show_rig_tags: bool
    show_guide_drawables: bool
    show_links: bool
    show_axis: bool
    show_upaxis: bool
    auto_update: bool
    needs_scene_reload: bool
    needs_reload: bool
    reload_event_posted: bool
    delayed_scene_reload: bool
    runcallbacks: bool
    drag_test_count: int
    is_component_dragging: bool
    key_consumed: bool
    def __init__(self, state: _AnimateState) -> None: ...
    @property
    def state(self) -> _AnimateState | None: ...
    @staticmethod
    def writabelNodeHandler(func: Callable[Concatenate['AutoRigTool', _P], _R]) -> Callable[Concatenate['AutoRigTool', _P], _R | None]:
        """
        allows us to ignore certain operations if the current node is not an apex autorig builder node type
        """
    def label(self) -> str: ...
    def category(self) -> str: ...
    def hudTemplate(self) -> list[hou._HudRow]: ...
    def initTagGadget(self, scene_viewer: hou.SceneViewer) -> None:
        """initializes the tag gadget and the tag widget"""
    @writabelNodeHandler
    def updateTagColors(self) -> None: ...
    def setTagMode(self, mode: str | None = None) -> None:
        """defines if the tags are to be shown for the guides or the rig or not at all
        """
    def setGuideSkel(self) -> None:
        """fetches the current guide skeleton geometry and updates the joint gadget and 
        the tag gadget with the geo"""
    def setRigSkel(self) -> None:
        """converts the current animation skeleton with its parms into a skeleton representation"""
    def setLightMode(self, on: bool = True, from_parm: bool = False) -> None:
        """defines if the skeleton should be black or white, this is helpful to change based
        on the base background color

        :param on: _description_, defaults to True
        :param from_parm: defines if the current state should be read from the node 
        """
    def setNumericalMode(self, on: bool = True, from_parm: bool = False) -> None:
        """defines if the skeleton should be black or white, this is helpful to change based
        on the base background color

        :param on: _description_, defaults to True
        :param from_parm: defines if the current state should be read from the node 
        """
    def updateRigSkel(self, force: bool = False) -> None: ...
    @writabelNodeHandler
    def updateGuideSkel(self, force: bool = False) -> hou.Geometry | None:
        """updates the current guide skeleton geometry and updates the joint 
        gadget and the tag gadget with the geo"""
    def initSubTools(self) -> None:
        """register all currently available subtools for the rig state, 
        we can in the futres extend this tu custom rig subtools"""
    def getRefHeight(self) -> float: ...
    @writabelNodeHandler
    def configureJointGadget(self) -> None: ...
    def spriteBtnSelectCb(self, name: str, pos: int | None, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None, set_value: bool = True) -> None: ...
    def initRigBuilder(self, kwargs: _ToolActivateKwargs) -> None:
        """initialized all the elements that are only relevant if the given node qualifies for the rig builder"""
    def onActivate(self, kwargs: _ToolActivateKwargs) -> None:
        """activates the rig state when we enter the rig state subtool"""
    def onDragTest(self, kwargs: ViewerStateDragDropKwargs) -> bool | None:
        """activates the subtools to apply components during drag from the asset browser"""
    def onDropGetOptions(self, kwargs: ViewerStateDragDropKwargs) -> Literal[True]:
        """this is being called when the drag motion from the assetbrowser is finished"""
    def onDropAccept(self, kwargs: ViewerStateDragDropKwargs) -> Literal[True]:
        """NOTE: the function is very likeley not even being called"""
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDrawInterrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def handlePrompter(self, force_update_message: bool = False) -> None:
        """handles the appearance of prompt messages for the autorigger. Sub tool descriptions 
        always win over the prompter that notifies the user about the missing update
        """
    def onResume(self, kwargs: ViewerStateKwargs) -> None: ...
    def onPoseStartEvent(self, kwargs: ViewerStateEventKwargs | _HandleStartUpdateKwargs) -> None:
        """hides the tag gadgets durring posing of the guide controls"""
    def onPoseStartPreInitEvent(self, kwargs: ViewerStateEventKwargs | _HandleStartUpdateKwargs) -> None: ...
    def onPostEvaluationEvent(self, kwargs: float) -> None:
        """updates the guide and rig skeleton used for the tag gadgets and thoser gadgets 
        after any evaluation"""
    def onParmUpdateEndFromWidget(self, control_parm: str | None = None) -> Literal[True] | None: ...
    def onPoseEndEvent(self, kwargs: ViewerStateEventKwargs | _HandleUpdateKwargs) -> None:
        """shows the tag gadgets after """
    def onPostMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onDeactivate(self) -> None:
        """deactivates the overall rig tool"""
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def onSelectionChanged(self, selection: Sequence[str], **kwargs: Never) -> bool: ...
    def addTagCB(self, value: str) -> None:
        """_summary_

        :param value: _description_
        """
    def reloadParmCB(self, *args: Never, **kwargs: Unpack[NodeEventKwargs]) -> None:
        """
        triggers a proper reloading of the rig character in the scene when the auto rig sop
        node parameters change. this auto reload behavior is important since we work with a caching
        system for the preview animation character. And this enables us to keep the reload lightweight
        """
    def delayedReload(self) -> None: ...
    def addParmCB(self) -> None: ...
    def removeParmCB(self) -> None: ...
    @writabelNodeHandler
    def removeSegments(self) -> None:
        """removes a segment to be built simply by removing the multiparm from 
        """
    @writabelNodeHandler
    def renameControlParms(self, old_pattern: str, new_pattern: str) -> None:
        """renames a component and updates all the guide positions and also updates all the viewport parameter data 
        matching the given action

        :param segment_name: _description_
        :param new_segment_name: _description_
        :return: _description_
        """
    @writabelNodeHandler
    def renameBodySides(self, left: str, right: str) -> None: ...
    @writabelNodeHandler
    def setPinOrientControls(self, clear: bool = False) -> None:
        """mirrors an given guide segment to the others side. this is based on the current config control
        selection 
        """
    @writabelNodeHandler
    def mirrorSegment(self, *args: Never, **kwargs: Never) -> Literal[True] | None:
        """mirrors an given guide segment to the others side. this is based on the current config control
        selection 
        """
    @writabelNodeHandler
    def setTwistValue(self) -> None: ...
    @writabelNodeHandler
    def setSegmentValue(self, *args: Never, **kwargs: Unpack[_SegmentValueKwargs]) -> Literal[True] | None:
        """changes the number of elements used for a guide segment based on a given parameter value
        """
    @writabelNodeHandler
    def mapSegment(self, segment_name: str, mapping: Mapping[str, str], sorted_keys: Sequence[str] | None, root: str | None = None, removed: str | None = None, t: hou.Vector3 | None = None, r: hou.Vector3 | None = None, new_segment_name: str | None = None) -> Literal[True]:
        """removes a segment to be built simply by removing the multiparm from 
        """
    @writabelNodeHandler
    def addSegment(self, segment_name: str, component_name: str, mapping: Mapping[str, str] | None = None, sorted_keys: Sequence[str] | None = None, root: str | None = None, removed: str | None = None, tags: str | None = None, t: hou.Vector3 | None = None, r: hou.Vector3 | None = None, s: hou.Vector3 | None = None, mirror: bool | None = None, numelements: int | None = None, reload_manager: bool = True) -> None: ...
    @writabelNodeHandler
    def decomposeTemplateToSegments(self, mapping_input: BijectiveMap[str, str], template_data: hou._OptionDict | apex.Dict, component_data: hou._OptionDict, variadic_input: Mapping[str, Sequence[tuple[str, str]]] | None = None, add_skeleton_fit: bool = True, rename_joints: bool = True) -> None:
        """
        Interprets template data parameter entries with actual entries coming from
        generated components. Processes multiple segments from a template and applies
        them to the node's multiparm.

        :param mapping_input: Bijective mapping between reference joints and actual guide joints (apex.apexutils.BijectiveMap)
        :param template_data: Template data containing segment definitions (apex.Dict)
        :param add_skeleton_fit: Whether to add a skeleton fit segment at position 0
        :param rename_joints: Whether the skeleton fit should rename joints via the mapping.
            When False, sets the guides parm to 'ignore_name' so AddSkeletonFit skips renaming.
        """
    @writabelNodeHandler
    def applyTemplateNames(self, on: bool = True) -> None:
        """Apply or revert skeleton fit joint renaming to all subsequent segments.

        When on=True, updates existing# entries in segments after skeleton fit
        to use the renamed (existing#) joint names from the skeleton fit mapping.
        When on=False, reverts them back to the original (default#) joint names.

        :param on: If True, apply renamed names; if False, revert to original names.
        """
    @writabelNodeHandler
    def getSegmentMap(self, segment_name: str) -> dict[str, str]:
        """finds the mapping entries for a given segment provided by name
        the mapping is returned as a dictionary with the following key value 
        pair structure
        map[existing_joint] = default joint
        """
    @writabelNodeHandler
    def getSegmentRoot(self, segment_name: str) -> str:
        """finds the root joint values of a given segment by name"""
    @writabelNodeHandler
    def getSegmentValue(self, segment_name: str, parm_name: str) -> int | float | str | dict[str, str] | hou.Ramp | hou.Geometry | tuple[int, ...] | tuple[float, ...] | tuple[str, ...] | tuple[hou.Ramp, ...] | tuple[dict[str, str], ...] | tuple[hou.Geometry | None, ...] | None:
        """finds the root joint values of a given segment by name"""
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def handleChildCompensate(self) -> None: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> None: ...
    def activateSubTool(self, toolname: str, **kwargs: Unpack[am._SubToolKwargs]) -> bool | None:
        """Starts a sub interaction mode """
    def applySubTool(self) -> Literal[True] | None: ...
    def cancelSubTool(self) -> bool | None: ...
    def deactivateSubTool(self) -> None: ...
    def subToolEvent(self, eventname: str, *args: object, **kwargs: object) -> Literal[True] | None: ...
    def getPickWalkData(self, rig_path: str) -> PickWalkRig | Literal[False]:
        """we fetch the pickwalker data for the component gadget where we map a reference skeleton
        to the guide skeleton via drag and drop. The pickwalker helps to map the skeletons based 
        on hierarchy and name patterns

        :param rig_path: _description_
        :return: _description_
        """
    def onPreLocateEvent(self, kwargs: ViewerStateEventKwargs | ViewerStateDragDropKwargs) -> bool: ...
    def onPoseEvent(self, kwargs: ViewerStateEventKwargs | _HandleUpdateKwargs) -> Literal[True] | None: ...
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    @writabelNodeHandler
    def updateRigLabel(self, needs_update: bool = False) -> None: ...
    def onCommand(self, name: str, kwargs: _ToolCommandArgs) -> None:
        """
        various commands that can be triggered to modify the rig state. Use cases are for example button
        triggers from SOP nodes or shelf tools
        """
    def showAll(self, on: bool = True, include_shapes: bool = False) -> None:
        """hides or shows the guides and the test character

        :param on: _description_, defaults to True
        :param include_shapes: _description_, defaults to False
        """
    def showChar(self, path: str, on: bool = True, include_shapes: bool = True) -> None:
        """
        sets the visibility for a given characters controls and optionally its shape to on or off
        :param path: defines the path to the given characters rig to be shown or hidden
        :param on: defines if the character is to be shown or hidden, defaults to True
        :param include_shapes: defines if the character shape is to be shown/hidden as well, defaults to True
        """
    def showGuides(self, on: bool = True, include_shapes: bool = True) -> None:
        """
        sets the visibility for a the guidees controls and optionally its shape to on or off
        :param on: defines if the character is to be shown or hidden, defaults to True
        :param include_shapes: defines if the character shape is to be shown/hidden as well, defaults to True
        """
    def showRig(self, on: bool = True, include_shapes: bool = True) -> None:
        """
        sets the visibility for a test rig characters controls and optionally its shape to on or off
        :param on: defines if the character is to be shown or hidden, defaults to True
        :param include_shapes: defines if the character shape is to be shown/hidden as well, defaults to True
        """
    def showShapes(self, on: bool = True, include_shapes: bool = True) -> None:
        """
        sets the visibility for a test rig characters controls and optionally its shape to on or off
        :param on: defines if the character is to be shown or hidden, defaults to True
        :param include_shapes: defines if the character shape is to be shown/hidden as well, defaults to True
        """
    @writabelNodeHandler
    def updateTemplateSegments(self, template_name: str, mapping_input: BijectiveMap[str, str] | None = None, variadic_input: Mapping[str, Sequence[tuple[str, str]]] | None = None, mapping_attrib: str | None = None, ref_renames: Mapping[str, str] | None = None, check_required_joints: bool = False) -> None:
        """Update existing segments to match a template.

        Ensures template segments exist with correct parameters and ordering.
        Only updates parameters that differ from the template. Non-template
        segments are preserved and placed after template segments.

        :param template_data: Template data containing segment definitions
        :param component_data: Component parameter data
        :param mapping_input: Optional BijectiveMap for joint name resolution
        :param variadic_input: Optional variadic matches per pair name
        :param check_required_joints: When True, verify that every joint flagged
            as required on the reference skeleton (int point attrib 'required'
            == 1) is mapped before applying. If any are missing the user is
            warned and may abort. For variadic pairs only the start/end joints
            are enforced. Silently skipped when mapping_attrib is '__custom__'.
        """

def load(viewer_state: _AnimateState) -> AutoRigTool: ...
