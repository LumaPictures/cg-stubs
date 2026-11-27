import ast
from . import _ast
from .. import types as types

class Constant(_ast.AST, ast_class=ast.Constant):
    def resolveType(self, **kwargs) -> None: ...
