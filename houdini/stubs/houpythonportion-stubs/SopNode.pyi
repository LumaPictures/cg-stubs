import hou
from collections.abc import Sequence

def generateInputAttribMenu(self: hou.SopNode, index: int, attrib_type: hou.EnumValue[hou.attribType] | None = None, data_type: hou.EnumValue[hou.attribData] | None = None, min_size: int = 1, max_size: int = -1, array_type: bool = True, scalar_type: bool = True, case_sensitive: bool = True, pattern: str = '*', decode_tokens: bool = False) -> tuple[str, ...]:
    '''
generateInputAttribMenu(self, index, attrib_type=None, data_type=None,
min_size=1, max_size=-1, array_type=True, scalar_type=True,
case_sensitive=True, pattern="*", decode_tokens=False) -> tuple of str

    Generates the tokens and labels for a parameter menu listing the
    input geometry\'s attributes. This method is a convenient wrapper
    around hou.Geometry.generateAttribMenu.

'''
def generateInputGroupMenu(self: hou.SopNode, index: int, group_types: hou.EnumValue[hou.geometryType] | Sequence[hou.EnumValue[hou.geometryType]] | None = None, include_selection: bool = True, include_name_attrib: bool = True, case_sensitive: bool = True, pattern: str = '*', decode_tokens: bool = False, parm: hou.Parm | None = None) -> tuple[str, ...]:
    '''
generateInputGroupMenu(self, index, group_types=None,
include_selection=True, include_name_attrib=True, case_sensitive=True,
pattern="*", decode_tokens=False, parm=None) -> tuple of str

    Generates the tokens and labels for a parameter menu listing the
    input geometry\'s groups. This method is a convenient wrapper around
    hou.Geometry.generateGroupMenu.

'''
