import ast
from . import apexast as apexast, types as types
from _typeshed import Incomplete

HOUDINI_VERSION: str
FUNCTIONS: Incomplete

def houdiniVersion(node: ast.Call) -> str: ...
