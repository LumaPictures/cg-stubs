from collections.abc import Collection, MutableSequence

from . import blocks
from .paths import WikiPath
from .zones import WikiContext

def denull(block_list: MutableSequence[blocks.BlockType]) -> None: ...
def get_raw_source(block: blocks.BlockType, context: WikiContext) -> list[blocks.BlockType]: ...
def make_include(
    ref: str | WikiPath,
    name: str | None = ...,
    value: str | None = ...,
    unwrap: bool | None = ...,
    retain: Collection[str] | None = ...,
    remove: Collection[str] | None = ...,
    newtype: str | None = ...,
    newid: str | None = ...,
) -> blocks.BlockType: ...
def parse_include_path(basepath: str | WikiPath, ref: str | WikiPath) -> blocks.BlockType: ...
def get_included(
    block: blocks.BlockType, context: WikiContext, root: blocks.BlockType
) -> list[blocks.BlockType]: ...
