from . import types as types
from .function import BuiltinFunction as BuiltinFunction, RegisteredFunction as RegisteredFunction
from _typeshed import Incomplete
from typing import NamedTuple

FUNCTIONS: Incomplete

class BuiltinConstant(NamedTuple):
    name: Incomplete
    type: Incomplete
    value: Incomplete

CONSTANTS: Incomplete
