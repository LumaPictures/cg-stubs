from collections.abc import Iterable
from typing import TypeAlias, type_check_only

import _pdg

_ParmValue: TypeAlias = int | float | str | Iterable[int | float | str]

class PyNode:
    def __init__(self, node: _pdg.Node) -> None: ...
    @type_check_only
    def __getitem__(self, key: str) -> _pdg.Port: ...

def __setitem__(node: _pdg.Node, key: str, value: _pdg.Port | _ParmValue) -> None: ...
