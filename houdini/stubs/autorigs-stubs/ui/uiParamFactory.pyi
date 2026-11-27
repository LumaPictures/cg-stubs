import hou
import typing
from . import uiParamColor as uiParamColor, uiParamComboBox as uiParamComboBox, uiParamFloat as uiParamFloat, uiParamInt as uiParamInt, uiParamOperator as uiParamOperator, uiParamString as uiParamString
from autorigs.ui.uiParamColor import UiParamColor as UiParamColor
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from autorigs.ui.uiParamInt import UiParamInt as UiParamInt
from autorigs.ui.uiParamNum import UiParamNum as UiParamNum
from collections.abc import Sequence
from typing import Literal, Never, TypeIs, TypedDict, Unpack

from typing import TypeVar
from typing import TypeVar
_ParamT = TypeVar('_ParamT', bound=UiParamNum)
class _SoftRangeKwargs(TypedDict, total=False):
    soft_range: tuple[float, float]

class _UiParamNumKwargs(TypedDict, total=False):
    defaults: Sequence[float]
    soft_range: tuple[float, float]

class UiParamFactory:
    TRANSLATE: Literal[0]
    ROTATE: Literal[1]
    SCALE: Literal[2]
    SIZE: Literal[3]
    WIRECOLOR: Literal[4]
    RADIUS: Literal[5]
    LENGTH: Literal[6]
    GSCALE: Literal[7]
    ANGLE: Literal[8]
    ROTATEX: Literal[9]
    ROTATEY: Literal[10]
    SUBDIVIDE: Literal[11]
    LOCATOR_NAME: Literal[12]
    LOCATOR_NUM: Literal[13]
    LOCATOR_PATH: Literal[14]
    LOCATOR_UVW: Literal[15]
    LOCATOR_PARENT_NAME: Literal[16]
    LOCATOR_PARENT_PATH: Literal[17]
    LOCATOR_PARENT_TYPE: Literal[18]
    LOCATOR_PRESET: Literal[19]
    JSON_MAPPING_LABELS: dict[int, str]
    TRANSLATE_JSON_LABEL: str
    ROTATE_JSON_LABEL: str
    SCALE_JSON_LABEL: str
    SIZE_JSON_LABEL: str
    WIRECOLOR_JSON_LABEL: str
    RADIUS_JSON_LABEL: str
    LENGTH_JSON_LABEL: str
    GSCALE_JSON_LABEL: str
    ANGLE_JSON_LABEL: str
    SUBDIVIDE_JSON_LABEL: str
    USCALE_JSON_LABEL: str
    JSON_INV_MAPPING: dict[str, int]
    MAPPING: dict[int, tuple[str, list[str]]]
    def __init__(self) -> None: ...
    @classmethod
    def paramTypeToJSON(cls, paramtype: int) -> None: ...
    @typing.overload
    @classmethod
    def createParams(cls, paramtype: Literal[4], nodes: list[hou.OpNode] | None) -> UiParamColor: ...
    @typing.overload
    @classmethod
    def createParams(cls, paramtype: Literal[11, 13], nodes: list[hou.OpNode] | None) -> UiParamInt: ...
    @typing.overload
    @classmethod
    def createParams(cls, paramtype: Literal[0, 1, 2, 3, 5, 6, 7, 8, 9, 10], nodes: list[hou.OpNode] | None) -> UiParamFloat: ...
    @typing.overload
    @classmethod
    def createParams(cls, paramtype: int, nodes: list[hou.OpNode] | None) -> UiParamFloat | UiParamColor | UiParamInt: ...
    @classmethod
    def hasValidNodeList(self, nodes: list[hou.OpNode] | None) -> TypeIs[list[hou.OpNode]]: ...
    @classmethod
    def linkParams(cls, param: UiParamNum, paramtype: int, nodes: list[hou.OpNode] | None) -> None: ...
    @classmethod
    def createFloatParams(cls, nodes: list[hou.OpNode] | None, mapping: tuple[str, Sequence[str]], custom_name: str = '') -> UiParamFloat: ...
    @classmethod
    def createColorParams(cls, nodes: list[hou.OpNode] | None, mapping: tuple[str, Sequence[str]]) -> UiParamColor: ...
    @classmethod
    def createIntParams(cls, nodes: list[hou.OpNode] | None, mapping: tuple[str, Sequence[str]], custom_name: str = '') -> UiParamInt: ...
    @typing.overload
    @classmethod
    def createTypeParams(cls, param_class: type[_ParamT], nodes: list[hou.OpNode] | None, mapping: tuple[str, Sequence[str]], custom_name: str = ..., **kwargs: Unpack[_UiParamNumKwargs]) -> _ParamT: ...
    @typing.overload
    @classmethod
    def createTypeParams(cls, param_class: type[_ParamT], nodes: list[hou.OpNode] | None, mapping: tuple[str, Sequence[str]], custom_name: str, *args: Unpack[tuple[Sequence[float]]], **kwargs: Unpack[_SoftRangeKwargs]) -> _ParamT: ...
    @typing.overload
    @classmethod
    def createTypeParams(cls, param_class: type[_ParamT], nodes: list[hou.OpNode] | None, mapping: tuple[str, Sequence[str]], custom_name: str, *args: Unpack[tuple[Sequence[float], tuple[float, float]]], **kwargs: Never) -> _ParamT: ...
