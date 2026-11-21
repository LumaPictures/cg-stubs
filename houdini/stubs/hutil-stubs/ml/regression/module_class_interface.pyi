# Houdini stubs generated from Houdini 22.0.466

from typing import TypeVar
from collections.abc import Sequence
from typing import TypeVar
_Names = TypeVar('_Names', bound=Sequence[str])
def interfaceFromParts(output_names: _Names) -> _Names: ...
def outputNamesFromInterface(interface: _Names) -> _Names: ...
