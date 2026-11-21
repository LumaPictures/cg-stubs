import ast
import pathlib
from typing import IO, ClassVar

from hutil.help.blocks import BlockType, Root, SpanType
from hutil.help.paths import WikiPath
from hutil.help.zones import WikiContext, Zone

NODE_TYPES: tuple[type[ast.Module], type[ast.ClassDef], type[ast.FunctionDef], type[ast.AsyncFunctionDef]]

class DocUnit:
    doc: str | None
    block_type: ClassVar[str]

class ModuleDoc(DocUnit):
    block_type: ClassVar[str]

class ClassDoc(DocUnit):
    block_type: ClassVar[str]
    def text(self) -> list[str | SpanType]: ...
    def block(self, ctx: WikiContext | None = ...) -> BlockType: ...

class AttrDoc(DocUnit):
    block_type: ClassVar[str]
    typename: str | None
    constant: str | None
    def text(self) -> list[str | SpanType]: ...
    def block(self, ctx: WikiContext | None = ...) -> BlockType: ...

class ArgDoc(DocUnit):
    block_type: ClassVar[str]
    typename: str | None
    default: str | None
    def text(self) -> list[str | SpanType]: ...
    def block(self, ctx: WikiContext | None = ...) -> BlockType: ...

class FuncDoc(DocUnit):
    block_type: ClassVar[str]
    returns: str | None
    def text(self) -> list[str | SpanType]: ...
    def block(self, ctx: WikiContext | None = ...) -> BlockType: ...

def unwrap_self_attr(target: ast.expr) -> str | None: ...
def process_node(node: NodeTypes, parents: list[DocUnit], comment_cache: CCache, module_name: str | None = ...) -> DocUnit | None: ...
def process_args(function: ast.FunctionDef | ast.AsyncFunctionDef, func_doc: FuncDoc) -> None: ...
def process_arg(arg: ast.arg, func_fq: str, *, default: str | None = ...) -> ArgDoc: ...
def load(source_file: pathlib.Path | str | IO[str], module_name: str = ..., file_name: str = ...) -> DocUnit | None: ...
def module_block(zone: Zone, path: str | WikiPath, module_name: str = ..., context: WikiContext | None = ...) -> Root: ...
