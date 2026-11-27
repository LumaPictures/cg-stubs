import apex.autorigcomponentgadget as ag
import apex.stateutils_2 as asu
import hou
from apex.autorigtool import AutoRigTool as AutoRigTool
from apex.taggadget import TagGadget as TagGadget
from collections.abc import Mapping
from houtypes import ViewerStateEventKwargs
from typing import Literal, Protocol
from typing_extensions import ReadOnly, TypedDict, Unpack

class _SubToolKwargs(TypedDict, total=False, extra_items=ReadOnly[object]):  # type: ignore[call-arg]
    primary: str
    parm: str
    nodeparm: str
    mode: str
    force: bool
    description: str
    extended_description: str
    tag: str
    component: str
    buildtemplate: bool
    taggadget: TagGadget
    rigpath: str
    rig_path: str
    label: str

class _DropGetOptionsKwargs(TypedDict):
    device: ag._ModifierKeys | None
    reason: hou.EnumValue[hou.uiEventReason]

class _AnimateState(asu._AnimateState, Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`): this module uses only the members `apex.stateutils_2._AnimateState` declares."""

class _SubTool(Protocol):
    description: str | None
    @property
    def tool(self) -> AutoRigTool | None: ...

GUIDE_MODE: str
GUIDE_TAG_MODE: str
RIG_TAG_MODE: str
DUAL_TAG_MODE: str
SEGMENT_PARM: str
TAG_MODE_KWARGS: str
PARM_NAME_KWARGS: str
NODE_PARM_NAME_KWARGS: str
FORCE_KWARGS: str
SUMMARY_KWARGS: str
DESCRIPTION_KWARGS: str
TAG_KWARGS: str
COMPONENT_KWARGS: str
BUILDTEMPLATE_KWARGS: str
TAG_GADGET_KWARGS: str
RIGPATH_KWARGS: str
PARENT_MAP: str
CHAIN_MAP: str
NEW_PARENT_MAP: str
HIERARCHY_MAP: str
RIGHT_KWARGS: str
LEFT_KWARGS: str
CENTERED_SEGMENTS: list[str]
DEFAULT_ROOT: str
DEFAULT_ICON: str

def generateSegmentName(component_name: str) -> str:
    """generates the correct segment name directly from the component name and the component metadata"""
def findSegmentBodyside(name: str, component_mapper: ag.ComponentJointMapper, tolerance: float = 0.1) -> int:
    """checks if a given new component is to be applied to the left or the right body side of the character,
    we extend it with the option to always mark a dedicated list of components as center components, e.g. the root,
    there left and right implementation would cause errors
    :return: 0 if left, 1 if right, 2 if centered
    """
def fixSegmentName(name: str, bodyside: int, leftpattern: str, rightpattern: str) -> tuple[str, bool]:
    """checks if the given segment name matches the current bodyside and opens a dialog that asks the user if a
    cleaned name should be set instead

    :param name: the current segment name
    :param bodyside: the bodyside mode, int, 0: left, 1: right, 2: center
    :param leftpattern: hou text pattern for the left bodyside
    :param rightpattern: hou text pattern for the right bodyside
    :return: the name to be use, True if the name got fixed
    """
def setSubToolDescription(subtool: _SubTool, iconpath: str | None = None, summary: str | None = None, description: str | None = None) -> None:
    """manages the change of the state icon style and icon description
    when a sub tool is used and sets the subtool description that is shown in the prompter. 
    if no icon path and no descriptions are given then the icon path and the description 
    will be reset to the defaults
    
    :param subtool: the current subtool to be processed
    :param iconpath: the path to the icon to be used, defaults to None
    :param summary: the description to be shown next to the mouse curso, defaults to None
    :param description: the description text to be shown in the prompter, default to None
    """
def centerRig(state: _AnimateState, rig_path: str, primary: str | None = None, reset: bool = False, apply: bool = True) -> str | None:
    """makes sure that the given rig root control is position at the origin. This 
    this is helpful for subtools that need to operate on the anim rig, which is usually 
    positioned next to the guides. The placement reduces unnecessary tumbling in the viewport

    :param state: the animate state
    :param rig_path: the path to the rig to be centered
    :param reset: _description_, defaults to False
    """

class TagSelector:
    """
    the interactive subtool to get one or more tags from a viewport interaction. Tags can be required from 
    skeletons and from rigs
    the queried tag is then used to either set a control parameter or a node parameter
    """
    description: str | None
    prim: str | None
    parm_name: str | None
    node_parm_name: str | None
    mode: str
    tag_gadget: TagGadget | None
    force: bool
    handle_state: bool
    def __init__(self, tool: AutoRigTool, **kwargs: Unpack[_SubToolKwargs]) -> None: ...
    @property
    def tool(self) -> AutoRigTool | None: ...
    def onActivate(self, **kwargs: Unpack[_SubToolKwargs]) -> Literal[True]:
        """_summary_
        """
    def onApply(self) -> Literal[True]:
        """applies the given selection back """
    def onCancel(self) -> Literal[True]:
        """exit from the tag selection tool when you hit escape"""

class ControlSelector:
    """
    this subtool sets the animate state in a control selection mode for a specified character 
    if the cursor will show a description about which parameter is to be modified by the given selection
    
    available options for the kwarg config:
    
    parm = the control parameter of the current priamry control where we want to set the control selection pattern
    nodeparm - a sop parame where we want to set the control selection pattern
    force = defines if an empty selection will set the given selection as an empty string or streat it as an abort
    and leave the existing setting intact
    description - defines what to write next to the cursor to give the user a hint about what to select
    
    """
    description: str | None
    prim: str | None
    parm: str | None
    nodeparm: str | None
    rig_path: str | None
    input_rig_path: str
    force: bool
    hide_rig: bool
    def __init__(self, tool: AutoRigTool, **kwargs: object) -> None: ...
    @property
    def tool(self) -> AutoRigTool | None: ...
    def onActivate(self, **kwargs: Unpack[_SubToolKwargs]) -> bool:
        """
        sets the kwargs configurations on subtool activation and brings the state into 
        control selecto mode
        """
    def onApply(self) -> bool:
        """
        applies the given selection as a string pattern either to the node parameter or to 
        a control string input parameter
        """
    def onCancel(self, **kwargs: object) -> Literal[True]:
        """
        cancels the control selection operation and exits the selection subtool
        """

class TagLocator:
    """
    generates a tag visualizer previes that can be for examples turned on or off based on the selection
    of specific controls. Tags can be shown either for a skeleton or for a rig
    """
    description: str | None
    prim: str | None
    parm_name: str | None
    node_parm_name: str | None
    tag_gadget: TagGadget | None
    tag_name: str | None
    def __init__(self, tool: AutoRigTool, **kwargs: object) -> None: ...
    @property
    def tool(self) -> AutoRigTool | None: ...
    def onActivate(self, **kwargs: Unpack[_SubToolKwargs]) -> Literal[True]:
        """activates and configures the tag visualizer based on parameter of the current selection or a specifc
        provided tag name"""
    def onDeactivate(self) -> Literal[True]:
        """removes the tag indicator again """
    def onCancel(self) -> None: ...

class JointTagModify:
    """
    this subtool allows the user to modify the controls that are associated with a given tag group. 
    This is necessary if one of the interactions for example generates a tag and we need to 
    adjust that group after the initial creation
    """
    description: str | None
    prim: str | None
    parm_name: str | None
    node_parm_name: str | None
    mode: str
    force: bool
    def __init__(self, tool: AutoRigTool, **kwargs: Unpack[_SubToolKwargs]) -> None: ...
    def onActivate(self, **kwargs: Unpack[_SubToolKwargs]) -> Literal[True]: ...
    def onApply(self) -> Literal[True]:
        """applies the given selection back """
    def onCancel(self) -> None: ...

class ComponentJointModify:
    description: str | None
    prim: str | None
    mode: str
    map: dict[str, str]
    active_joints: list[str]
    reference_skeleton: hou.Geometry | None
    rig_path: str | None
    component_name: str
    tag: str | None
    active_joint_pattern: str
    build_template: bool
    summary: str
    description_txt: str
    def __init__(self, tool: AutoRigTool, **kwargs: object) -> None:
        """modifies any existing mappings between an applied component via the autorig builder sop and the
        input guide skeleton. This mode is usually accessible via the config control of an existing control
        or via the node multiparm. 

        :param tool: the main rig state tool
        """
    @property
    def tool(self) -> AutoRigTool | None: ...
    def setActiveJoints(self, tag: str, map: Mapping[str, str], map_filter: str) -> None:
        """
        we need to define the guide controls that we actually want to map. 
        All other guide joints need to be unselectable. this step only applies for guides
        that already have been added
        """
    def onActivate(self, **kwargs: Unpack[_SubToolKwargs]) -> bool:
        """activates the subtool and collects all the info about the current component to be 
        updated with its mapping based on the kwargs input. The interaction is click based, 
        Since the mode is intended to update existing component mappings
        :return: True if the activation was successful
        """
    def applyTemplate(self) -> None: ...
    def onApply(self, **kwargs: object) -> Literal[True]:
        """
        applies the updated component joint mapping to the autorig builder sop multiparm
        for the segments and updates the guide positions accordingly.
        :return: True if the tool could be successfully applied
        """
    def onCancel(self, **kwargs: object) -> Literal[True]:
        """finish the subtool mode without applying any of the mapping values"""
    def onExit(self) -> None:
        """finish the subtool mode """

class ComponentJointCreate:
    """
    this mode is used for the initial drag from the asset browser to apply the given component
    to the joints directly. It does rely on the component gadget visualizer similar to the map modify gadget. 
    """
    description: str | None
    primary_control: None
    mode: str
    map: dict[str, str]
    active_joints: list[str]
    reference_skeleton: hou.Geometry | None
    rig_path: str | None
    component_name: str
    rig_template_data: hou._OptionDict | None
    active_joint_pattern: str
    remove_unmapped: bool
    description_txt: str
    template_drag_description_txt: str
    def __init__(self, tool: AutoRigTool, **kwargs: object) -> None: ...
    @property
    def tool(self) -> AutoRigTool | None: ...
    def onActivate(self, **kwargs: Unpack[_SubToolKwargs]) -> bool:
        """
        initialized the drag and drop action and configures all the variables relevant for the current
        component to be added to map properly. All the custom configurations must be provided
        with the kwargs
        """
    def onDropCancelled(self, **kwargs: object) -> bool:
        """we are only allowed to use the template input if the template input on the Autorig Builder SOP node
        has a connection on the second input for it
        """
    def onDropGetOptions(self, **kwargs: Unpack[_DropGetOptionsKwargs]) -> None:
        """
        once the initial drag and drop is done we get a popup that suggests a name of the new segments
        and the drag and drop inter action is being switched over to a click interaction for the component
        gadget
        """
    def applyTemplate(self) -> None: ...
    def onApply(self, **kwargs: object) -> bool:
        """
        adds the new component to the autorig builder segments stack and applies
        the mapping and the given segment name accordingly
        """
    def onCancel(self) -> Literal[True]:
        """exits the tool without applying the new segment."""
    def onExit(self) -> Literal[True]:
        """resets the component gadget properly for the next used and resets the descritiopns
        :return: True if the tool could exit properly
        """

class ComponentTagCreate:
    """this mode allows to create a new component with dragging and initially asign it to a given pre existing
    tag
    """
    description: str | None
    rig_path: str
    component_name: str
    label: str
    def __init__(self, tool: AutoRigTool, **kwargs: object) -> None: ...
    @property
    def tool(self) -> AutoRigTool | None: ...
    def onActivate(self, **kwargs: Unpack[_SubToolKwargs]) -> Literal[True]:
        """_summary_
        """
    def onDropGetOptions(self, **kwargs: Unpack[_DropGetOptionsKwargs]) -> None: ...
    def onApply(self, **kwargs: object) -> bool: ...
    def onCancel(self) -> Literal[True]: ...
    def onPostLocateEvent(self, **kwargs: Unpack[ViewerStateEventKwargs]) -> Literal[False]: ...
    def onExit(self) -> Literal[True]: ...

class ComponentCreate:
    """just drops the current outorig onto the rig no mapping or tagging included"""
    description: str | None
    rig_path: str
    component_name: str
    label: str
    def __init__(self, tool: AutoRigTool, **kwargs: object) -> None: ...
    @property
    def tool(self) -> AutoRigTool | None: ...
    def onActivate(self, **kwargs: Unpack[_SubToolKwargs]) -> Literal[True]:
        """_summary_
        """
    def onDropGetOptions(self, **kwargs: Unpack[_DropGetOptionsKwargs]) -> None: ...
    def onApply(self, **kwargs: object) -> bool: ...
    def onCancel(self) -> Literal[True]: ...
    def onPreLocateEvent(self, **kwargs: Unpack[ViewerStateEventKwargs]) -> None: ...
    def onExit(self) -> None: ...
