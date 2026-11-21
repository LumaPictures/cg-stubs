from collections.abc import Callable

import hou
from houtypes import ShelfToolKwargs

def genericDopGeoForceTool(
    sceneviewer: hou.SceneViewer,
    nodetypename: str,
    validategeofunc: Callable[[hou.ObjNode], object] | None,
    nodename: str | None,
    dop_prompt: str | None = ...,
    force_prompt: str | None = ...,
    exact_node_type: bool = ...,
) -> hou.DopNode | None: ...
def genericTool(
    scriptargs: ShelfToolKwargs,
    nodetypename: str,
    validategeofunc: Callable[[hou.ObjNode], object] | None = ...,
    nodename: str | None = ...,
    force_prompt: str | None = ...,
    exact_node_type: bool = ...,
) -> hou.OpNode | None: ...
