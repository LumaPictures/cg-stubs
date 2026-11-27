import ast
from . import _ast
from .. import types as types

class List(_ast.AST, ast_class=ast.List):
    def resolveType(self, **kwargs) -> None: ...
