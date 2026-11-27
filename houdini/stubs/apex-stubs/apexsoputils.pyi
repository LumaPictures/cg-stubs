import _apex
import apex.ui.selectionmanager.interface as ssi
import hou
from _typeshed import StrPath as StrPath
from apex import graphops as graphops
from collections.abc import Callable as Callable, Container, Iterable, MutableMapping, Sequence
from houtypes import ParmActionButtonKwargs, ParmCallbackKwargs, ParmMenuScriptKwargs
from hrecipes import rtypes as rtypes
from typing import Literal, NotRequired, TypedDict

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_R = TypeVar('_R')
_ParmValue: TypeAlias = int | float | str | dict[str, str] | hou.Ramp | hou.Geometry | None
_ParmTupleValue: TypeAlias = tuple[int, ...] | tuple[float, ...] | tuple[str, ...] | tuple[hou.Ramp, ...] | tuple[dict[str, str], ...] | tuple[hou.Geometry | None, ...]
_ParmDictValue: TypeAlias = _ParmValue | _ParmTupleValue | hou.Vector2 | hou.Vector3 | hou.Vector4 | hou.Matrix3 | hou.Matrix4 | list[dict[str, '_ParmDictValue']]
_ParmExpression: TypeAlias = str | list[str]
class _PythonSnippetKwargs(TypedDict):
    inputs: dict[int, hou.Geometry]

class _PackedFolderCopyKwargs(_PythonSnippetKwargs):
    keep: int

class _CopyAnimationKwargs(_PythonSnippetKwargs):
    parm_from: str
    parm_to: str
    rig: str
    rename: str
    keep: int
    setactiveclip: NotRequired[int]
    rename_channel_prim: NotRequired[bool]

class _PackArgs(TypedDict):
    geo: hou.Geometry
    path: str
    pack_geo: hou.Geometry
    treat_as_folder: bool
    visible: bool
    existing_paths: set[str]

COMPONENTSCRIPT_TXT_WARNING: str
COMPONENTSCRIPT_TITLE_WARNING: str
COMPONENTSCRIPT_NULL: str
COMPONENTSCRIPT_PARMNODE: str
COMPONENTSCRIPT_NAME_PARM: str
COMPONENTSTRIPT_SOURCE_PARM: str
COMPONENT_GUIDE_SRC_PARM: str
COMPONENT_GUIDE_SRC_PARM2: str
COMPONENTSCRIPT_PARM_BLACKLIST_OLD: list[str]
COMPONENTSCRIPT_PARM_BLACKLIST: list[str]
TAGS_ATTR: str
TRANSFORM_CONTROL_PATH: str
SOURCE_SCRIPT_PROP: str
PARM_SUFFIX: str
INPUT_INDEX: str

class TemplateParm:
    node: hou.OpNode
    name: str
    data: rtypes.ParmTemplateData
    instances: Sequence[int]
    def __init__(self, node: hou.OpNode, parm_name: str, parm_data: rtypes.ParmTemplateData, instances: Sequence[int]) -> None: ...
    def size(self) -> int: ...
    def eval(self) -> _ParmValue | _ParmTupleValue: ...
    def addParmsToDict(self, d: MutableMapping[str, _ParmDictValue]) -> None: ...
    def addExpressionsToDict(self, d: MutableMapping[str, _ParmExpression]) -> None: ...

class TemplateString(TemplateParm):
    def addExpressionsToDict(self, d: MutableMapping[str, _ParmExpression]) -> None: ...

class TemplateFloat(TemplateParm):
    def addParmsToDict(self, d: MutableMapping[str, _ParmDictValue]) -> None: ...

class TemplateGeometry(TemplateParm):
    def addParmsToDict(self, d: MutableMapping[str, _ParmDictValue]) -> None: ...

class TemplateFolder(TemplateParm):
    def addParmsToDict(self, d: MutableMapping[str, _ParmDictValue]) -> None: ...
    def addExpressionsToDict(self, d: MutableMapping[str, _ParmExpression]) -> None: ...

class TemplateMultiparm(TemplateParm):
    def addParmsToDict(self, d: MutableMapping[str, _ParmDictValue]) -> None: ...

PARM_TYPES: dict[str, type[TemplateParm] | Literal[False]]

def dictFromParms(node: hou.OpNode) -> dict[str, _ParmDictValue]: ...
def expressionsFromParms(node: hou.OpNode) -> dict[str, _ParmExpression]: ...
def applyPatch(objnode: hou.OpNode, filename: StrPath) -> None: ...

attrib_from_parm_verb: hou.SopVerb | hou.CopVerb | None

def convertSopGraph(sop_graph: hou.Geometry) -> None: ...
def getBindings(sop_graph: hou.Geometry | None, as_menu: bool = True) -> tuple[str, ...]: ...
def getGeoOutputs(sop_graph: hou.Geometry, as_menu: bool = True) -> list[str]: ...
def getGeoParms(sop_graph: hou.Geometry, as_menu: bool = True) -> list[str]: ...
def getDictAttribNames(geo: hou.Geometry | None, as_menu: bool = True) -> tuple[str, ...]: ...
def viewLog(panel_name: str = 'APEX Script Logging', include_python: bool = False) -> None:
    """opens up a floating pane with a specified pane name and with with the log filter set to apex. """
def viewApexEditor(panel_name: str = 'APEX Network View') -> None:
    """Split the active SceneViewer and show an ApexEditor in the bottom half.

    If an ApexEditor pane named *panel_name* already exists it is brought to
    focus instead of creating a new split.  Falls back to a floating panel if
    no SceneViewer is found.
    """
def viewCharacterPicker(panel_name: str = 'APEX Character Picker') -> None:
    """Open the APEX Character Picker panel."""
def viewAnimCatalog(panel_name: str = 'APEX Animation Catalog') -> None:
    """Open the APEX Animation Catalog panel."""
def copyView(scene_viewer: hou.SceneViewer | None = None) -> None:
    """Create a floating tearoff copy of the current geometry scene viewer."""
def setGraphDefaultsFromGeo(geo: hou.Geometry, parms_geo: hou.Geometry) -> None: ...
def componentParmsFromGraph(kwargs: ParmCallbackKwargs) -> None:
    """loads for the components script nodes the component parameters properly 
    We store it here since we need the function for several sop nodes, 
    :param kwargs: the kwargs for the you node call
    """
def setConstraintProperties(node: hou.SopNode) -> None: ...
def setEffectProperties(node: hou.SopNode) -> None: ...
def setupGraphPortMenuEntries(graph: _apex.Graph, inputs: bool = True, port_types: Container[str] | None = None, node_filter: str | None = None) -> list[str]: ...
def setupCallbackPortMenuEntries(callback: str, inputs: bool = True) -> list[str]: ...
def setupGraphInputMenu(geo: hou.Geometry, inputs: bool = True, blacklist: Container[str] | None = None) -> list[str]:
    """
    build for a graph geometry a menu with all the graph inputs if inputs is set to false then and output menu is being
    built
    """
def inputParmType(kwargs: ParmMenuScriptKwargs, geo: hou.Geometry) -> list[str]:
    """
    build for a graph geometry a menu with all the graph inputs if inputs is set to false then and output menu is being
    built
    """

GUIDE_COMPONENT_LABELS: dict[str, str]

def setupGuideComponentMenu(blacklist: Container[str] | None = None, defaults: Sequence[str] | None = None) -> list[str]:
    """
    build for a graph geometry a menu with all the graph inputs if inputs is set to false then and output menu is being
    built
    """
def setupTagsMenuEntries(geo: hou.Geometry | None = None, node: hou.SopNode | None = None, input_geometry: int = 0, path: str | None = None, pattern: bool = True) -> list[str]:
    """
    build either for a graph or for geometry a node/point tag menu

    :param node: the node the 
    :param input_geometry: _description_
    :param path: _description_, defaults to None
    :param pattern: decides if the current menu entry should be , defaults to 'apex'
    """
def setupControlsMenuEntries(geo: hou.Geometry | None = None, node: hou.SopNode | None = None, input_geometry: int = 0, path: str | None = None, pattern: str = '*') -> list[str]:
    """
    build a control name menu for a rig graph, either from geometry or from a node input

    :param node: the node whose input geometry holds the rig
    :param input_geometry: the node input index to read from
    :param path: packed folder path of the rig, defaults to None
    :param pattern: apex node pattern to filter the controls, defaults to '*'
    """
def setupNameMenuEntries(geo: hou.Geometry | None = None, node: hou.SopNode | None = None, input_geometry: int = 0, path: str | None = None, namedecorator: bool = False, apexpattern: str = '*') -> list[str]:
    """
    build either for a graph or for geometry a node/point name menu

    :param node: the node the 
    :param input_geometry: _description_
    :param path: _description_, defaults to None
    :param pattern: decides if the current menu entry should be , defaults to 'apex'
    """
def setupPackedAttribsMenuEntries(geo: hou.Geometry | None = None, node: hou.SopNode | None = None, input_geometry: int = 0, path: str = '', attrib_cls: hou.EnumValue[hou.attribType] = ..., attrib_type: hou.EnumValue[hou.attribData] = ...) -> tuple[str, ...] | list[str]:
    """
    builds an attrib menu based on either top level geometry or a packed geometry in 
    a packed folder structure
    can either fetch the geo from a node or directy from a geo input
    """
def setupPackedGroupsMenuEntries(geo: hou.Geometry | None = None, node: hou.SopNode | None = None, input_geometry: int = 0, path: str = '', attrib_cls: hou.EnumValue[hou.attribData] = ...) -> tuple[str, ...] | list[str]:
    """
    builds the dropdown menu entries for the attribs of a specific type and class
    for a geo or an element in a geo folder. The geo can be either fetched from a hou.Node or directly
    from a specified geometry
    """
def setupPackedPathsMenuEntries(geo: hou.Geometry | None = None, node: hou.SopNode | None = None, input_geometry: int | None = None, pattern: str = '*', filename: bool = False) -> list[str]:
    """builds the dropdown menu entries of a list of avialiable folders and paths in a given packed folder geometry.
    The geo can be either fetched from a hou.Node or directly from a specified geometry. 
    The pattern can be used to fetch just a subset of elements based on the apex path patterns.
    If filename is set the entries hold only the last path component instead of the full path.
    """
def setupControlShapeMenuEntries(geo: hou.Geometry | None = None, node: hou.SopNode | None = None, parentfolder: str | None = None, library_node: str | None = None) -> list[str]:
    """builds the dropdown menu entries all the available controls shape on a given unpacked character
    geometry. It checks for the standard controls of the transform control but also for the stand 
    The geo can be either fetched from a hou.Node or directly
    from a specified geometry
    """
def extractGraphFromPaths(geo: hou.Geometry, pattern: str | None = None) -> hou.Geometry:
    """checks if a given geo is a packed geometry and gives the option to pick one of the packed geos in that case
    the pattern defaults to graph types"""
def exception_catcher(func: Callable[[ParmCallbackKwargs], _R]) -> Callable[[ParmCallbackKwargs], _R | None]: ...
@exception_catcher
def apexscriptDecompile(kwargs: ParmCallbackKwargs) -> bool:
    """
    decompile function for apex script nodes, decompiles a given defined snippet from an input or a list of input
    sources if a graph has a snipped attrib then the snippet attrib can be used instead of decompiling
    NOTE: all parm names can be overwritten with the input kwargs
    using the given attrib name used with with an __parm appendix in order 
    """
def apexscriptSetHeaderTemplate(kwargs: ParmCallbackKwargs) -> None:
    """
    callback to set the header text propertly for apex script nodes
    """
def apexScriptGraphAsSnippet(kwargs: ParmCallbackKwargs) -> None:
    """
    loads a graph as snippet text for the apex script node. If the graph has no source_script property
    then the option is provided to decompile the given graph. Should the given geometry be a packed folder geo
    then the user can pick which geometry to use from the folder structure
    """
def apexScriptSubgraphAsSnippet(kwargs: ParmCallbackKwargs) -> None:
    """Loads the code from a given subgraph directory as a snippet. 
    NOTE: we do not offer the option to decompile the subgraphs for now only the 
    source_script property on the subgraph lib can be read in. 
    """
def apexScriptTextAsSnippet(kwargs: ParmCallbackKwargs) -> None: ...
def apexScriptSnippetAsText(kwargs: ParmCallbackKwargs) -> None:
    """
    saves the apex script snippet as text with the according configurations to store the header and the parminterface
    """
def offloadSubgraphSnippet(kwargs: ParmCallbackKwargs) -> None:
    """writes the subgraphs snippet as proper subgraphs out to disk"""
def setDefaultConfigControl(kwargs: ParmCallbackKwargs) -> None: ...
def resetAllStashedChanges(node: hou.SopNode) -> None:
    """Button callback for Scene Animate which deletes all stashed changes."""
def resetStashedAnimation(node: hou.SopNode) -> None:
    """Button callback for Scene Animate which deletes stashed animation."""

theClipName: str

def newStashedClip(node: hou.SopNode, clip_name_opt: str | None = None) -> None:
    """Button callback for Scene Animate to create a new animation."""
def resetCustomStashedChanges(node: hou.SopNode) -> None:
    """Button callback for Scene Animate which deletes specific changes."""
def editStashedAnimation(node: hou.SopNode) -> None:
    """Button callback for Scene Animate to edit the scene animation."""
def packedFolderCopySingle(geo: hou.Geometry | None, geo1: hou.Geometry, from_pattern: str, to_pattern: str, keep: bool | int = True, pack_fn: Callable[[_PackArgs], object] | None = None) -> bool:
    """ Do a single packed folder copy operation.

        @geo output geometry were we add the new packed folders/files.

        @geo1 is the geometry that we read the packed folders from.

        @from_pattern The @geo apex pattern given to extractPackedPaths().
         This selects the files to copy from.

        @to_pattern A string replace pattern for the destination

        @keep if False, will delete the 'from_pattern' from the output geometry.
         This makes the copy operation act as a cut/paste.

        @pack_fn is an optional lambda that is called with a single dict arg
         instead of geo.packToFolder(). It can be used to tweak the geometry
         before packing it or to reject the packing based on data inside of
         the attribute. If None, geo.packToFolder() is called. Otherwise, it's
         the lambda's responsability to call it.
    """
def packedFolderCopy(kwargs: _PackedFolderCopyKwargs) -> hou.Geometry:
    """ Packed Folder Copy Python Snippet code."""
def copyAnimation(kwargs: _CopyAnimationKwargs) -> hou.Geometry:
    """ Scene Copy Animation Python Snippet code."""
def sceneMerge(kwargs: _PythonSnippetKwargs) -> hou.Geometry:
    """ Scene Merge Python Snippet code.
        parms['sops{i}'] is special as we have a fixup step in the hda to glob
        the nodes from the parent_node.
    """
def getPathFromParmValue(s: str) -> str: ...
def importAnimations(kwargs: _PythonSnippetKwargs) -> hou.Geometry:
    """ Scene Import Animation Python Snippet code.
        parms['sops{i}'] is special as we have a fixup step in the hda to glob
        the nodes from the parent_node.
    """
def selectAnimationClipGeo(geo: hou.Geometry | None, add_animation_folder: bool = True) -> list[str]:
    """ Returns a list ofr animation from the geo.
    """
def selectAnimationClipCatalog(kwargs: ParmMenuScriptKwargs) -> list[str]:
    """ APEX Scene Import Animation menu script callback for the 'clips' parameter.
    """
def selectAnimationClipFrom(kwargs: ParmMenuScriptKwargs) -> list[str]:
    """ APEX Scene Copy Animation menu script callback for the 'from' parameter.
    """
def selectAnimationClipTo(kwargs: ParmMenuScriptKwargs) -> list[str]:
    """ APEX Scene Copy Animation menu script callback for the 'to' parameter.
    """
def selectActiveClip(kwargs: ParmMenuScriptKwargs) -> list[str]:
    """ APEX Scene Copy Animation menu script callback for the 'active_clip' parameter.
    """
def selectRigPath(kwargs: ParmMenuScriptKwargs) -> list[str]:
    """ APEX Scene Copy Animation menu script callback for the 'rig' parameter.
    """
def selectSceneImportAnimationFrom(kwargs: ParmMenuScriptKwargs) -> list[str] | None:
    """ APEX Scene Import Animation menu script callback for the 'from' parameter.
    """

SCENE_IMPORT_GEO_CACHE: str

def sceneImportAnimationReload(kwargs: ParmCallbackKwargs) -> None: ...
def sceneImportAnimationLoadGeometry(n: hou.OpNode, filename: str) -> hou.Geometry: ...
def selectSceneImportAnimationTo(kwargs: ParmMenuScriptKwargs) -> list[str]:
    """ APEX Scene Import Animation menu script callback for the 'to' parameter.
    """
def selectSceneImportAnimationRenamePath(kwargs: ParmMenuScriptKwargs) -> list[str]:
    """ APEX Scene Import Animation menu script callback for the 'rename#' parameter.
    """
def selectSceneImportAnimationRigPath(kwargs: ParmMenuScriptKwargs) -> list[str] | None:
    """ APEX Scene Import Animation menu script callback for the 'rig#' parameter.
    """
def setSelectedControls(kwargs: ParmActionButtonKwargs, includepath: bool = False, replace: bool = False, pattern: str = '*') -> None:
    """sets the currently selected controls as a parm value

    :param kwargs: the typical parm kwargs
    :param includepath: defines if the full control 
    path is to be used or only the control name, defaults to False
    :param replace: defines if the current parameter is to be replaced or extended. in case of extension, 
    duplicate entries will be accordingly managed
    """
def controlsFromGraph(graph: _apex.Graph, pattern: str = '*', control_group: bool = True, abstract: bool = True, transform: bool = True) -> list[str]:
    """finds all the controls from a graph based on a path pattern, 
    :param control_group: defines if control groups subnets should be inlcuded
    :param abstract: defines if abstract controls hould be included, 
    :param transform: defines if transform controls should be included
    """
def selectionSetFromPattern(sel_set: ssi.SelectionSets, graph: _apex.Graph, rig_path: str, pattern: str, set_path: str, color: hou.Color | None = None, mode: Literal[0, 1, 2] = 0) -> None:
    """creates or modifies a selection based for controls of a graph based on a given input pattern and adds the control 
    to a given selection set folder. any missing parent folder will be automatically created

    :param sel_set: the main selection sets to be modified
    :param graph: the rig graph to fetch the controls from
    :param rig_path: the scene path of the rig
    :param pattern: the apex pattern for the controls of the selection set to be created or modified
    :param set_path: the path to the set that is to be used for the current oepration
    :param color: the color of the selection set, defaults to None
    :param mode: defines if the found controls should be added (0), removed(1) or replaced(2), defaults to 0
    """
def selectionSetsFromTags(sets: ssi.SelectionSets, graph: _apex.Graph, rig_path: str, tags: Iterable[str], colors: Sequence[hou.Vector3], modes: Sequence[Literal[0, 1, 2]] | None = None, paths: Sequence[str] | None = None, use_lods: bool = True, use_subset_lods: bool = True, bodyparts: str = 'bodyparts') -> ssi.SelectionSets:
    """
    adds a series of selection sets based on pre assembled data. this format works well with selection
    set data based on multiparms for example

    :param sets: the selectionsets to be modified
    :param graph: the rig graph to fetch the controls from
    :param rig_path: the scene path of the rig
    :param tags: the collection of apex patterns to be used per selection set to be created
    :param colors: the color matching the index of the tags to be used per set
    :param modes: the operation mode, aka add, remove or replace, to be performed per seleciton sets, 
    if None then all the sets will be simply added
    :param paths: the set paths to be used for all the sets to be added, defaults to None, if not defined 
    the set name matches the tag name and the set name is added under the base folder defined with the 'bodyparts'. kwarg
    :param use_lods: defines if overall LOD sets for the character should be created, defaults to True
    :param use_subset_lods: defines if LOD sub sets are to be created per selection set tag group, defaults to True
    :param bodyparts: defines the name of the main folder where all the tag selectionsets are to 
    be stored under, defaults to 'bodyparts'
    """
def setupSelectionSetMenuEntries(geo: hou.Geometry | None = None, prefix: str = '') -> list[str]:
    """creates a menu with folderpaths for all current selection set folders stored on a given geometry"""
def setActiveClip(geo: hou.Geometry, active_clip: str) -> None:
    """ Set the active_clip on an APEX Scene geometry.
        @geo scene geometry to modify.
        @active_clip the full path to the new active_clip such as
         '/animation/default.clip'
    """
def exportSingleAnimationToFile(geo: hou.Geometry, clip_path: str, filename: str) -> None: ...
def createRopSetup(kwargs: ParmCallbackKwargs) -> None: ...
def exportAnimations(kwargs: ParmCallbackKwargs) -> None: ...
def loadClipsToParms(kwargs: ParmCallbackKwargs) -> None:
    """ Look in the Input geometry and fill all the parameters with the clip
        names.
    """
def loadAllToParms(kwargs: ParmCallbackKwargs) -> None:
    """ Reset everything to load all the clips in a single entry.
    """
def savePackedFoldersToFiles(geo: hou.Geometry, output_path: str, pattern: str = '*', geo_format: str = 'bgeo.sc') -> None:
    """ Extract all the geometries using the pattern and save everything in the
    dst_dir using the packed folder path."""
def loadConfigureCharacterMotionMixerPreset(n: hou.OpNode, preset_name: str) -> None: ...
