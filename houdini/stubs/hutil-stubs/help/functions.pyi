# Houdini stubs generated from Houdini 22.0.466

from . import blocks as blocks
from typing import Iterable, Sequence as Sequence

from typing import TypeAlias
from typing import TypeAlias
_Stringable: TypeAlias = 'str | int | float | blocks.WikiType | Sequence[_Stringable]'
def string(obj: _Stringable) -> str: ...
def slugify(text: blocks.Text, lower: bool = True, maxlen: int = 20) -> str: ...
def engroup(bs: Iterable[blocks.BlockType]) -> blocks.BlockType: ...
