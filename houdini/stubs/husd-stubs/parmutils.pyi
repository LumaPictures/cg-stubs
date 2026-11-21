import hou
from . import typeutils as typeutils
from builtins import range as range
from collections.abc import Mapping, Sequence
from hutil import py23 as py23
from pxr import Sdf as Sdf
from typing import TypedDict

from typing import TypeAlias
from typing import TypeAlias
_ParmScalar: TypeAlias = bool | int | float | str
_ParmDefaultValue: TypeAlias = _ParmScalar | tuple[_ParmScalar, ...] | list[_ParmScalar]
class _TemplateKwargs(TypedDict, total=False):
    num_components: int
    string_type: hou.EnumValue[hou.stringParmType]
    look: hou.EnumValue[hou.parmLook]
    naming_scheme: hou.EnumValue[hou.parmNamingScheme]
    min: int
    min_is_strict: bool

class _TemplateDescription(TypedDict):
    template: type[hou.StringParmTemplate | hou.ToggleParmTemplate | hou.FloatParmTemplate | hou.IntParmTemplate]
    kwargs: _TemplateKwargs

HUSD_PROPERTY_CATEGORY: str
TYPE_TEMPLATE_MAP: dict[str, _TemplateDescription]

def createParmTemplateForAttr(attrib_name: str, attrib_type: Sdf.ValueTypeName, parm_name: str | None = None, parm_label: str | None = None, parm_default: _ParmDefaultValue | None = None, parm_menu: Sequence[str] | None = None, parm_tags: Mapping[str, str] | None = None) -> hou.StringParmTemplate | hou.ToggleParmTemplate | hou.FloatParmTemplate | hou.IntParmTemplate:
    """
    Creates a `ParmTemplate` (*not* a parm, as the name would suggest) in which
    you can store a given USD type.

    :param attrib_name: The USD attribute name
    :param attrib_type: The USD type of the values you want to store

    :param parm_name: If this is not None, use this as the parameter name.
        If this is None, use the attribute name as the parameter name.
    :param parm_label: A human-readable label to use for the parameter.
    :param parm_default: a default value for the parameter. 
    :param parm_menu: if this is not None, it should be a sequence of internal 
        menu items. It is passed to the `hou.ParmTemplate.setMenuItems()` method
        of the created parm template.
    :param parm_tags: if this is not None, it should be a dictionary of items
        to add to the parm template's tags dictionary.
    :return: a `hou.ParmTemplate` instance.
    """
