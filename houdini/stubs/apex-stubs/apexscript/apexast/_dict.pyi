import ast
from . import _ast
from .. import types as types

class Dict(_ast.AST, ast_class=ast.Dict):
    def resolveType(self, **kwargs) -> None: ...
