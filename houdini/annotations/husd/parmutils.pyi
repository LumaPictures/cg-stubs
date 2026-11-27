from collections.abc import Mapping, Sequence
from typing import TypeAlias, TypedDict

import hou
from pxr import Sdf

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

_ParmScalar: TypeAlias = bool | int | float | str
_ParmDefaultValue: TypeAlias = (
    _ParmScalar | tuple[_ParmScalar, ...] | list[bool] | list[int] | list[float] | list[str]
)

HUSD_PROPERTY_CATEGORY: str
TYPE_TEMPLATE_MAP: dict[str, _TemplateDescription]

def createParmTemplateForAttr(
    attrib_name: str,
    attrib_type: Sdf.ValueTypeName,
    parm_name: str | None = ...,
    parm_label: str | None = ...,
    parm_default: _ParmDefaultValue | None = ...,
    parm_menu: Sequence[str] | None = ...,
    parm_tags: Mapping[str, str] | None = ...,
) -> hou.StringParmTemplate | hou.ToggleParmTemplate | hou.FloatParmTemplate | hou.IntParmTemplate: ...
