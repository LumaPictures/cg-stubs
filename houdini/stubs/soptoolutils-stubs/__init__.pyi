import hou
import toolutils
import typing
from collections.abc import Container, Iterable, Mapping, Sequence
from houtypes import ParmActionButtonKwargs, ParmCallbackKwargs, ParmMenuScriptKwargs, ShelfToolKwargs
from past.utils import old_div as old_div
from toolutils import OrientInfo as OrientInfo
from typing import Literal, NotRequired, TypedDict

from typing import TypeAlias
from collections.abc import Callable
from typing import TypeAlias
_Selections: TypeAlias = list[tuple[hou.GeometrySelection, hou.Selector]]
_GeometrySelections: TypeAlias = tuple[hou.OpNode | None, _Selections, hou.SopNode | None]
_BendRegion: TypeAlias = tuple[hou.Vector3, hou.Vector3, hou.Vector3, float]
_ObjFilter: TypeAlias = Callable[[hou.ObjNode | None], hou.ObjNode | None]
_SopManagerType: TypeAlias = Literal['chopnet', 'kinefx::rop_fbxanimoutput', 'kinefx::rop_fbxcharacteroutput', 'kinefx::rop_gltfcharacteroutput', 'labs::rop_zibravdb_compress::1.0', 'lopnet', 'matnet', 'objnet', 'rop_alembic', 'rop_dembones_skinningconverter', 'rop_fbx', 'rop_geometry', 'rop_geometryraw', 'rop_gltf', 'rop_gltf::2.0', 'rop_ml_exampleraw', 'ropnet', 'shopnet', 'sopnet', 'topnetmgr', 'vopnet', 'vopsoptype']
class _PaintParms(TypedDict):
    cdname: str
    overridecd: NotRequired[bool]

class _TextureMaskPaintParms(TypedDict):
    maskname: str

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

class _CustomSelectionQuery(_SelectGeometryQuery, total=False):
    parm_name: str
    is_required: bool

def scriptSopFilterTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, center_on_selection: bool = False, translate_parm_name: str | None = None, connected_selection: bool = True, orient: toolutils.OrientInfo | None = None, exact_node_type: bool = True) -> hou.OpNode | None:
    """ Creates a new script operator (OTL) that operates on
        existing geometry.  This can be used when no generic tool exists
        for the desired operator.
    """
def findDeformTypeInputSop(endnode: hou.SopNode) -> hou.SopNode | None:
    """ This function does a depth first traversal of the node
        input hierarchy to find the first deform-type node.
        Returns the deform-type node.  Returns None if no such node exists.
    """
def buildFloatAttribMenu(kwargs: ParmMenuScriptKwargs, parm_name: str | None = None, attrib_type: hou.EnumValue[hou.attribType] = ..., attrib_size: int = 1, geo: hou.Geometry | None = None) -> list[str]: ...
def buildSingleStringPointAttribMenu(kwargs: ParmMenuScriptKwargs, parm_name: str, input_id: int | None = None) -> list[str]: ...
def getGeometrySelections(sceneviewer: hou.SceneViewer, selectors: Sequence[hou.Selector], allow_obj_selection: bool = True, prompt: str | None = None) -> _GeometrySelections:
    ''' This function invokes a geometry selection for each
        selector in "selectors".  The selector is not started, but
        its properties are used when calling sceneviewer.selectGeometry().
    '''
def setGroupParmsOnSopNode(node: hou.SopNode, selector: hou.Selector, selection: hou.GeometrySelection) -> None:
    """ Sets the group type and group parameters on the given node
        based on the selection info.
    """
def initReusedSopFilterNode(reusednode: hou.SopNode, selections: Iterable[tuple[hou.GeometrySelection, hou.Selector]], container: hou.OpNode) -> None: ...
def initNewSopFilterNodeWithOutput(branch: bool, newnode: hou.SopNode, selections: Iterable[tuple[hou.GeometrySelection, hou.Selector]], container: hou.OpNode, outputnode: hou.SopNode, force_keep_original_objects: bool = False) -> None: ...
def initNewSopFilterNode(branch: bool, newnode: hou.SopNode, selections: Iterable[tuple[hou.GeometrySelection, hou.Selector]], container: hou.OpNode, force_keep_original_objects: bool = False) -> None: ...
def createSopNodeContainer(sceneviewer: hou.SceneViewer, newobjectname: str, merge_context: bool = False, merge_creator: str | None = None) -> hou.OpNode:
    """ Creates a scene level object node to contain a new SOP node.
        This function may return an existing object node if the Model in
        Context option is turned on, or the merge_context parameter is
        set to True.
    """
def createSopNodeFilter(container: hou.OpNode, nodetypename: str, nodename: str | None, exact_node_type: bool) -> hou.SopNode:
    """ Creates a SOP node that takes an input. """
def createSopNodeGenerator(container: hou.OpNode, nodetypename: str, nodename: str | None, merge_context: bool = False, exact_node_type: bool = True) -> hou.SopNode:
    """ Creates a SOP node that doesn't require an input. If the container
        already has nodes, this new SOP may be merged with the existing SOPs.
    """
def genericSopNodeGeneratorTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None, merge_context: bool = False, prompt: str | None = None, exact_node_type: bool = True) -> hou.SopNode:
    """ A generic tool for instantiating SOP generator nodes such as Box and
        Sphere. The user is prompted to select a location in the viewport if
        the tool was not invoked with the Ctrl key. The new SOP may be merged
        into an existing scene level object depending onthe merge_context
        parameter value.
    """
def getSelectors(nodetypename: str, selector_indices: Sequence[int] = ...) -> tuple[hou.Selector, ...] | list[hou.Selector]:
    """ Gets the node type to extract selector information
    """
def genericSopNodeFilterTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None, isreusable: bool = False, iscapture: bool = False, allow_obj_sel: bool = True, selector_indices: Sequence[int] = ..., exact_node_type: bool = True, selection: _GeometrySelections | None = None) -> hou.SopNode:
    """ A generic tool for creating a SOP node that takes another SOP node
        as input. The user is prompted for selections based on the selector
        bindings set in the OPbindings file.
    """
def customSopNodeFilterTool(scriptargs: ShelfToolKwargs, activepane: hou.SceneViewer, nodetypename: str, prompt: str | None = None, exact_node_type: bool = True) -> None: ...
def createMergedSelectionSopNodeFilterTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None, selection_query: _SelectGeometryQuery | None = None, empty_string_selects_all: bool = True, group_parm_name: str | None = None, grouptype_parm_name: str | None = None, parms_to_set: Mapping[str, hou.ParmArgType | hou.ParmTupleArgType] | None = None, exact_node_type: bool = True) -> hou.SopNode:
    """ Create a sop node for the given node type, name, and selection query.

        :param selection_query: A dictionary of keyword arguments to
            SceneViewer.selectGeometry() used to make the geometry selection.
        :param empty_string_selects_all: Whether an empty string represents
            everything being selected. If false, will use an asterisk when
            everything is selected.
        :param group_parm_name: The name of the group parameter. By default uses 'group'.
        :param grouptype_parm_name: The name of the group type parameter. By default uses 'grouptype'.
        :param params_to_set: A dictionary of parmeter name to value mappings to set on
            the created sop node.
        :param exact_node_type: See 'exact_node_type' on genericTool().
    """
def createCustomSelectionSopNodeFilterTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None, selection_queries: Iterable[_CustomSelectionQuery], exact_node_type: bool = True) -> list[hou.SopNode]:
    """ Creates sop nodes(s) for the given node type and selection queries.
        selection_queries is a list of dictionaries, where each dictionary
        corresponds to the argument list of SceneViewer.selectGeometry plus
        the additional keys 'parm_name', which is the name of the group
        parameter corresponding to the selection, and 'is_required', which
        specifies if the selection is required.
        Returns the list of sop nodes created.
    """
def genericCaptureTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None) -> hou.OpNode:
    """ Invokes a generic capture-type SOP tool. """
def genericReusableTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, iscapture: bool = False) -> hou.OpNode:
    """ Invokes a generic reusable SOP tool.
        If iscapture is True, then the tool is considered to be a capture-type
        tool.  Capture-type tools will attempt to create new nodes before
        any deform-type SOPs in the network.
    """
def customStateTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None) -> hou.OpNode | None:
    """ Invokes a custom SOP tool. This differs from genericTool() in that the
        custom state has custom selectors. For filters, we prompt for a single
        object, then enter into it before entering the custom state.
    """
@typing.overload
def genericTool(scriptargs: ShelfToolKwargs, nodetypename: _SopManagerType, nodename: str | None = ..., isreusable: bool = ..., iscapture: bool = ..., allow_obj_sel: bool = ..., custom: Literal[False] = ..., merge_context: bool = ..., orient: toolutils.OrientInfo | None = ..., exact_node_type: bool = ..., force_filter: bool = ..., selection: _GeometrySelections | None = ...) -> hou.OpNode: ...  # type: ignore[overload-overlap]
@typing.overload
def genericTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = ..., isreusable: bool = ..., iscapture: bool = ..., allow_obj_sel: bool = ..., custom: Literal[False] = ..., merge_context: bool = ..., orient: toolutils.OrientInfo | None = ..., exact_node_type: bool = ..., force_filter: bool = ..., selection: _GeometrySelections | None = ...) -> hou.SopNode: ...
@typing.overload
def genericTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = ..., isreusable: bool = ..., iscapture: bool = ..., allow_obj_sel: bool = ..., custom: bool = ..., merge_context: bool = ..., orient: toolutils.OrientInfo | None = ..., exact_node_type: bool = ..., force_filter: bool = ..., selection: _GeometrySelections | None = ...) -> hou.OpNode | None: ...
def chooseAndOpenGeoFile(scriptargs: ShelfToolKwargs, click_to_place: bool) -> None:
    """ Opens a file chooser that allows the user to select a geometry file(s).
    For each chosen file, a File SOP node is created to open that file.
    The 'click_to_place' determines whether the user needs to click on the
    construction plane to place the geometry, or whether it will be placed
    automatically at the world origin."""
def buildPaintNode(previtem: hou.SopNode | hou.SubnetIndirectInput, nextnode: hou.OpNode | None, parms: _PaintParms, props: Mapping[str, float | str | hou.Vector3], node_output_index: int = 0, next_input_index: int = 0, move_new_nodes: bool = True, use_existing: bool = True) -> hou.SopNode:
    """ Finds a paint node at or prior to node which matches parms.
        If not found, builds one.  If the attribute does not exist,
        creates the attribute to paint.
        It will be inserted prior to nextnode if not none.
    """
def buildTextureMaskPaintNode(skinprevitem: hou.SopNode | hou.SubnetIndirectInput | hou.OpNetworkDot | None, previtem: hou.SopNode | hou.SubnetIndirectInput | hou.OpNetworkDot, nextnode: hou.OpNode | None, parms: _TextureMaskPaintParms, props: Mapping[str, float | str | hou.Vector3], skin_output_index: int = 0, node_output_index: int = 0, next_input_index: int = 0, move_new_nodes: bool = True, use_existing: bool = True) -> hou.SopNode:
    """ Finds a texture mask paint node at or prior to node which matches parms.
        If not found, builds one.
        It will be inserted prior to nextnode if not none.
    """
def paintObject(scriptargs: ShelfToolKwargs, object_nodes: Iterable[hou.ObjNode | None], attribname: str, props: Mapping[str, float | str | hou.Vector3], objfilter: _ObjFilter | None = None) -> None:
    """ Paints an attribute on an object node. Loops through object_nodes and
        uses the first paintable object (it must have a valid display node).
        Existing Paint SOPs will be reused. If none is found, an Attribute
        Create SOP (if necessary) and a Paint SOP will be appended.
    """
def paintNodeInput(scriptargs: ParmActionButtonKwargs, node: hou.SopNode, inputidx: int, attribname: str, props: Mapping[str, float | str | hou.Vector3] | None = None, setdisplayflag: bool = False) -> None:
    """ Paints an attribute on node's inputidx-th input, provided it exists.
        Existing Paint SOPs will be reused. If none is found, an Attribute
        Create SOP (if necessary) and a Paint SOP will be inserted
        between the given node and the said input.
    """
def chooseAndPaintObject(scriptargs: ShelfToolKwargs, attribname: str, props: Mapping[str, float | str | hou.Vector3], prompt: str | None = None, objfilter: _ObjFilter | None = None) -> None:
    """ Interactively selects an object in which to paint an attribute and
        enters the paint state.  Existing Paint SOPs will be reused.
        Otherwise, an Attribute Create SOP (if necessary) and a Paint SOP will
        be appended.
    """
def chooseAndPaintEaseInObject(scriptargs: ShelfToolKwargs, attribname: str, props: Mapping[str, float | str | hou.Vector3], prompt: str | None = None, objfilter: _ObjFilter | None = None) -> None:
    """ Interactively selects an object in which to paint an attribute with
        ease-in and ease-out properties.
    """
def chooseAndApplyTexture(scriptargs: ShelfToolKwargs, attribname: str, props: Mapping[str, float | str | hou.Vector3], prompt: str | None = None, objfilter: _ObjFilter | None = None) -> None:
    """ Interactively selects an object to apply fluid map operator on
    """
def buildBlockPair(scriptargs: ShelfToolKwargs, name: str, begintype: str, endtype: str, wire_to_end: bool) -> tuple[hou.OpNode, hou.OpNode]:
    """ Builds a pair of block nodes, a begin and an end, and links
        them together nicely.

        wire_to_end means to wire to second input on node creation.
    """
def buildBlockMetadata(node: hou.OpNode) -> hou.SopNode:
    """ Creates a metadata import node pointed to ourself
        next to ourself.
    """
def buildBlockBeginCompile(node: hou.OpNode) -> None:
    """ Creates a begin compile block node 
        next to ourself.
    """
def setBendRegionParms(node: hou.OpNode, origin: hou.Vector3, up: hou.Vector3, capdir: hou.Vector3, caplen: float) -> None:
    """ Sets the bend region parameters on a Bend node
    """
def processPositions(node: hou.SopNode, handlepos: Sequence[hou.Vector3], group: str | None = None, grouptype: hou.EnumValue[hou.geometryType] | None = None) -> _BendRegion:
    """ Given two (or fewer) 3D vectors representing the bend
        region, returns the relevant vectors, such as the
        origin and direction of the region
    """
def createBendSop(scriptargs: ShelfToolKwargs, nodename: str | None = None) -> hou.OpNode: ...
def setupBendRegion(scriptargs: ShelfToolKwargs | ParmActionButtonKwargs, node: hou.SopNode | None, group: str | None = None, grouptype: hou.EnumValue[hou.geometryType] | None = None) -> _BendRegion | None:
    """ Sets the capture region based on either user selection
        or cooks the node and sets the capture region to encompass
        its bounding box.
    """
def getItemGeometry(item: hou.SopNode | hou.SubnetIndirectInput, outputindex: int = 0) -> hou.Geometry | None:
    """ Gets the geometry from the specified item's output index.

        If 'item' is a hou.SubnetIndirectInput, the parent subnet's connections
        are traversed until we find an actual node. We return None if we end up
        at an unconnected input.

        In the case of indirect inputs, the specified 'outputindex' is ignored,
        since the is no such concepts with indirect inputs. However, the
        traversal of the parent subnet's input connections may arrive at a
        node via an outputindex other than 0, in which case the geometry
        corresponding to that output is returned.
    """
def addBooleanTool(kwargs: ShelfToolKwargs) -> hou.OpNode | None: ...
def findViewersUV(kwargs: ShelfToolKwargs) -> str:
    """ Find the active viewer and return its uv attribute name.
        If no viewer, return 'uv'
    """
def addUVTool(kwargs: ShelfToolKwargs, nodetype: str, uvattribparm: str) -> hou.OpNode:
    """ Generically adds the given nodetype, returning the resulting SOP.
        The uvattribparm is a parameter that can be filled in with
        the viewer's current UV selection if this was put down in the
        viewport.
    """
def buildAttribAdjustFromActionButton(kwargs: ParmActionButtonKwargs | ParmCallbackKwargs, adjustnodetype: str, parms: Mapping[str, Mapping[str, hou.ParmArgType | hou.ParmTupleArgType]], use_existing: bool = True) -> hou.SopNode:
    """ Builds an Attribute Adjust node using the given parameters. Returns the
        Attribute Adjust node.

        :param kwargs: kwargs passed down from the Action Button script.
        :param adjustnodetype: The node type of Attribute Adjust. (attributeadjustfloat,
                                                                   attributeadjustfinteger,
                                                                   attributeadjustvector)
        :param parms: a dict of parms to set. Expected format:

                        myparms = { 'parms': { 'attrib': 'pscale',
                                               'operation': 'set',
                                               'valuetype': 'range',
                                            }
                                }

        :param use_existing: Checks for upstream Adjust nodes with Attribute
                Name parameter. If one exists, it will select it, rather than
                create a new Adjust node.
    """
def addNodeWithCurrentSelection(kwargs: ShelfToolKwargs, node_type: str, allowed_group_types: Container[str] | None = None, group_type_parm: str | None = None, group_parm: str = 'group', empty_means_all: bool = True, default_group_type: str = 'guess', asterisk_to_select_all: bool = False) -> hou.OpNode:
    ''' runs the genericTook(kwargs, node_type) but also sets the group parameter
        (and optionally grouptype parameter) using the current viewport selection.
        
        :param kwargs: kwargs passed down from the Action Button script.
        :param node_type: the type of the node to be created. 
        :param group_parm: name of the node parameter that holds the group 
                    expression
        :param alllowed_group_type: if not None, it restricts the group types
                    for the existing selection that can be used. For example,
                    it can be set to { \'prims\', \'points\', \'edges\', \'vertices\', 
                    \'breakpoints\' }
                    (which is the same as not setting it at all) or any subset 
                    of it. 
        :param group_type_parm: if the node has a group_type parameter it can
                    be specified here and it will be set according to the 
                    current selection. 
        :param empty_means_all: if set to False, an empty selection is 
                    reflected as "!*" instead of an empty string. 
        :param default_group_type: if selection carries no group type 
                    information but group_type_parm is specified, the value
                    of the group_type_parm is set to this default value.
    '''
def addPolyBevelTool(kwargs: ShelfToolKwargs) -> hou.OpNode: ...
def addUVFlattenTool(kwargs: ShelfToolKwargs) -> hou.OpNode: ...
def addUVFlattenFromPointsTool(kwargs: ShelfToolKwargs) -> hou.OpNode: ...
def buildRBDConfigureFromActionButton(kwargs: ParmActionButtonKwargs, parms: Mapping[str, Mapping[str, hou.ParmArgType | hou.ParmTupleArgType]], use_existing: bool = True) -> hou.SopNode:
    """ Builds an RBD Configure node using the given parameters. Returns the created node.

        :param kwargs: kwargs passed down from the Action Button script.

        :param parms: a dict of parms to set. Expected format:

                        myparms = { 'parms': { 'attrib': 'pscale',
                                               'operation': 'set',
                                               'valuetype': 'range',
                                            }
                                }

        :param use_existing: Checks for downstream RBD Configure nodes. 
                If one exists, it will select it, rather than
                create a new node.
    """
def buildRBDConstraintPropertiesFromActionButton(kwargs: ParmActionButtonKwargs, parms: Mapping[str, Mapping[str, hou.ParmArgType | hou.ParmTupleArgType]], use_existing: bool = True) -> hou.SopNode:
    """ Builds an RBD Constraint Poperties node using the given parameters. Returns the created node.

        :param kwargs: kwargs passed down from the Action Button script.

        :param parms: a dict of parms to set. Expected format:

                        myparms = { 'parms': { 'attrib': 'pscale',
                                               'operation': 'set',
                                               'valuetype': 'range',
                                            }
                                }

        :param use_existing: Checks for downstream RBD Constraint Properties nodes. 
                If one exists, it will select it, rather than
                create a new node.
    """
def computeRange(node: hou.SopNode, attribnameparm: hou.Parm, attribclassparm: hou.Parm, groupparm: hou.Parm, grouptypeparm: hou.Parm | None = None, inputindex: int = 0) -> tuple[float, float] | tuple[None, None]:
    """ Computes and returns the min and max values of an attribute using sop verbs.

        :param inputgeo: the geometry object to use for computing the range.

        :param attribnameparm: the parameter object that contains the name of the attribute to compute.

        :param attribclassparm: the parameter object that tells the class of the attribute to compute.

        :param groupparm: the parameter object that contains the group to use to compute. 

        :param grouptypeparm: the parameter obejct that tells the group type. If none given the attribclassparm will be used instead.

    """
