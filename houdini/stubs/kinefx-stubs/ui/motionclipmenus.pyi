import hou
from collections.abc import Container
from houtypes import ParmMenuScriptKwargs
from kinefx import motioncliputils as motioncliputils

def generateAttribMenu(kwargs: ParmMenuScriptKwargs, input_index: int = 0, use_rest_pose: bool = False, attrib_type: hou.EnumValue[hou.attribType] | None = None, data_type: hou.EnumValue[hou.attribData] | None = None, min_size: int = 1, max_size: int = -1, array_type: bool = True, scalar_type: bool = True, case_sensitive: bool = True, pattern: str = '*', decode_tokens: bool = False) -> tuple[str, ...]:
    """ A wrapper around the hou.Geometry.generateAttribMenu method that
        creates an attribute menu for the unpacked poses of the geometry from
        a node's MotionClip input. """
def generateAttribMenuInputFromParm(kwargs: ParmMenuScriptKwargs, parm_path: str, motionclip_inputs: Container[int] | None = None, use_rest_pose: bool = False, attrib_type: hou.EnumValue[hou.attribType] | None = None, data_type: hou.EnumValue[hou.attribData] | None = None, min_size: int = 1, max_size: int = -1, array_type: bool = True, scalar_type: bool = True, case_sensitive: bool = True, pattern: str = '*', decode_tokens: bool = False) -> tuple[str, ...]:
    """ A wrapper around the hou.Geometry.generateAttribMenu method. This
        method first evaluates an attribute to determine from which input to
        generate the attribute menu and then uses the 'motionclip_inputs' list
        to determine whether that input should be a MotionClip geometry. If
        'motionclip_inputs' is None, all inputs are treated as containing
        motionclip geometries. """
