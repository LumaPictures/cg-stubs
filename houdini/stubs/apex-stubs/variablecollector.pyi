import ast
from typing import Any

class VariableCollector(ast.NodeVisitor):
    myFoundVars: dict[str, Any]
    locals_dict: dict[str, Any]
    def __init__(self, locals_dict: dict[str, Any]) -> None: ...
    def generic_visit(self, node: ast.AST) -> None: ...
    def visit_Assign(self, node: ast.Assign) -> None: ...
    def visit_AnnAssign(self, node: ast.AnnAssign) -> None: ...

def collectVariables(source: str, locals_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Analyzes python code and collects variable assignments.
    Meant to assist autocomplete without having to execute code.

    Returns a dictionary with entries of (found variable id, dummy instances of the variable's type).
    The dummy variable may be None if it's too hard to find out (e.g. function calls).

    source: the source code to be analyzed.
    locals_dict: initial dictionary of locals to be considered. Used to translate classname strings to actual types.
    """
