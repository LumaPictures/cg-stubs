# Houdini stubs generated from Houdini 22.0.466

import hou
import toolutils
from PySide6 import QtCore
from collections.abc import Iterable, Sequence
from houtypes import ParmActionButtonKwargs, ShelfToolKwargs
from pxr import Sdf
from sceneviewerhooks import _MoveSelectionKwargs
from typing import Literal, TypedDict

class _LightMixerMenuKwargs(TypedDict):
    node: hou.LopNode
    indexes: Sequence[QtCore.QModelIndex]

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

@toolutils.reformatPermissionErrors
def genericTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, clicktoplace: bool | None = None, exact_node_type: bool = True, selection_parm_name: str | None = None, selection_allow_pattern: bool | None = None, treat_generator_as_filter: bool = False, allow_instance_proxies: bool = False, point_instances: int = ...) -> hou.OpNode:
    """ Delegates the creation of an lop node. In a network editor, the
        standard node creation tool is used. In a scene viewer, it delegates
        to genericLopGeneratorTool or genericLopFilterTool
        depending on whether or not the lop node type requires inputs.
    """
def genericGeneratorTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, clicktoplace: bool | None = None, prompt: str | None = None, exact_node_type: bool = True) -> hou.LopNode:
    """ Creates a LOP generator node. The node is either created at the
        origin, or asks the user to select a location in the viewport
        depending on the value of the clicktoplace parameter.
    """
def genericFilterTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, prompt: str | None = None, exact_node_type: bool = True, selection_parm_name: str | None = None, selection_allow_pattern: bool | None = None, allow_instance_proxies: bool = False, point_instances: int = ...) -> hou.LopNode:
    """ Creates a node that requires other nodes as input. """
def createLopNode(container: hou.LopNetwork | hou.LopNode, nodetypename: str, inputnodes: Iterable[hou.LopNode | None], nodename: str | None, exact_node_type: bool = True, primstring: str | None = None, selection_parm_name: str = 'primpattern', respect_insertion_point: bool = True, replace_inputs_outputs: bool = True) -> hou.LopNode:
    """ Creates a LOP node inside the specified container network. """
def getToolCategoryForPane(pane: hou.PathBasedPaneTab) -> hou.NodeTypeCategory | None: ...
def getLopNodeContainer(cwd: hou.OpNode) -> hou.LopNetwork | hou.LopNode | None:
    """ Returns the closest ancestor that can contain LOPs. If one isn't found
        in the hierarchy this returns hou.node('/stage').
    """
def buildBlockPair(scriptargs: ShelfToolKwargs, name: str, begintype: str, endtype: str, which_input: int, keep_end_input: bool) -> tuple[hou.OpNode, hou.OpNode]:
    """ Builds a pair of block nodes, a begin and an end, and links
        them together nicely.

        which_input is the index of the input on the end node to which we
        should connect the begin node.
    """
def createPointInstancer(kwargs: ShelfToolKwargs, node_name: str, method: str, sourcemode: str = 'first') -> None: ...
def saveViewToCamera(viewport: hou.GeometryViewport, cam_lop: hou.LopNode) -> None: ...
def saveViewXformToCamera(viewport: hou.GeometryViewport, xform: hou.Matrix4, cam_lop: hou.LopNode) -> None: ...
def setTranslateAndRotate(lop: hou.OpNode, xform: hou.Matrix4) -> None: ...
def genericCameraLightTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, clicktoplace: bool | None = None, lock_to_view: bool = True) -> hou.OpNode:
    """ A generic function for creating Camera or Light nodes of
        various types. This tool handles the initialization of the node
        transforms to match the current view if the Ctrl key was used to
        invoke the tool.
    """
def initConstraints(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str, inputs: Sequence[str], targets: Sequence[str], lookat: Sequence[str], upvector: Sequence[str], keep_offset: bool = False) -> hou.OpNode: ...
def constraintparentStateToolApply(scriptargs: ShelfToolKwargs, input_nodes: Sequence[str], target_nodes: Sequence[str], keep_offset: bool = False) -> hou.OpNode:
    """Parent Constraint Shelf Tool without Picking session"""
def constraintparentStateTool(kwargs: ShelfToolKwargs) -> None:
    """Parent Constraint Shelf Tool"""
def constraintpinStateToolApply(scriptargs: ShelfToolKwargs, input_nodes: Sequence[str], target_nodes: Sequence[str], keep_offset: bool = False) -> hou.OpNode:
    """Pin Constraint Shelf Tool without Picking session"""
def constraintpinStateTool(kwargs: ShelfToolKwargs) -> None:
    """Pin Constraint Shelf Tool"""
def constraintalignStateToolApply(scriptargs: ShelfToolKwargs, input_nodes: Sequence[str], target_nodes: Sequence[str], keep_offset: bool = False) -> hou.OpNode:
    """Align Constraint Shelf Tool without Picking session"""
def constraintalignStateTool(kwargs: ShelfToolKwargs) -> None:
    """Align Constraint Shelf Tool"""
def constraintlookatStateToolApply(scriptargs: ShelfToolKwargs, input_nodes: Sequence[str], target_nodes: Sequence[str], lookup_nodes: Sequence[str], keep_offset: bool = False) -> hou.OpNode:
    """Look At Constraint Shelf Tool without Picking session"""
def constraintlookatStateTool(kwargs: ShelfToolKwargs) -> None:
    """Look At Constraint Shelf Tool"""
def constraintpathStateToolApply(scriptargs: ShelfToolKwargs, input_nodes: Sequence[str], target_nodes: Sequence[str], lookat_nodes: Sequence[str], lookup_nodes: Sequence[str], keep_offset: bool = False) -> hou.OpNode:
    """Path Constraint Shelf Tool without Picking session"""
def constraintpathStateTool(kwargs: ShelfToolKwargs) -> None:
    """Path Constraint Shelf Tool"""
def constraintsurfaceStateToolApply(scriptargs: ShelfToolKwargs, input_nodes: Sequence[str], target_nodes: Sequence[str], lookat_nodes: Sequence[str], lookup_nodes: Sequence[str], keep_offset: bool = False) -> hou.OpNode:
    """Surface Constraint Shelf Tool without Picking session"""
def constraintsurfaceStateTool(kwargs: ShelfToolKwargs) -> None:
    """Surface Constraint Shelf Tool"""
def constraintpointsStateToolApply(scriptargs: ShelfToolKwargs, input_nodes: Sequence[str], target_nodes: Sequence[str], lookat_nodes: Sequence[str], lookup_nodes: Sequence[str], keep_offset: bool = False) -> hou.OpNode:
    """Points Constraint Shelf Tool without Picking session"""
def constraintpointsStateTool(kwargs: ShelfToolKwargs) -> None:
    """Points Constraint Shelf Tool"""
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
def getLightParent(lightmixer_node: hou.LopNode, create: bool = False) -> hou.LopNode | None:
    """ Get the subnet that the new light will be created in.
    """
def createLightSubnet(lightmixer_node: hou.LopNode) -> hou.LopNode: ...
def insertLight(insertionnode: hou.LopNode, lighttype: Literal['domelight', 'distantlight', 'cylinderlight', 'disklight', 'pointlight', 'rectanglelight', 'spherelight'] | None = None, lightnodetype: str | None = None, name: str | None = None, openparmeditor: bool = False, parentprimpath: str | None = None) -> hou.LopNode:
    '''
    insertionnode: Specify the node before which the light will be created.

    lighttype: Specify either "domelight", "distantlight", "cylinderlight", "disklight", "pointlight", "rectanglelight", "spherelight" for a built-in light of the specified type and shape.

    lightnodetype: Overrides the node type to be created. If not None, will ignore the lighttype argument.

    name: Specify a name for the light. Will default to using the lightnodetype if supplied or the lighttype otherwise.

    openparmeditor: Opens and pins a floating parm editor pane focused on the newly created light.
    '''
def duplicateLight(kwargs: _LightMixerMenuKwargs, primpath: str) -> None: ...
def getExistingNodeToEdit(nodetype: str, selection: Iterable[str | Sdf.Path] | None, testnode: hou.OpNode | None) -> hou.LopNode | None: ...
def referenceTestAsset(node: hou.OpNode | None = None, assetname: str | None = None) -> None: ...
def getFileNodeTypeName() -> Literal['sublayer', 'reference::2.0', 'assetreference'] | None: ...

theQuickCOPNetParmName: str
theQuickCOPNetParmLabel: str
theVopCopSignatures: dict[str, str]

def createCopTextureForShader(kwargs: ParmActionButtonKwargs) -> None:
    """
    Sets up a COP Network and placeholder pattern for a given shader node.
    """
def setupCopNetForMap(node: hou.OpNode | None = None, parm: hou.ParmTuple | None = None, kwargs: ParmActionButtonKwargs | None = None, file_suffix: str = '_file') -> None:
    """
    Action buttons attached to texture map inputs on quick materials, which creates an op: path to a COP node. 
    """

theSpecializeNewMaterialBaseParmDS: str
theSpecializedMaterialNodeSuffix: str

def specializeNewMaterials(kwargs: _ScenegraphMenuKwargs, suffix: str = ...) -> None:
    """
    Creates a new, specialized material from an existing base material. This
    function is invoked from the Scene Graph Tree, when right-clicking a material
    primitive.
    """

theKarmaLensMaterialParmDS: str
theKarmaLensMaterialFilePath: str

def createKarmaLensMaterial(node: hou.OpNode | None = None, kwargs: _LopNodeKwargs | None = None, ref_file_path: str = ...) -> None:
    """
    References the Karma Lens Material into LOPs.
    """
def setupKarmaCameraLensMaterial(kwargs: ParmActionButtonKwargs) -> None:
    """
    Camera LOP's have a shortcut button in Karma's folder, that calls this functioin to setup a lens material.
    """
def setupKarmaGlobalAOVMaterial(kwargs: ParmActionButtonKwargs) -> None:
    """
    Karma Render Settings have a shortcut button in the Image folder that
    calls this function to set up a Global AOV material.
    Creates a Material Library LOP containing a Karma MaterialX subnet with
    an unlit surface shader, then links it to the globalaovmaterial parm.
    """
def getStateToMoveSelection(kwargs: _MoveSelectionKwargs) -> dict[str, str | None]: ...
def getAdditionalRenderVars() -> list[dict[str, str]]:
    """Returns a list of dicts describing the default Karma AOVs to populate the Additional Render Vars LOP multi-parm"""
def getAdditionalRenderVarsMenu() -> list[str]: ...

theDefaultTestSceneCameraPath: str

def createTestSceneToolFromRecipe(kwargs: ShelfToolKwargs, recipe: str | None) -> None: ...
