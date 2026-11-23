from collections.abc import Sequence
from typing import TypeAlias

from . import blocks

_Stringable: TypeAlias = "str | int | float | blocks.WikiType | Sequence[_Stringable]"

def string(obj: _Stringable) -> str: ...
