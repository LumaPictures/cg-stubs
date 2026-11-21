# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Sequence
from hrecipes import rtypes
from hrecipes.api import Ref
from typing import Any

__all__ = ['dataFromParms', 'selectedItemsAsData', 'itemsAsData', 'createItemsFromData', 'clusterItemsAsData', 'createClusterItemsFromData', 'saveNodePresetRecipe', 'applyNodePresetRecipe', 'saveDecorationRecipe', 'applyDecorationRecipe', 'saveToolRecipe', 'applyToolRecipe', 'saveTabToolRecipe', 'applyTabToolRecipe', 'dataFromRecipe']

def dataFromParms(parms: Sequence[hou.ParmTuple], **parms_opts: Any) -> rtypes.ParmDataDict:
    """
dataFromParms(parms: Sequence[hou.ParmTuple], values: bool=True,
evaluate_values: bool=False, locked: bool=True, brief: bool=True,
multiparm_instances: bool=True, metadata: bool=False, verbose:
bool=False) -> dict[str,Any]

    Returns a JSON-like data structure representing the given list of
    hou.ParmTuple objects from a node.


    parms
        A list of hou.ParmTuple or hou.Parm instances from a node to
        save.

    values
        If this is True, the capture process saves the values of the
        parameters.

    evaluate_values
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    locked
        If this is True, the capture process saves the locked state of
        the parameters.

    brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    multiparm_instances
        If this is True, the capture processes multiparm instances of
        multiparm parent parameters.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

"""
def selectedItemsAsData(**items_opts: Any) -> rtypes.NetworkItemDataDict | None:
    '''
selectedItemsAsData(nodes_only: bool=False, children: bool=True,
editables: bool=True, inputs: bool=True, position: bool=True,
anchor_position: hou.Vector2=hou.Vector2(0, 0), flags: bool=True, parms:
bool=True, parms_as_brief: bool=True, default_parmvalues: bool=False,
evaluate_parmvalues: bool=False, parmtemplates: str="spare_only",
metadata: bool=False, verbose: bool=False) -> dict[str, Any]

    Returns a JSON-like data structure representing the currently
    selected network items.


    nodes_only
        If this is True, the capture process only saves nodes, ignoring
        sticky notes, network boxes, and dots.

    children
        If this is False, the capture process only saves the top level
        nodes, ignoring nodes inside subnets and unlocked assets.

    editables
        If this is False, the capture process ignores nodes inside
        editable dive target networks inside assets.

    inputs
        If this is True, the capture process saves input connections.

    position
        If this is True, the capture process saves the position of each
        network item in the network editor.

    anchor_position
        The reference position used to record positions of all items.

    flags
        If this is True, the capture process saves flag states.

    parms
        If this is True, based on default_parmvalues argument, the
        capture process saves any non-default parameter values or all
        parameter values. If this is False, no parameters are saved.
        Alternatively, to save a custom set of parameter values you can
        specify a list of hou.ParmTuple or hou.Parm instances, or
        strings representing names of parameters to capture.

    parms_as_brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    default_parmvalues
        Normally, when parms is True, the capture process only saves
        parameters with non-default values. If this is True, the capture
        process also saves parameters set to the default value. If the
        parms argument is a list of parameters to capture, this is
        ignored.

    evaluate_parmvalues
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    parmtemplates
        If this is "spare_only", the capture process only saves spare
        parameter templates so it can recreate them. This is helpful to
        ensure minimal change to the parameter interface on nodes where
        additional parameters were added. If this is "all", the capture
        process saves template data for all parameters.

    parmfilter
        This captures the settings used for the parameter filter and
        search bar for each node.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

'''
def itemsAsData(items: list[hou.NetworkMovableItem], **items_opts: Any) -> rtypes.NetworkItemDataDict | None:
    '''
itemsAsData(items: Sequence[hou.NetworkMovableItems], nodes_only:
bool=False, children: bool=True, editables:bool=True, inputs: bool=True,
position: bool=True, anchor_position: hou.Vector2=hou.Vector2(0, 0),
flags: bool=True, parms: bool=True, parms_as_brief: bool=True,
default_parmvalues: bool=False, evaluate_parmvalues: bool=False,
parmtemplates: str="spare_only", metadata: bool=False, verbose:
bool=False) -> dict[str, Any]

    Returns a JSON-like data structure representing the given network
    items.


    items
        A sequence of hou.NetworkMovableItem instances to capture that
        are created when the data is applied.

    nodes_only
        If this is True, the capture process only saves nodes, ignoring
        sticky notes, network boxes, and dots.

    children
        If this is False, the capture process only saves the top level
        nodes, ignoring nodes inside subnets and unlocked assets.

    editables
        If this is False, the capture process ignores nodes inside
        editable dive target networks inside assets.

    inputs
        If this is True, the capture process saves input connections.

    position
        If this is True, the capture process saves the node position.

    anchor_position
        The reference position used to record positions of all items.

    flags
        If this is True, the capture process saves flag states.

    parms
        If this is True, based on default_parmvalues argument, the
        capture process saves any non-default parameter values or all
        parameter values. If this is False, no parameters are saved.
        Alternatively, to save a custom set of parameter values you can
        specify a list of hou.ParmTuple or hou.Parm instances, or
        strings representing names of parameters to capture.

    parms_as_brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    default_parmvalues
        Normally, when parms is True, the capture process only saves
        parameters with non-default values. If this is True, the capture
        process also saves parameters set to the default value. If the
        parms argument is a list of parameters to capture, this is
        ignored.

    evaluate_parmvalues
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    parmtemplates
        If this is "spare_only", the capture process only saves spare
        parameter templates so it can recreate them. This is helpful to
        ensure minimal change to the parameter interface on nodes where
        additional parameters were added. If this is "all", the capture
        process saves template data for all parameters.

    parmfilter
        This captures the settings used for the parameter filter and
        search bar for each node.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

'''
def createItemsFromData(parent: hou.OpNode, data: rtypes.NetworkItemDataDict, **items_set_opts: Any) -> dict[str, hou.NetworkMovableItem]:
    """
createItemsFromData(parent: hou.OpNode, data: dict[str, Any],
clear_content: bool=False, force_item_creation: bool=True,
offset_position: hou.Vector2=hou.Vector2(0, 0),
external_connections=True, parms: bool=True, parmtemplates: bool=True,
children: bool=True, editables: bool=True, skip_notes: bool=False) ->
dict[str, hou.NetworkMovableItem]

    Given a network node and JSON-like data structure as returned by
    hou.data.selectedItemsAsData() or hou.data.itemsAsData() recreate
    the data items inside the network. Returns a dictionary mapping the
    names of the original captured items to the corresponding recreated
    items.


    parent
        The hou.OpNode in which to place the created items.

    data
        The network item data dictionary that describes a sequence of
        network items as data.

    clear_content
        If this is True, the content of parent is destroyed before item
        creation.

    force_item_creation
        If this is False and parent has an item with a matching name in
        the data, instead of creating the item, the existing item is
        used.

    offset_position
        A hou.Vector2 that offsets the position of all items recreated
        by the data.

    external_connections
        The external connections are wires that connect to other
        hou.NetworkMovableItem but were not captured as part of the
        recipe. If this is True, those connections are re-created to
        existing nodes with the same name.

    parms
        If this is False, do not apply any parameter value stored in the
        data to the node.

    parmtemplates
        If this is False, do not recreate any spare parameters stored in
        the data.

    children
        If this is False, do not recursively recreate any child network
        stored in the data.

    editables
        If this is False, do not recreate the contents of any editable
        dive targets stored in the data.

    skip_notes
        If this is True, do not recreate any sticky notes stored in the
        data.

"""
def clusterItemsAsData(items: Sequence[hou.NetworkMovableItem], **cluster_opts: Any) -> rtypes.ClusterData:
    '''
clusterItemsAsData(items: Sequence[hou.NetworkMovableItems],
target_node: [hou.OpNode], frame_nodes:
Sequence[hou.NetworkMovableItem]=None, selected_nodes:
Sequence[hou.NetworkMovableItem]=None, current_node:
hou.NetworkMovableItem=None, flags: bool=True, nodes_only: bool=False,
target_children: bool=False, children: bool=True, target_editables:
bool=False, editables: bool=True, target_parms: Union[bool,
Sequence[hou.ParmTuple], Sequence[str]]=True, parms: bool=True,
default_parmvalues: bool=False, evaluate_parmvalues: bool=False,
parms_as_brief: bool=True, parmtemplates: str="spare_only", metadata:
bool=False, verbose: bool=False) -> dict[str, Any]

    Returns a JSON-like data structure representing the given network
    items. The returned dictionary includes what would be returned by
    hou.data.itemsAsData() in a key, along with various other properties
    related to a squence of items. See cluster data dictionary for more
    information.


    items
        A sequence of hou.NetworkMovableItem instances to capture that
        are created when the data is applied.

    target_node
        An optional hou.OpNode instance. The picked node is tagged
        inside the data structure. When the content of this data is
        recreated by hou.data.createClusterItemsFromData() using a new
        target node instance (using target_node argument), other items
        are positioned and their channel references changed relative to
        that new target node.

    frame_nodes
        An optional sequence of hou.NetworkMovableItem instances that
        the Network Editor uses to frame itself after the items are
        created. The function that creates the items (for example,
        hou.data.applyDecorationRecipe or hou.data.applyToolRecipe) must
        also use frame=True argument for this to work.

    selected_nodes
        An optional sequence of hou.NetworkMovableItem instances to be
        selected after the items are created.

    current_node
        An optional hou.NetworkMovableItem instance. Specifies which
        item should be set as the current node after the items are
        created. The parameter interface of this node is displayed in
        the Parameter Pane.

    flags
        If this is True, the capture process saves flag states.

    nodes_only
        If this is True, the capture process only saves nodes, ignoring
        sticky notes, network boxes, and dots.

    target_children
        Whether to recursively save the contents of the
        target/central/anchor node (if it is a subnetwork or unlocked
        asset).

    children
        If this is False, the capture process only saves the top level
        nodes, ignoring nodes inside subnets and unlocked assets.

    target_editables
        Whether to save the contents of editable dive targets inside the
        target/central/anchor node, if any.

    editables
        If this is False, the capture process ignores nodes inside
        editable dive target networks inside assets.

    target_parms
        Whether to save parameter values on the target/central/anchor
        node, if any.

        If this is True, based on default_parmvalues argument, the
        capture process saves any non-default parameter values or all
        parameter values. If this is False, no parameters are saved.
        Alternatively, to save a custom set of parameter values you can
        specify a list of hou.ParmTuple or hou.Parm instances, or
        strings representing names of parameters to capture.

    parms
        If this is True, based on default_parmvalues argument, the
        capture process saves any non-default parameter values or all
        parameter values. If this is False, no parameters are saved.
        Alternatively, to save a custom set of parameter values you can
        specify a list of hou.ParmTuple or hou.Parm instances, or
        strings representing names of parameters to capture.

    default_parmvalues
        Normally, when parms is True, the capture process only saves
        parameters with non-default values. If this is True, the capture
        process also saves parameters set to the default value. If the
        parms argument is a list of parameters to capture, this is
        ignored.

    evaluate_parmvalues
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    parms_as_brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    parmtemplates
        If this is "spare_only", the capture process only saves spare
        parameter templates so it can recreate them. This is helpful to
        ensure minimal change to the parameter interface on nodes where
        additional parameters were added. If this is "all", the capture
        process saves template data for all parameters.

    parmfilter
        This captures the settings used for the parameter filter and
        search bar for each node.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

'''
def createClusterItemsFromData(parent: hou.OpNode, data: rtypes.ClusterData, **cluster_set_opts: Any) -> rtypes.ClusterOutputData:
    """
createClusterItemsFromData(parent: hou.OpNode, data: dict[str, Any],
target_node: hou.OpNode=None, clear_content=False, force_item_creation:
bool=True, external_connections=True, parms: bool=True, parmtemplates:
bool=True, children: bool=True, editables: bool=True, offset_position:
hou.Vector2=hou.Vector2(0, 0), skip_notes: bool=False) -> dict[str,
hou.NetworkMovableItem]

    Given a network node and JSON-like data structure as returned by
    hou.data.clusterItemsAsData(), recreate the data items inside the
    network. Returns a dictionary containing information about how the
    items were recreated.


    parent
        The hou.OpNode in which to place the created items.

    data
        The cluster data dictionary that describes a sequence of network
        items as data.

    target_node
        An optional hou.OpNode instance. The picked node is tagged
        inside the data structure. When the content of this data is
        recreated by hou.data.createClusterItemsFromData() using a new
        target node instance (using target_node argument), other items
        are positioned and their channel references changed relative to
        that new target node.

    external_connections
        The external connections are wires that connect to other
        hou.NetworkMovableItem but were not captured as part of the
        recipe. If this is True, those connections are re-created to
        existing nodes with the same name.

    parms
        If this is False, do not apply any parameter value stored in the
        data to the node.

    parmtemplates
        If this is False, do not recreate any spare parameters stored in
        the data.

    children
        If this is False, do not recursively recreate any child network
        stored in the data.

    editables
        If this is False, do not recreate the contents of any editable
        dive targets stored in the data.

    skip_notes
        If this is True, do not recreate any sticky notes stored in the
        data.

"""
def dataFromRecipe(name: str) -> rtypes._RecipeDataPayload:
    """
dataFromRecipe(name: str) -> dict[str, Any]

    Given an internal recipe name, returns a python dictionary of the
    JSON-like data structure stored in the recipe.


    name
        The internal name of the recipe from which to return the data
        structure.

"""
def saveParmPresetRecipe(name: str, label: str, location: str, parm: hou.ParmTuple, **parmpresetrecipe_opts: Any) -> Ref | None:
    '''
saveParmPresetRecipe(self, name: str, label: str, location: str, parm:
hou.ParmTuple, parmtype_patterns: str="", parmname_patterns: str="",
nodetype_patterns: str="", visible: bool=True, submenu: str="",
record_data: bool=True, prescript: str="", postscript: str="", comment:
str="", expand_to_dir: bool=False, multiparm_operation: str="set",
multiparm_start_index: int=0, multiparm_end_index: int=-1,
evaluate_parmvalues=False, metadata=False, verbose=False) -> None

    Saves parameter and multiparm instance values as a preset recipe. To
    apply the recipe to a parameter, use hou.data.applyParmPresetRecipe.


    name
        The internal name for the Data asset to store the recipe in.

    label
        The label for the recipe, used in menus where the user can
        select the recipe.

    location
        A string representing the path to the asset library (.hda file)
        to save the recipe asset into. Alternatively, if you use an
        opdef: path, such as opdef:/Sop/my_asset to reference an
        existing asset, Houdini will save the new recipe asset into the
        same library file as the referenced asset.

        If you use the special string Embedded, the asset will be saved
        as part of the current scene file. This is sometimes useful for
        sharing a self-contained, working scene file.

    parm
        A hou.ParmTuple instance to save data from. Multiparm parent
        saves its instance parameters as well.

    parmtype_pattern
        Houdini shows this as an available preset for parameter types
        (the string returned by hou.ParmTemplate.interfaceType) that
        match this pattern. See Parm type patterns for more information.
        If this is empty, the recipe uses a pattern that only matches
        the type of the parm argument.

    parmname_pattern
        Houdini shows this as an available preset for parameters whose
        internal name matches this pattern. See Parm name patterns for
        more information. If this is empty, the recipe uses a pattern
        that only matches the internal name of the parm argument.

    nodetype_patterns
        Houdini shows this as an available preset for node types whose
        internal name (with category, as in the string returned by
        hou.NodeType.nameWithCategory) matches this pattern. See Target
        node patterns for more information. If this is empty, the recipe
        uses a pattern that only matches the node type of the node
        argument.

    visible
        If this is False, the recipe is hidden from the menus. Hidden
        recipes are still listed in the Recipe Manager.

    submenu
        When submenu is provided, the recipes with the same submenu are
        grouped together in the Recipe menus, where the last invoked
        recipe name is also displayed for each submenu.

    record_data
        Whether to record the JSON-like data structure for the recipe.
        Set this to False when the recipe\'s only purpose is to run a
        python script.

    prescript
        An optional python script that runs before the recipe\'s data is
        applied.

        See Pre and postscripts for more information.

    postscript
        An optional python script that runs after the recipe\'s data is
        applied.

        See Pre and postscripts for more information.

    expand_to_dir
        If this is True, expands the content of the recipe into a
        directory in location argument.

    comment
        Optional comment string to associate with the recipe.

    multiparm_operation
        When parm argument is a multiparm parent, controls how the
        multiparm instances are combined with existing multiparm
        instances when the recipe is applied.


        set
            Any existing instance is removed and replaced with the
            instances saved with this recipe.

        set_from_index
            This asks the user to provide an index. Any existing
            multiparm instances starting from that index are changed
            according to the instances stored in this recipe.

        insert_at_index
            This asks the user to provide an index. The instances stored
            in this recipe are inserted after this index.

        insert_first
            The instances stored in this recipe are prepended to the
            existing instances.

        append
            The instances stored in this recipe are appended to the
            existing instances.

    multiparm_start_index
        The instance index number from which to record the instances.

    multiparm_end_index
        The instance index number until which to record the instances.
        The default -1 means all instances are recorded after
        multiparm_startindex argument.

    evaluate_parmvalues
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

'''
def applyParmPresetRecipe(name: str, parm: hou.Parm | hou.ParmTuple | None = None, **parmpresetrecipe_set_opts: Any) -> rtypes.ParmPresetOutputData | None:
    '''
applyParmPresetRecipe(self, name: str, parm: parm: hou.ParmTuple,
multiparm_operation: str="", multiparm_start_index: int = 0, prescript:
bool=True, postscript: bool=True) -> dict[str, Any]

    Applies the recipe specified by name to the given hou.ParmTuple
    instance.


    name
        The internal name of the recipe to apply.

    parm
        A hou.ParmTuple instance to apply the recipe to.

    multiparm_operation
        When parm argument is a multiparm parent, controls how the
        multiparm instances are combined with existing multiparm
        instances when the recipe is applied.


        set
            Any existing instance is removed and replaced with the
            instances saved with this recipe.

        set_from_index
            This asks the user to provide an index. Any existing
            multiparm instances starting from that index are changed
            according to the instances stored in this recipe.

        insert_at_index
            This asks the user to provide an index. The instances stored
            in this recipe are inserted after this index.

        insert_first
            The instances stored in this recipe are prepended to the
            existing instances.

        append
            The instances stored in this recipe are appended to the
            existing instances.

        When it is an empty string, the operation saved inside the
        recipe is used.

    prescript
        If this is False, do not run the pre python script saved with
        the recipe.

        See pre and postscripts for more information.

    postscript
        If this is False, do not run the post python script saved with
        the recipe.

        See pre and postscripts for more information.

    Returns a dictionary with the following keys:



        node
            The hou.Node object that contains the preset parameter the
            recipe was applied to.

        parms
            The hou.ParmTuple object that was set by the recipe on the
            node.

    For example, the output of a parm preset that sets the Type
    parameter on the Box SOP:

  > {
  >         \'node\': <hou.SopNode of type box at /obj/geo1/box1>,
  >         \'parm\': hou.ParmTuple type in /obj/geo1/box1>
  > }
'''
def saveNodePresetRecipe(name: str, label: str, location: str, node: hou.OpNode, **nodepresetrecipe_opts: Any) -> Ref | None:
    '''
saveNodePresetRecipe(self, name: str, label: str, location: str, node:
hou.OpNode, nodetype_patterns: str="", visible: bool=True, submenu:
str="", record_data: bool=True, prescript: str="", postscript: str="",
expand_to_dir: bool=False, comment: str="", nodes_only: bool=False,
flags: bool=False, children: bool=False, editables: bool=False, inputs:
bool=False, position: bool=False, parms: Union[bool,
Sequence[hou.ParmTuple], Sequence[str]]=True, default_parmvalues:
bool=False, evaluate_parmvalues: bool=False, parms_as_brief: bool=True,
parmtemplates: str="spare_only", metadata: bool=False, verbose:
bool=False) -> None

    Saves parameters, optionally children or the editable context of a
    node as a preset recipe. To apply the recipe to a node, use
    hou.data.applyNodePresetRecipe.


    name
        The internal name for the Data asset to store the recipe in.

    label
        The label for the recipe, used in menus where the user can
        select the recipe.

    location
        A string representing the path to the asset library (.hda file)
        to save the recipe asset into. Alternatively, if you use an
        opdef: path, such as opdef:/Sop/my_asset to reference an
        existing asset, Houdini will save the new recipe asset into the
        same library file as the referenced asset.

        If you use the special string Embedded, the asset will be saved
        as part of the current scene file. This is sometimes useful for
        sharing a self-contained, working scene file.

    node
        A hou.OpNode instance to save data from.

    nodetype_patterns
        Houdini shows this as an available preset for node types whose
        internal name (with category, as in the string returned by
        hou.NodeType.nameWithCategory) matches this pattern. See Target
        node patterns for more information. If this is empty, the recipe
        uses a pattern that only matches the node type of the node
        argument.

    visible
        If this is False, the recipe is hidden from the menus. Hidden
        recipes are still listed in the Recipe Manager.

    submenu
        When submenu is provided, the recipes with the same submenu are
        grouped together in the Recipe menus, where the last invoked
        recipe name is also displayed for each submenu.

    record_data
        Whether to record the JSON-like data structure for the recipe.
        Set this to False when the recipe\'s only purpose is to run a
        python script.

    prescript
        An optional python script that runs before the recipe\'s data is
        applied.

        See Pre and postscripts for more information.

    postscript
        An optional python script that runs after the recipe\'s data is
        applied.

        See Pre and postscripts for more information.

    expand_to_dir
        If this is True, expands the content of the recipe into a
        directory in location argument.

    comment
        Optional comment string to associate with the recipe.

    nodes_only
        If this is True, the capture process only saves nodes, ignoring
        sticky notes, network boxes, and dots.

    flags
        If this is True, the capture process saves flag states.

    children
        If this is False, the capture process only saves the top level
        nodes, ignoring nodes inside subnets and unlocked assets.

    editables
        If this is False, the capture process ignores nodes inside
        editable dive target networks inside assets.

    inputs
        If this is True, the capture process saves input connections.

    position
        If this is True, the capture process saves the node position.

    parms
        If this is True, based on default_parmvalues argument, the
        capture process saves any non-default parameter values or all
        parameter values. If this is False, no parameters are saved.
        Alternatively, to save a custom set of parameter values you can
        specify a list of hou.ParmTuple or hou.Parm instances, or
        strings representing names of parameters to capture.

    default_parmvalues
        Normally, when parms is True, the capture process only saves
        parameters with non-default values. If this is True, the capture
        process also saves parameters set to the default value. If the
        parms argument is a list of parameters to capture, this is
        ignored.

    evaluate_parmvalues
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    parms_as_brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    parmtemplates
        If this is "spare_only", the capture process only saves spare
        parameter templates so it can recreate them. This is helpful to
        ensure minimal change to the parameter interface on nodes where
        additional parameters were added. If this is "all", the capture
        process saves template data for all parameters.

    parmfilter
        This captures the settings used for the parameter filter and
        search bar for each node.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

'''
def applyNodePresetRecipe(name: str, node: hou.OpNode, **nodepresetrecipe_set_opts: Any) -> rtypes.NodePresetOutputData | tuple[str, str] | None:
    """
applyNodePresetRecipe(self, name: str, node: hou.OpNode, prescript:
bool=True, postscript: bool=True, parms: bool=True, parmtemplates:
bool=True, children: bool=True, editables: bool=True, skip_notes:
bool=True) -> dict[str, Any]

    Applies the recipe specified by name to the given hou.OpNode
    instance.


    name
        The internal name of the recipe to apply.

    node
        A hou.OpNode instance to apply the recipe to.

    prescript
        If this is False, do not run the pre python script saved with
        the recipe.

        See pre and postscripts for more information.

    postscript
        If this is False, do not run the post python script saved with
        the recipe.

        See pre and postscripts for more information.

    parms
        If this is False, do not apply any parameter value stored in the
        data to the node.

    parmtemplates
        If this is False, do not recreate any spare parameters stored in
        the data.

    children
        If this is False, do not recursively recreate any child network
        stored in the data.

    editables
        If this is False, do not recreate the contents of any editable
        dive targets stored in the data.

    skip_notes
        If this is True, do not recreate any sticky notes stored in the
        data.

    Returns a dictionary with the following keys:



        node
            The hou.OpNode object the recipe was applied to.

        parms
            Sequence of hou.ParmTuple objects set by the recipe on the
            node.

    For example, the output of a node preset that sets two parameters on
    the Box SOP:

  > {
  >         'node': <hou.SopNode of type box at /obj/geo1/box1>,
  >         'parms': [
  >                 <hou.ParmTuple type in /obj/geo1/box1>,
  >                 <hou.ParmTuple divrate in /obj/geo1/box1>
  >             ]
  > }
"""
def saveDecorationRecipe(name: str, label: str, location: str, central_node: hou.OpNode, decorator_items: Sequence[hou.NetworkMovableItem], **decoratorrecipe_opts: Any) -> Ref | None:
    '''
saveDecorationRecipe(self, name: str, label: str, location: str,
central_node: [hou.OpNode], decorator_items:
Sequence[hou.NetworkMovableItems], nodetype_patterns="", visible:
bool=True, submenu: str="", record_data: bool=True, prescript: str="",
postscript: str="", expand_to_dir: bool=False, comment: str="",
frame_nodes: Sequence[hou.NetworkMovableItem]=None, selected_nodes:
Sequence[hou.NetworkMovableItem]=None, current_node:
hou.NetworkMovableItem=None, nodes_only: bool=False, flags: bool=False,
central_children: bool=False, children: bool=True, central_editables:
bool=False, editables: bool=True, central_parms: Union[bool,
Sequence[hou.ParmTuple], Sequence[str]]=True, parms: bool=True,
default_parmvalues: bool=False, evaluate_parmvalues: bool=False,
parms_as_brief: bool=True, parmtemplates: str="spare_only", metadata:
bool=False, verbose: bool=False) -> None

    Saves a set of network items as a decoration recipe. To apply a
    saved decoration recipe, use hou.data.applyDecorationRecipe.



    central_node
        A [Hom:hou.OpNode] instance to use as the central node of the
        decoration. See decoration recipes for more information.

    decorator_items
        A sequence of hou.NetworkMovableItem instances to capture that
        are created when the recipe is applied.

    nodetype_patterns
        Houdini shows this as an available preset for node types whose
        internal name (with category, as in the string returned by
        hou.NodeType.nameWithCategory) matches this pattern. See Target
        node patterns for more information. If this is empty, the recipe
        uses a pattern that only matches the node type of the node
        argument.

    visible
        If this is False, the recipe is hidden from the menus. Hidden
        recipes are still listed in the Recipe Manager.

    submenu
        When submenu is provided, the recipes with the same submenu are
        grouped together in the Recipe menus, where the last invoked
        recipe name is also displayed for each submenu.

    record_data
        Whether to record the JSON-like data structure for the recipe.
        Set this to False when the recipe\'s only purpose is to run a
        python script.

    prescript
        An optional python script that runs before the recipe\'s data is
        applied.

        See Pre and postscripts for more information.

    postscript
        An optional python script that runs after the recipe\'s data is
        applied.

        See Pre and postscripts for more information.

    expand_to_dir
        If this is True, expands the content of the recipe into a
        directory in location argument.

    comment
        Optional comment string to associate with the recipe.

    frame_nodes
        An optional sequence of hou.NetworkMovableItem instances that
        the Network Editor uses to frame itself after the items are
        created. The function that creates the items (for example,
        hou.data.applyDecorationRecipe or hou.data.applyToolRecipe) must
        also use frame=True argument for this to work.

    selected_nodes
        An optional sequence of hou.NetworkMovableItem instances to be
        selected after the items are created.

    current_node
        An optional hou.NetworkMovableItem instance. Specifies which
        item should be set as the current node after the items are
        created. The parameter interface of this node is displayed in
        the Parameter Pane.

    nodes_only
        If this is True, the capture process only saves nodes, ignoring
        sticky notes, network boxes, and dots.

    flags
        If this is True, the capture process saves flag states.

    central_children
        Whether to recursively save the contents of the
        target/central/anchor node (if it is a subnetwork or unlocked
        asset).

    children
        Whether to recursively save the contents of subnetworks and
        unlocked assets other than the target/central/anchor node.

    central_editables
        Whether to save the contents of editable dive targets inside the
        target/central/anchor node, if any.

    editables
        Whether to save the contents of editable dive targets inside
        assets other than the target/central/anchor node.

    central_parms
        Whether to save parameter values on the target/central/anchor
        node, if any.

        If this is True, based on default_parmvalues argument, the
        capture process saves any non-default parameter values or all
        parameter values. If this is False, no parameters are saved.
        Alternatively, to save a custom set of parameter values you can
        specify a list of hou.ParmTuple or hou.Parm instances, or
        strings representing names of parameters to capture.

    parms
        Whether to save parameter values on nodes other than the
        target/central/anchor node. Based on default_parmvalues
        argument, the capture process saves any non-default parameter
        values or all parameter values.

    default_parmvalues
        Normally, when parms is True, the capture process only saves
        parameters with non-default values. If this is True, the capture
        process also saves parameters set to the default value. If the
        parms argument is a list of parameters to capture, this is
        ignored.

    evaluate_parmvalues
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    parms_as_brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    parmtemplates
        If this is "spare_only", the capture process only saves spare
        parameter templates so it can recreate them. This is helpful to
        ensure minimal change to the parameter interface on nodes where
        additional parameters were added. If this is "all", the capture
        process saves template data for all parameters.

    parmfilter
        This captures the settings used for the parameter filter and
        search bar for each node.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

'''
def applyDecorationRecipe(name: str, central_node: hou.OpNode | None = None, **decoratorrecipe_set_opts: Any) -> rtypes.DecorationOutputData | None:
    """
applyDecorationRecipe(self, name: str, central_node: hou.OpNode,
external_connections: bool=False, drop_on_wire: bool=False,
click_to_place: bool=False, avoid_overlap: bool=False, frame:
bool=False, parms: bool=True, parmtemplates: bool=True, children:
bool=True, editables: bool=True, skip_notes: bool=True) -> dict[str,
Any]

    Applies the decoration recipe specified by name to the given
    hou.OpNode instance.


    name
        The internal name of the recipe to apply.

    central_node
        The target hou.OpNode instance to apply the decoration to.
        Decorator items from the recipe are recreated around it.

    external_connections
        The external connections are wires that connect to other
        hou.NetworkMovableItem but were not captured as part of the
        recipe. If this is True, those connections are re-created to
        existing nodes with the same name.

    drop_on_wire
        Rewire existing connections into and out of the given central
        node.

    click_to_place
        If this is True, the user is asked to click in the Network
        Editor to place the content of the recipe.

    avoid_overlap
        If this is True, it moves the node tiles to avoid overlap.

    frame
        If this is True, the network editor frames around the nodes that
        were set using frame_nodes when the recipe was captured.

    parms
        If this is False, do not apply any parameter value stored in the
        data to the node.

    parmtemplates
        If this is False, do not recreate any spare parameters stored in
        the data.

    children
        If this is False, do not recursively recreate any child network
        stored in the data.

    editables
        If this is False, do not recreate the contents of any editable
        dive targets stored in the data.

    skip_notes
        If this is True, do not recreate any sticky notes stored in the
        data.

    Returns a dictionary with the following keys:



        central_node
            The hou.OpNode object the recipe was applied to.

        central_parms
            Sequence of hou.ParmTuple objects set by the recipe on the
            central node.

        framed_nodes
            Sequence of hou.OpNode objects that were set to be framed by
            the network editor.

        selected_nodes
            Sequence of hou.OpNode objects that were set to be selected
            after the recipe was applied.

        current_node
            The hou.OpNode object that was set to be the last selected
            node after the recipe was applied.

        items
            A dictionary of hou.OpNode objects (decorators) set around
            the central node, where the dictionary keys are the node
            names as they were recorded in the data, and the values are
            the hou.OpNode objects that were created by that data.

    For example, the output of a decoration that sets the Type parameter
    on the central node and creates a Null SOP as a decorator below the
    central node:

  > {
  >         'central_node': <hou.SopNode of type box at /obj/geo1/box1>,
  >         'central_parms': [
  >                 <hou.ParmTuple type in /obj/geo1/box1>
  >                 ],
  >         'items': [
  >                 'null1': <hou.SopNode of type box at /obj/geo1/null1>
  >                 ]
  > }
"""
def saveToolRecipe(name: str, label: str, location: str, anchor_node: hou.OpNode, **toolrecipe_opts: Any) -> Ref | None:
    '''
saveTabToolRecipe(self, name: str, label: str, location: str,
anchor_node: hou.OpNode, items: Sequence[hou.NetworkMovableItem]=None,
tab_submenu str:="Recipes", help_url: str="", visible: bool=True, icon:
str="BUTTONS_recipe", record_data: bool=True, prescript: str="",
postscript: str="", expand_to_dir: bool=False, comment: str="",
frame_nodes: Sequence[hou.NetworkMovableItem]=None, selected_nodes:
Sequence[hou.NetworkMovableItem]=None, current_node:
hou.NetworkMovableItem=None, nodes_only=False, flags: bool=False,
anchor_children: bool=False, children: bool=True, anchor_editables:
bool=False, editables: bool=True, anchor_parms: Union[bool,
Sequence[hou.ParmTuple], Sequence[str]] = True, parms: bool=True,
default_parmvalues: bool=False, evaluate_parmvalues: bool=False,
parms_as_brief: bool=True, parmtemplates: str="spare_only", metadata:
bool=False, verbose: bool=False) -> None

    Saves a set of network items as a tool recipe to be displayed in the
    Tab Menu Submenu. This is a shortcut to hou.data.saveToolRecipe().


    name
        The internal name for the Data asset to store the recipe in.

    label
        The label for the recipe, used in menus where the user can
        select the recipe.

    location
        A string representing the path to the asset library (.hda file)
        to save the recipe asset into. Alternatively, if you use an
        opdef: path, such as opdef:/Sop/my_asset to reference an
        existing asset, Houdini will save the new recipe asset into the
        same library file as the referenced asset.

        If you use the special string Embedded, the asset will be saved
        as part of the current scene file. This is sometimes useful for
        sharing a self-contained, working scene file.

    anchor_node
        A hou.OpNode instance to include as part of the recipe. When you
        drop the tool in a network later, the position you choose is
        applied to this node, and the other items in the recipe are
        positioned relative to it.

    items
        A sequence of hou.NetworkMovableItem instances to capture that
        are created when the data is applied.

    tab_submenu
        The label of the category submenu in which the new tool should
        appear on the tab menu. You can have the tool appear in multiple
        submenus by entering multiple menu labels separated by commas.
        For example, File IO, Recipes makes the tool appear in both the
        File IO and Recipes submenus of the tab menu.

    help_url
        Sets a URL where the help viewer should go to when the user
        requests help for this tool.

    visible
        If this is False, the recipe is hidden from the menus. Hidden
        recipes are still listed in the Recipe Manager.

    icon
        The icon associated with this recipe.

    record_data
        Whether to record the JSON-like data structure for the recipe.
        Set this to False when the recipe\'s only purpose is to run a
        python script.

    prescript
        An optional python script that runs before the recipe\'s data is
        applied.

        See Pre and postscripts for more information.

    postscript
        An optional python script that runs after the recipe\'s data is
        applied.

        See Pre and postscripts for more information.

    expand_to_dir
        If this is True, expands the content of the recipe into a
        directory in location argument.

    comment
        Optional comment string to associate with the recipe.

    frame_nodes
        An optional sequence of hou.NetworkMovableItem instances that
        the Network Editor uses to frame itself after the items are
        created. The function that creates the items (for example,
        hou.data.applyDecorationRecipe or hou.data.applyToolRecipe) must
        also use frame=True argument for this to work.

    selected_nodes
        An optional sequence of hou.NetworkMovableItem instances to be
        selected after the items are created.

    current_node
        An optional hou.NetworkMovableItem instance. Specifies which
        item should be set as the current node after the items are
        created. The parameter interface of this node is displayed in
        the Parameter Pane.

    nodes_only
        If this is True, the capture process only saves nodes, ignoring
        sticky notes, network boxes, and dots.

    flags
        If this is True, the capture process saves flag states.

    anchor_children
        Whether to recursively save the contents of the
        target/central/anchor node (if it is a subnetwork or unlocked
        asset).

    children
        Whether to recursively save the contents of subnetworks and
        unlocked assets other than the target/central/anchor node.

    anchor_editables
        Whether to save the contents of editable dive targets inside the
        target/central/anchor node, if any.

    editables
        Whether to save the contents of editable dive targets inside
        assets other than the target/central/anchor node.

    anchor_parms
        Whether to save parameter values on the target/central/anchor
        node, if any.

        If this is True, based on default_parmvalues argument, the
        capture process saves any non-default parameter values or all
        parameter values. If this is False, no parameters are saved.
        Alternatively, to save a custom set of parameter values you can
        specify a list of hou.ParmTuple or hou.Parm instances, or
        strings representing names of parameters to capture.

    children
        Whether to recursively save the contents of subnetworks and
        unlocked assets other than the target/central/anchor node.

    parms
        Whether to save parameter values on nodes other than the
        target/central/anchor node. Based on default_parmvalues
        argument, the capture process saves any non-default parameter
        values or all parameter values.

    default_parmvalues
        Normally, when parms is True, the capture process only saves
        parameters with non-default values. If this is True, the capture
        process also saves parameters set to the default value. If the
        parms argument is a list of parameters to capture, this is
        ignored.

    evaluate_parmvalues
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    parms_as_brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    parmtemplates
        If this is "spare_only", the capture process only saves spare
        parameter templates so it can recreate them. This is helpful to
        ensure minimal change to the parameter interface on nodes where
        additional parameters were added. If this is "all", the capture
        process saves template data for all parameters.

    parmfilter
        This captures the settings used for the parameter filter and
        search bar for each node.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

'''
def applyToolRecipe(name: str, **toolrecipe_set_opts: Any) -> rtypes.ToolOutputData | None:
    """
dataFromRecipe(name: str) -> dict[str, Any]

    Given an internal recipe name, returns a python dictionary of the
    JSON-like data structure stored in the recipe.


    name
        The internal name of the recipe from which to return the data
        structure.

"""
def saveTabToolRecipe(name: str, label: str, location: str, anchor_node: hou.OpNode, **toolrecipe_opts: Any) -> Ref | None: ...
def applyTabToolRecipe(name: str, **toolrecipe_set_opts: Any) -> rtypes.ToolOutputData | None: ...
