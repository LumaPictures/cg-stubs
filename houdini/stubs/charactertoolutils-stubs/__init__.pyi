# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Iterable, Mapping, Sequence
from houtypes import ShelfToolKwargs

pointMuscles: dict[str, int]
placementMethod: dict[str, int]

def genericPointMuscleTool(scriptargs: ShelfToolKwargs, nodetypename: str, exact_node_type: bool = True) -> hou.ObjNode | None:
    """ Creates a Point Muscle asset and allows the user to select the 
        parent objects.
    """
def multiTypeSelectionTool(scriptargs: ShelfToolKwargs, type_list: Sequence[str], default: int | None = None) -> str | None:
    """ Generate a list of node type descriptions that can be selected from
        when a shift click from a tool is detected.
    """
def selectInteriorPoint(method: int) -> hou.Vector3 | None:
    """ Based on a point selection within the viewport, it returns the world 
        space coordinate of the center/interior of the selected geometry based 
        on either the viewing direction or the normal of the first intersection 
        point. If the selected point does not intersect any geometry, nothing 
        will be returned. The selection method (view or normal) must be 
        specified as an argument.
        Ie. import charactertoolutils as c
            view = c.placementMethod.get('view')
            normal = c.placementMethod.get('normal')
            view_pt = c.selectInteriorPoint(view)
            normal_pt = c.selectInteriorPoint(normal)
    """
def createPoseScopeAttrib(attribname: str | None, geo: hou.Geometry) -> str:
    """create the pose scope attribute, if it does not already exist, using the given attribname 
    or the default 'pose_scope' otherwise. attribname should be a string and geo should be a
    hou.Geometry object
    """
def createPoseScopePickscript(label: str, language: str, script: str) -> list[str]:
    '''create the correctly formatted json string for the pose scope pickscript.
    label, language, and script are all strings. The correct format is:
    { "label": "...", "language": "...", "script": "..." }
    '''
def changePathRelToOwner(sop_node: hou.OpNode, channels: Iterable[str | None]) -> list[str]:
    """ Given a list of channel pattern strings and a hou.SopNode, expand to a
        list of paths relative to the owner object.  If add_warnings is True,
        then patterns which expand to nothing will get warnings added to
        sop_node.
    """
def addPoseScopeValues(attribname: str, geo: hou.Geometry, primgrouppattern: str, channels: list[str], pickscripts: list[str]) -> None:
    """adds the channels and pickscripts to the pose scope attribute on the primitives 
    specified by the primgrouppattern. attribname is a string, geo is a hou.Geometry object,
    primgrouppattern is a string (the pattern format is the same one used by the group
    fields on SOP nodes that take primitive selections), channels is a list of strings (full path
    to given channels - Ie. /obj/null1/tx), and pickscripts is a list of strings (in json format
    as specified in createPoseScopePickscript).
    """
def selectTrack(title: str | None = None, message: str | None = None, initial_selection: Mapping[str, Sequence[tuple[hou.ChopNode, str]]] | None = None, multiple_select: bool = False) -> list[hou.Track | None]:
    """ Open a chooser to select a channel. """
