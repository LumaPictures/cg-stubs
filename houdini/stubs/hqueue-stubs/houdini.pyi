import hou
import typing
from collections.abc import Sequence
from typing import Any
from typing_extensions import TypedDict, Unpack

class _RopRenderKwargs(TypedDict, total=False):
    frame_range: hou._FloatSequence
    res: Sequence[int]
    output_file: str | None
    output_format: str
    to_flipbook: bool
    quality: int
    ignore_inputs: bool
    method: hou.EnumValue[hou.renderMethod]
    ignore_bypass_flags: bool
    ignore_lock_flags: bool
    verbose: bool
    output_progress: bool

def hqScriptsDirPath() -> str:
    """Return the unexpanded directory containing the HQueue scripts."""
def loadHipFile(hip_file: str) -> None:
    """Load the specified .hip file.
        
    Raise an exception if the file could not be found or loaded.
    """
def getNode(node_path: str, src_node: hou.OpNode | None = None, follow_fetch_nodes: bool = False) -> hou.OpNode:
    """Return the node matching the specified node path.

    Raise an exception if no such node exists.

    You can optionally specify a source node, `src_node`, if the node path 
    is a relative path.

    If `follow_fetch_nodes` is True, then this function recursively follows
    Fetch nodes until the source node is encountered and then returns the
    source node.
    """
@typing.overload
def setParmValue(parm: hou.Parm, value: int | float | str) -> None: ...
@typing.overload
def setParmValue(parm: hou.ParmTuple, value: Sequence[int | float | str]) -> None: ...
@typing.overload
def setParmValue(parm: hou.Parm | hou.ParmTuple, value: int | float | str | Sequence[int | float | str]) -> None: ...
def setParmValueInRopNodeAndInputs(rop: hou.OpNode, parm_name: str, val: int | float | str | Sequence[int | float | str]) -> None:
    """Set the value for the given parameter in the specified ROP node
       and recursively in each of its ROP input nodes."""
def render(node: hou.OpNode, *args: Any, **kwargs: Unpack[_RopRenderKwargs]) -> None:
    """Render the specified node.

    Raise an exception if the node could not be rendered.
    """
def fileExists(file_path: str) -> bool:
    """Return true if the file path exists and False otherwise.

    This function checks the HOUDINI_PATHMAP environment variable to check
    other paths.
    """
def getFarmPathValue(parm: hou.Parm) -> str:
    """Return the path value stored in the given string parameter.

    If no expression is stored in the parameter, then return the
    parameter's unexpanded string as the path value.  This is to preserve
    the variables in the path since the path is intended to be used on the
    farm.

    If an expression is stored in the parameter, then return the
    parameter's evaluated value as the path value.
    """
def getVerboseLevel(rop: hou.OpNode | None = None) -> int:
    """Return the render verbose level to use in a render job.

    If `rop` is specified, then try to obtain the verbose level from
    the ROP node.
    """
def getRopNodeAndTileCallbackParm(rop_path: str, enable_checkpoints: bool, get_tile_callback: bool = True) -> tuple[hou.OpNode, hou.Parm | None]:
    """Return the requested ROP node.
    
    Also return the ROP node's tile callback parameter if it has
    a tile callback parameter.
    """
def setTileCallbackParmValue(parm: hou.Parm, frame_index: int, frame_number: int, num_frames: int) -> None:
    """Set the value of the specified tile callback parameter
       using the given arguments."""
def enableProgressReporting(rop: hou.OpNode) -> None:
    """Enable progress reporting on the given ROP node."""
def getImageFileTileSuffix(rop: hou.OpNode) -> str:
    """Return the tile suffix to use in image files as specified
       by the given output driver."""
