import ast
from . import _ast
from .. import types as types

class Attribute(_ast.AST, ast_class=ast.Attribute):
    def resolveName(self, **kwargs) -> None: ...
    def resolveType(self, **kwargs) -> None: ...
