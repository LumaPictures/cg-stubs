# Houdini stubs generated from Houdini 22.0.466

import _pdg
from .callback import PythonCallback as PythonCallback

from typing import TypeAlias
from collections.abc import Iterable
from typing import TypeAlias
_ParmValue: TypeAlias = int | float | str | Iterable[int | float | str]
class PyNode(PythonCallback):
    """
    Base class for nodes implemented in Python.
    """
    def __init__(self, node: _pdg.Node) -> None:
        """
        __init__(self, _pdg.Node) -> NoneType

        Initializes the node with a C++ node reference
        """
    def __getitem__(self, key: str) -> _pdg.Port: ...

def __setitem__(node: _pdg.Node, key: str, value: _pdg.Port | _ParmValue) -> None: ...
