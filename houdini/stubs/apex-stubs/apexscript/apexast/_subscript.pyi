import ast
from . import _ast
from .. import types as types

class Subscript(_ast.AST, ast_class=ast.Subscript):
    def resolveType(self, **kwargs) -> None: ...
