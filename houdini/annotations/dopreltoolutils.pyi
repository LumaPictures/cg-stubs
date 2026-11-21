from collections.abc import Callable, Sequence

import hou
from houtypes import ShelfToolKwargs

def validateCloth(dopobject: hou.DopData, affected: bool) -> None: ...
def validateRBD(dopobject: hou.DopData, affected: bool) -> None: ...
def checkNotPackedObject(dopobject: hou.DopData | None) -> None: ...
def validateBullet(dopobject: hou.DopData, affected: bool) -> None: ...
def validateRBDorBullet(dopobject: hou.DopData, affected: bool) -> None: ...
def validateSource(dopobject: hou.DopData, affected: bool) -> None: ...
def validateWire(dopobject: hou.DopData, affected: bool) -> None: ...
def genericRelToolSetParms(
    dopnode: hou.DopNode,
    affectedobjects: Sequence[hou.DopObject],
    affectorobjects: Sequence[hou.DopObject],
    mutual: bool,
) -> None: ...
def genericConstraint(
    sceneviewer: hou.SceneViewer,
    nodetypename: str,
    validateobjfunc: Callable[[hou.DopData, bool], object] | None,
    mutual: bool,
    allowaffector: bool,
    nodename: str | None,
    prompt: str | None,
    exact_node_type: bool,
) -> hou.DopNode | None: ...
def genericRelationship(
    sceneviewer: hou.SceneViewer,
    nodetypename: str,
    validateobjfunc: Callable[[hou.DopData, bool], object] | None,
    mutual: bool,
    wantaffector: bool,
    needaffector: bool,
    multiaffected: bool,
    multiaffector: bool,
    nodename: str | None,
    affected_prompt: str | None,
    affector_prompt: str | None,
    exact_node_type: bool,
) -> hou.DopNode | None: ...
def genericRelationshipTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    validateobjfunc: Callable[[hou.DopData, bool], object] | None,
    mutual: bool,
    wantaffector: bool,
    needaffector: bool,
    multiaffected: bool,
    multiaffector: bool,
    nodename: str | None = ...,
    affected_prompt: str | None = ...,
    affector_prompt: str | None = ...,
    exact_node_type: bool = ...,
) -> hou.OpNode | None: ...
def genericConstraintTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    validateobjfunc: Callable[[hou.DopData, bool], object] | None,
    mutual: bool,
    allowaffector: bool,
    nodename: str | None = ...,
    prompt: str | None = ...,
    exact_node_type: bool = ...,
) -> hou.OpNode | None: ...
