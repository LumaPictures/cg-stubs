import ast
from . import _ast

class Name(_ast.AST, ast_class=ast.Name):
    def resolveName(self, **kwargs) -> None: ...
