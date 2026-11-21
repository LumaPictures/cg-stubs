from collections.abc import Callable, Mapping
from typing import Literal, Never, TypeAlias, TypeVar, overload

import hou
from pxr import Usd

_V = TypeVar("_V")
_ParmValue: TypeAlias = int | float | str | dict[str, str] | hou.Ramp | hou.Geometry | None
_ParmTupleValue: TypeAlias = (
    tuple[int, ...] | tuple[float, ...] | tuple[str, ...] | tuple[hou.Ramp, ...]
    | tuple[dict[str, str], ...] | tuple[hou.Geometry | None, ...]
)

class Translator:
    SOP_DISPLAY_FLAG: int
    SOP_RENDER_FLAG: int
    def __init__(self, node: hou.ObjNode) -> None: ...
    # post_compute gets the parm's value, or the value given in place of a parm. A ParmTuple
    # has no evalAsString(), so force_eval_as_string fails for one.
    @overload
    @staticmethod
    def populateAttr(
        attr: Usd.Attribute,
        parm: hou.Parm,
        post_compute: Callable[[_ParmValue], object] | None = ...,
        force_eval_as_string: Literal[False] = ...,
    ) -> None: ...
    @overload
    @staticmethod
    def populateAttr(
        attr: Usd.Attribute,
        parm: hou.Parm,
        post_compute: Callable[[str], object] | None = ...,
        force_eval_as_string: Literal[True] = ...,
    ) -> None: ...
    @overload
    @staticmethod
    def populateAttr(
        attr: Usd.Attribute,
        parm: hou.ParmTuple,
        post_compute: Callable[[_ParmTupleValue], object] | None = ...,
        force_eval_as_string: Literal[False] = ...,
    ) -> None: ...
    @overload
    @staticmethod
    def populateAttr(
        attr: Usd.Attribute,
        parm: list[hou.Parm],
        post_compute: Callable[[tuple[_ParmValue, ...]], object] | None = ...,
        force_eval_as_string: Literal[False] = ...,
    ) -> None: ...
    @overload
    @staticmethod
    def populateAttr(
        attr: Usd.Attribute,
        parm: list[hou.Parm],
        post_compute: Callable[[tuple[str, ...]], object] | None = ...,
        force_eval_as_string: Literal[True] = ...,
    ) -> None: ...
    @overload
    @staticmethod
    def populateAttr(
        attr: Usd.Attribute,
        parm: None,
        post_compute: Callable[[Never], object] | None = ...,
        force_eval_as_string: bool = ...,
    ) -> None: ...
    @overload
    @staticmethod
    def populateAttr(
        attr: Usd.Attribute,
        parm: _V,
        post_compute: Callable[[_V], object] | None = ...,
        force_eval_as_string: bool = ...,
    ) -> None: ...
    def shouldTranslateNode(self) -> bool | None: ...
    def primType(self) -> str: ...
    def sopNodeFlag(self) -> int: ...
    def referencedNodePaths(self) -> dict[str, str]: ...
    def populatePrim(
        self,
        prim: Usd.Prim,
        referenced_node_prim_paths: Mapping[str, str],
        force_active: bool,
    ) -> None: ...

class Manager:
    def __init__(self) -> None: ...
    def registerTranslator(self, node_type: str, translator_cls: type[Translator]) -> None: ...
    def registerTranslatorForPattern(
        self, node_type_pattern: str, translator_cls: type[Translator]
    ) -> None: ...
    def getTranslators(self, node_path: str) -> list[Translator]: ...
