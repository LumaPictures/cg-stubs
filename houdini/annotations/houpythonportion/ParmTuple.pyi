from typing import Any, Self

import hou

class ParmTupleIterator:
    parm_tuple: hou.ParmTuple
    len: int
    idx: int
    def __init__(self, parm_tuple: hou.ParmTuple) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> hou.Parm: ...

def __iter__(self: hou.ParmTuple) -> ParmTupleIterator: ...
def set(
    self: hou.ParmTuple,
    value: hou.ParmTupleArgType | hou.ParmTuple,
    language: hou.EnumValue[hou.exprLanguage] | None = ...,
    follow_parm_references: bool = ...,
) -> None: ...
def saveClip(
    self: hou.ParmTuple,
    file_name: str,
    start: float | None = ...,
    end: float | None = ...,
    sample_rate: float = ...,
) -> None: ...
def loadClip(
    self: hou.ParmTuple, file_name: str, sample_rate: float = ..., start: float | None = ...
) -> None: ...
def setClipData(
    self: hou.ParmTuple,
    data: bytes,
    binary: bool = ...,
    blosc_compressed: bool = ...,
    sample_rate: float = ...,
    start: float | None = ...,
) -> None: ...
def clipData(
    self: hou.ParmTuple,
    start: float | None = ...,
    end: float | None = ...,
    binary: bool = ...,
    use_blosc_compression: bool = ...,
    sample_rate: float = ...,
) -> bytes: ...
def pressScriptActionButton(self: hou.ParmTuple, **kwargs: Any) -> None: ...
