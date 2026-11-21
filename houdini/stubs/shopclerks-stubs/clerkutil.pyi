import hou
from collections.abc import Iterable, Mapping, Sequence
from typing import TypeAlias
from typing_extensions import TypedDict

from typing import TypeAlias
from collections.abc import Callable
_OptionValue: TypeAlias = bool | int | float | str | tuple[int, ...] | tuple[float, ...] | tuple[str, ...] | hou.Vector2 | hou.Vector3 | hou.Vector4 | dict[str, '_OptionValue']
_ShopParmValue: TypeAlias = _OptionValue | dict[str, str] | hou.Ramp | hou.Geometry | None | tuple[hou.Ramp, ...] | tuple[dict[str, str], ...] | tuple[hou.Geometry | None, ...]
ShaderStringEvaluator: TypeAlias = Callable[[str, str, float, list[str], _ShopOptions], str]
class _ShopOptions(TypedDict, total=False, extra_items=_OptionValue):  # type: ignore[call-arg]
    rendertype: str
    shoptype: int
    forcevop: bool
    forcecop: bool
    soho_precision: int


def protect(pattern: str) -> str:
    """ Protect special characters by replacing with expected sequences """
def quote(pattern: str) -> str: ...
def shopParmTuple(parm: hou.ParmTuple, frame: float, options: _ShopOptions) -> list[_ShopParmValue]: ...

class ParmEvaluator:
    evaluator: ShaderStringEvaluator | None
    precision: int
    options: _ShopOptions
    map: dict[str, list[str]]
    def __init__(self, evaluator: ShaderStringEvaluator | None, precision: int, options: _ShopOptions, map: Mapping[str, str] | None = None) -> None: ...
    def getRampBasis(self, ramp: hou.Ramp, name: str, values: Sequence[hou.EnumValue[hou.rampBasis]]) -> list[tuple[str, str]]: ...
    def getRampNumKey(self, ramp: hou.Ramp, name: str, values: str) -> list[tuple[str, str]]: ...
    def getRampKeys(self, ramp: hou.Ramp, name: str, values: str) -> list[tuple[str, str]]: ...
    def getRampValues(self, ramp: hou.Ramp, name: str, values: str) -> list[tuple[str, str]]: ...
    def getParmValues(self, parm: hou.ParmTuple, values: str) -> list[tuple[str, str]]: ...
    def getParmValuesArray(self, parm: hou.ParmTuple, values: str, count: int) -> list[tuple[str, str]]: ...
    def isArrayParm(self, parm: hou.ParmTuple, n: int) -> bool: ...
    def shopParmTupleOverride(self, parm: hou.ParmTuple, frame: float) -> list[str] | None: ...
    def getRampParms(self, parm: hou.ParmTuple, frame: float) -> list[tuple[str, str]]: ...
    def getShaderParm(self, shadernode: hou.OpNode, frame: float, pname: str) -> list[tuple[str, str]]:
        ''' Returns an array of tuples (pairs of strings), representing
            parameter values for the given parameter names. Usually
            it\'s just one pair, but for parms such as ramps there may
            be several pairs in the array.  The first element of each pair 
            is the parameter name string with qualifiers (ie, type 
            and reference) and the second element is the string encoding 
            of the parameter value array.
            Eg, [(\'"color diffuseColor"\', \'[0.25 0.25 0.25]\')]
        '''
    def getShaderParms(self, shadernode: hou.OpNode, frame: float, parmnames: Iterable[str]) -> list[tuple[str, str]]:
        ''' Returns an array of tuples (pairs of strings), representing
            parameter values for the given parameter names.  The first 
            element of each pair is the parameter name string with qualifiers 
            (ie, type and reference) and the second element is the string 
            encoding of the parameter value array.
            Eg, [(\'"float diffuseGain"\', \'[0.5]\'), 
                 (\'"color diffuseColor"\', \'[0.25 0.25 0.25]\')]
        '''
