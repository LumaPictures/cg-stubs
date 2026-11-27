import ast
from . import _ast
from .. import types as types

class JoinedStr(_ast.AST, ast_class=ast.JoinedStr):
    def resolveType(self, **kwargs) -> None: ...
