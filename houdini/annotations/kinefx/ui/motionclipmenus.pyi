from collections.abc import Container

import hou
from houtypes import ParmMenuScriptKwargs

def generateAttribMenu(
    kwargs: ParmMenuScriptKwargs,
    input_index: int = ...,
    use_rest_pose: bool = ...,
    attrib_type: hou.EnumValue[hou.attribType] | None = ...,
    data_type: hou.EnumValue[hou.attribData] | None = ...,
    min_size: int = ...,
    max_size: int = ...,
    array_type: bool = ...,
    scalar_type: bool = ...,
    case_sensitive: bool = ...,
    pattern: str = ...,
    decode_tokens: bool = ...,
) -> tuple[str, ...]: ...
def generateAttribMenuInputFromParm(
    kwargs: ParmMenuScriptKwargs,
    parm_path: str,
    motionclip_inputs: Container[int] | None = ...,
    use_rest_pose: bool = ...,
    attrib_type: hou.EnumValue[hou.attribType] | None = ...,
    data_type: hou.EnumValue[hou.attribData] | None = ...,
    min_size: int = ...,
    max_size: int = ...,
    array_type: bool = ...,
    scalar_type: bool = ...,
    case_sensitive: bool = ...,
    pattern: str = ...,
    decode_tokens: bool = ...,
) -> tuple[str, ...]: ...
