import hou
import typing
from _typeshed import Incomplete
from builtins import map as map
from collections.abc import Callable as Callable, Collection, Iterable, Mapping as Mapping, MutableSequence, Sequence
from houtypes import ShelfToolKwargs
from typing import Literal, NamedTuple, Required, Self, TypedDict
from vopcallbacks import ShaderFxCallbacks

from typing import TypeVar
from typing import TypeVar
_NodeT = TypeVar('_NodeT', bound=hou.Node)
class _VopFxMenuKwargs(TypedDict, total=False):
    parm: Required[str]
    node: Required[str]
    input: Required[int]
    toolname: str
    altclick: bool
    ctrlclick: bool
    shiftclick: bool
    cmdclick: bool

class _VopInputPreset(TypedDict, total=False):
    type: Required[Literal['parameter', 'passthrough', 'constant', 'node'] | None]
    node_type: str | None
    node_output: int | str
    node_useexisting: bool
    node_folderlevel: int | None
    parm_name: str | None
    parm_label: str | None
    parm_type: str | None
    parm_useexisting: bool
    parm_invisible: bool
    parm_inheritname: bool
    preset: str | _VopNodePreset | None
    default_value: int | float | str | None
    node_folder: str | None
    node_prefix: str | None

class _VopNodePreset(TypedDict, total=False):
    node_type: str
    name: str
    default: bool
    parent: str
    inputs: dict[str, _VopInputPreset]
    excluded_inputs: Sequence[str]

VOPUI_HOST_PARM: str
VOPUI_USEHOSTFOLDER_PARM: str
VOPUI_USEHOSTPREFIX_PARM: str
VOPUI_FOLDER_PARM: str
VOPUI_PREFIX_PARM: str
VOPUI_MYFOLDER_PARM: str
VOPUI_MYPREFIX_PARM: str

class InputData(NamedTuple):
    inputnode: hou.VopNode
    inputname: str
    inputlabel: str
    inputparmtuple: hou.ParmTuple | None
    outputnode: hou.VopNode | None
    outputname: str | None

class PromotedParmData(NamedTuple('PromotedParmData', [('name', Incomplete), ('folders', Incomplete), ('parm', Incomplete), ('template', Incomplete), ('ref_parm', Incomplete)])):
    name: str
    folders: list[hou.FolderParmTemplate] | str
    parm: hou.Parm | None
    template: hou.ParmTemplate | None
    ref_parm: hou.ParmTuple | None
    def __new__(cls, name: str, folders: list[hou.FolderParmTemplate] | str = '', parm: hou.Parm | None = None, template: hou.ParmTemplate | None = None, ref_parm: hou.ParmTuple | None = None) -> Self: ...

def genericTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, exact_node_type: bool = True) -> hou.OpNode:
    """ Calls the generic tool handler for all nodes, which allows the
        user to lay down a node in the network editor.
    """
def jumpToNode(kwargs: _VopFxMenuKwargs, effect_type: str) -> None: ...

valid_data_types: set[str]

def checkValidParmDataType(data_type: str) -> bool: ...
def insertParmVop(node: hou.VopNode, input_index_or_name: int | str, parm_gen_type: hou.EnumValue[hou.vopParmGenType] = ..., parm_name: str | None = None, parm_label: str | None = None, parm_type: str | None = None, default_value: object = None, move_to_folder: bool = True) -> hou.VopNode | None:
    """ Creates a Parameter VOP for the given input. If the input has a
        corresponding parameter of the same name, all relevant attributes are
        copied over to the Parameter VOP.
    """
def createAllParmVops(node: hou.VopNode, parm_gen_type: hou.EnumValue[hou.vopParmGenType] = ...) -> None: ...
def setDefaultColor(parm_node: hou.OpNode, def_col: Sequence[float]) -> None: ...
def positionItems(target_node: hou.Node, items: tuple[hou.Node, ...]) -> None: ...
def hasNodeAsInputRecursive(node: hou.Node, find_node: hou.Node) -> bool: ...
@typing.overload
def getIndependentSiblingOfType(node: hou.VopNode, node_type: str | None, pool: Iterable[hou.Node] | None = ...) -> hou.VopNode | None: ...
@typing.overload
def getIndependentSiblingOfType(node: hou.OpNode, node_type: str | None, pool: Iterable[hou.Node] | None = ...) -> hou.OpNode | None: ...
@typing.overload
def getIndependentSiblingOfType(node: hou.Node, node_type: str | None, pool: Iterable[hou.Node] | None = ...) -> hou.Node | None: ...
def getInputIndex(node: hou.Node, index_or_name: int | str) -> int: ...
def getOutputIndex(node: hou.Node, index_or_name: int | str) -> int: ...
def getInputName(node: hou.Node, index_or_name: int | str) -> str: ...
def getOutputName(node: hou.Node, index_or_name: int | str) -> str: ...
def getInputLabel(node: hou.Node, index_or_name: int | str) -> str: ...
def getOutputLabel(node: hou.Node, index_or_name: int | str) -> str: ...
def checkHasInput(node: hou.Node, index_or_name: int | str) -> bool: ...
def checkHasOutput(node: hou.Node, index_or_name: int | str) -> bool: ...
def checkInput(node: hou.Node, index_or_name: int | str) -> int: ...
def checkOutput(node: hou.Node, index_or_name: int | str) -> int: ...
def getInputConnector(node: hou.Node, input_index_or_name: int | str) -> hou.NodeConnection | None: ...
@typing.overload
def getInputNode(node: hou.VopNode, input_index_or_name: int | str) -> hou.VopNode | None: ...
@typing.overload
def getInputNode(node: hou.OpNode, input_index_or_name: int | str) -> hou.OpNode | None: ...
@typing.overload
def getInputNode(node: hou.Node, input_index_or_name: int | str) -> hou.Node | None: ...
def getInputNodeOutputIndex(node: hou.Node, input_index_or_name: int | str) -> int | None: ...
def getInputParmTuple(node: hou.VopNode, index_or_name: int | str) -> hou.ParmTuple | None: ...
def setConnection(start_node: hou.OpNode, start_node_output: int | str, end_node: hou.VopNode, end_node_input: int | str, delete_unused: bool = True) -> None: ...
def findExclusiveInputNodes(endnode: hou.Node, endnode_input: int | str | None = None) -> list[hou.Node]:
    """ Recursively finds nodes that only output to 'endnode'. If endnode_input
        is not None, only nodes that only output to that input are returned.
    """
def destroyExclusiveInputNodes(endnode: hou.Node, endnode_input: int | str | None = None) -> None: ...
def replaceInput(node: hou.VopNode, input_index_or_name: int | str, new_input_node: hou.OpNode, output_index_or_name: int | str = 0) -> None:
    """ Sets the new input node, and deletes the existing input node (and it's
        inputs) if they only depended on 'node'.
    """
def addOrReplaceParm(node: hou.OpNode, parm_template: hou.ParmTemplate) -> hou.ParmTuple: ...
def addOrReplaceStringParm(node: hou.OpNode, parm_name: str, parm_label: str, string_type: hou.EnumValue[hou.stringParmType] = ...) -> hou.ParmTuple: ...
def collectParmChain(node: hou.OpNode, parm_name: str, usehost_name: str, separator: str, separator_at_end: bool = False, level: int = 0) -> str: ...
def getPromotionFolder(node: hou.OpNode, input_names: Collection[str] = ..., contributing_nodes: MutableSequence[hou.OpNode] | None = None) -> list[hou.FolderParmTemplate]: ...
def getPromotionFolderString(node: hou.OpNode, input_names: Collection[str] = ..., contributing_nodes: MutableSequence[hou.OpNode] | None = None) -> str: ...
def getParmPromotionFolder(parm_vop: hou.OpNode, contributing_nodes: MutableSequence[hou.OpNode] | None = None) -> list[hou.FolderParmTemplate] | Literal['']:
    """ Returns the folders that a parameter should be promoted to as a
        slash separated string

        This is done by checking which promotion folders the parm's output
        nodes specify. If there is a conflict between the folders on output
        nodes the deepest common folder is returned.

        If contributing_nodes is a list, it will be populated with all
        the nodes that contributed to the folder path.
    """
def getParmPromotionFolderString(parm_vop: hou.OpNode, contributing_nodes: MutableSequence[hou.OpNode] | None = None) -> str: ...
def getPromotionPrefix(node: hou.OpNode) -> str: ...
def createPromotionRefs(node: hou.OpNode) -> None: ...
def addPromotionParms(node: hou.OpNode, ui_host_node: hou.Node | None = None, folder: str | None = None, prefix: str | None = None, use_host_folder: bool = True, use_host_prefix: bool = True) -> None:
    """ Adds parameters which control how parameters are promoted from this
        node.

        The values of the parameters are set according to the arguments passed
        to this procedure.

        These parameters are added to 'node':

        vopui_host            Parameters promoted from 'node' will show up in
                                the folder of this host.

                                Default value: 'ui_host_node'

        vopui_usehostfolder   A toggle that controls whether to append to
                                host folder.

                                Default value: True

        vopui_usehostprefix   A toggle that controls whether to append to
                                host prefix.

                                Default value: True

        vopui_folder            The folder to add parameter.
                                If vopui_usehostfolder is True, this folder
                                will be appended to the host's folder

                                Default value: node.type().description()

        vopui_prefix            The prefix to use for parameters.
                                If vopui_usehostprefix is True, this prefix
                                will be appended to the host's prefix

                                Default value: ''

        vopui_myfolder          This is set up with a python expression which
                                computes the concatenated folder.

        vopui_myprefix          This is set up with a python expression which
                                computes the concatenated prefix.
    """
def getNewParmName(source_node: hou.OpNode, parm_name: str) -> str | None: ...
def translateConditionalNames(cond: str, translate_method: Callable[[str], str | None]) -> str:
    """ Updates the conditional with new parm names

        translate_method should take the old parm name as it's sole argument
        and return the new parm name
    """
def updateParmVopConditionals(parm_nodes: Iterable[hou.OpNode]) -> None:
    """ Replaces parm names in conditionals with the name parameters are
        exposed with.  i.e. with the name of the parm VOP plugged into
        the parameter's input, including it's prefix.
    """
def makeFilterNodePreset(passthrough_input_name: str, excluded_inputs: Sequence[str] = ...) -> _VopNodePreset: ...
def insertFilterNode(target_node: hou.VopNode, input_index_or_name: int | str, orig_input_node: hou.VopNode | None, new_input_node: hou.OpNode, filter_node_type: str, filter_node_input: int | str | None) -> hou.VopNode: ...
def getParmName(parm_vop: hou.OpNode) -> str: ...
def printTable(data: Iterable[Iterable[object]]) -> None: ...
def findCorrectlyPlacedItem(item: PromotedParmData, ptg: hou.ParmTemplateGroup, parm_set: Sequence[PromotedParmData], search_dir: int) -> int: ...
def movePromotedParameters(node: hou.OpNode) -> None:
    """Moves the VOP node's promoted parameters to the folder specified by the
       'In Folder' parameter."""
def moveParameters(ptg: hou.ParmTemplateGroup, parm_set: Sequence[PromotedParmData], included_parm_names: Collection[str] | None = None) -> None: ...
def movePromotedChildParameters(owner_node: hou.OpNode, included_parm_vops: Iterable[hou.OpNode] | None = None) -> None:
    """ Sorts and moves into folders all parameters promoted to this node

        If included_parm_vops is an iterable containing Parameter VOPs, only
        only parameters associated with those Parameter VOPs will be moved.
    """
def getInputData(node: hou.VopNode, input_index_or_name: int | str) -> InputData: ...

class VopInputPresetManager:
    node_presets: list[_VopNodePreset]
    valid_keys: set[str]
    def __init__(self) -> None: ...
    def validatePreset(self, preset: _VopNodePreset) -> None: ...
    def addPreset(self, preset: _VopNodePreset) -> None: ...
    def addPresets(self, presets: Iterable[_VopNodePreset]) -> None: ...
    def addPresetsFromJson(self, json_path: str) -> None: ...
    def filterPresets(self, node_type: str, preset_name: str | None = None, find_default_for_type: bool = False) -> list[_VopNodePreset]:
        """ Finds presets that match node_type and, if specified, the preset
            name.

            If find_default_for_type is True, the preset_name is ignored and
            the preset marked as default for the node_type is returned in a
            list.
        """
    def findPreset(self, node_type: str, preset_name: str | None = None) -> _VopNodePreset | None:
        """ Finds a preset that matches node_type as well as preset_name,
            if preset_name is not None.
        """
    def getPreset(self, node_type: str, preset_name_or_preset: str | _VopNodePreset | None = None) -> _VopNodePreset:
        """ Returns a preset that's already merged on top of all it's parents
        """
    def currentInputUsedByPreset(self, node_type: str, preset_name: str | _VopNodePreset | None) -> bool:
        """ Returns True if the nodes currently connected to the input of 'node'
            would be reused when an input of 'node_type' is created using the
            preset specified by 'preset_name'
        """
    def createInput(self, node: hou.VopNode, input_index_or_name: int | str, passthrough_input: InputData | None = None, type: Literal['parameter', 'passthrough', 'constant', 'node'] | None = 'parameter', node_type: str | None = None, node_output: int | str = 0, node_useexisting: bool = False, node_folderlevel: int | None = None, parm_name: str | None = None, parm_label: str | None = None, parm_type: str | None = None, parm_useexisting: bool = False, parm_invisible: bool = False, parm_inheritname: bool = False, parm_gen_type: hou.EnumValue[hou.vopParmGenType] | None = ..., preset: str | _VopNodePreset | None = None, default_value: int | float | str | None = None, node_folder: str | None = None, node_prefix: str | None = None, recurse: bool = True, replace_existing: bool = True, guard_conditionals: bool = False, add_promotion_parms: bool = False, depth: int = 0) -> tuple[hou.VopNode, ...]: ...
    def getInputPresetFromNodePreset(self, node: hou.Node, inputname: str, preset_name_or_preset: str | _VopNodePreset | None = None) -> _VopInputPreset | None: ...
    def checkNodePresetCreatesInput(self, node: hou.Node, input_index_or_name: int | str, preset_name_or_preset: str | _VopNodePreset | None = None) -> bool: ...
    def createInputUsingPreset(self, node: hou.VopNode, input_index_or_name: int | str, passthrough_input: InputData | None = None, parm_gen_type: hou.EnumValue[hou.vopParmGenType] | None = ..., recurse: bool = True, input_preset: _VopInputPreset | None = None, guard_conditionals: bool = False, replace_existing: bool = True, depth: int = 0) -> tuple[hou.VopNode, ...]: ...
    def createAllInputsFromPreset(self, node: hou.VopNode, passthrough_input: InputData | None = None, parm_gen_type: hou.EnumValue[hou.vopParmGenType] | None = ..., recurse: bool = True, preset_name_or_preset: str | _VopNodePreset | None = None, replace_existing: bool = True, depth: int = 0) -> tuple[hou.VopNode, ...]: ...

def createInputs(node: hou.VopNode, parm_gen_type: hou.EnumValue[hou.vopParmGenType] = ..., preset_name_or_preset: str | _VopNodePreset | None = None) -> None: ...
def autoCreateComputeLighting(shadernode: hou.VopNode) -> None: ...
def findContributingParms(node: hou.OpNode, target_name: str | None = None, _depth: int = 0) -> list[hou.ParmTuple]: ...
def wrapParmInFolder(ptg: hou.ParmTemplateGroup, parm_name: str, folder_label: str) -> None: ...
def findParmsToEmbed(node: hou.OpNode) -> list[PromotedParmData]: ...
def filterParmSetByPresets(parm_set: MutableSequence[PromotedParmData]) -> None: ...
def syncParmTemplateGroupToParmSet(ptg: hou.ParmTemplateGroup, parm_set: Sequence[PromotedParmData]) -> None: ...
def embedInputParms(node: hou.OpNode) -> None: ...
def embedInputParmVops(node: hou.VopNode) -> None: ...
def buildBlockPair(scriptargs: ShelfToolKwargs, name: str, opentype: str, closetype: str, encloseinputs: bool) -> hou.OpNode:
    """ Builds a pair of block nodes, a begin and an end, and links
        them together nicely.
    """
def getInputOfTypeRecursive(node: _NodeT | None, node_type: str, skip_self: bool) -> _NodeT | None: ...
def getInputOfTypeRecursiveHelper(node: _NodeT | None, node_type: str, skip_self: bool, array: tuple[_NodeT, ...]) -> _NodeT | None: ...
def insertParm(node: hou.VopNode, input_name: str, parm_gen_type: hou.EnumValue[hou.vopParmGenType] = ...) -> hou.VopNode: ...
def getInputsRecursive(node: _NodeT | None) -> tuple[_NodeT, ...]: ...
def getInputsRecursiveHelper(node: _NodeT | None, res: tuple[_NodeT, ...], array: tuple[_NodeT, ...]) -> tuple[_NodeT, ...]: ...
def deleteAllInputs(begin_node: hou.Node | None) -> None: ...
def parmVopEffect(kwargs: _VopFxMenuKwargs, effect_type: str, name_prefix: str | None = None, mix_with_existing_type: str | None = None, custom_creator: ShaderFxCallbacks | None = None, parm_gen_type: hou.EnumValue[hou.vopParmGenType] = ...) -> None:
    """ High-level utility function for creating a parm effect where the effect
        filters the parameter animation. It returns the created hou.VopNode.

        kwargs
            A dictionary containing the keyword 'parms', mapping to a
            tuple of hou.Parm objects that is to be affected.

        effect_type
            The type of the effect to create. Note that because some
            of them may involve more than one node, we can't just blindly
            make this the node type to create.

        name_prefix
            The name prefix used for the created node.
    """
def setMtlxRamp(node: hou.VopNode) -> None:
    """Reads in the keys and values of a Ramp parameter on a MaterialX ramp node
    and assigns it to the appropriate values in the MaterialX ramp node
    """

UTILITY_NODES: str
SUBNET_NODES: str
MTLX_TAB_MASK: str
KARMAMTLX_TAB_MASK: str
USDPREVIEW_TAB_MASK: str
INHERIT_DEFAULT_PATH: str
INHERIT_PARM_EXPRESSION: str

def _setupUsdMtlInherits(inherits_default: str = ..., control_parm: bool = True) -> list[hou.ParmTemplate]: ...
def createMaskedMtlXSubnet(kwargs: ShelfToolKwargs, name: str = 'mtlxmaterial', mask: str = ..., folder_label: str = 'MaterialX Builder', render_context: str = 'mtlx') -> hou.OpNode:
    """
    Creates a subnet, configured to be masked for specific VOP nodes, by 
    using the 'tabmenumask' spare parameter.
    """
def createMaskedUsdPreviewSubnet(kwargs: ShelfToolKwargs, name: str = 'usdpreviewsubnet', mask: str = ..., folder_label: str = 'USD Preview Material', render_context: str = '') -> hou.OpNode:
    """
    Creates a subnet, configured to be masked for specific VOP nodes, by 
    using the 'tabmenumask' spare parameter.
    """
