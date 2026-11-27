import _apex
import dbg
import hou
import typing
from _apexscene import ControlGroup as ControlGroup, Scene as Scene, ValuesView as ValuesView
from apex import Control as Control, ControlManager as ControlManager, extends_class as extends_class, stateutils_2 as asu
from apex.utils import timing as timing
from collections.abc import Container, Iterable, Mapping, Sequence
from typing import Literal, Protocol

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
class _AnimateState(asu._AnimateState, Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`): this module uses only the members `apex.stateutils_2._AnimateState` declares."""

NAMES_SUFFIX: str
TRIGGER_SELECTION_PROPERTY: str
TRIGGER_VISIBILITY_PROPERTY: str
CALLBACK_PROPERTY: str
CALLBACK_PROPERTY_SEL: str
CALLBACK_PROPERTY_BOXSEL: str
CALLBACK_PROPERTY_START: str
CALLBACK_PROPERTY_END: str
CONTROL_PROPERTY: str
CONTROL_GADGET_PARMS: str
SCROLL_PARM_PROPERTY: str
SCROLL_STEP_PROPERTY: str
SCROLL_CYCLE_PROPERTY: str
SNAP_SCROLL_PROPERTY: str
SNAP_DRAG_PROPERTY: str
SW_SCROLL_PROPERTY: str
SW_DRAG_PROPERTY: str
SELECTABLE_PROPERTY: str
SHOW_HANDLE_PROPERTY: str
ORBIT_PROPERTY: str
EXTERNALPARM_PROPERTY: str
MAP_PROPERTY_TYPES: list[str]
CALLBACK_PROPERTY_TYPES: list[str]
CONTROL_PARM_DATA: str
PARM_DATA_TYPE: str
PARM_DATA_MIN: str
PARM_DATA_MAX: str
PARM_DATA_MAX_LOCK: str
PARM_DATA_MIN_LOCK: str
PARM_DATA_MIN_LOCK_RANGE: str
PARM_DATA_MAX_LOCK_RANGE: str
TRANSLATE_PARM: str
ROTATE_PARM: str
SCALE_PARM: str
REFERENCE_PROP: str
REFERENCE_PARM: str
VISIBILITY_RIG_BIT: int
VISIBILITY_INTERNAL_BIT: int
VISIBILITY_CONSTRAINT_BIT: int
VISIBILITY_TOOL_BIT: int
ENABLE_RIG_BIT: int
ENABLE_CONSTRAINT_BIT: int
ENABLE_TOOL_BIT: int
CONTROL_GROUP_SUFFIX: str

def getTransformObject(scene: Scene, graph: _apex.Graph, name: str) -> int | None: ...

class ControlTransformData:
    xform: hou.Matrix4
    local: hou.Matrix4
    restlocal: hou.Matrix4
    parentxform: hou.Matrix4
    parentlocal: hou.Matrix4
    xord: int
    rord: int
    scaleinheritance: int
    def __init__(self, xform: hou.Matrix4, local: hou.Matrix4, restlocal: hou.Matrix4, parentxform: hou.Matrix4 | None, parentlocal: hou.Matrix4 | None, xord: int | None, rord: int | None, scaleinheritance: int | None) -> None: ...
    def xordString(self) -> str: ...
    def rordString(self) -> str: ...

class ControlMapping:
    t: str
    r: str
    s: str
    x: str
    y: str
    keys: set[str]
    def __init__(self, t: str | None = None, r: str | None = None, s: str | None = None, x: str | None = None, y: str | None = None, **kwargs: str) -> None: ...
    def initMapping(self, kwargs: Mapping[str, str]) -> None:
        """add all additional string arg entries as mapping elements """
    def mappingFromControlData(self, controldata: _apex.Dict) -> None:
        """
        add the data in the parm_data dict of the abstract control based on the parm_data structure to the mapping:
        my_control_key:
            parm:
                my_parm_name
        """
    def asDict(self) -> dict[str, str]: ...

class GroupMapping(ControlMapping):
    subcontrol_mapping: _apex.Dict
    def __init__(self, t: str | None = None, r: str | None = None, s: str | None = None, x: str | None = None, y: str | None = None, **kwargs: str) -> None: ...
    def subControlData(self, parm_name: str) -> tuple[str, str] | tuple[None, None]: ...
    def mappingFromGroupData(self, control_manager: ControlManager, groupdata: _apex.Dict) -> None:
        """group data should be a flat mapping that we store on the primary control"""

class ControlManagerExtension:
    @typing.overload
    def getControls(self, ordered: Literal[True]) -> list[Control]: ...
    @typing.overload
    def getControls(self, ordered: Literal[False] = ...) -> ValuesView[Control]: ...
    @typing.overload
    def getControls(self, ordered: bool = ...) -> list[Control] | ValuesView[Control]: ...
    def findControls(self, pattern: str) -> list[Control]: ...
    def generatePattern(self, rig_path: str) -> str: ...
    def update(self, scene: Scene, pattern: str | None = None, use_minimal_pattern: bool = False) -> None: ...
    def updateEnabledControls(self, scene: Scene) -> None: ...
    def getTempControl(self, scene: Scene, ctrl_path: str, rig_path: str) -> Control: ...
    def getControlXform(self, ctrl_path: str) -> hou.Matrix4: ...
    def getControlData(self, ctrl_path: str) -> ControlTransformData: ...
    def getControlGadgetData(self, ctrl_path: str) -> _apex.Dict:
        """fetches the static configuration parms of a custom control gadget on the control instance
        control
            parms
                my_control_gadget_key
                my_other_control_gadget_key
        """
    def getControlGadgetType(self, ctrl_path: str) -> str | None:
        """get the control gadget type of a given control

        :param control: _description_
        :return: _description_
        """
    def getScrollData(self, ctrl_path: str) -> tuple[str, float | int | bool, Literal['Float', 'Bool', 'Int'], bool] | tuple[None, None, None, None]:
        """fetches the static configuration parms of a custom control gadget on the control instance
        control
            parms
                my_control_gadget_key
                my_other_control_gadget_key
        """
    def getParmLimit(self, ctrl_path: str, parm: str, min: bool = True, use_soft_lock: bool = True) -> float | hou.Vector3 | None: ...
    def getControlMapping(self, ctrl_path: str, include_groups: bool = False) -> ControlMapping: ...
    def getRotateParms(self) -> dict[str, list[str]]: ...
    @typing.overload
    def controlsByProperty(self, ctrl_path: str, trigger_type: str = ..., descendants: Literal[False] = ...) -> _apex.StringArray | None: ...
    @typing.overload
    def controlsByProperty(self, ctrl_path: str, trigger_type: str = ..., descendants: bool = ...) -> _apex.StringArray | list[str] | None: ...
    def controlMapByProperty(self, ctrl_path: str, trigger_type: str = ...) -> dict[str, str]:
        """finds the control path that are associated with a given control to trigger like a quick 
        selection or visibility management
        That means we select the control and a different selection is being triggered. 

        :param ctrl_path: the path to the control where we want to check for the control paths for 
        a quick selection
        :return: the controls of the given rig path that are mapped to the control for quick selection
        """
    def hasProperty(self, ctrl_path: str, property_name: str = ...) -> bool: ...
    def getProperty(self, ctrl_path: str, property_name: str = ..., default: _T | None = None) -> _apex._Value | _T | None: ...
    def isSelectable(self, ctrl_path: str) -> bool:
        """Selectable unless SELECTABLE_PROPERTY is explicitly set to False."""
    def showHandle(self, ctrl_path: str) -> bool:
        """Show the xform gadget unless SHOW_HANDLE_PROPERTY is explicitly set to False."""
    def isOrbit(self, ctrl_path: str) -> bool:
        """Orbit mode is enabled when ORBIT_PROPERTY is explicitly set to True."""
    def externalRigParms(self, ctrl_path: str) -> _apex._Value | None:
        """Orbit mode is enabled when ORBIT_PROPERTY is explicitly set to True."""
    def getPropertiesScriptCallback(self, ctrl_path: str, event_type: str = ...) -> str | None:
        """script callback that is associated with a given control
        NOTE: we currently only support python script callbacks

        :param ctrl_path: the path to the control where we want to check for the control paths for a 
        script callback
        :return: the text of the callback to be returned
        """
    def controlGroupData(self, control_paths: Iterable[str] | None = None) -> tuple[list[str], list[str], list[str]]: ...
    def getGroup(self, ctrl_path: str) -> ControlGroup | None: ...
    def getGroupPrimary(self, ctrl_path: str) -> str | None: ...
    def containsGroup(self, ctrl_paths: Iterable[str]) -> bool: ...
    def isGroupPath(self, ctrl_path: str) -> bool: ...

def splitControlPath(ctrl_path: str) -> tuple[str, str]: ...
def controlRigPath(ctrl_path: str) -> str: ...
def controlName(ctrl_path: str) -> str: ...
def controlGroupPath(control: Control) -> str | None: ...
def setControlTemplateAttrib(geo: hou.Geometry, attr_name: str, control_paths: str | Sequence[str], on: bool, bits: int = 1) -> bool: ...
def setControlTemplateVisibility(geo: hou.Geometry, control_paths: str | Sequence[str], on: bool, bits: int = ...) -> bool: ...
def setControlTemplateInternal(geo: hou.Geometry, control_paths: str | Sequence[str], on: bool) -> bool: ...
def setControlTemplateEnabled(geo: hou.Geometry, control_paths: str | Sequence[str], on: bool, bits: int = ..., graph: _apex.Graph | None = None) -> Literal[True]: ...
def setControlGroupVisibility(scene: Scene, primary_control: str | None, controls: Sequence[str] | None = None, show: bool = True) -> Sequence[str] | None:
    """_summary_

        :param primary_control: _description_
        :param show: _description_, defaults to True
        """
def setControlsVisible(scene: Scene, ctrl_paths: Sequence[str], on: bool, bits: int = ...) -> None: ...
def setControlGraphEnabled(graph: _apex.Graph, control_paths: Iterable[str], on: bool) -> bool: ...
@dbg.ZoneScopedDecorator
def getControlEnabledFromTemplate(geo: hou.Geometry, ctrl_path: str) -> bool: ...
@dbg.ZoneScopedDecorator
def getEnabledControlsFromTemplate(geo: hou.Geometry, invert: bool = False, bit_mask: int | None = None, by_name: bool = False) -> list[str]: ...
@dbg.ZoneScopedDecorator
def getControlVisibleFromTemplate(geo: hou.Geometry, ctrl_path: str) -> bool: ...
@dbg.ZoneScopedDecorator
def getVisibleControlsFromTemplate(geo: hou.Geometry, invert: bool = False, bit_mask: int | None = ..., by_name: bool = False) -> list[str]: ...
def filterVisibleControls(scene: Scene, ctrl_paths: Iterable[str], invert: bool = False, bit_mask: int = ...) -> list[str]: ...
@dbg.ZoneScopedDecorator
def getInternalControlsFromTemplate(geo: hou.Geometry, invert: bool = False) -> list[str]: ...
@dbg.ZoneScopedDecorator
def copyTemplateAttribs(template: hou.Geometry, old_template: hou.Geometry) -> None: ...
def groupControlPathsByRig(ctrl_paths: Iterable[str], by_name: bool = False) -> dict[str, list[str]]: ...
def getParmsForControlsFromManager(ctrl_mgr: ControlManager, ctrl_paths: Iterable[str], include_animatable: bool = True, include_non_animatable: bool = False, components: str = '*', channels: bool = False, pattern: bool = False, include_controlgroups: bool = True) -> list[str]: ...
def getParmsForControls(scene: Scene, ctrl_paths: Iterable[str], include_animatable: bool = True, include_non_animatable: bool = False, components: str = '*', channels: bool = False, pattern: bool = False, include_controlgroups: bool = False) -> dict[str, list[str]]: ...
def getControlsFromChannels(scene: Scene, rig_path: str, channel_names: Container[str]) -> list[str]: ...
def addControlToManager(scene: Scene, ctrl_mgr: ControlManager, ctrl_path: str) -> None: ...
def getControlTransforms(scene: Scene, ctrl_paths: Iterable[str], group_by_rig: bool = False) -> dict[str, hou.Matrix4]:
    """
        Get transforms of controls in ctrl_paths

        :param ctrl_paths: list of controls
        :type ctrl_paths: List[str]
        :return: dictionary of controls and their transforms
        :rtype: Dict{str: hou.Matrix4}
        """
def getControlXformsByAction(scene: Scene, control_paths: Iterable[str], action: str | None = None, xforms: dict[str, hou.Matrix4] | None = None) -> dict[str, hou.Matrix4]:
    """fetches the xforms for a given trigger action on control properties either based on control paths or based 
        on a driver -> driven dictionary
        we can use control paths to pin the current xform postions
        and we can use the driver -> driven dict to snap the positions of marked controls to other controls
        """
def getControlReferenceGeo(scene: Scene, ctrl_path: str) -> hou.Geometry | None: ...
def clearControlAnimation(state: _AnimateState, ctrl_paths: Iterable[str], reset_to_default: bool = True, delete_channels: bool = False) -> None: ...
