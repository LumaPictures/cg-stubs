import _apex
import hou
import typing
from _apexscene import Scene as Scene
from apex.bake import InverseRig as InverseRig, _CtrlParms
from apex.control_2 import ControlManager as ControlManager, controlName as controlName
from collections.abc import Callable as Callable, Collection, ItemsView, KeysView, Mapping, ValuesView
from typing import Concatenate, Literal

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
_ControlT = TypeVar('_ControlT', bound='Control')
_AbstractSourceT = TypeVar('_AbstractSourceT', bound='AbstractSource')
_MappingT = TypeVar('_MappingT', bound='RigSkeletonMapping')
CONTROL_ATTR: str

class Joint:
    name: str
    rest_xform: hou.Matrix4
    rest_translation: hou.Vector3
    def __init__(self, idx: int, name: str, rest_skel: hou.Geometry, use_rest_transform: bool = False) -> None: ...
    def setRestXform(self, xfo: hou.Matrix4) -> None: ...
    def getPoint(self, skel: hou.Geometry) -> hou.Point | None: ...
    @typing.overload
    def xform(self, skel: hou.Geometry) -> hou.Matrix4: ...
    @typing.overload
    def xform(self, skel: dict[str, hou.Matrix4]) -> hou.Matrix4 | None: ...
    def restXform(self) -> hou.Matrix4: ...
    def restTranslation(self) -> hou.Vector3: ...
    def setControlOverride(self, value: bool = False, skel: hou.Geometry | None = None) -> None: ...
    def isControlOverride(self) -> bool: ...

class InvertSubnet:
    """Defines an inverse kinematic subnet that manages control-to-joint mappings.

    This class represents a subnet node in an APEX graph that handles inverse
    kinematic operations. It collects and manages the relationships between
    controls, joints, and abstract control parameters by analyzing the subnet's
    input ports.

    :param name: The name of the subnet node in the APEX graph
    :type name: str
    :param graph: The APEX graph containing the subnet node
    :type graph: apex.Graph

    :ivar control_names: List of Matrix4 control input port names
    :vartype control_names: list[str]
    :ivar joint_names: List of skeleton joint names (derived from ports ending with '_skel')
    :vartype joint_names: list[str]
    :ivar abstract_control_names: List of abstract parameter control names (non-Matrix4 ports)
    :vartype abstract_control_names: list[str]
    :ivar bypass_skel_parm: Parameter name for bypassing skeleton inputs
    :vartype bypass_skel_parm: str
    :ivar bypass_abstract_parm: Parameter name for bypassing abstract control inputs
    :vartype bypass_abstract_parm: str
    """
    name: str
    control_names: list[str]
    joint_names: list[str]
    abstract_control_names: list[str]
    bypass_skel_parm: str
    bypass_abstract_parm: str
    bypass_parms: list[str]
    def __init__(self, name: str, graph: _apex.Graph) -> None: ...
    def controls(self, controls_dict: Mapping[str, _ControlT]) -> list[_ControlT]: ...
    def bindControls(self, controls_dict: Mapping[str, 'Control']) -> None: ...
    def joints(self, joints_dict: Mapping[str, Joint]) -> list[Joint]: ...
    def jointInputBinding(self, joint: Joint) -> str: ...
    def abstractControls(self, controls_dict: Mapping[str, _AbstractSourceT]) -> list[_AbstractSourceT]: ...

class Control:
    path: str
    parmBinding: str
    rest_xform: hou.Matrix4
    rest_translation: hou.Vector3
    def __init__(self, path: str, ctrl_mgr: ControlManager) -> None: ...
    def xform(self, ctrl_mgr: ControlManager) -> hou.Matrix4: ...
    def setRestXform(self, xfo: hou.Matrix4) -> None: ...
    def restXform(self) -> hou.Matrix4: ...
    def restTranslation(self) -> hou.Vector3: ...
    def setJoints(self, joint: Joint, joints: Mapping[str, Joint], skel: hou.Geometry) -> None: ...
    def clearJoints(self) -> None: ...
    def computeXform(self, skel: hou.Geometry) -> hou.Matrix4: ...
    def setInvertSubnet(self, subnetname: str) -> None: ...
    def invertSubnet(self) -> str | None: ...

class JointControl(Control):
    use_offset: bool
    offset: hou.Matrix4
    joint: Joint | None
    def __init__(self, ctrl_path: str, ctrl_mgr: ControlManager, use_offset: bool = True) -> None: ...
    def setJoints(self, joint: Joint, joints: Mapping[str, Joint], skel: hou.Geometry) -> None: ...
    def clearJoints(self) -> None: ...
    def computeXform(self, skel: hou.Geometry) -> hou.Matrix4: ...

class AbstractSource:
    """handles any types of abstract parameter bindings for a rig. This also includes abstract
    controls but also abstract parameter values with out controls. The second scenario is 
    important for animated blendshape channel inputs. in the future we might want to also use them 
    to revert back to a proper control interface
    """
    name: str
    parmbindings: list[str]
    bindingsources: dict[str, Literal[0, 1, 2]]
    def __init__(self, name: str, rest_skel: hou.Geometry | None = None) -> None: ...
    def setBindingSources(self, skel: hou.Geometry) -> None:
        """generates a dict that defines the source for every given binding:
        0 - no input at all
        1 - the detail parms dict on the geo contains the binding
        2 - a detail attrib with the matching name in the style of blendshape channels

        :param skel: a dict key: parm binding name, value: the source enum
        """
    def computeValues(self, skel: hou.Geometry) -> _apex.Dict:
        """fetches the current value from a given skeleton geometry based on the earlier defined
        geo source for the given parameter 

        :param skel: the skeleton geo to fetch 
        """
    def hasBindings(self) -> bool: ...

class AbstractControl(AbstractSource):
    path: str
    parmbindings: list[str]
    bindings: Collection[str]
    bindingsources: dict[str, Literal[0, 1, 2]]
    def __init__(self, path: str, ctrl_mgr: ControlManager, rest_skel: hou.Geometry) -> None: ...
    def getBindParms(self, ctrl_mgr: ControlManager) -> None: ...

class PoleVectorControl(JointControl):
    root: Joint | None
    tip: Joint | None
    def __init__(self, ctrl_path: str, ctrl_mgr: ControlManager) -> None: ...
    @property
    def mid(self) -> Joint | None: ...
    def setJoints(self, joint: Joint, joints: Mapping[str, Joint], skel: hou.Geometry) -> None: ...
    def clearJoints(self) -> None: ...
    def computeXform(self, skel: hou.Geometry) -> hou.Matrix4: ...

class SkeletonBaker:
    """
    Provides common methods for retargeting from a source skeleton
    to the rig controls.
    It uses only scene data, can be useful for FBIK, Ragdoll, and other similar tools.

    :param scene: The scene that needs update
    :type scene: apex.Scene()
    :param rig_path: The path in the scene's data to the rig's apex.SceneGraph()
    :type rig_path: str
    :param rest_skel: The skeleton of rig (used to compute offset xforms)
    :type rest_skel: hou.Geometry
    """
    rig_skeleton: RigSkeleton
    mapping: RigSkeletonMapping | None
    mapped_controls: dict[str, JointControl]
    inverse_rig: InverseRig | None
    output_pattern: str
    MAP_BY_PROPERTY: int
    MAP_BY_NAME: int
    MAP_BY_XFORM: int
    def __init__(self, rig_skeleton: RigSkeleton, mapping: RigSkeletonMapping | None) -> None: ...
    @property
    def scene(self) -> Scene | None: ...
    @property
    def rig_path(self) -> str: ...
    def updateMapping(self, mapping: RigSkeletonMapping | None) -> None: ...
    def getEvaluatedTRS(self, xforms: hou.Geometry) -> dict[str, _CtrlParms]:
        """_summary_

        :param xforms: the skeleton geometry with the current positions and abstract values! this is NOT an array 
        :return: _description_
        """
    def updateRigParmsFromTRS(self, trs: Mapping[str, _CtrlParms], rig_parms: _apex.Dict | None = None) -> _apex.Dict: ...
    def updateInputGeometriesFromScene(self) -> None: ...

class RigSkeletonMapping:
    rig_skeleton: RigSkeleton
    controls_to_joints: dict[str, str]
    joints_to_control_paths: dict[str, list[str]]
    is_default: bool
    joint_override: bool
    default_mapping_used: bool
    def __init__(self, rig_skeleton: RigSkeleton, property_name: str | None = None, joint_override: bool = True) -> None: ...
    @staticmethod
    def overrideHandler(func: Callable[Concatenate[_MappingT, _P], _R]) -> Callable[Concatenate[_MappingT, _P], _R]: ...
    @property
    def controls(self) -> dict[str, JointControl]: ...
    @property
    def joints(self) -> dict[str, Joint]: ...
    @property
    def scene(self) -> Scene | None: ...
    @property
    def rig_path(self) -> str: ...
    def items(self) -> ItemsView[str, str]: ...
    def mappedJoints(self) -> KeysView[str]: ...
    def mappedControls(self) -> ValuesView[list[str]]: ...
    def reset(self) -> None: ...
    @overrideHandler
    def mapByProperty(self, property_name: str = 'mapping', reset: bool = True, xform_property_name: str | None = None) -> None: ...
    @overrideHandler
    def mapByName(self, reset: bool = True) -> None: ...
    @overrideHandler
    def mapByTransform(self, tolerance: float = 0.01, reset: bool = True) -> None: ...

class RigSkeleton:
    rig_path: str
    skel: hou.Geometry
    source_skel: hou.Geometry
    invertSubnets: dict[str, InvertSubnet]
    joints: dict[str, Joint]
    controls: dict[str, JointControl]
    abstractControls: dict[str, AbstractControl]
    output_pattern: str
    def __init__(self, scene: Scene, rig_path: str, skel: hou.Geometry, source_skel: hou.Geometry | None = None) -> None: ...
    @property
    def scene(self) -> Scene | None: ...
    def joint(self, joint_name: str) -> Joint | None: ...
    def control(self, ctrl_name: str) -> JointControl | None: ...
    def invertSubnet(self, inv_name: str) -> InvertSubnet | None: ...
    def abstractControl(self, ctrl_name: str) -> AbstractControl | None: ...
    def boundAbstractControls(self) -> list[AbstractControl]:
        """abstract controls that have a skeleton abstract parm binding"""
    def invertAbstractControls(self) -> list[AbstractControl]:
        """abstract controls that get value set by a custom inverter"""
    def activeAbstractControls(self) -> list[AbstractControl]: ...
    def overrideJoints(self) -> list[Joint]: ...
    def setAbstractControlBindings(self, skel: hou.Geometry) -> None: ...
