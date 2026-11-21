from collections.abc import Callable, Iterable, Sequence
from types import TracebackType
from typing import Any, Literal, Self, TypeAlias, TypeVar, overload

import hou
from houtypes import ParmActionButtonKwargs, ParmCallbackKwargs, ShelfToolKwargs
from toolutils import OrientInfo as OrientInfo, ToolboxTemplateGroup as ToolboxTemplateGroup

_T = TypeVar("_T")

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

theAllowedInputTypes: dict[str, tuple[str, ...]]

def showError(msg: str) -> None: ...

class AutoPaneState:
    pane: hou.SceneViewer
    oldpwd: hou.Node
    oldstate: str
    def __init__(self, pane: hou.SceneViewer) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...

class ConstraintToolbox(ToolboxTemplateGroup):
    keep_offset: int
    blend_mode: int
    def __init__(self, do_update: bool = ...) -> None: ...
    def update(self) -> None: ...

class ConstraintParentToolbox(ToolboxTemplateGroup):
    keep_offset: int
    blend_mode: int
    blend_value: float
    add_key: int
    blend_mask: int
    def __init__(self) -> None: ...
    def updateGlobals(self) -> None: ...

class ConstraintBlendToolbox(ToolboxTemplateGroup):
    keep_offset: int
    blend_mode: int
    blend_value: float
    blend_mask: int
    add_key: int
    def __init__(self) -> None: ...
    def updateGlobals(self) -> None: ...

class RightToolbox(ToolboxTemplateGroup):
    def __init__(self) -> None: ...

def matchTransform(kwargs: ParmActionButtonKwargs, option: int) -> None: ...

class ConstraintTransformToolbox(ToolboxTemplateGroup):
    pmode: int
    def __init__(self) -> None: ...
    def updateGlobals(self) -> None: ...

def getObjNodeContainer(cwd: hou.OpNode) -> hou.OpNode: ...
def createObjNode(
    container: hou.OpNode,
    nodetypename: str,
    inputnodes: Iterable[hou.NetworkMovableItem],
    nodename: str | None,
    exact_node_type: bool,
) -> hou.ObjNode: ...
def initEmptyGeometryObject(objectnode: hou.ObjNode) -> None: ...
def genericObjNodeGeneratorTool(
    scriptargs: ShelfToolKwargs | ParmCallbackKwargs,
    nodetypename: str,
    nodename: str | None,
    clicktoplace: bool | None,
    translate_parm_name: str | None = ...,
    prompt: str | None = ...,
    exact_node_type: bool = ...,
) -> hou.ObjNode: ...
def genericObjNodeFilterTool(
    scriptargs: ShelfToolKwargs | ParmCallbackKwargs,
    nodetypename: str,
    nodename: str | None,
    prompt: str | None = ...,
    exact_node_type: bool = ...,
) -> hou.ObjNode: ...
# The object manager types: the tool creates them in the current network, whatever its context,
# so they are not ObjNodes (`ropnet` is a RopNode, `matnet` a ShopNode, ...).
_ObjManagerType: TypeAlias = Literal[
    "chopnet",
    "cop2net",
    "copnet",
    "lopnet",
    "matnet",
    "ropnet",
    "shopnet",
    "topnet",
    "vopnet",
]
@overload
def genericTool(  # type: ignore[overload-overlap]
    scriptargs: ShelfToolKwargs | ParmCallbackKwargs,
    nodetypename: _ObjManagerType,
    nodename: str | None = ...,
    clicktoplace: bool | None = ...,
    translate_parm_name: str | None = ...,
    exact_node_type: bool = ...,
    orient: OrientInfo | None = ...,
) -> hou.OpNode: ...
@overload
def genericTool(
    scriptargs: ShelfToolKwargs | ParmCallbackKwargs,
    nodetypename: str,
    nodename: str | None = ...,
    clicktoplace: bool | None = ...,
    translate_parm_name: str | None = ...,
    exact_node_type: bool = ...,
    orient: OrientInfo | None = ...,
) -> hou.ObjNode: ...
def genericTool(
    scriptargs: ShelfToolKwargs | ParmCallbackKwargs,
    nodetypename: str,
    nodename: str | None = ...,
    clicktoplace: bool | None = ...,
    translate_parm_name: str | None = ...,
    exact_node_type: bool = ...,
    orient: OrientInfo | None = ...,
) -> hou.OpNode: ...
def customStateTool(
    scriptargs: ShelfToolKwargs,
    statename: str,
    nodename: str | None = ...,
    clicktoplace: bool | None = ...,
    translate_parm_name: str | None = ...,
) -> hou.OpNode | None: ...
def genericCameraLightTool(
    scriptargs: ShelfToolKwargs | ParmCallbackKwargs,
    nodetypename: str,
    nodename: str | None = ...,
    clicktoplace: bool | None = ...,
    lock_to_view: bool = ...,
) -> hou.OpNode: ...
def getViewportPivotDistance(viewport: hou.GeometryViewport) -> float: ...
def normalizeLightExposure(lightnode: hou.OpNode, dist: float) -> None: ...
def setGoodLightExposure(scriptargs: ShelfToolKwargs, lightnode: hou.OpNode) -> None: ...
def freeze(selected_obj: Sequence[hou.ObjNode]) -> None: ...
def createSkyLight(kwargs: ShelfToolKwargs) -> hou.OpNode: ...
def createChopnetWithRate(n: hou.OpNode, name: str) -> hou.OpNode: ...
def createChopWithRate(n: hou.OpNode, node_type: str, name: str | None = ...) -> hou.ChopNode: ...
def initOBJConstraints(objs: Iterable[hou.ObjNode]) -> list[hou.OpNode]: ...
def fixupArgNodes(arg_nodes: list[hou.ObjNode]) -> list[hou.ObjNode]: ...
def initOBJTarget(
    chop: hou.OpNode,
    arg_nodes: Sequence[hou.ObjNode | str | None],
    nodetype: str = ...,
    obj: hou.ObjNode | None = ...,
) -> list[hou.OpNode | None]: ...
def initOBJTargets(
    chops: Sequence[hou.OpNode],
    arg_nodes: Sequence[hou.ObjNode | str | None],
    nodetype: str = ...,
) -> list[list[hou.OpNode | None]]: ...
def initOBJTargetsOffset(
    chops: Sequence[hou.OpNode],
    arg_nodes: Sequence[hou.ObjNode | str | None],
    keep_offset: int,
) -> list[list[hou.OpNode | None]]: ...
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
def constraintsMenu(kwargs: ParmActionButtonKwargs) -> None: ...
def initConstraint(
    cname: str,
    clabel: str,
    chop: hou.OpNode | list[hou.OpNode | None],
    targets: hou.OpNode | list[hou.OpNode | None] | None,
    setflag: bool,
    useSetNextInput: bool = ...,
) -> hou.ChopNode: ...
def initConstraints(
    cname: str,
    clabel: str,
    chops: Sequence[hou.OpNode | list[hou.OpNode | None]],
    targets: Sequence[list[hou.OpNode | None]],
    setflag: bool = ...,
    useSetNextInput: bool = ...,
) -> list[hou.ChopNode]: ...
def initOffset(cname: str, clabel: str, obj: hou.ObjNode, constraint: hou.ChopNode) -> hou.ChopNode: ...
def initOffsets(input_nodes: Sequence[hou.ObjNode], constraints: Sequence[hou.ChopNode]) -> list[hou.ChopNode]: ...
def initOffsetTarget(obj: hou.ObjNode, n: hou.ChopNode, parent: hou.ChopNode, parent_outputidx: int) -> hou.ChopNode: ...
def initOffsetParents(input_nodes: Sequence[hou.ObjNode], blends: Sequence[hou.ChopNode]) -> list[list[hou.ChopNode]]: ...
def constraintaddkey(add_key: int, prm: hou.Parm, f: float, v0: float, v1: float) -> None: ...
def constraintaddkeyoffset(add_key: int, keep_offset: int, bld: hou.Parm | None, f: float, v0: float, v1: float) -> None: ...
@overload
def initOffsetBlends(
    input_nodes: Sequence[hou.ObjNode],
    constraints: list[hou.ChopNode],
    chops: Sequence[hou.OpNode],
    add_key: int,
    keep_offset: Literal[0, 1],
) -> list[hou.ChopNode]: ...
@overload
def initOffsetBlends(
    input_nodes: Sequence[hou.ObjNode],
    constraints: list[hou.ChopNode],
    chops: Sequence[hou.OpNode],
    add_key: int,
    keep_offset: Literal[2],
) -> list[list[hou.ChopNode]]: ...
@overload
def initOffsetBlends(
    input_nodes: Sequence[hou.ObjNode],
    constraints: list[hou.ChopNode],
    chops: Sequence[hou.OpNode],
    add_key: int,
    keep_offset: int,
) -> list[hou.ChopNode] | list[list[hou.ChopNode]]: ...
def constraintparentblendStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    arg_nodes: list[hou.ObjNode],
    keep_offset: int,
    blend_mode: int,
    add_key: int = ...,
    blend_value: float = ...,
    blend_mask: int = ...,
) -> list[hou.ChopNode]: ...
def constraintparentblendLayouts(
    chops: Sequence[hou.OpNode],
    parents: Sequence[hou.OpNode],
    blends: Sequence[hou.OpNode],
    blend_targets: Sequence[Sequence[hou.OpNode | None]],
    targets: Sequence[Iterable[hou.OpNode | None]],
) -> None: ...
def constraintparentblendLayout(
    chop: hou.OpNode,
    parent: hou.OpNode,
    blend: hou.OpNode,
    blend_target: hou.OpNode,
    targets: Iterable[hou.OpNode | None],
) -> None: ...
@overload
def constraintblendStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    arg_nodes: list[hou.ObjNode],
    keep_offset: Literal[0, 1] = ...,
    blend_mode: int = ...,
    add_key: int = ...,
    blend_value: float = ...,
    blend_mask: int = ...,
) -> list[hou.ChopNode]: ...
@overload
def constraintblendStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    arg_nodes: list[hou.ObjNode],
    keep_offset: Literal[2],
    blend_mode: int = ...,
    add_key: int = ...,
    blend_value: float = ...,
    blend_mask: int = ...,
) -> list[list[hou.ChopNode]]: ...
@overload
def constraintblendStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    arg_nodes: list[hou.ObjNode],
    keep_offset: int = ...,
    blend_mode: int = ...,
    add_key: int = ...,
    blend_value: float = ...,
    blend_mask: int = ...,
) -> list[hou.ChopNode] | list[list[hou.ChopNode]]: ...
@overload
def constraintsequenceStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    arg_nodes: list[hou.ObjNode],
    keep_offset: Literal[0, 1] = ...,
    add_key: int = ...,
    blend_value: float = ...,
    blend_mask: int = ...,
) -> list[hou.ChopNode]: ...
@overload
def constraintsequenceStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    arg_nodes: list[hou.ObjNode],
    keep_offset: Literal[2],
    add_key: int = ...,
    blend_value: float = ...,
    blend_mask: int = ...,
) -> list[list[hou.ChopNode]]: ...
@overload
def constraintsequenceStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    arg_nodes: list[hou.ObjNode],
    keep_offset: int = ...,
    add_key: int = ...,
    blend_value: float = ...,
    blend_mask: int = ...,
) -> list[hou.ChopNode] | list[list[hou.ChopNode]]: ...
@overload
def constraintsimpleblendStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    arg_nodes: list[hou.ObjNode],
    keep_offset: Literal[0, 1] = ...,
    add_key: int = ...,
    blend_value: float = ...,
    blend_mask: int = ...,
) -> list[hou.ChopNode]: ...
@overload
def constraintsimpleblendStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    arg_nodes: list[hou.ObjNode],
    keep_offset: Literal[2],
    add_key: int = ...,
    blend_value: float = ...,
    blend_mask: int = ...,
) -> list[list[hou.ChopNode]]: ...
@overload
def constraintsimpleblendStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    arg_nodes: list[hou.ObjNode],
    keep_offset: int = ...,
    add_key: int = ...,
    blend_value: float = ...,
    blend_mask: int = ...,
) -> list[hou.ChopNode] | list[list[hou.ChopNode]]: ...
def constraintparentblendStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def constraintblendStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def constrainttransformStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    pivot_nodes: Sequence[hou.ObjNode],
    pmode: int,
) -> list[hou.ChopNode]: ...
def constrainttransformStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def constraintlookatStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    lookat_nodes: list[hou.ObjNode],
    lookup_nodes: Sequence[hou.ObjNode],
    keep_offset: int,
) -> list[hou.ChopNode]: ...
def constraintlookatStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def initLookAtTargets(
    chops: Sequence[hou.OpNode],
    lookat_nodes: Sequence[hou.ObjNode],
    lookup_nodes: Sequence[hou.ObjNode],
) -> list[list[hou.OpNode | None]]: ...
def constraintpathStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    path_nodes: Sequence[hou.OpNode],
    lookat_nodes: Sequence[hou.ObjNode],
    lookup_nodes: Sequence[hou.ObjNode],
    keep_offset: int,
) -> list[hou.ChopNode]: ...
def constraintpathStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def constraintpointsStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    soppath_nodes: Sequence[hou.OpNode],
    lookat_nodes: Sequence[hou.ObjNode],
    lookup_nodes: Sequence[hou.ObjNode],
    keep_offset: int = ...,
    select_points: str | None = ...,
) -> list[hou.ChopNode]: ...
def constraintpointsStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def constraintsurfaceStateToolApply(
    input_nodes: Sequence[hou.ObjNode],
    lookat_nodes: Sequence[hou.ObjNode],
    lookup_nodes: Sequence[hou.ObjNode],
    keep_offset: int,
    select_location: Sequence[str | Sequence[float]] | None,
) -> list[hou.ChopNode]: ...
def constraintsurfaceStateTool(kwargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def objectsFromScriptArgs(scriptargs: ShelfToolKwargs | ParmActionButtonKwargs) -> list[hou.ObjNode]: ...
def constraintnetworkStateToolApply(scriptargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def getConstraintsOnParms(objs: Iterable[hou.OpNode], valid_values: int) -> list[hou.Parm]: ...
def constraintdisableStateTool(scriptargs: ShelfToolKwargs) -> None: ...
def constraintenableStateTool(scriptargs: ShelfToolKwargs) -> None: ...
def constrainttoggleStateTool(scriptargs: ShelfToolKwargs) -> None: ...
def constraintdeleteStateTool(scriptargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def constraintbakeStateTool(scriptargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def bakeanimationStateTool(scriptargs: ShelfToolKwargs) -> None: ...
def selectPrimitiveUVs(
    orisop: hou.OpNode | None,
    prompt: str,
    icon: str,
    label: str,
) -> list[bool | int | hou.Node | hou.Vector3 | None]: ...
def constraintsurfacePicked(
    n: hou.OpNode,
    npr: hou.Parm,
    picked: bool,
    new_sop: hou.ObjNode | hou.SopNode | None,
    new_prim: int | None,
    new_pos: hou.Vector3 | None,
    new_uvw: hou.Vector3 | None,
) -> None: ...
def checkShiftDown() -> bool: ...
def constraintsurfaceSelect(n: hou.ChopNode) -> None: ...
def constraintpointsSelect(n: hou.ChopNode) -> None: ...
def constraintgamepadStateTool(scriptargs: ShelfToolKwargs | ParmActionButtonKwargs) -> None: ...
def promoteParm(
    target_node: hou.OpNode,
    source_node: hou.OpNode,
    parm_name: str,
    folder: Sequence[str],
    has_menu: bool = ...,
    label: str | None = ...,
) -> None: ...
