import hou
from collections.abc import Sequence
from houtypes import ParmActionButtonKwargs
from typing import TypedDict

class _VisualizerDefaults(TypedDict):
    type: hou.ViewportVisualizerType | None
    parms: dict[str, str | int | float | hou.Ramp]

class _ViewportState(TypedDict, total=False):
    old_pickingcurrentnode: bool
    old_displaynode: hou.Node | None
    old_current: hou.Node | None
    old_pwd: hou.Node | None
    old_state: str
    node_was_current: bool
    old_group_picking: bool
    old_group_pick_mask: str

def groupTypeParmFromGeometryType(geotype: hou.EnumValue[hou.geometryType], parmtuple: hou.ParmTuple) -> str | None: ...
def geometryTypeFromGroupTypeParm(parmval: str) -> hou.EnumValue[hou.geometryType] | None:
    """ Convert a value from a group type parameter into a hou.geometryType.
    """
def showError(msg: str) -> None: ...
def getDefaultState(node_type: hou.OpNodeType) -> str | None: ...
def stashViewportState(pane: hou.SceneViewer, node: hou.OpNode, state: _ViewportState) -> None:
    """ Stash viewport options that we want to restore after a selection is
        completed.
    """
def restoreViewportState(pane: hou.SceneViewer, node: hou.OpNode, state: _ViewportState) -> None: ...
def getSelectionNode(kwargs: ParmActionButtonKwargs, create_tempnode: bool = True) -> tuple[hou.SopNode, hou.SopNode | None, int] | tuple[None, None, None]:
    """ A function to get the SOP node on which the selection is made in the
        selectGroupParm function.

        :param create_tempnode: Whether the creation of a temporary node is allowed when the display flag cannot be set on the node.
        :type create_tempnode: bool
        :return selectionnode: The selection node
        :rtype selectionnode: hou.SopNode
        :return tempnode: None or a Null SOP that was temporarily created because the selection node was inside a locked asset.
        :rtype selectionnode: hou.SopNode
        :return outputidx: The output index of the selection node which contains the selection geometry.
        :rtype outputidx: int
    """
def selectGroupParm(kwargs: ParmActionButtonKwargs) -> None:
    """ Performs a selection that is used to populate a SOP Group parameter field.
        This function takes a number of kwargs options to control the exact form
        of the returned selection, how the parameter should be set, the allowed
        selection types, etc.  If kwargs['ordered'] is present, then that alone
        specifies whether to do an ordered selection.  If kwargs['ordered'] is
        not present, then we try to determine orderedness from any selector bound
        to the node and parameter in question, and, failing that, default to an
        unordered selection.
    """
def replaceSelectionNumbersByNameAttributeRefs(sel: hou.Selection | None, geo: hou.Geometry | None, nameattr: str | None, parm: hou.Parm | hou.ParmTuple) -> bool:
    '''Replace the selection numbers by name attribute references
        \'sel\' is a hou.Selection
        \'geo\' is a hou.Geometry to use along with the selection
        \'nameattr\' is a name attribute to use for name matching or it can also
         be a channel reference string in the form chs("parmname")
        \'parm\' is the string parameter to write to. hou.Parm or ParmTuple
        Returns True if parmtuple value was updated or False otherwise.
        Raises an exception if parm isn\'t valid.
    '''
def selectPointGroupParmByName(kwargs: ParmActionButtonKwargs, inputindex: int = 0) -> None: ...
def selectGroupParmFromPolygons(kwargs: ParmActionButtonKwargs, geo: hou.Geometry | None) -> None:
    """ Similar to selectGroupParm() except that the given polygon geometry 
        is used for selecting instead.
    """
def convertObjectPathToSelection(geo: hou.Geometry | None, object_path: str) -> str: ...
def getMatchLength(p1: Sequence[str], p2: Sequence[str]) -> int: ...
def compactPaths(paths: list[str], all_paths: list[str]) -> list[str]: ...
def convertSelectionToObjectPath(geo: hou.Geometry, sel: hou.Selection) -> str: ...
def selectAlembicPaths(kwargs: ParmActionButtonKwargs) -> None:
    """ Function for selecting Alembic Object Path parameters for the Alembic SOP.
        Similar in concept to the selectGroupParm function, but with a few tweaks.
        The Select Group flag is always turned on, and the Group MAsk set to @path.
        One the selection is complete, the selected alembic paths are compared to
        the complete list of alembic paths for the geometry, and a minimal set of
        paths is generated which will include all selected geometry, and no
        unselected geometry.
    """
def selectMaterialGroupParm(kwargs: ParmActionButtonKwargs) -> None:
    """ Similar to the selectGroupParm function above, but with some tweaks that
        make it specific to the Material SOP. It always does a primitive selection.
        It always activates group select mode. The Group Mask is set based on the
        availability of the path attribute, then user-defined groups, and falling
        back to polygon connectivity if no other options are available.
    """
def findVisualizer(attrib: str, category: hou.EnumValue[hou.viewportVisualizerCategory], node: hou.OpNode | None) -> hou.ViewportVisualizer | None:
    """ Finds a visualizer for an attribute of the given name. Returned
        visualizer will be in the provided category (node needs to be
        specified for node visualizers). Returns None if no such visualizer
        exists.
    """
def findVolumeVisualizer(name: str, category: hou.EnumValue[hou.viewportVisualizerCategory], node: hou.OpNode | None) -> hou.ViewportVisualizer | None:
    """ Finds a visualizer for an volume of the given name. Returned
        visualizer will be in the provided category (node needs to be
        specified for node visualizers). Returns None if no such visualizer
        exists.
    """
def guessVisualizerDefaultsFromAttrib(attrib: hou.Attrib, attribclass: str) -> _VisualizerDefaults:
    """ Guesses the appropriate settings for the given attribute.
    """
def guessVisualizerDefaultsFromVolume(volumename: str, volume: hou.Prim | None) -> _VisualizerDefaults:
    """ Guesses the appropriate settings for the given volume.
    """
def setupVisualizer(viz: hou.ViewportVisualizer, name: str, viz_defaults: _VisualizerDefaults) -> None:
    """ Sets settings for the given vizualizer from the defaults
        and wires it to the provided attribute.
    """
def setupVolumeVisualizer(viz: hou.ViewportVisualizer, name: str, viz_defaults: _VisualizerDefaults) -> None:
    """ Sets settings for the given vizualizer from the defaults
        and wires it to the provided attribute.
    """
def turnOffVisualizers(vtype: hou.ViewportVisualizerType | None, category: hou.EnumValue[hou.viewportVisualizerCategory], node: hou.OpNode | None, viewport: hou.GeometryViewport) -> None:
    """ Turns off all visualizers that are of the given type and category.
    """
def toggleVisualizer(node: hou.SopNode, attribname: str, attribclass: str, category: hou.EnumValue[hou.viewportVisualizerCategory], viewport: hou.GeometryViewport, viz_defaults: _VisualizerDefaults | None = None, enable_only: bool = False, output_index: int = 0) -> hou.ViewportVisualizer | None:
    """ This function toggles visibility of an attribute visualizer. If a
        visualizer does not exist, a new one is created with appropriate
        settings.
        attribclass should be one of 'vertices', 'points', 'primitives', or
        'detail'.
    """
def toggleVisualizerInViewports(node: hou.SopNode, attribname: str, attribclass: str, category: hou.EnumValue[hou.viewportVisualizerCategory], curviewport: hou.GeometryViewport, viewports: Sequence[hou.GeometryViewport], viz_defaults: _VisualizerDefaults | None = None, enable_only: bool = False, output_index: int = 0) -> hou.ViewportVisualizer | None: ...
def actionToggleVisualizer(kwargs: ParmActionButtonKwargs, viz_defaults: _VisualizerDefaults | None = None) -> None:
    """ Toggles the visibility of attribute pointed to by kwargs['parmtuple']
        on the node kwargs['node'].  Meant to be used in action buttons
        to enable simple attribute visualization.

        Use kwargs['attribname'] to explicitly provide an attribute name
        instead of evaluating the parm tuple.
    """
def toggleVolumeVisualizer(node: hou.SopNode, volumename: str, category: hou.EnumValue[hou.viewportVisualizerCategory], viewport: hou.GeometryViewport | None, viz_defaults: _VisualizerDefaults | None = None, output_index: int = 0) -> None:
    """ This function toggles visibility of a volume visualizer. If a
        visualizer does not exist, a new one is created with appropriate
        settings.
    """
def actionToggleVolumeVisualizer(kwargs: ParmActionButtonKwargs, viz_defaults: _VisualizerDefaults | None = None) -> None:
    """ Toggles the visibility of volume pointed to by kwargs['parmtuple']
        on the node kwargs['node'].  Meant to be used in action buttons
        to enable simple volume visualization.

        Use kwargs['volumename'] to explicitly provide an attribute name
        instead of evaluating the parm tuple.
    """
def getDistanceVisualizerDefaults() -> _VisualizerDefaults:
    """ Returns a set of parameters suitable for visualizing distance values.
    """
def getMaskVisualizerDefaults() -> _VisualizerDefaults:
    """ Returns a set of parameters suitable for our canonical mask
        visualization
    """
def getFalseColorVisualizerDefaults() -> _VisualizerDefaults:
    """ Returns a set of parameters suitable for false colour
        visualization
    """
def getRandomColorVisualizerDefaults() -> _VisualizerDefaults:
    """ Returns a set of parameters suitable for random colour
        visualization, useful for integers
    """
def getDirectColorVisualizerDefaults() -> _VisualizerDefaults:
    """ Returns a set of parameters suitable for direct colour
        visualization
    """
def getNormalVectorColorVisualizerDefaults() -> _VisualizerDefaults:
    """ Returns a set of parameters suitable for visualizing normal vectors
        with color.
    """
def getVolumeTrailVisualizerDefaults() -> _VisualizerDefaults:
    """ Returns defaults for trail display of vector volumes.
    """
def getVolumeColorVisualizerDefaults() -> _VisualizerDefaults:
    """ Returns defaults for direct-color display of color volumes (0-1)
    """
def getVolumeFogVisualizerDefaults() -> _VisualizerDefaults:
    """ Returns defaults for false-color display of fog-volumes (0-1)
    """
def getTextVisualizerDefaults() -> _VisualizerDefaults:
    """ Returns defaults for text display of string attributes.
    """
