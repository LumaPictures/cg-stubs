from collections.abc import Callable, Container, Iterable, Mapping, Sequence
from typing import Literal, NotRequired, TypeAlias, TypedDict, overload

import hou
from houtypes import ParmActionButtonKwargs, ParmCallbackKwargs, ParmMenuScriptKwargs, ShelfToolKwargs
import toolutils
from toolutils import OrientInfo as OrientInfo

_Selections: TypeAlias = list[tuple[hou.GeometrySelection, hou.Selector]]
_GeometrySelections: TypeAlias = tuple[hou.OpNode | None, _Selections, hou.SopNode | None]
_BendRegion: TypeAlias = tuple[hou.Vector3, hou.Vector3, hou.Vector3, float]
_ObjFilter: TypeAlias = Callable[[hou.ObjNode | None], hou.ObjNode | None]

# The paint SOP settings buildPaintNode() and buildTextureMaskPaintNode() match and create.
class _PaintParms(TypedDict):
    cdname: str
    overridecd: NotRequired[bool]

class _TextureMaskPaintParms(TypedDict):
    maskname: str

# The keyword arguments of hou.SceneViewer.selectGeometry().
class _SelectGeometryQuery(TypedDict, total=False):
    prompt: str
    sel_index: int
    allow_drag: bool
    quick_select: bool
    use_existing_selection: bool
    initial_selection: str | None
    initial_selection_type: hou.EnumValue[hou.geometryType] | None
    ordered: bool
    geometry_types: Sequence[hou.EnumValue[hou.geometryType]]
    primitive_types: Sequence[hou.EnumValue[hou.primType]]
    allow_obj_sel: bool
    icon: str | None
    label: str | None
    prior_selection_paths: Sequence[str]
    prior_selection_ids: Sequence[str]
    prior_selections: Sequence[hou.Selection]
    allow_other_sops: bool
    consume_selections: bool
    toolbox_templategroup: hou.ParmTemplateGroup | None
    toolbox1_templategroup: hou.ParmTemplateGroup | None
    confirm_existing: bool
    pick_at_obj_level: bool
    select_parm: str | None

# createCustomSelectionSopNodeFilterTool pops these two before passing the rest on.
class _CustomSelectionQuery(_SelectGeometryQuery, total=False):
    parm_name: str
    is_required: bool

def scriptSopFilterTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    nodename: str | None = ...,
    center_on_selection: bool = ...,
    translate_parm_name: str | None = ...,
    connected_selection: bool = ...,
    orient: toolutils.OrientInfo | None = ...,
    exact_node_type: bool = ...,
) -> hou.OpNode | None: ...
def findDeformTypeInputSop(endnode: hou.SopNode) -> hou.SopNode | None: ...
def buildFloatAttribMenu(
    kwargs: ParmMenuScriptKwargs,
    parm_name: str | None = ...,
    attrib_type: hou.EnumValue[hou.attribType] = ...,
    attrib_size: int = ...,
    geo: hou.Geometry | None = ...,
) -> list[str]: ...
def buildSingleStringPointAttribMenu(kwargs: ParmMenuScriptKwargs, parm_name: str, input_id: int | None = ...) -> list[str]: ...
def getGeometrySelections(
    sceneviewer: hou.SceneViewer,
    selectors: Sequence[hou.Selector],
    allow_obj_selection: bool = ...,
    prompt: str | None = ...,
) -> _GeometrySelections: ...
def setGroupParmsOnSopNode(node: hou.SopNode, selector: hou.Selector, selection: hou.GeometrySelection) -> None: ...
def initReusedSopFilterNode(
    reusednode: hou.SopNode,
    selections: Iterable[tuple[hou.GeometrySelection, hou.Selector]],
    container: hou.OpNode,
) -> None: ...
def initNewSopFilterNodeWithOutput(
    branch: bool,
    newnode: hou.SopNode,
    selections: Iterable[tuple[hou.GeometrySelection, hou.Selector]],
    container: hou.OpNode,
    outputnode: hou.SopNode,
    force_keep_original_objects: bool = ...,
) -> None: ...
def initNewSopFilterNode(
    branch: bool,
    newnode: hou.SopNode,
    selections: Iterable[tuple[hou.GeometrySelection, hou.Selector]],
    container: hou.OpNode,
    force_keep_original_objects: bool = ...,
) -> None: ...
def createSopNodeContainer(
    sceneviewer: hou.SceneViewer,
    newobjectname: str,
    merge_context: bool = ...,
    merge_creator: str | None = ...,
) -> hou.OpNode: ...
def createSopNodeFilter(container: hou.OpNode, nodetypename: str, nodename: str | None, exact_node_type: bool) -> hou.SopNode: ...
def createSopNodeGenerator(
    container: hou.OpNode,
    nodetypename: str,
    nodename: str | None,
    merge_context: bool = ...,
    exact_node_type: bool = ...,
) -> hou.SopNode: ...
def genericSopNodeGeneratorTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    nodename: str | None,
    merge_context: bool = ...,
    prompt: str | None = ...,
    exact_node_type: bool = ...,
) -> hou.SopNode: ...
def getSelectors(nodetypename: str, selector_indices: Sequence[int] = ...) -> tuple[hou.Selector, ...] | list[hou.Selector]: ...
def genericSopNodeFilterTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    nodename: str | None,
    isreusable: bool = ...,
    iscapture: bool = ...,
    allow_obj_sel: bool = ...,
    selector_indices: Sequence[int] = ...,
    exact_node_type: bool = ...,
    selection: _GeometrySelections | None = ...,
) -> hou.SopNode: ...
def customSopNodeFilterTool(
    scriptargs: ShelfToolKwargs,
    activepane: hou.SceneViewer,
    nodetypename: str,
    prompt: str | None = ...,
    exact_node_type: bool = ...,
) -> None: ...
def createMergedSelectionSopNodeFilterTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    nodename: str | None,
    selection_query: _SelectGeometryQuery | None = ...,
    empty_string_selects_all: bool = ...,
    group_parm_name: str | None = ...,
    grouptype_parm_name: str | None = ...,
    parms_to_set: Mapping[str, hou.ParmArgType | hou.ParmTupleArgType] | None = ...,
    exact_node_type: bool = ...,
) -> hou.SopNode: ...
def createCustomSelectionSopNodeFilterTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    nodename: str | None,
    selection_queries: Iterable[_CustomSelectionQuery],
    exact_node_type: bool = ...,
) -> list[hou.SopNode]: ...
def genericCaptureTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = ...) -> hou.OpNode: ...
def genericReusableTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = ..., iscapture: bool = ...) -> hou.OpNode: ...
def customStateTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = ...) -> hou.OpNode | None: ...
# The SOP manager types: the tool creates them in the current network, whatever its context, so
# they are not SopNodes (`ropnet` is a RopNode, `matnet` a ShopNode, ...).
_SopManagerType: TypeAlias = Literal[
    "chopnet",
    "kinefx::rop_fbxanimoutput",
    "kinefx::rop_fbxcharacteroutput",
    "kinefx::rop_gltfcharacteroutput",
    "labs::rop_zibravdb_compress::1.0",
    "lopnet",
    "matnet",
    "objnet",
    "rop_alembic",
    "rop_dembones_skinningconverter",
    "rop_fbx",
    "rop_geometry",
    "rop_geometryraw",
    "rop_gltf",
    "rop_gltf::2.0",
    "rop_ml_exampleraw",
    "ropnet",
    "shopnet",
    "sopnet",
    "topnetmgr",
    "vopnet",
    "vopsoptype",
]
@overload
def genericTool(  # type: ignore[overload-overlap]
    scriptargs: ShelfToolKwargs,
    nodetypename: _SopManagerType,
    nodename: str | None = ...,
    isreusable: bool = ...,
    iscapture: bool = ...,
    allow_obj_sel: bool = ...,
    custom: Literal[False] = ...,
    merge_context: bool = ...,
    orient: toolutils.OrientInfo | None = ...,
    exact_node_type: bool = ...,
    force_filter: bool = ...,
    selection: _GeometrySelections | None = ...,
) -> hou.OpNode: ...
@overload
def genericTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    nodename: str | None = ...,
    isreusable: bool = ...,
    iscapture: bool = ...,
    allow_obj_sel: bool = ...,
    custom: Literal[False] = ...,
    merge_context: bool = ...,
    orient: toolutils.OrientInfo | None = ...,
    exact_node_type: bool = ...,
    force_filter: bool = ...,
    selection: _GeometrySelections | None = ...,
) -> hou.SopNode: ...
@overload
def genericTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    nodename: str | None = ...,
    isreusable: bool = ...,
    iscapture: bool = ...,
    allow_obj_sel: bool = ...,
    custom: bool = ...,
    merge_context: bool = ...,
    orient: toolutils.OrientInfo | None = ...,
    exact_node_type: bool = ...,
    force_filter: bool = ...,
    selection: _GeometrySelections | None = ...,
) -> hou.OpNode | None: ...
def genericTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    nodename: str | None = ...,
    isreusable: bool = ...,
    iscapture: bool = ...,
    allow_obj_sel: bool = ...,
    custom: bool = ...,
    merge_context: bool = ...,
    orient: toolutils.OrientInfo | None = ...,
    exact_node_type: bool = ...,
    force_filter: bool = ...,
    selection: _GeometrySelections | None = ...,
) -> hou.OpNode | None: ...
def chooseAndOpenGeoFile(scriptargs: ShelfToolKwargs, click_to_place: bool) -> None: ...
def buildPaintNode(
    previtem: hou.SopNode | hou.SubnetIndirectInput,
    nextnode: hou.OpNode | None,
    parms: _PaintParms,
    props: Mapping[str, float | str | hou.Vector3],
    node_output_index: int = ...,
    next_input_index: int = ...,
    move_new_nodes: bool = ...,
    use_existing: bool = ...,
) -> hou.SopNode: ...
def buildTextureMaskPaintNode(
    skinprevitem: hou.SopNode | hou.SubnetIndirectInput | hou.OpNetworkDot | None,
    previtem: hou.SopNode | hou.SubnetIndirectInput | hou.OpNetworkDot,
    nextnode: hou.OpNode | None,
    parms: _TextureMaskPaintParms,
    props: Mapping[str, float | str | hou.Vector3],
    skin_output_index: int = ...,
    node_output_index: int = ...,
    next_input_index: int = ...,
    move_new_nodes: bool = ...,
    use_existing: bool = ...,
) -> hou.SopNode: ...
def paintObject(
    scriptargs: ShelfToolKwargs,
    object_nodes: Iterable[hou.ObjNode | None],
    attribname: str,
    props: Mapping[str, float | str | hou.Vector3],
    objfilter: _ObjFilter | None = ...,
) -> None: ...
def paintNodeInput(
    scriptargs: ParmActionButtonKwargs,
    node: hou.SopNode,
    inputidx: int,
    attribname: str,
    props: Mapping[str, float | str | hou.Vector3] | None = ...,
    setdisplayflag: bool = ...,
) -> None: ...
def chooseAndPaintObject(
    scriptargs: ShelfToolKwargs,
    attribname: str,
    props: Mapping[str, float | str | hou.Vector3],
    prompt: str | None = ...,
    objfilter: _ObjFilter | None = ...,
) -> None: ...
def chooseAndPaintEaseInObject(
    scriptargs: ShelfToolKwargs,
    attribname: str,
    props: Mapping[str, float | str | hou.Vector3],
    prompt: str | None = ...,
    objfilter: _ObjFilter | None = ...,
) -> None: ...
def chooseAndApplyTexture(
    scriptargs: ShelfToolKwargs,
    attribname: str,
    props: Mapping[str, float | str | hou.Vector3],
    prompt: str | None = ...,
    objfilter: _ObjFilter | None = ...,
) -> None: ...
def buildBlockPair(
    scriptargs: ShelfToolKwargs,
    name: str,
    begintype: str,
    endtype: str,
    wire_to_end: bool,
) -> tuple[hou.OpNode, hou.OpNode]: ...
def buildBlockMetadata(node: hou.OpNode) -> hou.SopNode: ...
def buildBlockBeginCompile(node: hou.OpNode) -> None: ...
def setBendRegionParms(node: hou.OpNode, origin: hou.Vector3, up: hou.Vector3, capdir: hou.Vector3, caplen: float) -> None: ...
def processPositions(
    node: hou.SopNode,
    handlepos: Sequence[hou.Vector3],
    group: str | None = ...,
    grouptype: hou.EnumValue[hou.geometryType] | None = ...,
) -> _BendRegion: ...
def createBendSop(scriptargs: ShelfToolKwargs, nodename: str | None = ...) -> hou.OpNode: ...
def setupBendRegion(
    scriptargs: ShelfToolKwargs | ParmActionButtonKwargs,
    node: hou.SopNode | None,
    group: str | None = ...,
    grouptype: hou.EnumValue[hou.geometryType] | None = ...,
) -> _BendRegion | None: ...
def getItemGeometry(item: hou.SopNode | hou.SubnetIndirectInput, outputindex: int = ...) -> hou.Geometry | None: ...
def addBooleanTool(kwargs: ShelfToolKwargs) -> hou.OpNode | None: ...
def findViewersUV(kwargs: ShelfToolKwargs) -> str: ...
def addUVTool(kwargs: ShelfToolKwargs, nodetype: str, uvattribparm: str) -> hou.OpNode: ...
def buildAttribAdjustFromActionButton(
    kwargs: ParmActionButtonKwargs | ParmCallbackKwargs,
    adjustnodetype: str,
    parms: Mapping[str, Mapping[str, hou.ParmArgType | hou.ParmTupleArgType]],
    use_existing: bool = ...,
) -> hou.SopNode: ...
def addNodeWithCurrentSelection(
    kwargs: ShelfToolKwargs,
    node_type: str,
    allowed_group_types: Container[str] | None = ...,
    group_type_parm: str | None = ...,
    group_parm: str = ...,
    empty_means_all: bool = ...,
    default_group_type: str = ...,
    asterisk_to_select_all: bool = ...,
) -> hou.OpNode: ...
def addPolyBevelTool(kwargs: ShelfToolKwargs) -> hou.OpNode: ...
def addUVFlattenTool(kwargs: ShelfToolKwargs) -> hou.OpNode: ...
def addUVFlattenFromPointsTool(kwargs: ShelfToolKwargs) -> hou.OpNode: ...
def buildRBDConfigureFromActionButton(
    kwargs: ParmActionButtonKwargs,
    parms: Mapping[str, Mapping[str, hou.ParmArgType | hou.ParmTupleArgType]],
    use_existing: bool = ...,
) -> hou.SopNode: ...
def buildRBDConstraintPropertiesFromActionButton(
    kwargs: ParmActionButtonKwargs,
    parms: Mapping[str, Mapping[str, hou.ParmArgType | hou.ParmTupleArgType]],
    use_existing: bool = ...,
) -> hou.SopNode: ...
def computeRange(
    node: hou.SopNode,
    attribnameparm: hou.Parm,
    attribclassparm: hou.Parm,
    groupparm: hou.Parm,
    grouptypeparm: hou.Parm | None = ...,
    inputindex: int = ...,
) -> tuple[float, float] | tuple[None, None]: ...
