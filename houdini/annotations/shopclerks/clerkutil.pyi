from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import TypeAlias

import hou
from typing_extensions import TypedDict

# A value of the UT_Options that Houdini passes the clerks as `options`: its own keys
# (`rendertype`, `shoptype`, `forcevop`, `soho_precision`, ...) and the values that override
# a shader's parameters, by parameter name.
_OptionValue: TypeAlias = (
    bool
    | int
    | float
    | str
    | tuple[int, ...]
    | tuple[float, ...]
    | tuple[str, ...]
    | hou.Vector2
    | hou.Vector3
    | hou.Vector4
    | dict[str, "_OptionValue"]
)
# What shopParmTuple gives for each component: its override, or what it evaluates to.  A
# ramp parameter gives the whole tuple's value.
_ShopParmValue: TypeAlias = (
    _OptionValue
    | dict[str, str]
    | hou.Ramp
    | hou.Geometry
    | None
    | tuple[hou.Ramp, ...]
    | tuple[dict[str, str], ...]
    | tuple[hou.Geometry | None, ...]
)


class _ShopOptions(TypedDict, total=False, extra_items=_OptionValue):
    rendertype: str
    shoptype: int
    forcevop: bool
    forcecop: bool
    soho_precision: int

ShaderStringEvaluator: TypeAlias = Callable[[str, str, float, list[str], _ShopOptions], str]

def protect(pattern: str) -> str: ...
def quote(pattern: str) -> str: ...
def shopParmTuple(
    parm: hou.ParmTuple, frame: float, options: _ShopOptions
) -> list[_ShopParmValue]: ...

class ParmEvaluator:
    evaluator: ShaderStringEvaluator | None
    precision: int
    options: _ShopOptions
    map: dict[str, list[str]]
    def __init__(
        self,
        evaluator: ShaderStringEvaluator | None,
        precision: int,
        options: _ShopOptions,
        map: Mapping[str, str] | None = ...,
    ) -> None: ...
    def getRampBasis(
        self, ramp: hou.Ramp, name: str, values: Sequence[hou.EnumValue[hou.rampBasis]]
    ) -> list[tuple[str, str]]: ...
    def getRampNumKey(
        self, ramp: hou.Ramp, name: str, values: str
    ) -> list[tuple[str, str]]: ...
    def getRampKeys(
        self, ramp: hou.Ramp, name: str, values: str
    ) -> list[tuple[str, str]]: ...
    def getRampValues(
        self, ramp: hou.Ramp, name: str, values: str
    ) -> list[tuple[str, str]]: ...
    def getParmValues(self, parm: hou.ParmTuple, values: str) -> list[tuple[str, str]]: ...
    def getParmValuesArray(
        self, parm: hou.ParmTuple, values: str, count: int
    ) -> list[tuple[str, str]]: ...
    def isArrayParm(self, parm: hou.ParmTuple, n: int) -> bool: ...
    def shopParmTupleOverride(
        self, parm: hou.ParmTuple, frame: float
    ) -> list[str] | None: ...
    def getRampParms(self, parm: hou.ParmTuple, frame: float) -> list[tuple[str, str]]: ...
    def getShaderParm(
        self, shadernode: hou.OpNode, frame: float, pname: str
    ) -> list[tuple[str, str]]: ...
    def getShaderParms(
        self, shadernode: hou.OpNode, frame: float, parmnames: Iterable[str]
    ) -> list[tuple[str, str]]: ...
