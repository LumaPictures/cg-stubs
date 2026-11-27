import ast
from . import _ast
from .. import types as types

class Tuple(_ast.AST, ast_class=ast.Tuple):
    def resolveType(self, **kwargs) -> None: ...
