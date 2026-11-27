import hou
import typing
from collections.abc import Callable as Callable, Iterable, Sequence
from houtypes import ParmActionButtonKwargs, ParmCallbackKwargs, ShelfToolKwargs
from toolutils import OrientInfo as OrientInfo, ToolboxTemplateGroup as ToolboxTemplateGroup
from types import TracebackType
from typing import Literal, Self

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_T = TypeVar('_T')
_ObjManagerType: TypeAlias = Literal['chopnet', 'cop2net', 'copnet', 'lopnet', 'matnet', 'ropnet', 'shopnet', 'topnet', 'vopnet']
msgPressEnterAccept: str
msgOptDir: str
msgOptUp: str
msgOptPivot: str
msgSelectObject: str
msgParentBlendName: str
msgParentBlendCreate: str
msgParentBlendTargets: str
msgBlendName: str
msgBlendCreate: str
msgBlendTargets: str
msgPathName: str
msgPathCreate: str
msgPathObject: str
msgPathDir: str
msgPathUp: str
msgLookAtName: str
msgLookAtCreate: str
msgLookAtDir: str
msgLookAtUp: str
msgPointsName: str
msgPointsCreate: str
msgPointsTarget: str
msgPointsDir: str
msgPointsUp: str
msgSurfaceName: str
msgSurfaceCreate: str
msgSurfaceTarget: str
msgSurfaceDir: str
msgSurfaceUp: str
msgTransformName: str
msgTransformCreate: str
msgTransformPivot: str
msgSurfacePick: str
toolboxBlendModes: list[str]
toolboxBlendMode_Proportional: int
toolboxBlendMode_Difference: int
toolboxBlendMode_Sequence: int
toolboxBlendMode_Simple: int
toolboxOffsetModes: list[str]
toolboxOffsetMode_None: Literal[0]
toolboxOffsetMode_After: Literal[1]
toolboxOffsetMode_Before: Literal[2]
toolboxPivotModes: list[str]
toolboxPivotMode_TranslateFromPivotInput: int
toolboxPivotMode_RotateFromPivotInput: int
toolboxPivotMode_BothFromPivotInput: int

def showError(msg: str) -> None:
    """Display an error message."""

class AutoPaneState:
    """Auto Scope class to keep a Pane State"""
    pane: hou.SceneViewer
    oldpwd: hou.OpNode | None
    oldstate: str
    def __init__(self, pane: hou.SceneViewer) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...

class ConstraintToolbox(ToolboxTemplateGroup):
    """Common toolbox for all constraints"""
    keep_offset: int
    blend_mode: int
    def __init__(self, do_update: bool = True) -> None: ...
    def update(self) -> None:
        """All constraints have a keep_offset toggle at the end"""

class ConstraintParentToolbox(ToolboxTemplateGroup):
    """Toolbox for parent constraints"""
    keep_offset: int
    blend_mode: int
    blend_value: float
    add_key: int
    blend_mask: int
    def __init__(self) -> None: ...
    def updateGlobals(self) -> None: ...

class ConstraintBlendToolbox(ToolboxTemplateGroup):
    """Toolbox for blend constraints"""
    keep_offset: int
    blend_mode: int
    blend_value: float
    blend_mask: int
    add_key: int
    def __init__(self) -> None: ...
    def updateGlobals(self) -> None: ...

class RightToolbox(ToolboxTemplateGroup):
    """Empty Right Toolbox to fill the right side of the toolbox"""
    def __init__(self) -> None: ...

def matchTransform(kwargs: ParmActionButtonKwargs, option: int) -> None:
    """ Called when a match transform button is clicked. """

class ConstraintTransformToolbox(ToolboxTemplateGroup):
    """Toolbox for transform constraints"""
    pmode: int
    def __init__(self) -> None: ...
    def updateGlobals(self) -> None: ...

def getObjNodeContainer(cwd: hou.OpNode) -> hou.OpNode:
    """ Returns the scene level object that is or contains the specified
        node (which should be a SOP node or Object node).
    """
def createObjNode(container: hou.OpNode, nodetypename: str, inputnodes: Iterable[hou.NetworkMovableItem], nodename: str | None, exact_node_type: bool) -> hou.ObjNode:
    """ Creates an Object node inside the specified container network. """
def initEmptyGeometryObject(objectnode: hou.ObjNode) -> None:
    """ Destroy the File SOP that gets created inside a default Geometry
        Object.
    """
def genericObjNodeGeneratorTool(scriptargs: ShelfToolKwargs | ParmCallbackKwargs, nodetypename: str, nodename: str | None, clicktoplace: bool | None, translate_parm_name: str | None = None, prompt: str | None = None, exact_node_type: bool = True) -> hou.ObjNode:
    """ Creates an Object Generator node. The node is either created at the
        origin, or asks the user to select a location in the viewport
        depending on the value of the clicktoplace parameter.
    """
def genericObjNodeFilterTool(scriptargs: ShelfToolKwargs | ParmCallbackKwargs, nodetypename: str, nodename: str | None, prompt: str | None = None, exact_node_type: bool = True) -> hou.ObjNode:
    """ Creates an Object node that requires other object nodes as input. """
@typing.overload
def genericTool(scriptargs: ShelfToolKwargs | ParmCallbackKwargs, nodetypename: _ObjManagerType, nodename: str | None = ..., clicktoplace: bool | None = ..., translate_parm_name: str | None = ..., exact_node_type: bool = ..., orient: OrientInfo | None = ...) -> hou.OpNode: ...  # type: ignore[overload-overlap]
@typing.overload
def genericTool(scriptargs: ShelfToolKwargs | ParmCallbackKwargs, nodetypename: str, nodename: str | None = ..., clicktoplace: bool | None = ..., translate_parm_name: str | None = ..., exact_node_type: bool = ..., orient: OrientInfo | None = ...) -> hou.ObjNode: ...
def customStateTool(scriptargs: ShelfToolKwargs, statename: str, nodename: str | None = None, clicktoplace: bool | None = None, translate_parm_name: str | None = None) -> hou.OpNode | None:
    """ Invokes a custom object state if invoked from a scene viewer. This
        allows the custom state to control the creation and configuration of
        the object node. In a network editor this function calls the
        standard node creation code.
    """
def genericCameraLightTool(scriptargs: ShelfToolKwargs | ParmCallbackKwargs, nodetypename: str, nodename: str | None = None, clicktoplace: bool | None = None, lock_to_view: bool = True) -> hou.OpNode:
    """ A generic function for creating Camera or Light object nodes of
        various types. This tool handles the initialization of the node
        transforms to match the current view if the Ctrl key was used to
        invoke the tool. Otherwise the user is prompted for a location.
    """
def getViewportPivotDistance(viewport: hou.GeometryViewport) -> float: ...
def normalizeLightExposure(lightnode: hou.OpNode, dist: float) -> None:
    """ Sets the light exposure such that brightness at a distance 'dist'
        equals the value of the light_intensity parameter. This compensates for
        physical attenuation, if set. """
def setGoodLightExposure(scriptargs: ShelfToolKwargs, lightnode: hou.OpNode) -> None:
    """ Sets the light exposure such that brightness is 1.0 at the
        viewport pivot, compensating for physical attenuation, if set. Does
        nothing when scriptargs indicate that ctrl or cmd weren't being held,
        since that means the light wasn't created from the viewport camera. In
        that case we don't currently have a good estimate of the required
        exposure."""

theAllowedInputTypes: dict[str, tuple[str, ...]]

def freeze(selected_obj: Sequence[hou.ObjNode]) -> None:
    """ Freezes the transforms of the given list of geometry objects. Transform
        SOPs are added in order to move the world transforms of the objects
        to the geometry level.
    """
def createSkyLight(kwargs: ShelfToolKwargs) -> hou.OpNode:
    """ Creates a linked sky light and sunlight pair.
    """
def createChopnetWithRate(n: hou.OpNode, name: str) -> hou.OpNode:
    """ Creates a CHOPnet and add rate spare parameter if one of its parents doesn't have it already.
    """
def createChopWithRate(n: hou.OpNode, node_type: str, name: str | None = None) -> hou.ChopNode:
    """ Creates a CHOP node and add rate references.
    """
def initOBJConstraints(objs: Iterable[hou.ObjNode]) -> list[hou.OpNode]: ...
def fixupArgNodes(arg_nodes: list[hou.ObjNode]) -> list[hou.ObjNode]: ...
def initOBJTarget(chop: hou.OpNode, arg_nodes: Sequence[hou.ObjNode | str | None], nodetype: str = 'constraintobject', obj: hou.ObjNode | None = None) -> list[hou.OpNode | None]: ...
def initOBJTargets(chops: Sequence[hou.OpNode], arg_nodes: Sequence[hou.ObjNode | str | None], nodetype: str = 'constraintobject') -> list[list[hou.OpNode | None]]: ...
def initOBJTargetsOffset(chops: Sequence[hou.OpNode], arg_nodes: Sequence[hou.ObjNode | str | None], keep_offset: int) -> list[list[hou.OpNode | None]]: ...
def initParentTargets(chops: Sequence[hou.OpNode], objs: Sequence[hou.ObjNode]) -> list[list[hou.OpNode | None]]: ...
def getInputsRecursively(n: hou.Node, a: list[hou.Node | None]) -> None: ...
def layoutInputs(n: hou.Node) -> None: ...
def forceObject(o: _T | list[_T] | tuple[_T, ...]) -> _T: ...
def forceList(l: _T | list[_T] | tuple[_T, ...]) -> list[_T] | tuple[_T, ...]: ...

class ConstraintMenuEntry:
    name: str
    icon: str
    cb: Callable[[ParmActionButtonKwargs], object] | None
    def __init__(self, name: str, icon: str, cb: Callable[[ParmActionButtonKwargs], object] | None) -> None: ...

def constraintsMenuUserEntries() -> list[ConstraintMenuEntry]: ...
def constraintsMenuBuiltinEntries() -> list[ConstraintMenuEntry]: ...
def constraintsMenuEntries() -> list[ConstraintMenuEntry]: ...
def constraintsMenu(kwargs: ParmActionButtonKwargs) -> None:
    """Callback for the constraint_path extra button"""
def initConstraint(cname: str, clabel: str, chop: hou.OpNode | list[hou.OpNode | None], targets: hou.OpNode | list[hou.OpNode | None] | None, setflag: bool, useSetNextInput: bool = True) -> hou.ChopNode: ...
def initConstraints(cname: str, clabel: str, chops: Sequence[hou.OpNode | list[hou.OpNode | None]], targets: Sequence[list[hou.OpNode | None]], setflag: bool = True, useSetNextInput: bool = True) -> list[hou.ChopNode]: ...
def initOffset(cname: str, clabel: str, obj: hou.ObjNode, constraint: hou.ChopNode) -> hou.ChopNode: ...
def initOffsets(input_nodes: Sequence[hou.ObjNode], constraints: Sequence[hou.ChopNode]) -> list[hou.ChopNode]: ...
def initOffsetTarget(obj: hou.ObjNode, n: hou.ChopNode, parent: hou.ChopNode, parent_outputidx: int) -> hou.ChopNode: ...
def initOffsetParents(input_nodes: Sequence[hou.ObjNode], blends: Sequence[hou.ChopNode]) -> list[list[hou.ChopNode]]: ...
def constraintaddkey(add_key: int, prm: hou.Parm, f: float, v0: float, v1: float) -> None: ...
def constraintaddkeyoffset(add_key: int, keep_offset: int, bld: hou.Parm | None, f: float, v0: float, v1: float) -> None: ...
@typing.overload
def initOffsetBlends(input_nodes: Sequence[hou.ObjNode], constraints: list[hou.ChopNode], chops: Sequence[hou.OpNode], add_key: int, keep_offset: Literal[0, 1]) -> list[hou.ChopNode]: ...
@typing.overload
def initOffsetBlends(input_nodes: Sequence[hou.ObjNode], constraints: list[hou.ChopNode], chops: Sequence[hou.OpNode], add_key: int, keep_offset: Literal[2]) -> list[list[hou.ChopNode]]: ...
@typing.overload
def initOffsetBlends(input_nodes: Sequence[hou.ObjNode], constraints: list[hou.ChopNode], chops: Sequence[hou.OpNode], add_key: int, keep_offset: int) -> list[hou.ChopNode] | list[list[hou.ChopNode]]: ...
def constraintparentblendStateToolApply(input_nodes: Sequence[hou.ObjNode], arg_nodes: list[hou.ObjNode], keep_offset: int, blend_mode: int, add_key: int = False, blend_value: float = 1.0, blend_mask: int = 511) -> list[hou.ChopNode]:
    """Parent Blend Constraint Shelf Tool without Picking session"""
def constraintparentblendLayouts(chops: Sequence[hou.OpNode], parents: Sequence[hou.OpNode], blends: Sequence[hou.OpNode], blend_targets: Sequence[Sequence[hou.OpNode | None]], targets: Sequence[Iterable[hou.OpNode | None]]) -> None: ...
def constraintparentblendLayout(chop: hou.OpNode, parent: hou.OpNode, blend: hou.OpNode, blend_target: hou.OpNode, targets: Iterable[hou.OpNode | None]) -> None: ...
@typing.overload
def constraintblendStateToolApply(input_nodes: Sequence[hou.ObjNode], arg_nodes: list[hou.ObjNode], keep_offset: Literal[0, 1] = ..., blend_mode: int = ..., add_key: int = ..., blend_value: float = ..., blend_mask: int = ...) -> list[hou.ChopNode]: ...
@typing.overload
def constraintblendStateToolApply(input_nodes: Sequence[hou.ObjNode], arg_nodes: list[hou.ObjNode], keep_offset: Literal[2], blend_mode: int = ..., add_key: int = ..., blend_value: float = ..., blend_mask: int = ...) -> list[list[hou.ChopNode]]: ...
@typing.overload
def constraintblendStateToolApply(input_nodes: Sequence[hou.ObjNode], arg_nodes: list[hou.ObjNode], keep_offset: int = ..., blend_mode: int = ..., add_key: int = ..., blend_value: float = ..., blend_mask: int = ...) -> list[hou.ChopNode] | list[list[hou.ChopNode]]: ...
@typing.overload
def constraintsequenceStateToolApply(input_nodes: Sequence[hou.ObjNode], arg_nodes: list[hou.ObjNode], keep_offset: Literal[0, 1] = ..., add_key: int = ..., blend_value: float = ..., blend_mask: int = ...) -> list[hou.ChopNode]: ...
@typing.overload
def constraintsequenceStateToolApply(input_nodes: Sequence[hou.ObjNode], arg_nodes: list[hou.ObjNode], keep_offset: Literal[2], add_key: int = ..., blend_value: float = ..., blend_mask: int = ...) -> list[list[hou.ChopNode]]: ...
@typing.overload
def constraintsequenceStateToolApply(input_nodes: Sequence[hou.ObjNode], arg_nodes: list[hou.ObjNode], keep_offset: int = ..., add_key: int = ..., blend_value: float = ..., blend_mask: int = ...) -> list[hou.ChopNode] | list[list[hou.ChopNode]]: ...
@typing.overload
def constraintsimpleblendStateToolApply(input_nodes: Sequence[hou.ObjNode], arg_nodes: list[hou.ObjNode], keep_offset: Literal[0, 1] = ..., add_key: int = ..., blend_value: float = ..., blend_mask: int = ...) -> list[hou.ChopNode]: ...
@typing.overload
def constraintsimpleblendStateToolApply(input_nodes: Sequence[hou.ObjNode], arg_nodes: list[hou.ObjNode], keep_offset: Literal[2], add_key: int = ..., blend_value: float = ..., blend_mask: int = ...) -> list[list[hou.ChopNode]]: ...
@typing.overload
def constraintsimpleblendStateToolApply(input_nodes: Sequence[hou.ObjNode], arg_nodes: list[hou.ObjNode], keep_offset: int = ..., add_key: int = ..., blend_value: float = ..., blend_mask: int = ...) -> list[hou.ChopNode] | list[list[hou.ChopNode]]: ...
def constraintparentblendStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None:
    """Parent Blend Constraint Shelf Tool"""
def constraintblendStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None:
    """Blend Constraint Shelf Tool"""
def constrainttransformStateToolApply(input_nodes: Sequence[hou.ObjNode], pivot_nodes: Sequence[hou.ObjNode], pmode: int) -> list[hou.ChopNode]:
    """Transform Constraint Shelf Tool without Picking session"""
def constrainttransformStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None:
    """Transform Constraint Shelf Tool"""
def constraintlookatStateToolApply(input_nodes: Sequence[hou.ObjNode], lookat_nodes: list[hou.ObjNode], lookup_nodes: Sequence[hou.ObjNode], keep_offset: int) -> list[hou.ChopNode]:
    """Look At Constraint Shelf Tool without Picking session"""
def constraintlookatStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None:
    """Look At Constraint Shelf Tool"""
def initLookAtTargets(chops: Sequence[hou.OpNode], lookat_nodes: Sequence[hou.ObjNode], lookup_nodes: Sequence[hou.ObjNode]) -> list[list[hou.OpNode | None]]: ...
def constraintpathStateToolApply(input_nodes: Sequence[hou.ObjNode], path_nodes: Sequence[hou.OpNode], lookat_nodes: Sequence[hou.ObjNode], lookup_nodes: Sequence[hou.ObjNode], keep_offset: int) -> list[hou.ChopNode]:
    """Path Constraint Shelf Tool without Picking session"""
def constraintpathStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None:
    """Path Constraint Shelf Tool"""
def constraintpointsStateToolApply(input_nodes: Sequence[hou.ObjNode], soppath_nodes: Sequence[hou.OpNode], lookat_nodes: Sequence[hou.ObjNode], lookup_nodes: Sequence[hou.ObjNode], keep_offset: int = False, select_points: str | None = None) -> list[hou.ChopNode]:
    """Points Constraint Shelf Tool without Picking session"""
def constraintpointsStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None:
    """Points Constraint Shelf Tool"""
def constraintsurfaceStateToolApply(input_nodes: Sequence[hou.ObjNode], lookat_nodes: Sequence[hou.ObjNode], lookup_nodes: Sequence[hou.ObjNode], keep_offset: int, select_location: Sequence[str | Sequence[float]] | None) -> list[hou.ChopNode]:
    """Surface Constraint Shelf Tool without Picking session"""
def constraintsurfaceStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None:
    """Surface Constraint Shelf Tool"""
def objectsFromScriptArgs(scriptargs: ShelfToolKwargs | ParmActionButtonKwargs) -> list[hou.ObjNode]: ...
def constraintnetworkStateToolApply(scriptargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def getConstraintsOnParms(objs: Iterable[hou.OpNode], valid_values: int) -> list[hou.Parm]: ...
def constraintdisableStateTool(scriptargs: ShelfToolKwargs) -> None: ...
def constraintenableStateTool(scriptargs: ShelfToolKwargs) -> None: ...
def constrainttoggleStateTool(scriptargs: ShelfToolKwargs) -> None: ...
def constraintdeleteStateTool(scriptargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def constraintbakeStateTool(scriptargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def bakeanimationStateTool(scriptargs: ShelfToolKwargs) -> None: ...
def selectPrimitiveUVs(orisop: hou.OpNode | None, prompt: str, icon: str, label: str) -> list[bool | int | hou.ObjNode | hou.SopNode | hou.Vector3 | None]: ...
def constraintsurfacePicked(n: hou.OpNode, npr: hou.Parm, picked: bool, new_sop: hou.ObjNode | hou.SopNode | None, new_prim: int | None, new_pos: hou.Vector3 | None, new_uvw: hou.Vector3 | None) -> None: ...
def checkShiftDown() -> bool: ...
def constraintsurfaceSelect(n: hou.ChopNode) -> None: ...
def constraintpointsSelect(n: hou.ChopNode) -> None: ...
def constraintgamepadStateTool(scriptargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def promoteParm(target_node: hou.OpNode, source_node: hou.OpNode, parm_name: str, folder: Sequence[str], has_menu: bool = False, label: str | None = None) -> None: ...
