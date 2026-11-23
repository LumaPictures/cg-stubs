from collections.abc import Iterable, Sequence
from typing import Literal, TypedDict

import hou
from houtypes import ParmActionButtonKwargs, ShelfToolKwargs
from pxr import Sdf
from PySide6 import QtCore
from sceneviewerhooks import _MoveSelectionKwargs

# The kwargs of the Light Mixer's light menu (LightMixerAttributeMenu.xml).
class _LightMixerMenuKwargs(TypedDict):
    node: hou.LopNode
    indexes: Sequence[QtCore.QModelIndex]

# The kwargs of the Scene Graph Tree's primitive menu (UsdStagePrimMenu.xml).
class _ScenegraphMenuKwargs(TypedDict):
    node: hou.LopNode
    primpaths: Sequence[str]

class _LopNodeKwargs(TypedDict):
    node: hou.LopNode

msgPressEnterAccept: str
msgOptDir: str
msgOptUp: str
msgSelectObject: str
msgPathName: str
msgPathCreate: str
msgPathTarget: str
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
msgParentName: str
msgParentCreate: str
msgParentTarget: str
msgPinName: str
msgPinCreate: str
msgPinTarget: str
msgAlignName: str
msgAlignCreate: str
msgAlignTarget: str
POINT_INSTANCES_NOT_ALLOWED: int
POINT_INSTANCES_ALLOWED: int
POINT_INSTANCES_REQUIRED: int
theQuickCOPNetParmName: str
theQuickCOPNetParmLabel: str
theVopCopSignatures: dict[str, str]
theSpecializeNewMaterialBaseParmDS: str
theSpecializedMaterialNodeSuffix: str
theKarmaLensMaterialParmDS: str
theKarmaLensMaterialFilePath: str
theDefaultTestSceneCameraPath: str

def genericTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    nodename: str | None = ...,
    clicktoplace: bool | None = ...,
    exact_node_type: bool = ...,
    selection_parm_name: str | None = ...,
    selection_allow_pattern: bool | None = ...,
    treat_generator_as_filter: bool = ...,
    allow_instance_proxies: bool = ...,
    point_instances: int = ...,
) -> hou.OpNode: ...
def genericGeneratorTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    nodename: str | None = ...,
    clicktoplace: bool | None = ...,
    prompt: str | None = ...,
    exact_node_type: bool = ...,
) -> hou.LopNode: ...
def genericFilterTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    nodename: str | None = ...,
    prompt: str | None = ...,
    exact_node_type: bool = ...,
    selection_parm_name: str | None = ...,
    selection_allow_pattern: bool | None = ...,
    allow_instance_proxies: bool = ...,
    point_instances: int = ...,
) -> hou.LopNode: ...
def createLopNode(
    container: hou.LopNetwork | hou.LopNode,
    nodetypename: str,
    inputnodes: Iterable[hou.LopNode | None],
    nodename: str | None,
    exact_node_type: bool = ...,
    primstring: str | None = ...,
    selection_parm_name: str = ...,
    respect_insertion_point: bool = ...,
    replace_inputs_outputs: bool = ...,
) -> hou.LopNode: ...
def getToolCategoryForPane(pane: hou.PathBasedPaneTab) -> hou.NodeTypeCategory | None: ...
def getLopNodeContainer(cwd: hou.OpNode) -> hou.LopNetwork | hou.LopNode | None: ...
def buildBlockPair(
    scriptargs: ShelfToolKwargs,
    name: str,
    begintype: str,
    endtype: str,
    which_input: int,
    keep_end_input: bool,
) -> tuple[hou.OpNode, hou.OpNode]: ...
def createPointInstancer(kwargs: ShelfToolKwargs, node_name: str, method: str, sourcemode: str = ...) -> None: ...
def saveViewToCamera(viewport: hou.GeometryViewport, cam_lop: hou.LopNode) -> None: ...
def saveViewXformToCamera(viewport: hou.GeometryViewport, xform: hou.Matrix4, cam_lop: hou.LopNode) -> None: ...
def setTranslateAndRotate(lop: hou.OpNode, xform: hou.Matrix4) -> None: ...
def genericCameraLightTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    nodename: str | None = ...,
    clicktoplace: bool | None = ...,
    lock_to_view: bool = ...,
) -> hou.OpNode: ...
def initConstraints(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    nodename: str,
    inputs: Sequence[str],
    targets: Sequence[str],
    lookat: Sequence[str],
    upvector: Sequence[str],
    keep_offset: bool = ...,
) -> hou.OpNode: ...
def constraintparentStateToolApply(
    scriptargs: ShelfToolKwargs,
    input_nodes: Sequence[str],
    target_nodes: Sequence[str],
    keep_offset: bool = ...,
) -> hou.OpNode: ...
def constraintparentStateTool(kwargs: ShelfToolKwargs) -> None: ...
def constraintpinStateToolApply(
    scriptargs: ShelfToolKwargs,
    input_nodes: Sequence[str],
    target_nodes: Sequence[str],
    keep_offset: bool = ...,
) -> hou.OpNode: ...
def constraintpinStateTool(kwargs: ShelfToolKwargs) -> None: ...
def constraintalignStateToolApply(
    scriptargs: ShelfToolKwargs,
    input_nodes: Sequence[str],
    target_nodes: Sequence[str],
    keep_offset: bool = ...,
) -> hou.OpNode: ...
def constraintalignStateTool(kwargs: ShelfToolKwargs) -> None: ...
def constraintlookatStateToolApply(
    scriptargs: ShelfToolKwargs,
    input_nodes: Sequence[str],
    target_nodes: Sequence[str],
    lookup_nodes: Sequence[str],
    keep_offset: bool = ...,
) -> hou.OpNode: ...
def constraintlookatStateTool(kwargs: ShelfToolKwargs) -> None: ...
def constraintpathStateToolApply(
    scriptargs: ShelfToolKwargs,
    input_nodes: Sequence[str],
    target_nodes: Sequence[str],
    lookat_nodes: Sequence[str],
    lookup_nodes: Sequence[str],
    keep_offset: bool = ...,
) -> hou.OpNode: ...
def constraintpathStateTool(kwargs: ShelfToolKwargs) -> None: ...
def constraintsurfaceStateToolApply(
    scriptargs: ShelfToolKwargs,
    input_nodes: Sequence[str],
    target_nodes: Sequence[str],
    lookat_nodes: Sequence[str],
    lookup_nodes: Sequence[str],
    keep_offset: bool = ...,
) -> hou.OpNode: ...
def constraintsurfaceStateTool(kwargs: ShelfToolKwargs) -> None: ...
def constraintpointsStateToolApply(
    scriptargs: ShelfToolKwargs,
    input_nodes: Sequence[str],
    target_nodes: Sequence[str],
    lookat_nodes: Sequence[str],
    lookup_nodes: Sequence[str],
    keep_offset: bool = ...,
) -> hou.OpNode: ...
def constraintpointsStateTool(kwargs: ShelfToolKwargs) -> None: ...
def getViewportPivotDistance(viewport: hou.GeometryViewport) -> float: ...
def normalizeLightExposure(lightnode: hou.OpNode, dist: float) -> None: ...
def setGoodLightExposure(scriptargs: ShelfToolKwargs, lightnode: hou.OpNode) -> None: ...
def getLightParent(lightmixer_node: hou.LopNode, create: bool = ...) -> hou.LopNode | None: ...
def createLightSubnet(lightmixer_node: hou.LopNode) -> hou.LopNode: ...
def insertLight(
    insertionnode: hou.LopNode,
    lighttype: Literal["domelight", "distantlight", "cylinderlight", "disklight", "pointlight", "rectanglelight", "spherelight"] | None = ...,
    lightnodetype: str | None = ...,
    name: str | None = ...,
    openparmeditor: bool = ...,
    parentprimpath: str | None = ...,
) -> hou.LopNode: ...
def duplicateLight(kwargs: _LightMixerMenuKwargs, primpath: str) -> None: ...
def getExistingNodeToEdit(nodetype: str, selection: Iterable[str | Sdf.Path] | None, testnode: hou.OpNode | None) -> hou.LopNode | None: ...
def referenceTestAsset(node: hou.OpNode | None = ..., assetname: str | None = ...) -> None: ...
def getFileNodeTypeName() -> Literal["sublayer", "reference::2.0", "assetreference"] | None: ...
def createCopTextureForShader(kwargs: ParmActionButtonKwargs) -> None: ...
def setupCopNetForMap(
    node: hou.OpNode | None = ...,
    parm: hou.ParmTuple | None = ...,
    kwargs: ParmActionButtonKwargs | None = ...,
    file_suffix: str = ...,
) -> None: ...
def specializeNewMaterials(kwargs: _ScenegraphMenuKwargs, suffix: str = ...) -> None: ...
def createKarmaLensMaterial(node: hou.OpNode | None = ..., kwargs: _LopNodeKwargs | None = ..., ref_file_path: str = ...) -> None: ...
def setupKarmaCameraLensMaterial(kwargs: ParmActionButtonKwargs) -> None: ...
def setupKarmaGlobalAOVMaterial(kwargs: ParmActionButtonKwargs) -> None: ...
def getStateToMoveSelection(kwargs: _MoveSelectionKwargs) -> dict[str, str | None]: ...
def getAdditionalRenderVars() -> list[dict[str, str]]: ...
def getAdditionalRenderVarsMenu() -> list[str]: ...
def createTestSceneToolFromRecipe(kwargs: ShelfToolKwargs, recipe: str | None) -> None: ...
