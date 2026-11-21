from collections.abc import Sequence

import hou

def generateInputAttribMenu(
    self: hou.SopNode,
    index: int,
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
def generateInputGroupMenu(
    self: hou.SopNode,
    index: int,
    group_types: hou.EnumValue[hou.geometryType] | Sequence[hou.EnumValue[hou.geometryType]] | None = ...,
    include_selection: bool = ...,
    include_name_attrib: bool = ...,
    case_sensitive: bool = ...,
    pattern: str = ...,
    decode_tokens: bool = ...,
    parm: hou.Parm | None = ...,
) -> tuple[str, ...]: ...
